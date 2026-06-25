from __future__ import annotations

from collections import defaultdict
from html import escape

from .config import README_PATH
from .jobs import MatchedJob, parse_job_datetime, utc_now_label
from .text import markdown_escape

START = "<!-- JOBS:START -->"
END = "<!-- JOBS:END -->"


def render_job_date(value: str) -> str:
    parsed = parse_job_datetime(value)
    if parsed.year <= 1:
        return "Unknown"
    return parsed.strftime("%Y-%m-%d")


def render_h1b_sponsorship(sponsors: bool) -> str:
    return "✅ Yes" if sponsors else "❌ No"


def render_apply_button(url: str) -> str:
    safe_url = escape((url or "").replace("|", "%7C"), quote=True)
    return (
        f'<a href="{safe_url}">'
        '<img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square">'
        "</a>"
    )


def _date_sort_key(date_label: str):
    if date_label == "Unknown":
        return parse_job_datetime("")
    return parse_job_datetime(date_label)


def _jobs_by_date(jobs: list[MatchedJob]) -> list[tuple[str, list[MatchedJob]]]:
    grouped: dict[str, list[MatchedJob]] = defaultdict(list)
    for item in jobs:
        grouped[render_job_date(item.job.published_at)].append(item)

    ordered: list[tuple[str, list[MatchedJob]]] = []
    for date_label in sorted(grouped, key=_date_sort_key, reverse=True):
        ordered.append(
            (
                date_label,
                sorted(
                    grouped[date_label],
                    key=lambda item: (not item.h1b_sponsor, -item.score, item.job.title.lower()),
                ),
            )
        )
    return ordered


def render_jobs_table(jobs: list[MatchedJob]) -> str:
    if not jobs:
        return (
            f"_Last updated: {utc_now_label()}_\n\n"
            "No matching jobs found that met the role, resume, USA-only, no-clearance, "
            "posted-on/after June 19, 2026, and <=2 years filters."
        )

    total_sponsors = sum(1 for item in jobs if item.h1b_sponsor)
    grouped_jobs = _jobs_by_date(jobs)
    lines = [
        f"_Last updated: {utc_now_label()}_",
        "",
        f"**Showing {len(jobs)} roles across {len(grouped_jobs)} posting dates.** H-1B sponsor matches: **{total_sponsors}**.",
    ]

    for date_label, date_jobs in grouped_jobs:
        sponsor_count = sum(1 for item in date_jobs if item.h1b_sponsor)
        lines.extend(
            [
                "",
                f"### {date_label} · {len(date_jobs)} role{'s' if len(date_jobs) != 1 else ''} · {sponsor_count} H-1B sponsor match{'es' if sponsor_count != 1 else ''}",
                "",
                "| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |",
                "| --- | --- | --- | ---: | --- | ---: | --- |",
            ]
        )
        for item in date_jobs:
            job = item.job
            lines.append(
                "| {role} | {company} | {location} | {years} | {sponsor} | {alignment}% | {apply} |".format(
                    role=markdown_escape(job.title),
                    company=markdown_escape(job.company),
                    location=markdown_escape(job.location),
                    years=markdown_escape(item.years_required),
                    sponsor=render_h1b_sponsorship(item.h1b_sponsor),
                    alignment=item.score,
                    apply=render_apply_button(job.url),
                )
            )
    return "\n".join(lines)


def update_readme(jobs: list[MatchedJob], readme_path=README_PATH) -> None:
    content = readme_path.read_text(encoding="utf-8")
    if START not in content or END not in content:
        raise ValueError(f"{readme_path} must contain {START} and {END} markers")
    generated = render_jobs_table(jobs)
    before, rest = content.split(START, 1)
    _, after = rest.split(END, 1)
    readme_path.write_text(f"{before}{START}\n{generated}\n{END}{after}", encoding="utf-8")
