# Jobs4Me Live

Resume-aware job finder for early-career AI, machine learning, data science, analytics, and software engineering roles.

The scheduled workflow fetches current postings, keeps only roles related to:

- AI and machine learning
- Data science, analytics, and data engineering
- Software, platform, infrastructure, cloud, web, and mobile engineering

It filters out postings that explicitly ask for more than 2 years of experience and annotates each company with an `H1B Sponsor` field based on prior sponsorship records loaded from `data/h1b_sponsors_seed.csv` and, optionally, an external CSV configured with `H1B_SPONSORS_CSV_URL`. The H-1B field is informational only and no longer filters jobs out.

## How it works

1. Reads resume keywords from `resume/profile.yml` and optionally `resume/resume.pdf`.
2. Fetches jobs from company boards listed in `data/ats_boards.yml` plus Workable global search.
3. Keeps only the allowed role families.
4. Keeps only USA-region roles.
5. Removes security-clearance jobs.
6. Rejects explicit requirements above 2 years; jobs with no stated years are kept as `Not specified`.
7. Scores each job from 0-100 against the resume keywords.
8. Adds an informational H-1B sponsor field.
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

ATS board configuration lives in `data/ats_boards.yml`. The app supports Greenhouse, Lever, Ashby, Workday, SmartRecruiters, Workable, Pinpoint, and Breezy. It also searches Workable's global jobs API for relevant U.S. roles.

To use the PDF resume parser, place your resume at `resume/resume.pdf`. The workflow installs `pypdf`, so PDF parsing is available in GitHub Actions.

## H-1B Sponsor Field

`Yes` means the normalized company name matched prior sponsor records in the loaded sponsor data. `No` means no prior record was found in the configured data sources; it is not legal advice or a guarantee about future sponsorship.

## Automation

The GitHub Actions workflow in `.github/workflows/update-jobs.yml` runs every 6 hours (`0 */6 * * *`, UTC) and commits README updates when the generated table changes. GitHub Pages/README display is updated from those commits.

<!-- JOBS:START -->
_Last updated: 2026-06-24 20:01 UTC_

| Date | Role | Job | Company | Location | Years | H1B Sponsor | Score | Source |
| --- | --- | --- | --- | --- | ---: | --- | ---: | --- |
| 2026-06-24 | Software Engineering | [Software Engineer, Storage](https://job-boards.greenhouse.io/doordashusa/jobs/8024644) | DoorDash | San Francisco, CA; Seattle, WA; New York, NY | 2 | No | 19 | Greenhouse |
| 2026-06-24 | Software Engineering | [Software Engineer II, Backend](https://www.brex.com/careers/8606540002?gh_jid=8606540002) | Brex | Seattle, Washington, United States | 2 | No | 22 | Greenhouse |
| 2026-06-24 | Software Engineering | [Software Engineer II, Backend](https://www.brex.com/careers/8606538002?gh_jid=8606538002) | Brex | San Francisco, California, United States | 2 | No | 22 | Greenhouse |
| 2026-06-24 | Software Engineering | [Software Engineer II, Backend](https://www.brex.com/careers/8606534002?gh_jid=8606534002) | Brex | New York, New York, United States | 2 | No | 22 | Greenhouse |
| 2026-06-24 | AI / ML | [Applied AI Engineer, Fullstack](https://jobs.ashbyhq.com/ramp/6a7e382f-240a-4952-b9e5-7fe2b3856bc9) | Ramp | New York, NY (HQ) | Not specified | No | 15 | Ashby |
| 2026-06-24 | Software Engineering | [1675 - Software Engineer](https://jobs.workable.com/view/9BDAEdPgw1jHZ9qHNcs3CU/1675---software-engineer-in-washington-at-sigma-defense) | Sigma Defense | Washington, District of Columbia, United States | Not specified | No | 7 | Workable Global |
| 2026-06-24 | Software Engineering | [1504 - Software Systems Engineer](https://jobs.workable.com/view/6KRa9XjyrAfMYRMrMN979U/remote-1504---software-systems-engineer-in-united-states-at-sigma-defense) | Sigma Defense | United States | Not specified | No | 4 | Workable Global |
| 2026-06-24 | Data Science / Analytics | [1698 - Data Scientist](https://jobs.workable.com/view/5TG657X6U2RNTsjjbehotc/1698---data-scientist-in-san-diego-at-sigma-defense) | Sigma Defense | San Diego, California, United States | Not specified | No | 7 | Workable Global |
| 2026-06-24 | AI / ML | [Network Engineer (with Programming) - Data & AI Systems](https://jobs.workable.com/view/97B6bSoKgbRH74Pm2KWH75/remote-network-engineer-(with-programming)---data-%26-ai-systems-in-united-states-at-weekday-ai) | Weekday AI | United States | Not specified | No | 7 | Workable Global |
| 2026-06-24 | Data Science / Analytics | [Data Science Experts](https://jobs.workable.com/view/uHAWJpuYHeu9GFHewRjN9T/remote-data-science-experts-in-united-states-at-weekday-ai) | Weekday AI | United States | Not specified | No | 15 | Workable Global |
| 2026-06-23 | AI / ML | [AI Research Engineer – Agentic AI](https://jobs.smartrecruiters.com/BoschGroup/744000133692982) | Bosch | Sunnyvale, CA, United States | Not specified | No | 4 | SmartRecruiters |
| 2026-06-23 | Software Engineering | [Software Engineer, Core Infrastructure - Moveworks](https://jobs.smartrecruiters.com/ServiceNow/744000133688694) | ServiceNow | Mountain View, CALIFORNIA, United States | 2 | Yes | 22 | SmartRecruiters |
| 2026-06-23 | AI / ML | [AI Solutions Strategist](https://jobs.ashbyhq.com/ramp/cbdf2857-1675-4b68-8cb5-2f92a20faa75) | Ramp | New York, NY (HQ) | Not specified | No | 11 | Ashby |
| 2026-06-23 | Software Engineering | [Software Engineer II, Backend (Infrastructure Platform)](https://job-boards.greenhouse.io/affirm/jobs/7764834003) | Affirm | Remote US | 1.5 | No | 15 | Greenhouse |
| 2026-06-23 | Software Engineering | [Software Engineer](https://jobs.workable.com/view/5MDBPGz7TxiTVLSXAcqXmQ/hybrid-software-engineer-in-waltham-at-allego) | Allego | Waltham, Massachusetts, United States | Not specified | No | 7 | Workable Global |
| 2026-06-23 | Software Engineering | [Software Engineer (Cloud, Cross-Platform & .NET Systems)](https://jobs.workable.com/view/pvPiwA6W3djGdKJE4oRiQK/software-engineer-(cloud%2C-cross-platform-%26-.net-systems)-in-houston-at-altom-transport) | Altom Transport | Houston, Texas, United States | Not specified | No | 22 | Workable Global |
| 2026-06-23 | Software Engineering | [Software Engineer (Cloud, Cross-Platform & .NET Systems)](https://jobs.workable.com/view/bPcGwmRzWViLboS3bj3Kih/software-engineer-(cloud%2C-cross-platform-%26-.net-systems)-in-chicago-at-altom-transport) | Altom Transport | Chicago, Illinois, United States | Not specified | No | 22 | Workable Global |
| 2026-06-23 | AI / ML | [Junior Software Engineer (AI-Forward)](https://jobs.workable.com/view/p9YoNg3zEXVYyMquLapXM7/junior-software-engineer-(ai-forward)-in-austin-at-texas-sports-academy-main) | Texas Sports Academy Main | Austin, Texas, United States | 0-2 | No | 11 | Workable Global |
| 2026-06-23 | Software Engineering | [Java Software Engineer](https://jobs.workable.com/view/kHwr7QjnSBcM2ZU2zhyg9g/java-software-engineer-in-newark-at-almashines) | Almashines | Newark, New Jersey, United States | Not specified | No | 7 | Workable Global |
| 2026-06-23 | Data Science / Analytics | [Data Engineer / Data Modeler](https://jobs.workable.com/view/hM1hzkw267qBLj8urGjz5c/remote-data-engineer-%2F-data-modeler-in-united-states-at-essnova-solutions%2C-inc.) | Essnova Solutions, Inc. | United States | Not specified | No | 7 | Workable Global |
| 2026-06-23 | AI / ML | [Jr. AI Prompt Engineer](https://jobs.workable.com/view/2tpEw5MgyfuWBmYZuPbD9d/remote-jr.-ai-prompt-engineer-in-ashburn-at-ignite-it) | Ignite IT | Ashburn, Virginia, United States | 0-2 | No | 7 | Workable Global |
| 2026-06-23 | AI / ML | [Software Engineer (ML Data & Annotation Pipelines)](https://jobs.workable.com/view/mVoGDsvx434Fsv3Pc9WRqB/software-engineer-(ml-data-%26-annotation-pipelines)-in-mossville-at-diversified-services-network%2C-inc.) | Diversified Services Network, Inc. | Mossville, Illinois, United States | Not specified | No | 22 | Workable Global |
| 2026-06-23 | AI / ML | [Business Analyst - Data & AI Practice](https://jobs.workable.com/view/haz4PHpYb3Wkw14KXsQ8Mi/remote-business-analyst---data-%26-ai-practice-in-united-states-at-coretek-services) | Coretek Services | United States | Not specified | No | 19 | Workable Global |
| 2026-06-23 | Data Science / Analytics | [Intern (Economic Development Data Analyst)](https://jobs.workable.com/view/4Dq2aKBjpeQXwfBQxANWNd/intern-(economic-development-data-analyst)-in-pittsburgh-at-steer) | Steer | Pittsburgh, Pennsylvania, United States | Not specified | No | 4 | Workable Global |
| 2026-06-22 | Software Engineering | [Software Engineer, Developer Productivity](https://www.rubrik.com/company/careers/departments/job.7922976?gh_jid=7922976) | Rubrik | Palo Alto, CA | 2 | No | 22 | Greenhouse |
| 2026-06-22 | AI / ML | [Machine Learning Engineer](https://job-boards.greenhouse.io/reddit/jobs/8014401) | Reddit | New York City, NY | Not specified | No | 41 | Greenhouse |
| 2026-06-22 | Software Engineering | [Software Engineer](https://job-boards.greenhouse.io/reddit/jobs/8013591) | Reddit | San Francisco, CA | Not specified | No | 22 | Greenhouse |
| 2026-06-22 | AI / ML | [Machine Learning Engineer](https://job-boards.greenhouse.io/reddit/jobs/8014436) | Reddit | San Francisco, CA | Not specified | No | 41 | Greenhouse |
| 2026-06-22 | AI / ML | [Associate AI/ML Software Developer (req-256)](https://jobs.workable.com/view/fioZmnAbKWqJsr4YtQcb1N/associate-ai%2Fml-software-developer-(req-256)-in-tysons-at-cathexis) | CATHEXIS | Tysons, Virginia, United States | Not specified | No | 11 | Workable Global |
| 2026-06-22 | AI / ML | [Associate AI/ML Software Developer (req-258)](https://jobs.workable.com/view/65HU1Jh8cm9kmKkLXfDEDj/associate-ai%2Fml-software-developer-(req-258)-in-redwood-city-at-cathexis) | CATHEXIS | Redwood City, California, United States | Not specified | No | 11 | Workable Global |
<!-- JOBS:END -->
