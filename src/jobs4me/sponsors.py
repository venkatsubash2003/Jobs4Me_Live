from __future__ import annotations

import csv
import os
from pathlib import Path
from urllib.request import urlopen

from .config import SPONSOR_SEED_PATH
from .text import normalize_company

COMPANY_COLUMNS = (
    "company",
    "employer",
    "employer_name",
    "petitioner",
    "petitioner_name",
    "EMPLOYER_NAME",
)


def _read_csv_rows(path_or_url: str) -> list[dict[str, str]]:
    if path_or_url.startswith(("http://", "https://")):
        with urlopen(path_or_url, timeout=45) as response:
            text = response.read().decode("utf-8", errors="replace")
    else:
        text = Path(path_or_url).read_text(encoding="utf-8")
    return list(csv.DictReader(text.splitlines()))


def load_h1b_sponsors(seed_path: Path = SPONSOR_SEED_PATH) -> set[str]:
    sponsors: set[str] = set()

    if seed_path.exists():
        for row in _read_csv_rows(str(seed_path)):
            if str(row.get("h1b_sponsor", "")).strip().lower() in {"yes", "y", "true", "1"}:
                sponsors.add(normalize_company(row.get("company", "")))

    external_source = os.getenv("H1B_SPONSORS_CSV_URL", "").strip()
    if external_source:
        for row in _read_csv_rows(external_source):
            company = next((row.get(column, "") for column in COMPANY_COLUMNS if row.get(column)), "")
            normalized = normalize_company(company)
            if normalized:
                sponsors.add(normalized)

    return {company for company in sponsors if company}


def is_h1b_sponsor(company: str, sponsors: set[str]) -> bool:
    normalized = normalize_company(company)
    if not normalized:
        return False
    if normalized in sponsors:
        return True
    return any(normalized in sponsor or sponsor in normalized for sponsor in sponsors if len(sponsor) >= 5)
