# Jobs4Me Live

Resume-aware job finder for early-career AI, data science, machine learning, and software engineering roles.

The scheduled workflow fetches current postings, keeps only roles related to:

- AI Engineer
- Data Science Engineer
- Machine Learning Engineer
- Software Engineer

It filters out postings that ask for more than 2 years of experience and annotates each company with an `H1B Sponsor` field based on prior sponsorship records loaded from `data/h1b_sponsors_seed.csv` and, optionally, an external CSV configured with `H1B_SPONSORS_CSV_URL`.

## How it works

1. Reads resume keywords from `resume/profile.yml` and optionally `resume/resume.pdf`.
2. Fetches jobs from company boards listed in `data/ats_boards.yml`.
3. Keeps only the allowed role families.
4. Keeps only USA-region roles.
5. Removes security-clearance jobs.
6. Keeps OPT-friendly roles: explicit OPT/CPT/visa-sponsorship language or a prior H-1B sponsor match, while rejecting postings that say no sponsorship.
7. Requires 0-2 years of experience or an early-career title such as junior, entry-level, new grad, or graduate.
8. Scores each job against the resume keywords.
9. Sorts newest postings first and rewrites the generated jobs table below.

## Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m jobs4me.update_readme
```

## Configuration

Environment variables:

- `MAX_JOBS`: maximum rows to write, default `30`.
- `H1B_SPONSORS_CSV_URL`: optional CSV URL or local path with employer names from historical H-1B records.

ATS board configuration lives in `data/ats_boards.yml`. The app supports Greenhouse, Lever, Ashby, Workday, SmartRecruiters, Workable, Pinpoint, and Breezy. These platforms expose company-specific boards, not one global feed, so add company identifiers there as your target list grows.

To use the PDF resume parser, place your resume at `resume/resume.pdf`. The workflow installs `pypdf`, so PDF parsing is available in GitHub Actions.

## H-1B Sponsor Field

`Yes` means the normalized company name matched prior sponsor records in the loaded sponsor data. `No` means no prior record was found in the configured data sources; it is not legal advice or a guarantee about future sponsorship.

## Automation

The GitHub Actions workflow in `.github/workflows/update-jobs.yml` runs every 6 hours and commits README updates when the generated table changes.

<!-- JOBS:START -->
_Last updated: 2026-06-23 02:53 UTC_

No matching jobs found that met the role, resume, USA-only, OPT-friendly, no-clearance, and <=2 years filters.
<!-- JOBS:END -->
