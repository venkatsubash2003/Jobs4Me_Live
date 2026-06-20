from jobs4me.jobs import Job, classify_role, experience_label, filter_jobs, max_years_required
from jobs4me.resume import ResumeProfile
from jobs4me.text import normalize_company


def test_role_filter_allows_only_target_roles():
    assert classify_role("Machine Learning Engineer") == "Machine Learning Engineer"
    assert classify_role("Senior Machine Learning Engineer") is None
    assert classify_role("Product Manager") is None


def test_years_required_rejects_over_two_years():
    assert max_years_required("Requires 0-2 years of experience") == 2
    assert max_years_required("3+ years of experience") == 3
    assert experience_label("Junior Data Scientist", "Python role") == "0-2"
    assert experience_label("Data Scientist", "Python role") is None


def test_filter_jobs_requires_resume_match_and_h1b_lookup():
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
            description="Python and machine learning role. Requires 1 year of experience.",
        )
    ]
    matches = filter_jobs(jobs, profile, {normalize_company("Google")})
    assert len(matches) == 1
    assert matches[0].h1b_sponsor is True
