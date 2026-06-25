from jobs4me.jobs import Job, MatchedJob
from jobs4me.readme import render_jobs_table


def test_render_jobs_table_groups_by_date_and_sorts_within_date():
    sponsor_job = Job(
        title="Machine Learning Engineer",
        company="Google",
        url="https://example.com/sponsor",
        location="United States",
        source="Test",
        published_at="2026-06-24T10:15:00Z",
        description="Requires 1 year of experience.",
    )
    higher_score_non_sponsor_job = Job(
        title="Software Engineer",
        company="Example",
        url="https://example.com/non-sponsor",
        location="United States",
        source="Test",
        published_at="2026-06-24T18:30:00Z",
        description="Requires 1 year of experience.",
    )
    older_job = Job(
        title="Data Scientist",
        company="Older Example",
        url="https://example.com/older",
        location="United States",
        source="Test",
        published_at="2026-06-23T10:15:00Z",
        description="Requires 1 year of experience.",
    )
    table = render_jobs_table(
        [
            MatchedJob(
                job=older_job,
                role="Data Science / Analytics",
                years_required="1",
                score=90,
                h1b_sponsor=True,
            ),
            MatchedJob(
                job=higher_score_non_sponsor_job,
                role="Software Engineering",
                years_required="1",
                score=95,
                h1b_sponsor=False,
            ),
            MatchedJob(
                job=sponsor_job,
                role="AI / ML",
                years_required="1",
                score=40,
                h1b_sponsor=True,
            ),
        ]
    )
    assert "### 2026-06-24 · 2 roles · 1 H-1B sponsor match" in table
    assert "### 2026-06-23 · 1 role · 1 H-1B sponsor match" in table
    assert "| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |" in table
    assert "| Machine Learning Engineer | Google | United States | 1 | ✅ Yes | 40% | <a href=\"https://example.com/sponsor\">" in table
    assert "| Software Engineer | Example | United States | 1 | ❌ No | 95% | <a href=\"https://example.com/non-sponsor\">" in table
    assert '<img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square">' in table
    assert table.index("### 2026-06-24") < table.index("### 2026-06-23")
    assert table.index("Machine Learning Engineer") < table.index("Software Engineer")
