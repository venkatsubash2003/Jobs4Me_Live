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
2. Fetches jobs from Remote OK and Remotive public endpoints.
3. Keeps only the allowed role families.
4. Requires the job description to mention an experience requirement of 0-2 years.
5. Scores each job against the resume keywords.
6. Looks up whether the company has prior H-1B sponsorship records.
7. Rewrites the generated jobs table below.

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
- `REMOTEOK_URL`: override the Remote OK API URL.
- `REMOTIVE_URLS`: comma-separated Remotive API URLs to query.

To use the PDF resume parser, place your resume at `resume/resume.pdf`. The workflow installs `pypdf`, so PDF parsing is available in GitHub Actions.

## H-1B Sponsor Field

`Yes` means the normalized company name matched prior sponsor records in the loaded sponsor data. `No` means no prior record was found in the configured data sources; it is not legal advice or a guarantee about future sponsorship.

## Automation

The GitHub Actions workflow in `.github/workflows/update-jobs.yml` runs every 6 hours and commits README updates when the generated table changes.

<!-- JOBS:START -->
_Last updated: 2026-06-20 02:45 UTC_

| Role | Job | Company | Location | Years | H1B Sponsor | Score | Source |
| --- | --- | --- | --- | ---: | --- | ---: | --- |
| Data Science Engineer | [Junior Data Scientist](https://remoteOK.com/remote-jobs/remote-junior-data-scientist-why-hiring-1133570) | Why Hiring | Canada, | 0-2 | No | 1 | Remote OK |
<!-- JOBS:END -->
