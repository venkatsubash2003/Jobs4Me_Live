from __future__ import annotations

from .config import README_PATH
from .jobs import MatchedJob, utc_now_label
from .text import markdown_escape

START = "<!-- JOBS:START -->"
END = "<!-- JOBS:END -->"


def render_jobs_table(jobs: list[MatchedJob]) -> str:
    if not jobs:
        return (
            f"_Last updated: {utc_now_label()}_\n\n"
            "No matching jobs found that met the role, resume, USA-only, no-clearance, and <=2 years filters."
        )

    lines = [
        f"_Last updated: {utc_now_label()}_",
        "",
        "| Role | Job | Company | Location | Years | H1B Sponsor | Score | Source |",
        "| --- | --- | --- | --- | ---: | --- | ---: | --- |",
    ]
    for item in jobs:
        job = item.job
        lines.append(
            "| {role} | [{title}]({url}) | {company} | {location} | {years} | {sponsor} | {score} | {source} |".format(
                role=markdown_escape(item.role),
                title=markdown_escape(job.title),
                url=job.url,
                company=markdown_escape(job.company),
                location=markdown_escape(job.location),
                years=markdown_escape(item.years_required),
                sponsor="Yes" if item.h1b_sponsor else "No",
                score=item.score,
                source=markdown_escape(job.source),
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
