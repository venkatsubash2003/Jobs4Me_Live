from jobs4me.jobs import (
    Job,
    classify_role,
    experience_label,
    filter_jobs,
    is_usa_role,
    max_years_required,
    parse_job_datetime,
    requires_security_clearance,
    score_job,
)
from jobs4me.resume import ResumeProfile


def test_role_filter_allows_only_target_roles():
    assert classify_role("Machine Learning Engineer") == "AI / ML"
    assert classify_role("Applied Scientist, New Grad") == "AI / ML"
    assert classify_role("Data Analyst") == "Data Science / Analytics"
    assert classify_role("Cloud Engineer") == "Software Engineering"
    assert classify_role("Senior Machine Learning Engineer") is None
    assert classify_role("Product Manager") is None


def test_years_required_rejects_over_two_years():
    assert max_years_required("Requires 0-2 years of experience") == 2
    assert max_years_required("3+ years of experience") == 3
    assert experience_label("Junior Data Scientist", "Python role") == "0-2"
    assert experience_label("Data Scientist", "Python role") == "Not specified"
    assert experience_label("Data Scientist", "Requires 5+ years of experience") is None


def test_parse_job_datetime_handles_epoch_milliseconds():
    parsed = parse_job_datetime("1717200000000")
    assert parsed.year == 2024


def test_score_job_is_normalized_to_100():
    profile = ResumeProfile(
        name="Test",
        keywords=("python", "machine learning", "sql", "react"),
        excluded_keywords=(),
        raw_text="python machine learning sql react",
    )
    job = Job(
        title="Machine Learning Engineer",
        company="Example",
        url="https://example.com/job",
        location="United States",
        source="Test",
        published_at="2026-01-01",
        description="Build Python systems.",
    )
    assert score_job(job, profile) == 50


def test_filter_jobs_keeps_non_sponsor_when_other_filters_match():
    profile = ResumeProfile(
        name="Test",
        keywords=("python", "machine learning"),
        excluded_keywords=(),
        raw_text="python machine learning",
    )
    jobs = [
        Job(
            title="Machine Learning Engineer",
            company="Google LLC",
            url="https://example.com/job",
            location="Remote",
            source="Test",
            published_at="2026-01-01",
            description="Python and machine learning role in the United States. Requires 1 year of experience.",
        )
    ]
    matches = filter_jobs(jobs, profile, set())
    assert len(matches) == 1
    assert matches[0].h1b_sponsor is False


def test_filter_jobs_sorts_newest_then_h1b_then_alignment():
    profile = ResumeProfile(
        name="Test",
        keywords=("python", "machine learning", "sql", "react"),
        excluded_keywords=(),
        raw_text="python machine learning sql react",
    )
    jobs = [
        Job(
            title="Machine Learning Engineer",
            company="No Sponsor",
            url="https://example.com/high",
            location="United States",
            source="Test",
            published_at="2026-01-01",
            description="Python machine learning SQL role. Requires 1 year of experience.",
        ),
        Job(
            title="Machine Learning Engineer",
            company="Google",
            url="https://example.com/sponsor",
            location="United States",
            source="Test",
            published_at="2026-01-03",
            description="Python machine learning role. Requires 1 year of experience.",
        ),
        Job(
            title="Machine Learning Engineer",
            company="No Sponsor 2",
            url="https://example.com/newer",
            location="United States",
            source="Test",
            published_at="2026-01-04",
            description="Python machine learning role. Requires 1 year of experience.",
        ),
    ]
    matches = filter_jobs(jobs, profile, {"google"})
    assert [match.job.url for match in matches] == [
        "https://example.com/newer",
        "https://example.com/sponsor",
        "https://example.com/high",
    ]


def test_usa_and_security_clearance_filters():
    usa_job = Job(
        title="Software Engineer",
        company="Test",
        url="https://example.com/usa",
        location="Remote - United States",
        source="Test",
        published_at="2026-01-02",
        description="Entry-level role. OPT and STEM OPT welcome.",
    )
    clearance_job = Job(
        title="Software Engineer",
        company="Test",
        url="https://example.com/clearance",
        location="Virginia, United States",
        source="Test",
        published_at="2026-01-01",
        description="Requires active Secret security clearance.",
    )
    non_us_job = Job(
        title="Software Engineer",
        company="Test",
        url="https://example.com/non-us",
        location="Amsterdam, Netherlands",
        source="Test",
        published_at="2026-01-03",
        description="Global company with offices in the United States.",
    )
    canada_job = Job(
        title="Software Engineer",
        company="Test",
        url="https://example.com/canada",
        location="Toronto, ON, CA",
        source="Test",
        published_at="2026-01-03",
        description="Python role.",
    )
    assert is_usa_role(usa_job) is True
    assert is_usa_role(non_us_job) is False
    assert is_usa_role(canada_job) is False
    assert requires_security_clearance(clearance_job) is True
