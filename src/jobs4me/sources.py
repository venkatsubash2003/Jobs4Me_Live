from __future__ import annotations

import json
import os
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta, timezone
from typing import Any, Callable
from urllib.parse import quote, urlencode
from urllib.request import Request, urlopen

import yaml

from .config import ATS_BOARDS_PATH, ATS_SYSTEMS, COMPANY_BOARDS_PATH
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
AVATURE_TERMS = ("software engineer", "data engineer", "developer", "data scientist", "machine learning")
AVATURE_PAGE_SIZE = 10
AVATURE_PAGES_PER_TERM = 5
AVATURE_DETAIL_LIMIT = 70
AVATURE_ARTICLE = re.compile(r"<article class=\"article--result.*?</article>", re.S)
AVATURE_LINK = re.compile(r'<a href="(https://[^"]*?/JobDetail/[^"]+)"[^>]*>(.*?)</a>', re.S)
AVATURE_SPAN = re.compile(r"<span>(.*?)</span>", re.S)
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


def _fetch_text(url: str) -> str:
    request = Request(
        url,
        headers={
            "Accept": "text/html,application/xhtml+xml",
            "User-Agent": "Jobs4Me-Live/0.2 (+https://github.com/)",
        },
    )
    with urlopen(request, timeout=HTTP_TIMEOUT) as response:
        return response.read().decode("utf-8", errors="replace")


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
    boards = {system: [] for system in ATS_SYSTEMS}
    seen: set[tuple[str, str]] = set()

    def add_board(system: str, config: dict[str, Any]) -> None:
        if system not in boards:
            return
        key = (system, _board_identity(system, config).lower())
        if not key[1] or key in seen:
            return
        seen.add(key)
        boards[system].append(config)

    if not ATS_BOARDS_PATH.exists():
        data = {}
    else:
        data = yaml.safe_load(ATS_BOARDS_PATH.read_text(encoding="utf-8")) or {}
    for system in ATS_SYSTEMS:
        for item in data.get(system, []) if isinstance(data, dict) else []:
            if isinstance(item, dict):
                add_board(system, item)

    if COMPANY_BOARDS_PATH.exists():
        rows = json.loads(COMPANY_BOARDS_PATH.read_text(encoding="utf-8"))
        for item in rows if isinstance(rows, list) else []:
            config = _normalize_company_board(item)
            if config:
                system, board = config
                add_board(system, board)

    return boards


def _board_identity(system: str, config: dict[str, Any]) -> str:
    if system == "greenhouse":
        return str(config.get("token", ""))
    if system == "lever":
        return str(config.get("site", ""))
    if system == "ashby":
        return str(config.get("organization", ""))
    if system == "workday":
        return "|".join(str(config.get(key, "")) for key in ("host", "tenant", "site"))
    if system == "smartrecruiters":
        return str(config.get("company_id", ""))
    if system == "workable":
        return str(config.get("account", ""))
    if system == "pinpoint":
        return str(config.get("host", ""))
    if system == "breezy":
        return str(config.get("company_id", ""))
    if system == "avature":
        return str(config.get("host", ""))
    return json.dumps(config, sort_keys=True)


def _normalize_company_board(item: Any) -> tuple[str, dict[str, Any]] | None:
    if not isinstance(item, dict):
        return None
    system = normalize_space(str(item.get("ats") or "")).lower()
    slug = normalize_space(str(item.get("slug") or ""))
    company = normalize_space(str(item.get("company") or slug))
    if not system or not slug:
        return None

    if system == "greenhouse":
        return system, {"company": company, "token": slug}
    if system == "lever":
        return system, {"company": company, "site": slug}
    if system == "ashby":
        return system, {"company": company, "organization": slug}
    if system == "workday":
        parts = slug.split("|")
        if len(parts) != 3:
            return None
        tenant, dc, site = parts
        return system, {
            "company": company,
            "host": f"{tenant}.{dc}.myworkdayjobs.com",
            "tenant": tenant,
            "site": site,
        }
    if system == "smartrecruiters":
        return system, {"company": company, "company_id": slug}
    if system == "workable":
        return system, {"company": company, "account": slug}
    if system == "pinpoint":
        host = slug if "." in slug else f"{slug}.pinpointhq.com"
        return system, {"company": company, "host": host}
    if system == "breezy":
        return system, {"company": company, "company_id": slug}
    if system == "avature":
        return system, {"company": company, "host": slug.removeprefix("https://").strip("/")}
    return None


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


def _avature_jobs(config: dict[str, Any]) -> list[Job]:
    host = str(config["host"]).removeprefix("https://").strip("/")
    base = f"https://{host}/en_US/careers/SearchJobs"
    jobs: list[Job] = []
    seen_urls: set[str] = set()
    detail_count = 0
    for term in AVATURE_TERMS:
        if detail_count >= AVATURE_DETAIL_LIMIT:
            break
        for page in range(AVATURE_PAGES_PER_TERM):
            query = urlencode({"search": term, "sort": "relevancy", "jobOffset": page * AVATURE_PAGE_SIZE})
            try:
                page_html = _fetch_text(f"{base}?{query}")
            except Exception:
                break
            articles = AVATURE_ARTICLE.findall(page_html)
            if not articles:
                break
            new_on_page = 0
            for article in articles:
                link = AVATURE_LINK.search(article)
                if not link:
                    continue
                url, raw_title = link.group(1), strip_html(link.group(2))
                title = normalize_space(raw_title)
                if not title or url in seen_urls:
                    continue
                seen_urls.add(url)
                new_on_page += 1
                if not _title_worth_detail(title):
                    continue
                if detail_count >= AVATURE_DETAIL_LIMIT:
                    break
                detail = _avature_detail(url)
                detail_count += 1
                if not detail or not detail.get("published_at"):
                    continue
                spans = [strip_html(value) for value in AVATURE_SPAN.findall(article)]
                location = detail.get("location") or (spans[-1] if spans else "")
                jobs.append(
                    Job(
                        title=title,
                        company=_company(config, host.split(".", 1)[0]),
                        url=url,
                        location=_locations_text(location),
                        source="Avature",
                        published_at=str(detail.get("published_at") or ""),
                        description=strip_html(str(detail.get("description") or "")),
                    )
                )
            if not new_on_page or detail_count >= AVATURE_DETAIL_LIMIT:
                break
    return jobs


def _avature_detail(url: str) -> dict[str, str] | None:
    try:
        html = _fetch_text(url)
    except Exception:
        return None
    for match in re.finditer(r"<script[^>]*application/ld\+json[^>]*>(.*?)</script>", html, re.S):
        try:
            data = json.loads(match.group(1))
        except Exception:
            continue
        if not isinstance(data, dict) or data.get("@type") != "JobPosting":
            continue
        location = data.get("jobLocation") or {}
        if isinstance(location, list):
            location = location[0] if location else {}
        address = location.get("address", {}) if isinstance(location, dict) else {}
        location_text = ", ".join(
            part
            for part in (
                _location_part(address.get("addressLocality")),
                _location_part(address.get("addressRegion")),
                _country_name(_location_part(address.get("addressCountry"))),
            )
            if part
        )
        return {
            "published_at": str(data.get("datePosted") or "")[:10],
            "description": strip_html(str(data.get("description") or "")),
            "location": location_text,
        }
    return None


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
    "avature": _avature_jobs,
}


def _fetch_task_batch(
    tasks: list[tuple[str, dict[str, Any], Callable[[dict[str, Any]], list[Job]]]],
    workers: int,
) -> list[Job]:
    jobs: list[Job] = []
    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {
            executor.submit(fetcher, config): (system, config)
            for system, config, fetcher in tasks
        }
        for completed, future in enumerate(as_completed(futures), start=1):
            system, config = futures[future]
            try:
                jobs.extend(future.result())
            except Exception as exc:
                company = config.get("company") or config.get("token") or config.get("site") or config
                print(f"warning: failed to fetch {system} board {company}: {exc}")
            if completed % 100 == 0:
                print(f"Fetched {completed}/{len(tasks)} boards; {len(jobs)} raw jobs so far", flush=True)
    return jobs


def fetch_jobs() -> list[Job]:
    jobs: list[Job] = []
    boards = _load_boards()
    standard_tasks: list[tuple[str, dict[str, Any], Callable[[dict[str, Any]], list[Job]]]] = []
    workday_tasks: list[tuple[str, dict[str, Any], Callable[[dict[str, Any]], list[Job]]]] = []
    for system in ATS_SYSTEMS:
        for config in boards.get(system, []):
            task = (system, config, FETCHERS[system])
            if system == "workday":
                workday_tasks.append(task)
            else:
                standard_tasks.append(task)

    workers = int(os.getenv("FETCH_WORKERS", "24"))
    workday_workers = int(os.getenv("WORKDAY_FETCH_WORKERS", "2"))
    workday_limit = os.getenv("WORKDAY_BOARD_LIMIT")
    if workday_limit is not None:
        workday_tasks = workday_tasks[: max(0, int(workday_limit))]
    print(f"Fetching {len(standard_tasks)} ATS boards with {workers} workers", flush=True)
    jobs.extend(_fetch_task_batch(standard_tasks, workers))
    print(f"Fetching {len(workday_tasks)} Workday boards with {workday_workers} workers", flush=True)
    jobs.extend(_fetch_task_batch(workday_tasks, workday_workers))

    try:
        jobs.extend(_workable_global_jobs())
    except Exception as exc:
        print(f"warning: failed to fetch Workable global search: {exc}")
    return jobs
