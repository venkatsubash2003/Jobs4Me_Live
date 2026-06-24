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
    assert "| Role | Job | Company | Location | Date | Years | H1B Sponsor | Score | Source |" in table
    assert "| Software Engineering | [Software Engineer](https://example.com/job) | Example | United States | 2026-06-24 | 1 | No | 3 | Test |" in table
