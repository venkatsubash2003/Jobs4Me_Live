from __future__ import annotations

import json
from typing import Any, Callable
from urllib.parse import urlencode
from urllib.request import Request, urlopen

import yaml

from .config import ATS_BOARDS_PATH, ATS_SYSTEMS
from .jobs import Job
from .text import normalize_space, strip_html

Parser = Callable[[object, dict[str, Any]], list[Job]]


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
    with urlopen(request, timeout=45) as response:
        return json.loads(response.read().decode("utf-8", errors="replace"))


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
                published_at=str(item.get("updated_at") or item.get("created_at") or ""),
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
        description = " ".join(
            str(item.get(key, ""))
            for key in ("descriptionPlain", "description", "additionalPlain", "additional")
        )
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
    rows: list[dict[str, Any]] = []
    offset = 0
    while offset < 100:
        payload = _fetch_json(base, {"appliedFacets": {}, "limit": 20, "offset": offset, "searchText": ""})
        batch = payload.get("jobPostings", []) if isinstance(payload, dict) else []
        rows.extend(item for item in batch if isinstance(item, dict))
        if len(batch) < 20:
            break
        offset += 20

    jobs: list[Job] = []
    for item in rows:
        external_path = str(item.get("externalPath") or "")
        detail_url = f"https://{host}{external_path}" if external_path.startswith("/") else f"https://{host}/{site}{external_path}"
        jobs.append(
            Job(
                title=normalize_space(str(item.get("title", ""))),
                company=_company(config, tenant),
                url=detail_url,
                location=_locations_text(item.get("locationsText") or item.get("locations")),
                source="Workday",
                published_at=str(item.get("postedOn") or item.get("startDate") or ""),
                description=strip_html(json.dumps(item)),
            )
        )
    return jobs


def _smartrecruiters_jobs(config: dict[str, Any]) -> list[Job]:
    company_id = str(config["company_id"])
    query = urlencode({"limit": 100})
    payload = _fetch_json(f"https://api.smartrecruiters.com/v1/companies/{company_id}/postings?{query}")
    rows = payload.get("content", []) if isinstance(payload, dict) else []
    jobs: list[Job] = []
    for item in rows:
        if not isinstance(item, dict):
            continue
        location = item.get("location") if isinstance(item.get("location"), dict) else {}
        jobs.append(
            Job(
                title=normalize_space(str(item.get("name", ""))),
                company=_company(config, company_id),
                url=str(item.get("ref") or item.get("releasedDate") or ""),
                location=_locations_text(location.get("fullLocation") or location.get("city") or ""),
                source="SmartRecruiters",
                published_at=str(item.get("releasedDate") or item.get("updatedDate") or ""),
                description=strip_html(json.dumps(item)),
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
        jobs.append(
            Job(
                title=normalize_space(str(item.get("title", ""))),
                company=_company(config, payload.get("name", account) if isinstance(payload, dict) else account),
                url=str(item.get("url") or item.get("shortlink") or f"https://apply.workable.com/{account}/j/{shortcode}/"),
                location=_locations_text(item.get("location") or item.get("locations") or item.get("country")),
                source="Workable",
                published_at=str(item.get("published") or item.get("published_on") or item.get("created_at") or ""),
                description=strip_html(str(item.get("description") or json.dumps(item))),
            )
        )
    return jobs


def _pinpoint_jobs(config: dict[str, Any]) -> list[Job]:
    host = str(config["host"]).removeprefix("https://").strip("/")
    payload = _fetch_json(f"https://{host}/jobs.json")
    rows = payload.get("jobs", payload) if isinstance(payload, dict) else payload
    jobs: list[Job] = []
    for item in rows if isinstance(rows, list) else []:
        if not isinstance(item, dict):
            continue
        jobs.append(
            Job(
                title=normalize_space(str(item.get("title", ""))),
                company=_company(config, host.split(".", 1)[0]),
                url=str(item.get("url") or item.get("job_url") or ""),
                location=_locations_text(item.get("location") or item.get("locations")),
                source="Pinpoint",
                published_at=str(item.get("updated_at") or item.get("created_at") or item.get("published_at") or ""),
                description=strip_html(str(item.get("description") or json.dumps(item))),
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
    for system in ATS_SYSTEMS:
        fetcher = FETCHERS[system]
        for config in boards.get(system, []):
            try:
                jobs.extend(fetcher(config))
            except Exception as exc:
                company = config.get("company") or config.get("token") or config.get("site") or config
                print(f"warning: failed to fetch {system} board {company}: {exc}")
    return jobs
