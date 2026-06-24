from jobs4me.jobs import Job, MatchedJob
from jobs4me.readme import render_jobs_table


def test_render_jobs_table_includes_date_column():
    job = Job(
        title="Software Engineer",
        company="Example",
        url="https://example.com/job",
        location="United States",
        source="Test",
        published_at="2026-06-24T10:15:00Z",
        description="Requires 1 year of experience.",
    )
    table = render_jobs_table(
        [
            MatchedJob(
                job=job,
                role="Software Engineering",
                years_required="1",
                score=3,
                h1b_sponsor=False,
            )
        ]
    )
    assert "| Date | Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |" in table
    assert "| 2026-06-24 | Software Engineer | Example | United States | 1 | ❌ No | 3% | [Apply](https://example.com/job) |" in table
