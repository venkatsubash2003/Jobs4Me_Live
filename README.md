<p align="center">
  <img alt="Update jobs" src="https://github.com/venkatsubash2003/Jobs4Me_Live/actions/workflows/update-jobs.yml/badge.svg">
  <img alt="Refresh every 6 hours" src="https://img.shields.io/badge/refresh-every%206%20hours-111827">
  <img alt="USA only" src="https://img.shields.io/badge/region-USA%20only-2563eb">
  <img alt="Early career" src="https://img.shields.io/badge/experience-0--2%20years-16a34a">
  <img alt="Max jobs" src="https://img.shields.io/badge/max%20jobs-60-f97316">
</p>

<h1 align="center">Jobs4Me Live</h1>

<p align="center">
  Resume-aware job radar for early-career AI, machine learning, data science, analytics, and software engineering roles in the United States.
</p>

---

## Live Board Rules

| Signal | What this repo does |
| --- | --- |
| Role fit | Keeps AI/ML, data science, analytics, data engineering, software, platform, cloud, web, mobile, and closely related engineering roles. |
| Experience | Keeps 0-2 year roles. Jobs with no explicit years are shown as `Not specified`; roles asking for more than 2 years are removed. |
| Location | Keeps U.S. roles only, including U.S.-remote roles. |
| Security clearance | Removes postings that require clearance, public trust, polygraph, or U.S. citizenship-only eligibility. |
| H-1B signal | Shows `✅ Yes` when the company appears in prior H-1B sponsor records; otherwise shows `❌ No`. This is informational only. |
| Resume alignment | Converts resume keyword matches into a 0-100% alignment score for each role. |

## Dashboard Layout

Jobs are grouped into separate tables by posting date. The newest dates appear first. Inside each date table, H-1B sponsor matches are listed first, then roles with the strongest resume alignment percentage.

## Data Sources

This scraper pulls from ATS boards configured in `data/ats_boards.yml`, including Greenhouse, Lever, Ashby, Workday, SmartRecruiters, Workable, Pinpoint, and Breezy. It also searches Workable's global jobs API for relevant U.S. roles.

## Automation

GitHub Actions runs `.github/workflows/update-jobs.yml` every 6 hours using the cron schedule `0 */6 * * *` in UTC. When fresh matches change the generated section below, the workflow commits the updated `README.md` back to this repository.

## Run Locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m jobs4me.update_readme
```

## Configuration

| Variable | Purpose |
| --- | --- |
| `MAX_JOBS` | Maximum rows to write, default `60`. |
| `H1B_SPONSORS_CSV_URL` | Optional CSV URL or local path with employer names from historical H-1B records. |

To use the PDF resume parser, place your resume at `resume/resume.pdf`. The workflow installs `pypdf`, so PDF parsing is available in GitHub Actions.

## Latest Matches

<!-- JOBS:START -->
_Last updated: 2026-06-25 16:18 UTC_

**Showing 60 roles across 9 posting dates.** H-1B sponsor matches: **4**.

### 2026-06-25 · 3 roles · 1 H-1B sponsor match

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer - Moveworks | ServiceNow | Mountain View, CALIFORNIA, United States | 2 | ✅ Yes | 22% | <a href="https://jobs.smartrecruiters.com/ServiceNow/744000134304689"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Engineer I | Frontier Medicines | South San Francisco, California, United States | Not specified | ❌ No | 11% | <a href="https://jobs.workable.com/view/t4nn6yTEUyur9CmKuJBZT1/ai-engineer-i-in-south-san-francisco-at-frontier-medicines"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Analytics Intern | Massachusetts Life Sciences Center | Waltham, Massachusetts, United States | Not specified | ❌ No | 7% | <a href="https://jobs.workable.com/view/mvWpDiUcZdFNPjmH6VdSxA/hybrid-data-analytics-intern-in-waltham-at-massachusetts-life-sciences-center"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-06-24 · 15 roles · 1 H-1B sponsor match

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Machine Learning Engineer, Agentic AI Systems - Moveworks | ServiceNow | Mountain View, CALIFORNIA, United States | Not specified | ✅ Yes | 37% | <a href="https://jobs.smartrecruiters.com/ServiceNow/744000134027173"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer II, Backend | Brex | Seattle, Washington, United States | 2 | ❌ No | 22% | <a href="https://www.brex.com/careers/8606540002?gh_jid=8606540002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer II, Backend | Brex | San Francisco, California, United States | 2 | ❌ No | 22% | <a href="https://www.brex.com/careers/8606538002?gh_jid=8606538002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer II, Backend | Brex | New York, New York, United States | 2 | ❌ No | 22% | <a href="https://www.brex.com/careers/8606534002?gh_jid=8606534002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Storage | DoorDash | San Francisco, CA; Seattle, WA; New York, NY | 2 | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/doordashusa/jobs/8024644"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Applied AI Engineer, Fullstack | Ramp | New York, NY (HQ) | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/ramp/6a7e382f-240a-4952-b9e5-7fe2b3856bc9"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Science Experts | Weekday AI | United States | Not specified | ❌ No | 15% | <a href="https://jobs.workable.com/view/uHAWJpuYHeu9GFHewRjN9T/remote-data-science-experts-in-united-states-at-weekday-ai"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Engineer, Product | Brex | San Francisco, California, United States | Not specified | ❌ No | 11% | <a href="https://www.brex.com/careers/8606845002?gh_jid=8606845002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Associate Software Engineer | OptiTrack | Corvallis, Oregon, United States | Not specified | ❌ No | 11% | <a href="https://jobs.workable.com/view/v9bPjPpxbu6w7ZW8rWPW6D/associate-software-engineer-in-corvallis-at-optitrack"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| 1675 - Software Engineer | Sigma Defense | Washington, District of Columbia, United States | Not specified | ❌ No | 7% | <a href="https://jobs.workable.com/view/9BDAEdPgw1jHZ9qHNcs3CU/1675---software-engineer-in-washington-at-sigma-defense"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| 1698 - Data Scientist | Sigma Defense | San Diego, California, United States | Not specified | ❌ No | 7% | <a href="https://jobs.workable.com/view/5TG657X6U2RNTsjjbehotc/1698---data-scientist-in-san-diego-at-sigma-defense"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Engineer, Ecosystem | Brex | San Francisco, California, United States | Not specified | ❌ No | 7% | <a href="https://www.brex.com/careers/8606890002?gh_jid=8606890002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Engineer, Ecosystem | Brex | Seattle, Washington, United States | Not specified | ❌ No | 7% | <a href="https://www.brex.com/careers/8606885002?gh_jid=8606885002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Network Engineer (with Programming) - Data & AI Systems | Weekday AI | United States | Not specified | ❌ No | 7% | <a href="https://jobs.workable.com/view/97B6bSoKgbRH74Pm2KWH75/remote-network-engineer-(with-programming)---data-%26-ai-systems-in-united-states-at-weekday-ai"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| 1504 - Software Systems Engineer | Sigma Defense | United States | Not specified | ❌ No | 4% | <a href="https://jobs.workable.com/view/6KRa9XjyrAfMYRMrMN979U/remote-1504---software-systems-engineer-in-united-states-at-sigma-defense"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-06-23 · 12 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer (Cloud, Cross-Platform & .NET Systems) | Altom Transport | Houston, Texas, United States | Not specified | ❌ No | 22% | <a href="https://jobs.workable.com/view/pvPiwA6W3djGdKJE4oRiQK/software-engineer-(cloud%2C-cross-platform-%26-.net-systems)-in-houston-at-altom-transport"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer (Cloud, Cross-Platform & .NET Systems) | Altom Transport | Chicago, Illinois, United States | Not specified | ❌ No | 22% | <a href="https://jobs.workable.com/view/bPcGwmRzWViLboS3bj3Kih/software-engineer-(cloud%2C-cross-platform-%26-.net-systems)-in-chicago-at-altom-transport"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer (ML Data & Annotation Pipelines) | Diversified Services Network, Inc. | Mossville, Illinois, United States | Not specified | ❌ No | 22% | <a href="https://jobs.workable.com/view/mVoGDsvx434Fsv3Pc9WRqB/software-engineer-(ml-data-%26-annotation-pipelines)-in-mossville-at-diversified-services-network%2C-inc."><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Business Analyst - Data & AI Practice | Coretek Services | United States | Not specified | ❌ No | 19% | <a href="https://jobs.workable.com/view/haz4PHpYb3Wkw14KXsQ8Mi/remote-business-analyst---data-%26-ai-practice-in-united-states-at-coretek-services"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer II, Backend (Infrastructure Platform) | Affirm | Remote US | 1.5 | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/affirm/jobs/7764834003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Solutions Strategist | Ramp | New York, NY (HQ) | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/ramp/cbdf2857-1675-4b68-8cb5-2f92a20faa75"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Junior Software Engineer (AI-Forward) | Texas Sports Academy Main | Austin, Texas, United States | 0-2 | ❌ No | 11% | <a href="https://jobs.workable.com/view/p9YoNg3zEXVYyMquLapXM7/junior-software-engineer-(ai-forward)-in-austin-at-texas-sports-academy-main"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Engineer / Data Modeler | Essnova Solutions, Inc. | United States | Not specified | ❌ No | 7% | <a href="https://jobs.workable.com/view/hM1hzkw267qBLj8urGjz5c/remote-data-engineer-%2F-data-modeler-in-united-states-at-essnova-solutions%2C-inc."><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Jr. AI Prompt Engineer | Ignite IT | Ashburn, Virginia, United States | 0-2 | ❌ No | 7% | <a href="https://jobs.workable.com/view/2tpEw5MgyfuWBmYZuPbD9d/remote-jr.-ai-prompt-engineer-in-ashburn-at-ignite-it"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer | Allego | Waltham, Massachusetts, United States | Not specified | ❌ No | 7% | <a href="https://jobs.workable.com/view/5MDBPGz7TxiTVLSXAcqXmQ/hybrid-software-engineer-in-waltham-at-allego"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Research Engineer – Agentic AI | Bosch | Sunnyvale, CA, United States | Not specified | ❌ No | 4% | <a href="https://jobs.smartrecruiters.com/BoschGroup/744000133692982"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Intern (Economic Development Data Analyst) | Steer | Pittsburgh, Pennsylvania, United States | Not specified | ❌ No | 4% | <a href="https://jobs.workable.com/view/4Dq2aKBjpeQXwfBQxANWNd/intern-(economic-development-data-analyst)-in-pittsburgh-at-steer"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-06-22 · 14 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Machine Learning Engineer | Reddit | New York City, NY | Not specified | ❌ No | 41% | <a href="https://job-boards.greenhouse.io/reddit/jobs/8014401"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Machine Learning Engineer | Reddit | San Francisco, CA | Not specified | ❌ No | 41% | <a href="https://job-boards.greenhouse.io/reddit/jobs/8014436"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer | Reddit | San Francisco, CA | Not specified | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/reddit/jobs/8013591"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Developer Productivity | Rubrik | Palo Alto, CA | 2 | ❌ No | 22% | <a href="https://www.rubrik.com/company/careers/departments/job.7922976?gh_jid=7922976"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Forward Deployment Engineer - Frontier AI Deployments | Accellor | Mountain View, California, United States | Not specified | ❌ No | 19% | <a href="https://jobs.workable.com/view/qU1WALePUyLWeSM3SrU9zM/hybrid-forward-deployment-engineer---frontier-ai-deployments-in-mountain-view-at-accellor"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Forward Deployment Engineer - Frontier AI Deployments | Accellor | San Francisco, California, United States | Not specified | ❌ No | 19% | <a href="https://jobs.workable.com/view/xa7cjZWy3KrLAighNZ43vN/hybrid-forward-deployment-engineer---frontier-ai-deployments-in-san-francisco-at-accellor"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Software Developer (req-257) | CATHEXIS | Tysons, Virginia, United States | Not specified | ❌ No | 11% | <a href="https://jobs.workable.com/view/i59ZsDc2Du3p2KcX6dcJdv/ai%2Fml-software-developer-(req-257)-in-tysons-at-cathexis"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Software Developer (req-259) | CATHEXIS | Redwood City, California, United States | Not specified | ❌ No | 11% | <a href="https://jobs.workable.com/view/uTvKkGydXPngs6oKPbbCLo/ai%2Fml-software-developer-(req-259)-in-redwood-city-at-cathexis"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Associate AI/ML Software Developer (req-256) | CATHEXIS | Tysons, Virginia, United States | Not specified | ❌ No | 11% | <a href="https://jobs.workable.com/view/fioZmnAbKWqJsr4YtQcb1N/associate-ai%2Fml-software-developer-(req-256)-in-tysons-at-cathexis"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Associate AI/ML Software Developer (req-258) | CATHEXIS | Redwood City, California, United States | Not specified | ❌ No | 11% | <a href="https://jobs.workable.com/view/65HU1Jh8cm9kmKkLXfDEDj/associate-ai%2Fml-software-developer-(req-258)-in-redwood-city-at-cathexis"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer in Security | Flexcompute Inc. | Watertown, Massachusetts, United States | Not specified | ❌ No | 11% | <a href="https://jobs.workable.com/view/1Wu9EJ8mkSnr4v6RJPNhrc/software-engineer-in-security-in-watertown-at-flexcompute-inc."><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Systems Engineer - Forward-Deployed Builder | AI Acquisition | United States | Not specified | ❌ No | 4% | <a href="https://jobs.workable.com/view/bYBM1XUdBbeG1c8KLjvPbh/remote-ai-systems-engineer---forward-deployed-builder-in-united-states-at-ai-acquisition"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Backend Engineer (NYC) | MLabs | New York, New York, United States | Not specified | ❌ No | 4% | <a href="https://jobs.workable.com/view/6AQjUPZGuvia6buDc3N3AZ/hybrid-backend-engineer-(nyc)-in-new-york-at-mlabs"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Infrastructure/Backend Engineer | MLabs | New York, New York, United States | Not specified | ❌ No | 4% | <a href="https://jobs.workable.com/view/srcxQ1aRFQm8rftXK4Qoe5/hybrid-infrastructure%2Fbackend-engineer-in-new-york-at-mlabs"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-06-20 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Embedded Software Engineer (Consumer Home) | TP-Link Systems Inc. | Irvine, California, United States | Not specified | ❌ No | 11% | <a href="https://jobs.workable.com/view/8vJyEYxzWfr74zHUjRv6DL/embedded-software-engineer-(consumer-home)-in-irvine-at-tp-link-systems-inc."><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Embedded Software Engineer (Wireless) | TP-Link Systems Inc. | Irvine, California, United States | Not specified | ❌ No | 11% | <a href="https://jobs.workable.com/view/8mYxUXFkjkWYhsPtH8er5e/embedded-software-engineer-(wireless)-in-irvine-at-tp-link-systems-inc."><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-06-19 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Data Analyst | Hack The Box | United States | Not specified | ❌ No | 15% | <a href="https://jobs.workable.com/view/vXH1Ce3ZPXjAcsc33h4pTS/remote-data-analyst-in-united-states-at-hack-the-box"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Full Stack Engineer (AI Platform) | WorldVia | Atlanta, Georgia, United States | Not specified | ❌ No | 15% | <a href="https://jobs.workable.com/view/c1ndtYyoKcHrTZ8pfPkfoy/hybrid-full-stack-engineer-(ai-platform)-in-atlanta-at-worldvia"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-06-18 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Data Analyst - Healthcare Payer | Tiger Analytics Inc. | Chicago, Illinois, United States | Not specified | ❌ No | 19% | <a href="https://jobs.workable.com/view/3XqWyLCmhTNqZjKf85zLfC/hybrid-data-analyst---healthcare-payer-in-chicago-at-tiger-analytics-inc."><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer II, Back-end (Card Mgmt & Transaction Processing) | Affirm | Remote US | 1.5 | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/affirm/jobs/7766277003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-06-17 · 3 roles · 1 H-1B sponsor match

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer, DevOps - Moveworks | ServiceNow | Mountain View, CALIFORNIA, United States | Not specified | ✅ Yes | 4% | <a href="https://jobs.smartrecruiters.com/ServiceNow/744000132715119"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Engineers | Accellor | Mountain View, California, United States | Not specified | ❌ No | 33% | <a href="https://jobs.workable.com/view/9kiDdviPjNupVTu6Yq4rQo/ai-engineers-in-mountain-view-at-accellor"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Engineers | Accellor | San Francisco, California, United States | Not specified | ❌ No | 33% | <a href="https://jobs.workable.com/view/1jCARuH9ADsR1oFDmF4iqF/ai-engineers-in-san-francisco-at-accellor"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-06-16 · 7 roles · 1 H-1B sponsor match

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Partner Business Development - AI & Data Transformation (Americas) | ServiceNow | Chicago, Illinois, United States | Not specified | ✅ Yes | 4% | <a href="https://jobs.smartrecruiters.com/ServiceNow/744000132426144"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Full Stack AI Developer | Enterprise Knowledge | Arlington, Virginia, United States | Not specified | ❌ No | 33% | <a href="https://jobs.workable.com/view/uxNr5H3YKc8gay9EbCykcq/hybrid-full-stack-ai-developer-in-arlington-at-enterprise-knowledge"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Full-Stack AI Engineer (evergreen) | Komodo Health | San Francisco, CA | Not specified | ❌ No | 26% | <a href="https://job-boards.greenhouse.io/komodohealth/jobs/8584991002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Full Stack Engineer, Mobile | Shift Robotics | Austin, Texas, United States | Not specified | ❌ No | 15% | <a href="https://jobs.workable.com/view/mArW32FUAj3w4ukYsS6Mox/full-stack-engineer%2C-mobile-in-austin-at-shift-robotics"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Operations Data Analyst II (Healthcare Claims Processing) | Healthcare Management Administrators | Bellevue, Washington, United States | Not specified | ❌ No | 11% | <a href="https://jobs.workable.com/view/9ohuQsnP4ZncteV8EAekKQ/remote-operations-data-analyst-ii-(healthcare-claims-processing)-in-bellevue-at-healthcare-management-administrators"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer | FairCom | Sandy, Utah, United States | Not specified | ❌ No | 7% | <a href="https://jobs.workable.com/view/iJQs5LjRLmDSDguWW2FoeL/hybrid-software-engineer-in-sandy-at-faircom"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer | FairCom | Columbia, Missouri, United States | Not specified | ❌ No | 7% | <a href="https://jobs.workable.com/view/nwEYQ1waB7NZ9G6yfzLWYH/hybrid-software-engineer-in-columbia-at-faircom"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
<!-- JOBS:END -->
