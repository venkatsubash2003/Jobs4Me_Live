from __future__ import annotations

import json
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta, timezone
from typing import Any, Callable
from urllib.parse import quote, urlencode
from urllib.request import Request, urlopen

import yaml

from .config import ATS_BOARDS_PATH, ATS_SYSTEMS
from .jobs import Job
from .text import normalize_space, strip_html

Parser = Callable[[object, dict[str, Any]], list[Job]]
HTTP_TIMEOUT = 20

WORKDAY_SEARCH_TERMS = ("software engineer", "developer", "data scientist", "machine learning")
WORKDAY_PAGES_PER_TERM = 6
WORKDAY_DETAIL_LIMIT = 80
WORKABLE_GLOBAL_TERMS = (
    "software engineer",
    "machine learning engineer",
    "ai engineer",
    "data scientist",
    "data engineer",
    "data analyst",
    "full stack developer",
    "backend engineer",
    "frontend engineer",
)
WORKABLE_GLOBAL_PAGES = 8
TITLE_HINT = re.compile(
    r"engineer|developer|programmer|software|\bsde\b|\bswe\b|data |machine learning|"
    r"\bml\b|\bai\b|scientist|analyst|analytics|full stack|front.?end|back.?end|"
    r"devops|sre|cloud|platform",
    re.I,
)
TITLE_SENIOR = re.compile(
    r"\b(senior|sr\.?|staff|principal|lead|director|manager|head|vp|distinguished|architect|fellow)\b",
    re.I,
)
ISO_COUNTRY = {
    "us": "United States",
    "usa": "United States",
    "ca": "Canada",
    "gb": "United Kingdom",
    "uk": "United Kingdom",
    "in": "India",
    "de": "Germany",
    "fr": "France",
    "nl": "Netherlands",
    "sg": "Singapore",
    "au": "Australia",
    "br": "Brazil",
    "mx": "Mexico",
}


def _fetch_json(url: str, data: dict[str, Any] | None = None) -> object:
    body = json.dumps(data).encode("utf-8") if data is not None else None
    request = Request(
        url,
        data=body,
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": "Jobs4Me-Live/0.2 (+https://github.com/)",
        },
        method="POST" if body else "GET",
    )
    with urlopen(request, timeout=HTTP_TIMEOUT) as response:
        return json.loads(response.read().decode("utf-8", errors="replace"))


def _absolute_date_from_relative(value: str) -> str:
    raw = str(value or "").strip()
    lowered = raw.lower()
    if not raw:
        return ""
    if not any(term in lowered for term in ("posted", "today", "yesterday", "day ago", "days ago", "month ago", "months ago")):
        return raw
    days: int | None
    if "today" in lowered or "just posted" in lowered:
        days = 0
    elif "yesterday" in lowered:
        days = 1
    else:
        day_match = re.search(r"(\d+)\+?\s*day", lowered)
        month_match = re.search(r"(\d+)\+?\s*month", lowered)
        if day_match:
            days = int(day_match.group(1))
        elif month_match:
            days = int(month_match.group(1)) * 30
        else:
            days = None
    if days is None:
        return raw
    return (datetime.now(timezone.utc) - timedelta(days=days)).strftime("%Y-%m-%d")


def _load_boards() -> dict[str, list[dict[str, Any]]]:
    if not ATS_BOARDS_PATH.exists():
        return {system: [] for system in ATS_SYSTEMS}
    data = yaml.safe_load(ATS_BOARDS_PATH.read_text(encoding="utf-8")) or {}
    return {
        system: [item for item in data.get(system, []) if isinstance(item, dict)]
        for system in ATS_SYSTEMS
    }


def _company(config: dict[str, Any], fallback: str = "") -> str:
    return normalize_space(str(config.get("company") or fallback))


def _locations_text(values: Any) -> str:
    if isinstance(values, str):
        return normalize_space(values)
    if isinstance(values, dict):
        return normalize_space(str(values.get("name") or values.get("location") or ""))
    if isinstance(values, list):
        parts = []
        for item in values:
            if isinstance(item, dict):
                parts.append(str(item.get("name") or item.get("location") or ""))
            else:
                parts.append(str(item))
        return normalize_space(", ".join(part for part in parts if part))
    return ""


def _location_part(value: Any) -> str:
    if value is None:
        return ""
    text = normalize_space(str(value))
    return "" if text.lower() == "none" else text


def _country_name(code: str) -> str:
    return ISO_COUNTRY.get((code or "").strip().lower(), code or "")


def _title_worth_detail(title: str) -> bool:
    return bool(TITLE_HINT.search(title or "")) and not TITLE_SENIOR.search(title or "")


def _greenhouse_jobs(config: dict[str, Any]) -> list[Job]:
    token = str(config["token"])
    url = f"https://boards-api.greenhouse.io/v1/boards/{token}/jobs?content=true"
    payload = _fetch_json(url)
    rows = payload.get("jobs", []) if isinstance(payload, dict) else []
    jobs: list[Job] = []
    for item in rows:
        if not isinstance(item, dict):
            continue
        jobs.append(
            Job(
                title=normalize_space(str(item.get("title", ""))),
                company=_company(config, token),
                url=str(item.get("absolute_url") or ""),
                location=_locations_text(item.get("location") or item.get("offices")),
                source="Greenhouse",
                published_at=str(item.get("first_published") or item.get("updated_at") or item.get("created_at") or ""),
                description=strip_html(str(item.get("content", ""))),
            )
        )
    return jobs


def _lever_jobs(config: dict[str, Any]) -> list[Job]:
    site = str(config["site"])
    payload = _fetch_json(f"https://api.lever.co/v0/postings/{site}?mode=json")
    rows = payload if isinstance(payload, list) else []
    jobs: list[Job] = []
    for item in rows:
        if not isinstance(item, dict):
            continue
        categories = item.get("categories") if isinstance(item.get("categories"), dict) else {}
        parts = [str(item.get(key, "")) for key in ("descriptionPlain", "description")]
        for listing in item.get("lists", []) or []:
            if isinstance(listing, dict):
                parts.append(str(listing.get("text", "")))
                parts.append(str(listing.get("content", "")))
        parts.extend(str(item.get(key, "")) for key in ("additionalPlain", "additional"))
        description = " ".join(part for part in parts if part)
        jobs.append(
            Job(
                title=normalize_space(str(item.get("text", ""))),
                company=_company(config, site),
                url=str(item.get("hostedUrl") or item.get("applyUrl") or ""),
                location=_locations_text(categories.get("location", "")),
                source="Lever",
                published_at=str(item.get("createdAt") or ""),
                description=strip_html(description),
            )
        )
    return jobs


def _ashby_jobs(config: dict[str, Any]) -> list[Job]:
    organization = str(config["organization"])
    url = f"https://api.ashbyhq.com/posting-api/job-board/{organization}?includeCompensation=true"
    payload = _fetch_json(url)
    rows = payload.get("jobs", []) if isinstance(payload, dict) else []
    jobs: list[Job] = []
    for item in rows:
        if not isinstance(item, dict):
            continue
        location = item.get("locationName") or item.get("location") or item.get("secondaryLocations")
        description = " ".join(str(item.get(key, "")) for key in ("descriptionPlain", "descriptionHtml", "description"))
        jobs.append(
            Job(
                title=normalize_space(str(item.get("title", ""))),
                company=_company(config, organization),
                url=str(item.get("jobUrl") or item.get("applyUrl") or ""),
                location=_locations_text(location),
                source="Ashby",
                published_at=str(item.get("publishedAt") or item.get("updatedAt") or ""),
                description=strip_html(description),
            )
        )
    return jobs


def _workday_jobs(config: dict[str, Any]) -> list[Job]:
    host = str(config["host"]).removeprefix("https://").strip("/")
    tenant = str(config["tenant"])
    site = str(config["site"])
    base = f"https://{host}/wday/cxs/{tenant}/{site}/jobs"
    cxs = f"https://{host}/wday/cxs/{tenant}/{site}"
    public_base = f"https://{host}/en-US/{site}"
    rows: list[dict[str, Any]] = []
    seen_paths: set[str] = set()
    detail_count = 0
    for term in WORKDAY_SEARCH_TERMS:
        offset = 0
        for _ in range(WORKDAY_PAGES_PER_TERM):
            payload = _fetch_json(base, {"appliedFacets": {}, "limit": 20, "offset": offset, "searchText": term})
            batch = payload.get("jobPostings", []) if isinstance(payload, dict) else []
            if not batch:
                break
            for item in batch:
                if not isinstance(item, dict):
                    continue
                external_path = str(item.get("externalPath") or "")
                if not external_path or external_path in seen_paths:
                    continue
                seen_paths.add(external_path)
                if _title_worth_detail(str(item.get("title", ""))) and detail_count < WORKDAY_DETAIL_LIMIT:
                    detail = _workday_detail(f"{cxs}{external_path}")
                    if detail:
                        item = {**item, **detail}
                        detail_count += 1
                rows.append(item)
            offset += 20
            if offset >= int(payload.get("total", 0) or 0):
                break

    jobs: list[Job] = []
    for item in rows:
        external_path = str(item.get("externalPath") or "")
        detail_url = f"{public_base}{external_path}" if external_path.startswith("/") else f"https://{host}/{site}{external_path}"
        location = item.get("location") or item.get("locationsText") or item.get("locations")
        if not location or re.match(r"^\d+\s+locations?$", str(location).strip(), re.I):
            segments = external_path.strip("/").split("/")
            if len(segments) >= 2 and segments[0] == "job":
                location = segments[1].replace("---", ", ").replace("--", " ").replace("-", " ")
        jobs.append(
            Job(
                title=normalize_space(str(item.get("title", ""))),
                company=_company(config, tenant),
                url=detail_url,
                location=_locations_text(location),
                source="Workday",
                published_at=_absolute_date_from_relative(str(item.get("posted") or item.get("postedOn") or item.get("startDate") or "")),
                description=strip_html(str(item.get("description") or json.dumps(item))),
            )
        )
    return jobs


def _workday_detail(url: str) -> dict[str, Any] | None:
    try:
        payload = _fetch_json(url)
    except Exception:
        return None
    info = payload.get("jobPostingInfo", {}) if isinstance(payload, dict) else {}
    locations = [info.get("location", "")]
    locations.extend(info.get("additionalLocations", []) or [])
    return {
        "description": strip_html(str(info.get("jobDescription", ""))),
        "location": "; ".join(location for location in locations if location),
        "posted": info.get("startDate", "") or info.get("postedOn", ""),
    }


def _smartrecruiters_jobs(config: dict[str, Any]) -> list[Job]:
    company_id = str(config["company_id"])
    base = f"https://api.smartrecruiters.com/v1/companies/{company_id}/postings"
    rows: list[dict[str, Any]] = []
    offset = 0
    for _ in range(3):
        query = urlencode({"limit": 100, "offset": offset})
        payload = _fetch_json(f"{base}?{query}")
        batch = payload.get("content", []) if isinstance(payload, dict) else []
        rows.extend(item for item in batch if isinstance(item, dict))
        if len(batch) < 100:
            break
        offset += 100
        if offset >= int(payload.get("totalFound", 0) or 0):
            break
    jobs: list[Job] = []
    for index, item in enumerate(rows):
        if not isinstance(item, dict):
            continue
        location = item.get("location") if isinstance(item.get("location"), dict) else {}
        description = str(item.get("name", ""))
        if index < 80:
            try:
                detail = _fetch_json(f"{base}/{item.get('id', '')}")
                sections = ((detail.get("jobAd", {}) or {}).get("sections", {}) or {}) if isinstance(detail, dict) else {}
                description = " ".join(
                    strip_html(str((sections.get(key, {}) or {}).get("text", "")))
                    for key in ("jobDescription", "qualifications", "responsibilities")
                ) or description
            except Exception:
                pass
        location_text = ", ".join(
            part
            for part in (
                _location_part(location.get("city")),
                _location_part(location.get("region")),
                _country_name(_location_part(location.get("country"))),
            )
            if part
        )
        jobs.append(
            Job(
                title=normalize_space(str(item.get("name", ""))),
                company=_company(config, company_id),
                url=f"https://jobs.smartrecruiters.com/{company_id}/{item.get('id', '')}",
                location=_locations_text(location.get("fullLocation") or location_text),
                source="SmartRecruiters",
                published_at=str(item.get("releasedDate") or item.get("updatedDate") or ""),
                description=strip_html(description),
            )
        )
    return jobs


def _workable_jobs(config: dict[str, Any]) -> list[Job]:
    account = str(config["account"])
    url = f"https://apply.workable.com/api/v1/widget/accounts/{account}?details=true"
    payload = _fetch_json(url)
    rows = payload.get("jobs", []) if isinstance(payload, dict) else []
    jobs: list[Job] = []
    for item in rows:
        if not isinstance(item, dict):
            continue
        shortcode = str(item.get("shortcode") or "")
        location_text = ", ".join(
            part
            for part in (
                _location_part(item.get("city")),
                _location_part(item.get("state")),
                _location_part(item.get("country")),
            )
            if part
        )
        description = " ".join(
            str(item.get(key, ""))
            for key in ("description", "requirements", "benefits")
        )
        jobs.append(
            Job(
                title=normalize_space(str(item.get("title", ""))),
                company=_company(config, payload.get("name", account) if isinstance(payload, dict) else account),
                url=str(item.get("url") or item.get("shortlink") or f"https://apply.workable.com/{account}/j/{shortcode}/"),
                location=_locations_text(location_text or item.get("location") or item.get("locations") or item.get("country")),
                source="Workable",
                published_at=str(item.get("published") or item.get("published_on") or item.get("created_at") or ""),
                description=strip_html(description or json.dumps(item)),
            )
        )
    return jobs


def _pinpoint_jobs(config: dict[str, Any]) -> list[Job]:
    host = str(config["host"]).removeprefix("https://").strip("/")
    try:
        payload = _fetch_json(f"https://{host}/postings.json")
        rows = payload.get("data", []) if isinstance(payload, dict) else payload
    except Exception:
        payload = _fetch_json(f"https://{host}/jobs.json")
        rows = payload.get("jobs", payload) if isinstance(payload, dict) else payload
    jobs: list[Job] = []
    for item in rows if isinstance(rows, list) else []:
        if not isinstance(item, dict):
            continue
        location = item.get("location")
        if isinstance(location, dict):
            location = ", ".join(
                part
                for part in (
                    _location_part(location.get("city")),
                    _location_part(location.get("region")),
                    _location_part(location.get("country")),
                )
                if part
            ) or location.get("name", "")
        jobs.append(
            Job(
                title=normalize_space(str(item.get("title", ""))),
                company=_company(config, host.split(".", 1)[0]),
                url=str(item.get("url") or item.get("job_url") or ""),
                location=_locations_text(location or item.get("locations")),
                source="Pinpoint",
                published_at=str(item.get("updated_at") or item.get("created_at") or item.get("published_at") or ""),
                description=strip_html(str(item.get("description", "")) + " " + str(item.get("key_responsibilities", ""))),
            )
        )
    return jobs


def _breezy_jobs(config: dict[str, Any]) -> list[Job]:
    company_id = str(config["company_id"])
    payload = _fetch_json(f"https://{company_id}.breezy.hr/json")
    rows = payload if isinstance(payload, list) else payload.get("jobs", []) if isinstance(payload, dict) else []
    jobs: list[Job] = []
    for item in rows:
        if not isinstance(item, dict):
            continue
        jobs.append(
            Job(
                title=normalize_space(str(item.get("name") or item.get("title") or "")),
                company=_company(config, company_id),
                url=str(item.get("url") or item.get("application_url") or ""),
                location=_locations_text(item.get("location")),
                source="Breezy",
                published_at=str(item.get("updated_at") or item.get("created_at") or ""),
                description=strip_html(str(item.get("description") or json.dumps(item))),
            )
        )
    return jobs


def _workable_global_jobs() -> list[Job]:
    jobs: list[Job] = []
    seen: set[str] = set()
    for term in WORKABLE_GLOBAL_TERMS:
        base = (
            "https://jobs.workable.com/api/v1/jobs?query="
            + quote(term)
            + "&location="
            + quote("United States")
        )
        token = ""
        for _ in range(WORKABLE_GLOBAL_PAGES):
            url = base + (f"&pageToken={token}" if token else "")
            try:
                payload = _fetch_json(url)
            except Exception:
                break
            rows = payload.get("jobs", []) if isinstance(payload, dict) else []
            if not rows:
                break
            for item in rows:
                if not isinstance(item, dict):
                    continue
                job_id = str(item.get("id") or item.get("url") or "")
                if not job_id or job_id in seen:
                    continue
                seen.add(job_id)
                location = item.get("location") if isinstance(item.get("location"), dict) else {}
                location_text = ", ".join(
                    part
                    for part in (
                        _location_part(location.get("city")),
                        _location_part(location.get("subregion")),
                        _location_part(location.get("countryName")),
                    )
                    if part
                )
                if not location_text and item.get("workplace") == "remote":
                    location_text = "Remote, United States"
                company = item.get("company") if isinstance(item.get("company"), dict) else {}
                jobs.append(
                    Job(
                        title=normalize_space(str(item.get("title", ""))),
                        company=normalize_space(str(company.get("title", ""))),
                        url=str(item.get("url") or ""),
                        location=normalize_space(location_text),
                        source="Workable Global",
                        published_at=str(item.get("created", "") or "")[:10],
                        description=strip_html(str(item.get("description", ""))),
                    )
                )
            token = str(payload.get("nextPageToken") or "") if isinstance(payload, dict) else ""
            if not token:
                break
    return jobs


FETCHERS: dict[str, Callable[[dict[str, Any]], list[Job]]] = {
    "greenhouse": _greenhouse_jobs,
    "lever": _lever_jobs,
    "ashby": _ashby_jobs,
    "workday": _workday_jobs,
    "smartrecruiters": _smartrecruiters_jobs,
    "workable": _workable_jobs,
    "pinpoint": _pinpoint_jobs,
    "breezy": _breezy_jobs,
}


def fetch_jobs() -> list[Job]:
    jobs: list[Job] = []
    boards = _load_boards()
    tasks: list[tuple[str, dict[str, Any], Callable[[dict[str, Any]], list[Job]]]] = []
    for system in ATS_SYSTEMS:
        for config in boards.get(system, []):
            tasks.append((system, config, FETCHERS[system]))

    with ThreadPoolExecutor(max_workers=12) as executor:
        futures = {
            executor.submit(fetcher, config): (system, config)
            for system, config, fetcher in tasks
        }
        for future in as_completed(futures):
            system, config = futures[future]
            try:
                jobs.extend(future.result())
            except Exception as exc:
                company = config.get("company") or config.get("token") or config.get("site") or config
                print(f"warning: failed to fetch {system} board {company}: {exc}")

    try:
        jobs.extend(_workable_global_jobs())
    except Exception as exc:
        print(f"warning: failed to fetch Workable global search: {exc}")
    return jobs
