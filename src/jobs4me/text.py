from __future__ import annotations

import html
import re
import unicodedata
from html.parser import HTMLParser


class _TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []

    def handle_data(self, data: str) -> None:
        if data.strip():
            self.parts.append(data)


def strip_html(value: str) -> str:
    parser = _TextExtractor()
    parser.feed(value or "")
    return normalize_space(html.unescape(" ".join(parser.parts)))


def normalize_space(value: str) -> str:
    return re.sub(r"\s+", " ", value or "").strip()


def normalize_company(value: str) -> str:
    value = unicodedata.normalize("NFKD", value or "").encode("ascii", "ignore").decode()
    value = value.lower()
    value = re.sub(r"\b(incorporated|inc|llc|ltd|limited|corp|corporation|co|company|plc|usa|us)\b", "", value)
    value = re.sub(r"[^a-z0-9]+", " ", value)
    return normalize_space(value)


def markdown_escape(value: str) -> str:
    return (value or "").replace("|", "\\|").replace("\n", " ")
