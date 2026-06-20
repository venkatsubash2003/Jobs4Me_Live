from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
README_PATH = ROOT / "README.md"
PROFILE_PATH = ROOT / "resume" / "profile.yml"
RESUME_PDF_PATH = ROOT / "resume" / "resume.pdf"
SPONSOR_SEED_PATH = ROOT / "data" / "h1b_sponsors_seed.csv"

ALLOWED_ROLE_LABELS = (
    "AI Engineer",
    "Data Science Engineer",
    "Machine Learning Engineer",
    "Software Engineer",
)

REMOTEOK_URL = "https://remoteok.com/api"
REMOTIVE_URLS = (
    "https://remotive.com/api/remote-jobs?search=software%20engineer",
    "https://remotive.com/api/remote-jobs?search=machine%20learning%20engineer",
    "https://remotive.com/api/remote-jobs?search=ai%20engineer",
    "https://remotive.com/api/remote-jobs?search=data%20scientist",
    "https://remotive.com/api/remote-jobs?category=software-dev",
    "https://remotive.com/api/remote-jobs?category=data",
)
