from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any

from .config import ALLOWED_ROLE_LABELS
from .resume import ResumeProfile
from .text import normalize_space, strip_html


@dataclass(frozen=True)
class Job:
    title: str
    company: str
    url: str
    location: str
    source: str
    published_at: str
    description: str


@dataclass(frozen=True)
class MatchedJob:
    job: Job
    role: str
    years_required: str
    score: int
    h1b_sponsor: bool


MIN_JOB_DATE = datetime(2026, 6, 19, tzinfo=timezone.utc)

ROLE_PATTERNS: tuple[tuple[str, tuple[re.Pattern[str], ...]], ...] = (
    (
        "AI / ML",
        (
            re.compile(r"\b(ai|artificial intelligence|machine\s+learning|ml|deep\s+learning|llm|generative\s+ai)\b", re.I),
            re.compile(r"\b(applied\s+scientist|research\s+scientist|ai\s+scientist|ml\s+scientist)\b", re.I),
            re.compile(r"\b(computer\s+vision|nlp|natural\s+language\s+processing|prompt\s+engineer)\b", re.I),
        ),
    ),
    (
        "Data Science / Analytics",
        (
            re.compile(r"\bdata\s+(science|scientist|engineer|analyst|analytics|modeling|platform)\b", re.I),
            re.compile(r"\b(analytics\s+engineer|business\s+intelligence|bi\s+engineer|quantitative\s+analyst)\b", re.I),
            re.compile(r"\b(etl|elt|data\s+pipeline|data\s+warehouse)\b", re.I),
        ),
    ),
    (
        "Software Engineering",
        (
            re.compile(r"\bsoftware\s+(development\s+)?engineer\b", re.I),
            re.compile(r"\b(sde|backend|back[-\s]?end|frontend|front[-\s]?end|full[-\s]?stack|platform|infrastructure)\s+engineer\b", re.I),
            re.compile(r"\b(devops|cloud|site\s+reliability|sre|systems)\s+engineer\b", re.I),
            re.compile(r"\b(application|mobile|ios|android|web)\s+developer\b", re.I),
        ),
    ),
)

SENIORITY_EXCLUSIONS = re.compile(
    r"\b(senior|sr\.?|staff|principal|lead|manager|director|head|vp|architect)\b",
    re.I,
)
EARLY_CAREER_HINTS = re.compile(r"\b(junior|jr\.?|entry[-\s]?level|new\s+grad|graduate|early\s+career)\b", re.I)
SECURITY_CLEARANCE = re.compile(
    r"\b(security\s+clearance|active\s+clearance|secret\s+clearance|top\s+secret|ts/sci|sci\s+clearance|"
    r"polygraph|public\s+trust|dod\s+clearance|clearable|u\.?s\.?\s+citizenship\s+required)\b",
    re.I,
)
USA_LOCATION = re.compile(
    r"\b(united\s+states|usa|u\.s\.a\.|u\.s\.|us-only|remote\s+-?\s+us|remote\s+-?\s+usa|"
    r"alabama|alaska|arizona|arkansas|california|colorado|connecticut|delaware|florida|georgia|"
    r"hawaii|idaho|illinois|indiana|iowa|kansas|kentucky|louisiana|maine|maryland|massachusetts|"
    r"michigan|minnesota|mississippi|missouri|montana|nebraska|nevada|new\s+hampshire|new\s+jersey|"
    r"new\s+mexico|new\s+york|north\s+carolina|north\s+dakota|ohio|oklahoma|oregon|pennsylvania|"
    r"rhode\s+island|south\s+carolina|south\s+dakota|tennessee|texas|utah|vermont|virginia|"
    r"washington|west\s+virginia|wisconsin|wyoming|"
    r"\b(?:AL|AK|AZ|AR|CA|CO|CT|DE|FL|GA|HI|ID|IL|IN|IA|KS|KY|LA|ME|MD|MA|MI|MN|MS|MO|MT|"
    r"NE|NV|NH|NJ|NM|NY|NC|ND|OH|OK|OR|PA|RI|SC|SD|TN|TX|UT|VT|VA|WA|WV|WI|WY)\b)\b",
    re.I,
)
NON_US_LOCATION = re.compile(
    r"\b(canada|mexico|brazil|argentina|united\s+kingdom|uk|england|scotland|ireland|germany|france|"
    r"spain|italy|netherlands|amsterdam|belgium|switzerland|austria|czechia|greece|ukraine|"
    r"russia|turkey|luxembourg|sweden|norway|denmark|finland|poland|portugal|romania|bulgaria|"
    r"croatia|slovakia|slovenia|estonia|lithuania|latvia|"
    r"india|mumbai|vietnam|thailand|malaysia|philippines|indonesia|singapore|japan|china|taiwan|taipei|"
    r"australia|melbourne|new\s+zealand|united\s+arab\s+emirates|uae|dubai|saudi\s+arabia|qatar|egypt|"
    r"south\s+africa|nigeria|kenya|sri\s+lanka|bangladesh|pakistan|nepal|emea|apac|europe|latin\s+america|"
    r"south\s+korea|seoul|hong\s+kong|tel\s+aviv|israel|chile|santiago|toronto|ontario|kitchener|waterloo|"
    r"montreal|montréal|qu[eé]bec|calgary|british\s+columbia|s[ãa]o\s+paulo|rio\s+de\s+janeiro|"
    r"kuala\s+lumpur|bangkok|dhaka|paris|new\s+delhi|jakarta|manila|berlin|hanoi|nha\s+trang|"
    r"tokyo|prague|munich|dublin|london|belgrade|serbia|one-north|malm[oö]|wroc[łl]aw|\bpl\b|gurugram)\b",
    re.I,
)

EXPERIENCE_PATTERNS = (
    re.compile(r"\b(?P<min>\d+(?:\.\d+)?)\s*[-+]\s*(?P<max>\d+(?:\.\d+)?)\s*\+?\s*years?\b", re.I),
    re.compile(r"\b(?P<num>\d+(?:\.\d+)?)\s*\+?\s*(?:years?|yrs?|yoe)\b", re.I),
    re.compile(r"\b(?P<num>\d+(?:\.\d+)?)\s*\+?\s*years?\s+(?:of\s+)?(?:industry\s+|professional\s+|relevant\s+|software\s+|hands[- ]on\s+)?experience\b", re.I),
    re.compile(r"\bexperience\s*(?:of|:)?\s*(?P<num>\d+(?:\.\d+)?)\s*\+?\s*years?\b", re.I),
    re.compile(r"\b(?:minimum|min\.?|at\s+least|at\s+min)[^\d]{0,20}(?P<num>\d+(?:\.\d+)?)\s*(?:years?|yrs?|yoe)\b", re.I),
)


def classify_role(title: str) -> str | None:
    if SENIORITY_EXCLUSIONS.search(title or ""):
        return None
    for role, patterns in ROLE_PATTERNS:
        if any(pattern.search(title or "") for pattern in patterns):
            return role
    return None


def max_years_required(text: str) -> float | None:
    years: list[float] = []
    for pattern in EXPERIENCE_PATTERNS:
        for match in pattern.finditer(text or ""):
            if "max" in match.groupdict() and match.group("max"):
                years.append(float(match.group("max")))
            elif match.groupdict().get("num"):
                years.append(float(match.group("num")))
    return max(years) if years else None


def experience_label(title: str, description: str) -> str | None:
    required_years = max_years_required(f"{title} {description}")
    if required_years is not None:
        return f"{required_years:g}" if required_years <= 2 else None
    if EARLY_CAREER_HINTS.search(title or ""):
        return "0-2"
    return "Not specified"


def score_job(job: Job, profile: ResumeProfile) -> int:
    haystack = f"{job.title} {job.description}".lower()
    keywords = tuple(keyword for keyword in profile.keywords if keyword)
    if not keywords:
        return 0
    matches = sum(1 for keyword in keywords if keyword in haystack)
    return min(100, round((matches / len(keywords)) * 100))


def parse_job_datetime(value: str) -> datetime:
    raw = (value or "").strip()
    if not raw:
        return datetime.min.replace(tzinfo=timezone.utc)
    if raw.isdigit():
        timestamp = int(raw)
        if timestamp > 10_000_000_000:
            timestamp = timestamp / 1000
        return datetime.fromtimestamp(timestamp, tz=timezone.utc)
    normalized = raw.replace("Z", "+00:00")
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError:
        return datetime.min.replace(tzinfo=timezone.utc)
    if parsed.tzinfo is None:
        return parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def is_recent_enough(job: Job, minimum: datetime = MIN_JOB_DATE) -> bool:
    return parse_job_datetime(job.published_at) >= minimum


def is_usa_role(job: Job) -> bool:
    location = job.location or ""
    if NON_US_LOCATION.search(f"{job.title} {location}"):
        return False
    return bool(USA_LOCATION.search(f"{location} {job.description}"))


def requires_security_clearance(job: Job) -> bool:
    return bool(SECURITY_CLEARANCE.search(f"{job.title} {job.description}"))


def filter_jobs(jobs: list[Job], profile: ResumeProfile, sponsors: set[str]) -> list[MatchedJob]:
    matched: list[MatchedJob] = []
    seen_urls: set[str] = set()
    for job in jobs:
        if job.url in seen_urls:
            continue
        seen_urls.add(job.url)

        if not is_recent_enough(job):
            continue

        role = classify_role(job.title)
        if role not in ALLOWED_ROLE_LABELS:
            continue

        if requires_security_clearance(job):
            continue

        if not is_usa_role(job):
            continue

        years = experience_label(job.title, job.description)
        if years is None:
            continue

        score = score_job(job, profile)
        if score <= 0:
            continue

        from .sponsors import is_h1b_sponsor

        h1b_sponsor = is_h1b_sponsor(job.company, sponsors)

        matched.append(
            MatchedJob(
                job=job,
                role=role,
                years_required=years,
                score=score,
                h1b_sponsor=h1b_sponsor,
            )
        )

    return sorted(
        matched,
        key=lambda item: (parse_job_datetime(item.job.published_at), item.h1b_sponsor, item.score),
        reverse=True,
    )


def parse_remoteok(payload: Any) -> list[Job]:
    rows = payload[1:] if isinstance(payload, list) and payload and "legal" in payload[0] else payload
    jobs: list[Job] = []
    for item in rows if isinstance(rows, list) else []:
        if not isinstance(item, dict):
            continue
        jobs.append(
            Job(
                title=normalize_space(str(item.get("position", ""))),
                company=normalize_space(str(item.get("company", ""))),
                url=str(item.get("url") or item.get("apply_url") or ""),
                location=normalize_space(str(item.get("location", "Remote"))),
                source="Remote OK",
                published_at=str(item.get("date") or ""),
                description=strip_html(str(item.get("description", ""))),
            )
        )
    return jobs


def parse_remotive(payload: Any) -> list[Job]:
    rows = payload.get("jobs", []) if isinstance(payload, dict) else []
    jobs: list[Job] = []
    for item in rows:
        if not isinstance(item, dict):
            continue
        jobs.append(
            Job(
                title=normalize_space(str(item.get("title", ""))),
                company=normalize_space(str(item.get("company_name", ""))),
                url=str(item.get("url") or ""),
                location=normalize_space(str(item.get("candidate_required_location", "Remote"))),
                source="Remotive",
                published_at=str(item.get("publication_date") or ""),
                description=strip_html(str(item.get("description", ""))),
            )
        )
    return jobs


def utc_now_label() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
