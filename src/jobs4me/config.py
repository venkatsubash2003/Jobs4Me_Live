from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
README_PATH = ROOT / "README.md"
PROFILE_PATH = ROOT / "resume" / "profile.yml"
RESUME_PDF_PATH = ROOT / "resume" / "resume.pdf"
SPONSOR_SEED_PATH = ROOT / "data" / "h1b_sponsors_seed.csv"
ATS_BOARDS_PATH = ROOT / "data" / "ats_boards.yml"

ALLOWED_ROLE_LABELS = (
    "AI Engineer",
    "Data Science Engineer",
    "Machine Learning Engineer",
    "Software Engineer",
)

ATS_SYSTEMS = (
    "greenhouse",
    "lever",
    "ashby",
    "workday",
    "smartrecruiters",
    "workable",
    "pinpoint",
    "breezy",
)
