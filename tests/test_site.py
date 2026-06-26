import json
from datetime import datetime, timezone

from jobs4me.jobs import Job, MatchedJob
from jobs4me.site import build_site_payload, update_site


def _matched_job() -> MatchedJob:
    return MatchedJob(
        job=Job(
            title="Machine Learning Engineer",
            company="Example AI",
            url="https://example.com/apply",
            location="Remote - USA",
            source="Test",
            published_at="2026-06-24T10:15:00Z",
            description="Requires 1 year of experience.",
        ),
        role="AI / ML",
        years_required="1",
        score=82,
        h1b_sponsor=True,
    )


def test_build_site_payload_contains_job_data_and_metrics():
    payload = build_site_payload([_matched_job()], now=datetime(2026, 6, 25, 18, 29, tzinfo=timezone.utc))

    assert payload["domains"] == "Data Science, AI/ML, Data Analytics, Software Engineering, ML Engineer"
    assert payload["region"] == "USA"
    assert payload["experience"] == "0-2 years"
    assert payload["next_fetch_in"] == "02 hours: 31 minutes"
    assert payload["stats"] == {
        "total_jobs": 1,
        "h1b_sponsors": 1,
        "posting_dates": 1,
        "latest_date": "2026-06-24",
    }
    assert payload["jobs"][0]["role"] == "Machine Learning Engineer"
    assert payload["jobs"][0]["h1b_sponsor"] is True
    assert payload["jobs"][0]["alignment"] == 82


def test_update_site_writes_index_and_json(tmp_path):
    index_path = tmp_path / "index.html"
    data_path = tmp_path / "jobs.json"

    update_site(
        [_matched_job()],
        site_dir=tmp_path,
        index_path=index_path,
        data_path=data_path,
        now=datetime(2026, 6, 25, 18, 29, tzinfo=timezone.utc),
    )

    assert index_path.exists()
    assert data_path.exists()
    assert "Jobs4Me Live" in index_path.read_text(encoding="utf-8")
    payload = json.loads(data_path.read_text(encoding="utf-8"))
    assert payload["jobs"][0]["company"] == "Example AI"
