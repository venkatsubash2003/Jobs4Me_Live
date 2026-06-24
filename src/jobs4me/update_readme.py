from __future__ import annotations

import os

from .jobs import filter_jobs
from .readme import update_readme
from .resume import load_resume_profile
from .sources import fetch_jobs
from .sponsors import load_h1b_sponsors


def main() -> None:
    max_jobs = int(os.getenv("MAX_JOBS", "60"))
    profile = load_resume_profile()
    sponsors = load_h1b_sponsors()
    jobs = fetch_jobs()
    matches = filter_jobs(jobs, profile, sponsors)[:max_jobs]
    update_readme(matches)
    print(f"Fetched {len(jobs)} jobs; wrote {len(matches)} matches to README.md")


if __name__ == "__main__":
    main()
