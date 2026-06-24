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
7. Scores each job against the resume keywords.
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

The GitHub Actions workflow in `.github/workflows/update-jobs.yml` runs every 6 hours and commits README updates when the generated table changes.

<!-- JOBS:START -->
_Last updated: 2026-06-24 01:42 UTC_

| Role | Job | Company | Location | Years | H1B Sponsor | Score | Source |
| --- | --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineering | [Software Engineer, Core Infrastructure - Moveworks](https://jobs.smartrecruiters.com/ServiceNow/744000133688694) | ServiceNow | Mountain View, CALIFORNIA, United States | 2 | Yes | 6 | SmartRecruiters |
| AI / ML | [AI Solutions Strategist](https://jobs.ashbyhq.com/ramp/cbdf2857-1675-4b68-8cb5-2f92a20faa75) | Ramp | New York, NY (HQ) | Not specified | No | 3 | Ashby |
| Software Engineering | [Software Engineer II, Backend (Infrastructure Platform)](https://job-boards.greenhouse.io/affirm/jobs/7764834003) | Affirm | Remote US | 1.5 | No | 4 | Greenhouse |
| Software Engineering | [Software Engineer](https://jobs.workable.com/view/5MDBPGz7TxiTVLSXAcqXmQ/hybrid-software-engineer-in-waltham-at-allego) | Allego | Waltham, Massachusetts, United States | Not specified | No | 2 | Workable Global |
| Software Engineering | [Software Engineer (Cloud, Cross-Platform & .NET Systems)](https://jobs.workable.com/view/pvPiwA6W3djGdKJE4oRiQK/software-engineer-(cloud%2C-cross-platform-%26-.net-systems)-in-houston-at-altom-transport) | Altom Transport | Houston, Texas, United States | Not specified | No | 6 | Workable Global |
| Software Engineering | [Software Engineer (Cloud, Cross-Platform & .NET Systems)](https://jobs.workable.com/view/bPcGwmRzWViLboS3bj3Kih/software-engineer-(cloud%2C-cross-platform-%26-.net-systems)-in-chicago-at-altom-transport) | Altom Transport | Chicago, Illinois, United States | Not specified | No | 6 | Workable Global |
| AI / ML | [Junior Software Engineer (AI-Forward)](https://jobs.workable.com/view/p9YoNg3zEXVYyMquLapXM7/junior-software-engineer-(ai-forward)-in-austin-at-texas-sports-academy-main) | Texas Sports Academy Main | Austin, Texas, United States | 0-2 | No | 3 | Workable Global |
| Software Engineering | [Java Software Engineer](https://jobs.workable.com/view/kHwr7QjnSBcM2ZU2zhyg9g/java-software-engineer-in-newark-at-almashines) | Almashines | Newark, New Jersey, United States | Not specified | No | 2 | Workable Global |
| Data Science / Analytics | [Data Engineer / Data Modeler](https://jobs.workable.com/view/hM1hzkw267qBLj8urGjz5c/remote-data-engineer-%2F-data-modeler-in-united-states-at-essnova-solutions%2C-inc.) | Essnova Solutions, Inc. | United States | Not specified | No | 2 | Workable Global |
| AI / ML | [Jr. AI Prompt Engineer](https://jobs.workable.com/view/2tpEw5MgyfuWBmYZuPbD9d/remote-jr.-ai-prompt-engineer-in-ashburn-at-ignite-it) | Ignite IT | Ashburn, Virginia, United States | 0-2 | No | 2 | Workable Global |
| AI / ML | [Software Engineer (ML Data & Annotation Pipelines)](https://jobs.workable.com/view/mVoGDsvx434Fsv3Pc9WRqB/software-engineer-(ml-data-%26-annotation-pipelines)-in-mossville-at-diversified-services-network%2C-inc.) | Diversified Services Network, Inc. | Mossville, Illinois, United States | Not specified | No | 6 | Workable Global |
| Data Science / Analytics | [Data Analyst Intern](https://jobs.workable.com/view/dVco5FRea1ahxmRupZGhJS/data-analyst-intern-in-braintree-at-liberty-bay-credit-union) | Liberty Bay Credit Union | Braintree, Massachusetts, United States | Not specified | No | 3 | Workable Global |
| AI / ML | [Business Analyst - Data & AI Practice](https://jobs.workable.com/view/haz4PHpYb3Wkw14KXsQ8Mi/remote-business-analyst---data-%26-ai-practice-in-united-states-at-coretek-services) | Coretek Services | United States | Not specified | No | 5 | Workable Global |
| Data Science / Analytics | [Intern (Economic Development Data Analyst)](https://jobs.workable.com/view/4Dq2aKBjpeQXwfBQxANWNd/intern-(economic-development-data-analyst)-in-pittsburgh-at-steer) | Steer | Pittsburgh, Pennsylvania, United States | Not specified | No | 1 | Workable Global |
| Software Engineering | [Software Engineer, Developer Productivity](https://www.rubrik.com/company/careers/departments/job.7922976?gh_jid=7922976) | Rubrik | Palo Alto, CA | 2 | No | 6 | Greenhouse |
| AI / ML | [Machine Learning Engineer](https://job-boards.greenhouse.io/reddit/jobs/8014401) | Reddit | New York City, NY | Not specified | No | 11 | Greenhouse |
| Software Engineering | [Software Engineer](https://job-boards.greenhouse.io/reddit/jobs/8013591) | Reddit | San Francisco, CA | Not specified | No | 6 | Greenhouse |
| AI / ML | [Machine Learning Engineer](https://job-boards.greenhouse.io/reddit/jobs/8014436) | Reddit | San Francisco, CA | Not specified | No | 11 | Greenhouse |
| AI / ML | [Associate AI/ML Software Developer (req-256)](https://jobs.workable.com/view/fioZmnAbKWqJsr4YtQcb1N/associate-ai%2Fml-software-developer-(req-256)-in-tysons-at-cathexis) | CATHEXIS | Tysons, Virginia, United States | Not specified | No | 3 | Workable Global |
| AI / ML | [Associate AI/ML Software Developer (req-258)](https://jobs.workable.com/view/65HU1Jh8cm9kmKkLXfDEDj/associate-ai%2Fml-software-developer-(req-258)-in-redwood-city-at-cathexis) | CATHEXIS | Redwood City, California, United States | Not specified | No | 3 | Workable Global |
| AI / ML | [AI/ML Software Developer (req-257)](https://jobs.workable.com/view/i59ZsDc2Du3p2KcX6dcJdv/ai%2Fml-software-developer-(req-257)-in-tysons-at-cathexis) | CATHEXIS | Tysons, Virginia, United States | Not specified | No | 3 | Workable Global |
| AI / ML | [AI/ML Software Developer (req-259)](https://jobs.workable.com/view/uTvKkGydXPngs6oKPbbCLo/ai%2Fml-software-developer-(req-259)-in-redwood-city-at-cathexis) | CATHEXIS | Redwood City, California, United States | Not specified | No | 3 | Workable Global |
| Software Engineering | [Backend Engineer (NYC)](https://jobs.workable.com/view/6AQjUPZGuvia6buDc3N3AZ/hybrid-backend-engineer-(nyc)-in-new-york-at-mlabs) | MLabs | New York, New York, United States | Not specified | No | 1 | Workable Global |
| Software Engineering | [Software Engineer in Security](https://jobs.workable.com/view/1Wu9EJ8mkSnr4v6RJPNhrc/software-engineer-in-security-in-watertown-at-flexcompute-inc.) | Flexcompute Inc. | Watertown, Massachusetts, United States | Not specified | No | 3 | Workable Global |
| AI / ML | [Forward Deployment Engineer - Frontier AI Deployments](https://jobs.workable.com/view/qU1WALePUyLWeSM3SrU9zM/hybrid-forward-deployment-engineer---frontier-ai-deployments-in-mountain-view-at-accellor) | Accellor | Mountain View, California, United States | Not specified | No | 5 | Workable Global |
| AI / ML | [Forward Deployment Engineer - Frontier AI Deployments](https://jobs.workable.com/view/xa7cjZWy3KrLAighNZ43vN/hybrid-forward-deployment-engineer---frontier-ai-deployments-in-san-francisco-at-accellor) | Accellor | San Francisco, California, United States | Not specified | No | 5 | Workable Global |
| AI / ML | [AI Systems Engineer - Forward-Deployed Builder](https://jobs.workable.com/view/bYBM1XUdBbeG1c8KLjvPbh/remote-ai-systems-engineer---forward-deployed-builder-in-united-states-at-ai-acquisition) | AI Acquisition | United States | Not specified | No | 1 | Workable Global |
| Software Engineering | [Infrastructure/Backend Engineer](https://jobs.workable.com/view/srcxQ1aRFQm8rftXK4Qoe5/hybrid-infrastructure%2Fbackend-engineer-in-new-york-at-mlabs) | MLabs | New York, New York, United States | Not specified | No | 1 | Workable Global |
| Software Engineering | [Embedded Software Engineer (Wireless)](https://jobs.workable.com/view/8mYxUXFkjkWYhsPtH8er5e/embedded-software-engineer-(wireless)-in-irvine-at-tp-link-systems-inc.) | TP-Link Systems Inc. | Irvine, California, United States | Not specified | No | 3 | Workable Global |
| Software Engineering | [Embedded Software Engineer (Consumer Home)](https://jobs.workable.com/view/8vJyEYxzWfr74zHUjRv6DL/embedded-software-engineer-(consumer-home)-in-irvine-at-tp-link-systems-inc.) | TP-Link Systems Inc. | Irvine, California, United States | Not specified | No | 3 | Workable Global |
<!-- JOBS:END -->
