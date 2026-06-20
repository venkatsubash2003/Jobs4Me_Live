from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import yaml

from .config import PROFILE_PATH, RESUME_PDF_PATH


@dataclass(frozen=True)
class ResumeProfile:
    name: str
    keywords: tuple[str, ...]
    excluded_keywords: tuple[str, ...]
    raw_text: str


def _read_pdf_text(path: Path) -> str:
    if not path.exists():
        return ""
    try:
        from pypdf import PdfReader
    except ImportError:
        return ""

    reader = PdfReader(str(path))
    return "\n".join(page.extract_text() or "" for page in reader.pages)


def load_resume_profile(profile_path: Path = PROFILE_PATH, pdf_path: Path = RESUME_PDF_PATH) -> ResumeProfile:
    data = yaml.safe_load(profile_path.read_text(encoding="utf-8")) if profile_path.exists() else {}
    keywords = tuple(str(item).lower() for item in data.get("keywords", []))
    excluded = tuple(str(item).lower() for item in data.get("excluded_keywords", []))
    pdf_text = _read_pdf_text(pdf_path)
    raw_text = "\n".join([str(data), pdf_text]).lower()
    return ResumeProfile(
        name=str(data.get("name", "")),
        keywords=keywords,
        excluded_keywords=excluded,
        raw_text=raw_text,
    )
