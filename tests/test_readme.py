from datetime import datetime, timezone

from jobs4me.jobs import Job, MatchedJob
from jobs4me.readme import next_fetch_label, render_jobs_table, render_metrics, update_readme


def test_next_fetch_label_counts_down_to_next_three_hour_slot():
    assert next_fetch_label(datetime(2026, 6, 25, 18, 0, tzinfo=timezone.utc)) == "03 hours: 00 minutes"
    assert next_fetch_label(datetime(2026, 6, 25, 18, 29, tzinfo=timezone.utc)) == "02 hours: 31 minutes"
    assert next_fetch_label(datetime(2026, 6, 25, 23, 50, tzinfo=timezone.utc)) == "00 hours: 10 minutes"


def test_render_metrics_shows_requested_readme_metrics():
    metrics = render_metrics(datetime(2026, 6, 25, 18, 29, tzinfo=timezone.utc))
    assert "Domains" in metrics
    assert "Data Science, AI/ML, Data Analytics, Software Engineering, ML Engineer" in metrics
    assert "🇺🇸 USA" in metrics
    assert "Next job fetch in" in metrics
    assert "02 hours: 31 minutes" in metrics
    assert "0-2 years" in metrics


def test_update_readme_refreshes_metrics_and_jobs_sections(tmp_path):
    readme_path = tmp_path / "README.md"
    readme_path.write_text(
        "\n".join(
            [
                "# Test",
                "<!-- METRICS:START -->",
                "old metrics",
                "<!-- METRICS:END -->",
                "<!-- JOBS:START -->",
                "old jobs",
                "<!-- JOBS:END -->",
            ]
        ),
        encoding="utf-8",
    )

    update_readme([], readme_path, now=datetime(2026, 6, 25, 18, 29, tzinfo=timezone.utc))

    content = readme_path.read_text(encoding="utf-8")
    assert "Data Science, AI/ML, Data Analytics, Software Engineering, ML Engineer" in content
    assert "02 hours: 31 minutes" in content
    assert "old metrics" not in content
    assert "old jobs" not in content
    assert "No matching jobs found" in content


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
