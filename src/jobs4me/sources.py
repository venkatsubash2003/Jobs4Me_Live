from __future__ import annotations

import json
import os
from urllib.request import Request, urlopen

from .config import REMOTEOK_URL, REMOTIVE_URLS
from .jobs import Job, parse_remoteok, parse_remotive


def _fetch_json(url: str) -> object:
    request = Request(
        url,
        headers={
            "Accept": "application/json",
            "User-Agent": "Jobs4Me-Live/0.1 (+https://github.com/)",
        },
    )
    with urlopen(request, timeout=45) as response:
        return json.loads(response.read().decode("utf-8", errors="replace"))


def fetch_jobs() -> list[Job]:
    jobs: list[Job] = []
    remotive_urls = [
        url.strip()
        for url in os.getenv("REMOTIVE_URLS", ",".join(REMOTIVE_URLS)).split(",")
        if url.strip()
    ]
    sources = [(os.getenv("REMOTEOK_URL", REMOTEOK_URL), parse_remoteok)]
    sources.extend((url, parse_remotive) for url in remotive_urls)
    for url, parser in sources:
        try:
            jobs.extend(parser(_fetch_json(url)))
        except Exception as exc:
            print(f"warning: failed to fetch {url}: {exc}")
    return jobs
