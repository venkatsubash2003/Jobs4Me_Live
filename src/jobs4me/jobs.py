from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import datetime
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


ROLE_PATTERNS: tuple[tuple[str, tuple[re.Pattern[str], ...]], ...] = (
    (
        "AI Engineer",
        (
            re.compile(r"\b(ai|artificial intelligence)\s+engineer\b", re.I),
            re.compile(r"\bengineer\b.*\b(ai|artificial intelligence|llm|generative ai)\b", re.I),
        ),
    ),
    (
        "Data Science Engineer",
        (
            re.compile(r"\bdata\s+science\s+engineer\b", re.I),
            re.compile(r"\bdata\s+scientist\b", re.I),
            re.compile(r"\bmachine\s+learning\s+data\s+engineer\b", re.I),
        ),
    ),
    (
        "Machine Learning Engineer",
        (
            re.compile(r"\bmachine\s+learning\s+engineer\b", re.I),
            re.compile(r"\bml\s+engineer\b", re.I),
        ),
    ),
    (
        "Software Engineer",
        (
            re.compile(r"\bsoftware\s+(development\s+)?engineer\b", re.I),
            re.compile(r"\bbackend\s+engineer\b", re.I),
            re.compile(r"\bfull[-\s]?stack\s+engineer\b", re.I),
            re.compile(r"\bfrontend\s+engineer\b", re.I),
        ),
    ),
)

SENIORITY_EXCLUSIONS = re.compile(
    r"\b(senior|sr\.?|staff|principal|lead|manager|director|head|vp|architect)\b",
    re.I,
)
EARLY_CAREER_HINTS = re.compile(r"\b(junior|jr\.?|entry[-\s]?level|new\s+grad|graduate|early\s+career)\b", re.I)

EXPERIENCE_PATTERNS = (
    re.compile(r"\b(?P<min>\d+(?:\.\d+)?)\s*[-+]\s*(?P<max>\d+(?:\.\d+)?)\s*\+?\s*years?\b", re.I),
    re.compile(r"\b(?P<num>\d+(?:\.\d+)?)\s*\+?\s*years?\s+(?:of\s+)?experience\b", re.I),
    re.compile(r"\bexperience\s*(?:of|:)?\s*(?P<num>\d+(?:\.\d+)?)\s*\+?\s*years?\b", re.I),
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
    return None


def score_job(job: Job, profile: ResumeProfile) -> int:
    haystack = f"{job.title} {job.description}".lower()
    return sum(1 for keyword in profile.keywords if keyword and keyword in haystack)


def filter_jobs(jobs: list[Job], profile: ResumeProfile, sponsors: set[str]) -> list[MatchedJob]:
    matched: list[MatchedJob] = []
    seen_urls: set[str] = set()
    for job in jobs:
        if job.url in seen_urls:
            continue
        seen_urls.add(job.url)

        role = classify_role(job.title)
        if role not in ALLOWED_ROLE_LABELS:
            continue

        years = experience_label(job.title, job.description)
        if years is None:
            continue

        score = score_job(job, profile)
        if score <= 0:
            continue

        from .sponsors import is_h1b_sponsor

        matched.append(
            MatchedJob(
                job=job,
                role=role,
                years_required=years,
                score=score,
                h1b_sponsor=is_h1b_sponsor(job.company, sponsors),
            )
        )

    return sorted(matched, key=lambda item: (item.score, item.h1b_sponsor, item.job.published_at), reverse=True)


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
    return datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
