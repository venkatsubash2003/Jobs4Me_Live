<p align="center">
  <img alt="Update jobs" src="https://github.com/venkatsubash2003/Jobs4Me_Live/actions/workflows/update-jobs.yml/badge.svg">
  <img alt="Refresh every 6 hours" src="https://img.shields.io/badge/refresh-every%206%20hours-111827">
  <img alt="USA only" src="https://img.shields.io/badge/region-USA%20only-2563eb">
  <img alt="Early career" src="https://img.shields.io/badge/experience-0--2%20years-16a34a">
  <img alt="No result cap" src="https://img.shields.io/badge/results-no%20cap-f97316">
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

This scraper pulls from ATS boards configured in `data/ats_boards.yml` plus the larger imported inventory in `data/companies.json`. Supported systems include Greenhouse, Lever, Ashby, Workday, SmartRecruiters, Workable, Pinpoint, Breezy, and Avature. It also searches Workable's global jobs API for relevant U.S. roles.

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
| `FETCH_WORKERS` | Concurrent workers for non-Workday ATS boards, default `24`. |
| `WORKDAY_FETCH_WORKERS` | Concurrent workers for Workday boards, default `2` to reduce `429` rate limits. |
| `WORKDAY_BOARD_LIMIT` | Optional cap for Workday boards during debugging or constrained runs. Leave unset to attempt all imported Workday boards. |
| `H1B_SPONSORS_CSV_URL` | Optional CSV URL or local path with employer names from historical H-1B records. |

To use the PDF resume parser, place your resume at `resume/resume.pdf`. The workflow installs `pypdf`, so PDF parsing is available in GitHub Actions.

## Latest Matches

<!-- JOBS:START -->
_Last updated: 2026-06-25 18:01 UTC_

**Showing 2713 roles across 569 posting dates.** H-1B sponsor matches: **64**.

### 2026-06-25 · 19 roles · 2 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer - Moveworks | ServiceNow | Mountain View, CALIFORNIA, United States | 2 | ✅ Yes | 22% | <a href="https://jobs.smartrecruiters.com/ServiceNow/744000134304689"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Flex Solution Engineer | Snowflake | US-CA-Remote | 2 | ✅ Yes | 11% | <a href="https://jobs.ashbyhq.com/snowflake/7c0fa868-20c5-4727-9f22-a5ab4bfbc08b"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer II, Machine Learning (Feature Platform) | Affirm | Remote US | 1.5 | ❌ No | 26% | <a href="https://job-boards.greenhouse.io/affirm/jobs/7785600003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Product Engineer | PostHog | Remote | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/posthog/bd597451-e465-46f6-857f-befe28366f20"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Research Engineer / Research Scientist -Personal AGI, Proactivity | OpenAI | San Francisco | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/openai/e57d196b-4fa0-4463-bd33-d8189f0d3541"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer - Cloud Platform (Networks) | Neo4j | Malmö | Not specified | ❌ No | 22% | <a href="https://boards.greenhouse.io/neo4j/jobs/4692129006?gh_jid=4692129006"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Co-Op, ML Scientist for Biology | Lila Sciences | San Francisco, CA USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/lilasciences/jobs/4294212009"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Operations AI Engineer (Contract) | Front | Santiago, Chile | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/frontcareers/7a57e034-915d-4e44-9016-79fa3721b94a"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Research Engineer/Research Scientist - Personal AGI, North Stars | OpenAI | San Francisco | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/openai/171ebca6-de53-4d6e-a312-30332f353957"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Research Scientist - Computational Neuroscience | Astera | Hybrid | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/astera/0a1a566e-c48d-4605-b78f-458c234df670"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Insights | Benchling | San Francisco, CA | 2 | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/benchling/259613a6-686a-4756-82fd-e653d53e9904"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Associate Software Engineer – C++ (Computer Aided Manufacturing) | Protolabs | Brooklyn Park, MN | Not specified | ❌ No | 15% | <a href="https://jobs.lever.co/protolabs/9da2126b-76e7-4d10-aee7-ec97cbff5bec"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Infrastructure Engineer | Gauntlet | New York | 1 | ❌ No | 15% | <a href="https://jobs.lever.co/gauntlet/56230d07-8402-4ed8-99d2-cc76391108fa"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Engineer I | Frontier Medicines | South San Francisco, California, United States | Not specified | ❌ No | 11% | <a href="https://jobs.workable.com/view/t4nn6yTEUyur9CmKuJBZT1/ai-engineer-i-in-south-san-francisco-at-frontier-medicines"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Infrastructure Engineer | SpaceX | Redmond, WA | 1 | ❌ No | 11% | <a href="https://boards.greenhouse.io/spacex/jobs/8604308002?gh_jid=8604308002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Analytics Intern | Massachusetts Life Sciences Center | Waltham, Massachusetts, United States | Not specified | ❌ No | 7% | <a href="https://jobs.workable.com/view/mvWpDiUcZdFNPjmH6VdSxA/hybrid-data-analytics-intern-in-waltham-at-massachusetts-life-sciences-center"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Embedded Software Engineer | Icarus | El Segundo | 1 | ❌ No | 7% | <a href="https://job-boards.greenhouse.io/icarus/jobs/5279638008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Paid Research Participant – AI Training Study (Columbus, OH) | HumanSignal | Columbus, OH | Not specified | ❌ No | 7% | <a href="https://job-boards.greenhouse.io/humansignal/jobs/6101368004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Business Intelligence & Data Analytics Intern (Undergraduate) | Phamily | New York, NY | Not specified | ❌ No | 4% | <a href="https://job-boards.greenhouse.io/jobsatphamily/jobs/5281446008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-06-24 · 40 roles · 1 H-1B sponsor match

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Machine Learning Engineer, Agentic AI Systems - Moveworks | ServiceNow | Mountain View, CALIFORNIA, United States | Not specified | ✅ Yes | 37% | <a href="https://jobs.smartrecruiters.com/ServiceNow/744000134027173"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Machine Learning Intern- Immediate Start | Phamily | New York | Not specified | ❌ No | 41% | <a href="https://job-boards.greenhouse.io/jobsatphamily/jobs/5281239008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer (Apps & Firmware) | Western Digital | San Jose, CA, United States | 2 | ❌ No | 41% | <a href="https://jobs.smartrecruiters.com/WesternDigital/744000134025669"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer I | Aledade | Remote, United States | 1 | ❌ No | 37% | <a href="https://jobs.lever.co/aledade/1f5c4e2f-d8f7-4c55-aefb-d4bf300b1e6f"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Research Scientist (diffusion) | Genmo | San Francisco HQ | Not specified | ❌ No | 33% | <a href="https://jobs.ashbyhq.com/genmo/0f8462cc-c351-41b0-a794-3558c63646e2"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Analytics Engineer | Coinbase | Remote - USA | 2 | ❌ No | 30% | <a href="https://www.coinbase.com/careers/positions/8020892?gh_jid=8020892"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Engineer | Axle | Rockville, MD | Not specified | ❌ No | 30% | <a href="https://job-boards.greenhouse.io/axle/jobs/5172769007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Research Scientist (post-training) | Genmo | San Francisco HQ | Not specified | ❌ No | 30% | <a href="https://jobs.ashbyhq.com/genmo/f09286ef-c08d-49c4-8635-c1d952440865"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Associate Software Engineer | OptiTrack | Corvallis, Oregon, United States | Not specified | ❌ No | 26% | <a href="https://apply.workable.com/j/8350BCB8F9"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Machine Learning Engineer - Simulation Framework | Zoox | Foster City, CA | Not specified | ❌ No | 26% | <a href="https://jobs.lever.co/zoox/00694777-4083-426f-8382-3d0073c34787"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Scientist Intern | Nuro | Mountain View, California (HQ) | Not specified | ❌ No | 22% | <a href="https://nuro.ai/careersitem?gh_jid=7594577"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer II, Backend | Brex | Seattle, Washington, United States | 2 | ❌ No | 22% | <a href="https://www.brex.com/careers/8606540002?gh_jid=8606540002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer II, Backend | Brex | San Francisco, California, United States | 2 | ❌ No | 22% | <a href="https://www.brex.com/careers/8606538002?gh_jid=8606538002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer II, Backend | Brex | New York, New York, United States | 2 | ❌ No | 22% | <a href="https://www.brex.com/careers/8606534002?gh_jid=8606534002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer Intern | Auctane | Wrocław, PL | Not specified | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/auctane/jobs/7781233003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, ML Serving - Rime Ai | Unusual | San Francisco, California | Not specified | ❌ No | 22% | <a href="https://jobs.lever.co/unusual/ef80001d-bc4a-44e6-968c-d7270f80b618"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Sensor Integration | Mach9 | San Francisco | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/mach9/5449e5ee-fcd5-4243-851d-00b8230aadc9"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Applied ML/CS PhD Internship (6+ months) | Cartesian | Cambridge, MA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/cartesiansystems/jobs/4295536009"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Founding Data Engineer | Probably Genetic | San Francisco | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/probablygenetic/23feff17-8951-4e55-b9a0-5a47ffb0f7bf"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Storage | DoorDash | San Francisco, CA; Seattle, WA; New York, NY | 2 | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/doordashusa/jobs/8024644"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Applied AI Engineer, Fullstack | Ramp | New York, NY (HQ) | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/ramp/6a7e382f-240a-4952-b9e5-7fe2b3856bc9"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Science Experts | Weekday AI | United States | Not specified | ❌ No | 15% | <a href="https://jobs.workable.com/view/uHAWJpuYHeu9GFHewRjN9T/remote-data-science-experts-in-united-states-at-weekday-ai"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Jr .Net Developer with AI | qode.world | South Carolina, South Carolina, United States | 0-2 | ❌ No | 15% | <a href="https://apply.workable.com/j/F2AB12392E"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Development Engineer in Test | One Brief | United States \| Remote | 2 | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/onebrief/fbd0fd12-5aed-4428-9373-55ec2c5076f3"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer II | Sony Interactive Entertainment | United States, San Mateo, CA | Not specified | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/sonyinteractiveentertainmentglobal/jobs/6101023004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Dev Velocity (all levels) | Render | Remote: United States | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/render/a3f88090-5e37-43a7-b392-04b02056db6d"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Telemetry (Starlink) | SpaceX | Redmond, WA | 2 | ❌ No | 15% | <a href="https://boards.greenhouse.io/spacex/jobs/8606724002?gh_jid=8606724002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Engineer, Agentic Ad Creative (Multimodal) | NewsBreak | Mountain View, California, United States | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/newsbreak/jobs/4691989006"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Engineer, Product | Brex | San Francisco, California, United States | Not specified | ❌ No | 11% | <a href="https://www.brex.com/careers/8606845002?gh_jid=8606845002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Associate Software Engineer | OptiTrack | Corvallis, Oregon, United States | Not specified | ❌ No | 11% | <a href="https://jobs.workable.com/view/v9bPjPpxbu6w7ZW8rWPW6D/associate-software-engineer-in-corvallis-at-optitrack"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Backend Engineer (EST timezone) | PostHog | Remote | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/posthog/af00b414-fdb3-41b5-8843-828b4a0e373a"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Development Engineer in Test [Geospatial] | One Brief | United States \| Remote | 2 | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/onebrief/8ee26b8a-97dd-4035-95e2-6ebe657fa59b"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| 1675 - Software Engineer | Sigma Defense | Washington, District of Columbia, United States | Not specified | ❌ No | 7% | <a href="https://jobs.workable.com/view/9BDAEdPgw1jHZ9qHNcs3CU/1675---software-engineer-in-washington-at-sigma-defense"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| 1698 - Data Scientist | Sigma Defense | San Diego, California, United States | Not specified | ❌ No | 7% | <a href="https://jobs.workable.com/view/5TG657X6U2RNTsjjbehotc/1698---data-scientist-in-san-diego-at-sigma-defense"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Deployment Intern | Prodigal | Mumbai | Not specified | ❌ No | 7% | <a href="https://job-boards.greenhouse.io/prodigal/jobs/5172601007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Engineer, Ecosystem | Brex | San Francisco, California, United States | Not specified | ❌ No | 7% | <a href="https://www.brex.com/careers/8606890002?gh_jid=8606890002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Engineer, Ecosystem | Brex | Seattle, Washington, United States | Not specified | ❌ No | 7% | <a href="https://www.brex.com/careers/8606885002?gh_jid=8606885002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Network Engineer (with Programming) - Data & AI Systems | Weekday AI | United States | Not specified | ❌ No | 7% | <a href="https://jobs.workable.com/view/97B6bSoKgbRH74Pm2KWH75/remote-network-engineer-(with-programming)---data-%26-ai-systems-in-united-states-at-weekday-ai"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| 1504 - Software Systems Engineer | Sigma Defense | United States | Not specified | ❌ No | 4% | <a href="https://jobs.workable.com/view/6KRa9XjyrAfMYRMrMN979U/remote-1504---software-systems-engineer-in-united-states-at-sigma-defense"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Associate Sales Representative (Agentic AI Automation) | UiPath | Remote-Taipei | Not specified | ❌ No | 4% | <a href="https://jobs.ashbyhq.com/uipath/2347f629-ef49-4beb-bd56-e7d5d053030e"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-06-23 · 25 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Application Software Engineer (C#/ Python), Data | SpaceX | Starbase, TX | 2 | ❌ No | 41% | <a href="https://boards.greenhouse.io/spacex/jobs/8604664002?gh_jid=8604664002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Full Stack Engineer, Machine Learning Tooling | Flock Safety | Remote - USA | Not specified | ❌ No | 37% | <a href="https://jobs.ashbyhq.com/Flock%20Safety/edad75bb-6b93-46ff-b336-c45c96b93120"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer - ML/Computer Vision (Battery Sorting) | Redwood Materials | San Francisco, California, United States | 2 | ❌ No | 30% | <a href="https://boards.greenhouse.io/redwoodmaterials/jobs/6099577004?gh_jid=6099577004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Application Software Engineer, Manufacturing | SpaceX | Hawthorne, CA | 2 | ❌ No | 26% | <a href="https://boards.greenhouse.io/spacex/jobs/8603667002?gh_jid=8603667002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| NetSuite Application Developer | Bandwidth | Raleigh, NC | Not specified | ❌ No | 26% | <a href="https://job-boards.greenhouse.io/bandwidth/jobs/8011448"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer (ML Data & Annotation Pipelines) | Diversified Services Network, Inc. | Mossville, Illinois, United States | Not specified | ❌ No | 26% | <a href="https://jobs.workable.com/view/mVoGDsvx434Fsv3Pc9WRqB/software-engineer-(ml-data-%26-annotation-pipelines)-in-mossville-at-diversified-services-network%2C-inc."><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer (Cloud, Cross-Platform & .NET Systems) | Altom Transport | Houston, Texas, United States | Not specified | ❌ No | 22% | <a href="https://jobs.workable.com/view/pvPiwA6W3djGdKJE4oRiQK/software-engineer-(cloud%2C-cross-platform-%26-.net-systems)-in-houston-at-altom-transport"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer (Cloud, Cross-Platform & .NET Systems) | Altom Transport | Chicago, Illinois, United States | Not specified | ❌ No | 22% | <a href="https://jobs.workable.com/view/bPcGwmRzWViLboS3bj3Kih/software-engineer-(cloud%2C-cross-platform-%26-.net-systems)-in-chicago-at-altom-transport"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Deployment Engineer, Messenger Integrations | OpenAI | San Francisco | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/openai/f827e381-91a0-40b7-8ae9-b56540642a74"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Business Analyst - Data & AI Practice | Coretek Services | United States | Not specified | ❌ No | 19% | <a href="https://jobs.workable.com/view/haz4PHpYb3Wkw14KXsQ8Mi/remote-business-analyst---data-%26-ai-practice-in-united-states-at-coretek-services"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Junior DevOps Engineer | Threatlocker | Orlando, FL | 0-2 | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/threatlocker/jobs/6100007004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| ML/RL Engineer, Behavior Planning | Bot Auto | Houston, TX or San Francisco Bay Area | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/botauto/jobs/5277558008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer II, Backend (Infrastructure Platform) | Affirm | Remote US | 1.5 | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/affirm/jobs/7764834003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Solutions Strategist | Ramp | New York, NY (HQ) | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/ramp/cbdf2857-1675-4b68-8cb5-2f92a20faa75"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Chief Transformation and AI Officer | Penta Group | Remote | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/pentagrp/dbcf8bfe-80fa-410f-b3c1-1061c46f9abd"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Embedded Software Engineer, Satellite Antenna (Starlink) | SpaceX | Redmond, WA | 1 | ❌ No | 11% | <a href="https://boards.greenhouse.io/spacex/jobs/8603628002?gh_jid=8603628002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Junior Software Engineer (AI-Forward) | Texas Sports Academy Main | Austin, Texas, United States | 0-2 | ❌ No | 11% | <a href="https://jobs.workable.com/view/p9YoNg3zEXVYyMquLapXM7/junior-software-engineer-(ai-forward)-in-austin-at-texas-sports-academy-main"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Engineer / Data Modeler | Essnova Solutions, Inc. | United States | Not specified | ❌ No | 7% | <a href="https://jobs.workable.com/view/hM1hzkw267qBLj8urGjz5c/remote-data-engineer-%2F-data-modeler-in-united-states-at-essnova-solutions%2C-inc."><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Jr. AI Prompt Engineer | Ignite IT | Ashburn, Virginia, United States | 0-2 | ❌ No | 7% | <a href="https://jobs.workable.com/view/2tpEw5MgyfuWBmYZuPbD9d/remote-jr.-ai-prompt-engineer-in-ashburn-at-ignite-it"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer | Allego | Waltham, Massachusetts, United States | Not specified | ❌ No | 7% | <a href="https://jobs.workable.com/view/5MDBPGz7TxiTVLSXAcqXmQ/hybrid-software-engineer-in-waltham-at-allego"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Adoption Engineer | Cursor | Remote | Not specified | ❌ No | 4% | <a href="https://jobs.ashbyhq.com/cursor/ecc15f50-5d5b-4f79-a14c-e424b0c1bec6"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Research Engineer – Agentic AI | Bosch | Sunnyvale, CA, United States | Not specified | ❌ No | 4% | <a href="https://jobs.smartrecruiters.com/BoschGroup/744000133692982"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Founding Account Executive - Roboto AI | Unusual | Seattle, Washington | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/unusual/6db358ab-f0d5-4ff9-8585-c071e16ea37c"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Intern (Economic Development Data Analyst) | Steer | Pittsburgh, Pennsylvania, United States | Not specified | ❌ No | 4% | <a href="https://jobs.workable.com/view/4Dq2aKBjpeQXwfBQxANWNd/intern-(economic-development-data-analyst)-in-pittsburgh-at-steer"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Reporting Data Scientist | AECOM | Sacramento, CA, United States | Not specified | ❌ No | 4% | <a href="https://jobs.smartrecruiters.com/AECOM2/744000133687009"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-06-22 · 40 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Data Science Intern | Centerfield | Los Angeles, California | Not specified | ❌ No | 44% | <a href="https://jobs.ashbyhq.com/centerfield/916dcf42-d69a-4f00-875a-f8fe630e0f33"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer (Contract) | Civis Analytics | Chicago, IL; Washington, DC; Remote | 2 | ❌ No | 44% | <a href="https://job-boards.greenhouse.io/civisanalytics/jobs/8021887"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Machine Learning Engineer | Reddit | New York City, NY | Not specified | ❌ No | 41% | <a href="https://job-boards.greenhouse.io/reddit/jobs/8014401"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Machine Learning Engineer | Reddit | San Francisco, CA | Not specified | ❌ No | 41% | <a href="https://job-boards.greenhouse.io/reddit/jobs/8014436"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Machine Learning Engineer | Intuitive Surgical | San Francisco, CA, United States | Not specified | ❌ No | 26% | <a href="https://jobs.smartrecruiters.com/Intuitive/744000133419509"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer - Medical Applications & Algorithms | HeartFlow | San Francisco, California, United States | 2 | ❌ No | 26% | <a href="https://job-boards.greenhouse.io/heartflowinc/jobs/6098696004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Computer Vision Engineering Intern - Fall 2026 | Intuitive Surgical | Sunnyvale, CA, United States | Not specified | ❌ No | 22% | <a href="https://jobs.smartrecruiters.com/Intuitive/744000133458290"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Engineer | PrizePicks | Atlanta, GA preferred, Remote | Not specified | ❌ No | 22% | <a href="http://prizepicks.com/position?gh_jid=7777284003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer | Reddit | San Francisco, CA | Not specified | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/reddit/jobs/8013591"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Developer Productivity | Rubrik | Palo Alto, CA | 2 | ❌ No | 22% | <a href="https://www.rubrik.com/company/careers/departments/job.7922976?gh_jid=7922976"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Applied AI Research & Engineering Intern | AirCapture | Berkeley, CA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/aircapture/jobs/4687916006"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Forward Deployment Engineer - Frontier AI Deployments | Accellor | Mountain View, California, United States | Not specified | ❌ No | 19% | <a href="https://jobs.workable.com/view/qU1WALePUyLWeSM3SrU9zM/hybrid-forward-deployment-engineer---frontier-ai-deployments-in-mountain-view-at-accellor"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Forward Deployment Engineer - Frontier AI Deployments | Accellor | San Francisco, California, United States | Not specified | ❌ No | 19% | <a href="https://jobs.workable.com/view/xa7cjZWy3KrLAighNZ43vN/hybrid-forward-deployment-engineer---frontier-ai-deployments-in-san-francisco-at-accellor"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| LLM Ops Engineer | Heidi Health | Melbourne | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/heidihealth.com.au/028b77a2-0074-4333-9b3f-2dd408589582"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer II - (.Net) | PAR Tech | Gurugram | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/PAR%20Technology/5a44b2fe-8c62-49e2-82fe-2d3eee5e5502"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Engineering Systems | Apex | Los Angeles | 2 | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/apex-technology-inc/b14b559f-f540-4762-b327-af9a9f12e364"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Backend Engineer | PostHog | Remote | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/posthog/1803b1de-d33b-4542-8e38-b6c4954cb789"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Clinical Data Analyst II | Penumbra Inc | Your Remote US Home Office | 2 | ❌ No | 15% | <a href="https://jobs.lever.co/penumbrainc/f3263041-be26-4e97-9bb6-abf558cac6e7"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Infrastructure/Backend Engineer | MLabs | New York, New York, United States | Not specified | ❌ No | 15% | <a href="https://apply.workable.com/j/38B05E705D"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Project - Data Engineer | Deloitte | Multiple Locations | 1 | ❌ No | 15% | <a href="https://apply.deloitte.com/en_US/careers/JobDetail/Project-Data-Engineer/357376"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Site Reliability Engineer | StackAV | Pittsburgh, PA or Remote | Not specified | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/stackav/jobs/5170448007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Software Developer (req-257) | CATHEXIS | Tysons, Virginia, United States | Not specified | ❌ No | 11% | <a href="https://jobs.workable.com/view/i59ZsDc2Du3p2KcX6dcJdv/ai%2Fml-software-developer-(req-257)-in-tysons-at-cathexis"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Software Developer (req-259) | CATHEXIS | Redwood City, California, United States | Not specified | ❌ No | 11% | <a href="https://jobs.workable.com/view/uTvKkGydXPngs6oKPbbCLo/ai%2Fml-software-developer-(req-259)-in-redwood-city-at-cathexis"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Associate AI/ML Software Developer (req-256) | CATHEXIS | Tysons, Virginia, United States | Not specified | ❌ No | 11% | <a href="https://jobs.workable.com/view/fioZmnAbKWqJsr4YtQcb1N/associate-ai%2Fml-software-developer-(req-256)-in-tysons-at-cathexis"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Associate AI/ML Software Developer (req-258) | CATHEXIS | Redwood City, California, United States | Not specified | ❌ No | 11% | <a href="https://jobs.workable.com/view/65HU1Jh8cm9kmKkLXfDEDj/associate-ai%2Fml-software-developer-(req-258)-in-redwood-city-at-cathexis"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Backend Engineer (NYC) | MLabs | New York, New York, United States | Not specified | ❌ No | 11% | <a href="https://apply.workable.com/j/206E156BC4"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer in Security | Flexcompute Inc. | Watertown, Massachusetts, United States | Not specified | ❌ No | 11% | <a href="https://jobs.workable.com/view/1Wu9EJ8mkSnr4v6RJPNhrc/software-engineer-in-security-in-watertown-at-flexcompute-inc."><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Technical Recruiter, AI/ML | Waymo | Mountain View, California, USA | Not specified | ❌ No | 11% | <a href="https://careers.withwaymo.com/jobs?gh_jid=8010005"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Operator - Research Programs | Distyl | San Francisco | Not specified | ❌ No | 7% | <a href="https://jobs.ashbyhq.com/distyl/f726c016-a0b4-404a-9b83-8615cf141689"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Commissioning Platform Engineer | Blueprint Technologies | Atlanta, GA | 2 | ❌ No | 7% | <a href="https://job-boards.greenhouse.io/bpcs/jobs/8022473"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Analyst - Sales | Heidi Health | Melbourne | Not specified | ❌ No | 7% | <a href="https://jobs.ashbyhq.com/heidihealth.com.au/ce0ddab1-e9be-48b7-a48d-884caabffdab"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Deployment Associate, AI Solutions | Brellium | New York City | 2 | ❌ No | 7% | <a href="https://jobs.ashbyhq.com/brellium/65f55c9f-4614-4b41-a64b-0cdb6a55792e"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Development Engineer in Test II (SDET Contractor) | Sony Interactive Entertainment | United States, San Mateo, CA | Not specified | ❌ No | 7% | <a href="https://job-boards.greenhouse.io/sonyinteractiveentertainmentglobal/jobs/6099174004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Development Engineer in Test II (SDET Contractor) | Sony Interactive Entertainment | United States, Los Angeles, CA | Not specified | ❌ No | 7% | <a href="https://job-boards.greenhouse.io/sonyinteractiveentertainmentglobal/jobs/6020548004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, C++ (Simulations) | SpaceX | Hawthorne, CA | 2 | ❌ No | 7% | <a href="https://boards.greenhouse.io/spacex/jobs/8603609002?gh_jid=8603609002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Systems Engineer - Forward-Deployed Builder | AI Acquisition | United States | Not specified | ❌ No | 4% | <a href="https://jobs.workable.com/view/bYBM1XUdBbeG1c8KLjvPbh/remote-ai-systems-engineer---forward-deployed-builder-in-united-states-at-ai-acquisition"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Backend Engineer (NYC) | MLabs | New York, New York, United States | Not specified | ❌ No | 4% | <a href="https://jobs.workable.com/view/6AQjUPZGuvia6buDc3N3AZ/hybrid-backend-engineer-(nyc)-in-new-york-at-mlabs"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Analyst, ACO Operations - Part time, Contract | Pearl Health | Seattle, New York City, Boston, or Remote | Not specified | ❌ No | 4% | <a href="https://jobs.ashbyhq.com/pearlhealth/77c51f6c-ba07-4566-a247-f4f06ae16d6f"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Infrastructure/Backend Engineer | MLabs | New York, New York, United States | Not specified | ❌ No | 4% | <a href="https://jobs.workable.com/view/srcxQ1aRFQm8rftXK4Qoe5/hybrid-infrastructure%2Fbackend-engineer-in-new-york-at-mlabs"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Recruitment Intern - AI & Automation | Eulerity | New York, NY | Not specified | ❌ No | 4% | <a href="https://job-boards.greenhouse.io/eulerity/jobs/4691149006"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-06-21 · 4 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Applied AI Engineer, Silicon Engineering | Etched.ai | San Jose | Not specified | ❌ No | 30% | <a href="https://jobs.ashbyhq.com/Etched/831bfa22-d883-450b-9b10-2a16421525a0"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Analyst Internship | ConnectPrep | Boston, Massachusetts, United States | Not specified | ❌ No | 22% | <a href="https://apply.workable.com/j/E4655645B8"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/HPC/NeoCloud Pre-Sales System Engineer UAE | Pure Storage | Dubai, UAE | Not specified | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/purestorage/jobs/8001588"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, C++ (Dragon) | SpaceX | Hawthorne, CA | 2 | ❌ No | 7% | <a href="https://boards.greenhouse.io/spacex/jobs/8601802002?gh_jid=8601802002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-06-20 · 5 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| ML Engineer, Generative Video | Mirage | Union Square, New York City | 2 | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/mirage/d8b43e0a-3a1a-462a-a845-6ed888c08b57"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| ML Engineer, Agentic Systems | Mirage | Union Square, New York City | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/mirage/dc97e719-f69a-47bb-812e-1ea9e7693662"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS | Mirage | Union Square, New York City | 2 | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/mirage/7dca065e-c70d-453d-b0d4-5c75b283d136"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Embedded Software Engineer (Consumer Home) | TP-Link Systems Inc. | Irvine, California, United States | Not specified | ❌ No | 11% | <a href="https://jobs.workable.com/view/8vJyEYxzWfr74zHUjRv6DL/embedded-software-engineer-(consumer-home)-in-irvine-at-tp-link-systems-inc."><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Embedded Software Engineer (Wireless) | TP-Link Systems Inc. | Irvine, California, United States | Not specified | ❌ No | 11% | <a href="https://jobs.workable.com/view/8mYxUXFkjkWYhsPtH8er5e/embedded-software-engineer-(wireless)-in-irvine-at-tp-link-systems-inc."><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-06-19 · 9 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Backend Engineer | Mem0 | San Francisco Bay Area | 2 | ❌ No | 26% | <a href="https://jobs.ashbyhq.com/mem0/77259c2d-aaa7-4d6d-a206-75f1a36f997d"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Full Stack Engineer | Mem0 | San Francisco Bay Area | 2 | ❌ No | 26% | <a href="https://jobs.ashbyhq.com/mem0/6b1ed871-ddb6-4910-a320-eea2c4d3671a"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Solutions Engineer (Fixed-Term) | Field AI | Irvine, CA | Not specified | ❌ No | 19% | <a href="https://jobs.lever.co/field-ai/65561b5c-2348-4b88-9e73-ff9c6265dbf4"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Analyst | Hack The Box | United States | Not specified | ❌ No | 15% | <a href="https://jobs.workable.com/view/vXH1Ce3ZPXjAcsc33h4pTS/remote-data-analyst-in-united-states-at-hack-the-box"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Embedded Software Engineer | ALTEN Technology | Lafayette, CO | Not specified | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/altentechnologyusa/jobs/5169765007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Full Stack Engineer (AI Platform) | WorldVia | Atlanta, Georgia, United States | Not specified | ❌ No | 15% | <a href="https://jobs.workable.com/view/c1ndtYyoKcHrTZ8pfPkfoy/hybrid-full-stack-engineer-(ai-platform)-in-atlanta-at-worldvia"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Forward Deployed Engineer, (AI) - Acom | Valsoft Corporation | Beirut, Beirut Governorate, Lebanon | Not specified | ❌ No | 7% | <a href="https://apply.workable.com/j/A58C4FF905"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Sensor Platform | Nuro | Mountain View, California (HQ) | 2 | ❌ No | 7% | <a href="https://nuro.ai/careersitem?gh_jid=8017598"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Creative Designer, Email | Hightouch | Remote, United States | Not specified | ❌ No | 4% | <a href="https://job-boards.greenhouse.io/hightouch/jobs/6097447004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-06-18 · 31 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Data Engineer | Horizon Surgical Systems | Los Angeles, California | 2 | ❌ No | 33% | <a href="https://job-boards.greenhouse.io/horizonsurgicalsystems/jobs/5166527007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Perception | Hayden AI | San Francisco HQ Office | Not specified | ❌ No | 33% | <a href="https://jobs.ashbyhq.com/haydenai/5baa44bf-e5c5-4544-960f-87131bd5b078"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Application Software Engineer, Inference | SpaceX | Palo Alto, CA | 2 | ❌ No | 30% | <a href="https://boards.greenhouse.io/spacex/jobs/8598844002?gh_jid=8598844002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Deep Learning Engineer | Hayden AI | San Francisco HQ Office | 2 | ❌ No | 30% | <a href="https://jobs.ashbyhq.com/haydenai/f9da378a-156e-4fa4-8d8c-34580a05b4c9"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Fullstack Software Engineer, New Grad | Hadrian | Los Angeles, CA | 0-2 | ❌ No | 30% | <a href="https://jobs.ashbyhq.com/hadrian-automation/41472a42-c3c3-40bd-a784-8a3fbab47be3"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Application Software Engineer, Manufacturing Systems | SpaceX | Redmond, WA | 2 | ❌ No | 26% | <a href="https://boards.greenhouse.io/spacex/jobs/8600019002?gh_jid=8600019002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Application Software Engineer, Manufacturing Systems | SpaceX | Bastrop, TX | 2 | ❌ No | 26% | <a href="https://boards.greenhouse.io/spacex/jobs/8600012002?gh_jid=8600012002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Full Stack Software Engineer (Application Software) | SpaceX | Redmond, WA | 2 | ❌ No | 26% | <a href="https://boards.greenhouse.io/spacex/jobs/8600005002?gh_jid=8600005002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer | FanDuel | Atlanta, Georgia, United States | Not specified | ❌ No | 26% | <a href="https://www.fanduel.careers/open-positions?gh_jid=8016515"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Product Experiences | Peregrine | San Francisco, California, Unites States | 2 | ❌ No | 26% | <a href="https://job-boards.greenhouse.io/peregrinetechnologies/jobs/4704820005"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Engineer, Evaluation | Distyl | San Francisco | 2 | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/distyl/13aa2aa1-e5e4-4bab-b2ea-7d8ff5658076"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Science Intern | Doctors Without Borders | New York, New York, United States | Not specified | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/msfcareers/jobs/5271141008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Forward Deployed AI Engineer | Distyl | San Francisco | 2 | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/distyl/46728319-c47a-48c8-bbfb-af0d9bff2ea2"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, PCBA (Starlink) | SpaceX | Redmond, WA | 1 | ❌ No | 22% | <a href="https://boards.greenhouse.io/spacex/jobs/8584271002?gh_jid=8584271002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Analyst | 2K | Novato, California, United States | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/2k/jobs/7651067003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Analyst - Healthcare Payer | Tiger Analytics Inc. | Chicago, Illinois, United States | Not specified | ❌ No | 19% | <a href="https://jobs.workable.com/view/3XqWyLCmhTNqZjKf85zLfC/hybrid-data-analyst---healthcare-payer-in-chicago-at-tiger-analytics-inc."><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Analyst – Quality & Customer Satisfaction | ALTEN Technology | Greensboro, North Carolina | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/altentechnologyusa/jobs/5168949007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer | LINQ | Birmingham | 2 | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/linqapp/a80957d5-94b1-4be4-9d1b-f396ec3b36eb"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer II, Back-end (Card Mgmt & Transaction Processing) | Affirm | Remote US | 1.5 | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/affirm/jobs/7766277003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Backend Engineer, Identity | Tailscale | Remote (United States) | Not specified | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/tailscale/jobs/4707649005"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Site Reliability Engineer | Allegiant Air | Las Vegas, NV | Not specified | ❌ No | 15% | <a href="https://jobs.lever.co/allegiantair/d373daf3-798e-427d-a6f4-c112633e5697"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Frontend Engineer | Tailscale | Remote (United States) | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/tailscale/jobs/4707457005"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Infrastructure Engineer - Oracle DBA | Warner Music | Bangalore | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/wmg/cc5124f5-1380-474e-95a5-611dad0654fe"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Marketing Intern | Exowatt | Miami, FL | Not specified | ❌ No | 7% | <a href="https://jobs.lever.co/exowatt/2f9e8254-401b-4f77-adcb-c4f01734c8fb"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Systems Engineer (Level 1) | New Era Technology | Nelson | Not specified | ❌ No | 7% | <a href="https://job-boards.greenhouse.io/neweratech/jobs/8575481002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Language Trainer - Korean | Wing Assistant | Busan | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/getwingapp/41c2c772-69e0-4242-8b90-f57253427679"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Language Trainer - Korean | Wing Assistant | Daejeon | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/getwingapp/3e54ecd8-3431-421e-a764-73338b475b8f"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Language Trainer - Korean | Wing Assistant | Daegu | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/getwingapp/4e443fe0-d6b0-4001-a236-d5c6bf503c60"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Language Trainer - Korean | Wing Assistant | Seongnam, Gyeonggi Province | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/getwingapp/61601cb3-74ba-41a4-80a8-dc97273737f2"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Associate Data Scientist I | AbbVie | North Chicago, IL, United States | Not specified | ❌ No | 4% | <a href="https://jobs.smartrecruiters.com/AbbVie/3743990013697956"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Associate Sales Representative (Agentic AI Automation) | UiPath | Shanghai | Not specified | ❌ No | 4% | <a href="https://jobs.ashbyhq.com/uipath/9d35ebad-7978-4acd-926e-0e416da4c7eb"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-06-17 · 21 roles · 1 H-1B sponsor match

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer, DevOps - Moveworks | ServiceNow | Mountain View, CALIFORNIA, United States | Not specified | ✅ Yes | 4% | <a href="https://jobs.smartrecruiters.com/ServiceNow/744000132715119"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer | Coinbase | Charlotte, NC | 2 | ❌ No | 37% | <a href="https://www.coinbase.com/careers/positions/8003605?gh_jid=8003605"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Engineers | Accellor | Mountain View, California, United States | Not specified | ❌ No | 33% | <a href="https://jobs.workable.com/view/9kiDdviPjNupVTu6Yq4rQo/ai-engineers-in-mountain-view-at-accellor"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Engineers | Accellor | San Francisco, California, United States | Not specified | ❌ No | 33% | <a href="https://jobs.workable.com/view/1jCARuH9ADsR1oFDmF4iqF/ai-engineers-in-san-francisco-at-accellor"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Full Stack Engineer | David AI | San Francisco | 2 | ❌ No | 33% | <a href="https://jobs.ashbyhq.com/david-ai/5d727f24-c97a-4344-9a7c-f2da5220f86e"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Machine Learning Engineer | Quantcast | San Francisco, CA | 1 | ❌ No | 33% | <a href="https://jobs.lever.co/quantcast/85c49bea-f862-4972-a334-a8e24d47fec7"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Prompt Engineer (Contract) | Netomi | Gurugram | Not specified | ❌ No | 33% | <a href="https://jobs.lever.co/netomi/21d1bdfc-5f7b-4aa9-934b-e9ec02d5788f"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer 2, Autonomous Lab | Ginkgo Bioworks | Boston, Massachusetts | Not specified | ❌ No | 30% | <a href="https://job-boards.greenhouse.io/ginkgobioworks/jobs/5166911007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Applied AI Engineer, Advertising Agents | NewsBreak | Mountain View, California, United States | 2 | ❌ No | 26% | <a href="https://job-boards.greenhouse.io/newsbreak/jobs/4690262006"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Backend | Mirage | Union Square, New York City | 2 | ❌ No | 26% | <a href="https://jobs.ashbyhq.com/mirage/3988e47d-d596-4b5c-8f21-a851b97873ea"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Forward Deployed ML Engineer | Triomics | New York Office | 2 | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/triomics/df6ea402-6286-4461-b628-5821cfcb92b4"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Deployment Analyst | Silna Health | NYC | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/silnahealth.com/28ba5d0b-b862-4e04-995d-d5eff22d269e"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Full Stack Software Engineer, Agent Enablement | OpenAI | San Francisco | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/openai/2d7f1028-ce9b-49c7-acc8-782714ca1cf4"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer II, Onboarding - Ripple | The Job Sauce | San Francisco (Hybrid) | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/The%20Job%20Sauce/58106dc9-e2e6-4fa3-b34e-9021c23d40b3"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Avionics Systems Engineer | Rocket Lab USA | Auckland, NZ | 2 | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/rocketlab/jobs/7776990003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Backend Software Engineer | Hadrian | Los Angeles, CA | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/hadrian-automation/ec8cc324-bca9-4f27-812b-70416d6340a4"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Financial Data Analyst - Power Platform Specialist #2967 | Wade Trim | Taylor, MI | 2 | ❌ No | 15% | <a href="https://jobs.lever.co/wadetrim/96c817b6-56d8-49fc-baa5-ec62725e9039"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer II | Deloitte | Hermitage, Tennessee, United States | 1 | ❌ No | 15% | <a href="https://apply.deloitte.com/en_US/careers/JobDetail/Software-Engineer-II/356998"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer II, Pipeline Automation & Acceleration | Aurora Innovation | Pittsburgh, Pennsylvania | Not specified | ❌ No | 15% | <a href="https://aurora.tech/jobs/8591934002?gh_jid=8591934002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Networking (Features) | Tailscale | Remote (United States) | Not specified | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/tailscale/jobs/4706998005"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Implementation Engineer - Lumina AI | Valsoft Corporation | Beirut, Beirut Governorate, Lebanon | Not specified | ❌ No | 7% | <a href="https://apply.workable.com/j/F9D9780D4A"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-06-16 · 20 roles · 3 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| AI Research Scientist, New Grad – Agents & Reinforcement Learning | Snowflake | US-WA-Bellevue | 0-2 | ✅ Yes | 30% | <a href="https://jobs.ashbyhq.com/snowflake/1bad12df-f443-426f-9d09-e96fc780d698"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer | Stripe | New York, NY | 2 | ✅ Yes | 22% | <a href="https://stripe.com/jobs/search?gh_jid=8009143"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Partner Business Development - AI & Data Transformation (Americas) | ServiceNow | Chicago, Illinois, United States | Not specified | ✅ Yes | 4% | <a href="https://jobs.smartrecruiters.com/ServiceNow/744000132426144"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Full Stack AI Developer | Enterprise Knowledge | Arlington, Virginia, United States | Not specified | ❌ No | 33% | <a href="https://jobs.workable.com/view/uxNr5H3YKc8gay9EbCykcq/hybrid-full-stack-ai-developer-in-arlington-at-enterprise-knowledge"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Junior Data Scientist | Oura | Hybrid - Helsinki, Uusimaa; Hybrid - Oulu, North Ostrobothnia | 2 | ❌ No | 30% | <a href="https://job-boards.greenhouse.io/oura/jobs/4287026009"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, ML Infrastructure, Optimization | Nuro | Mountain View, California (HQ) | 2 | ❌ No | 30% | <a href="https://nuro.ai/careersitem?gh_jid=6916236"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Application Software Engineer, Safety & Training | SpaceX | Hawthorne, CA | 2 | ❌ No | 26% | <a href="https://boards.greenhouse.io/spacex/jobs/8593365002?gh_jid=8593365002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Full-Stack AI Engineer (evergreen) | Komodo Health | San Francisco, CA | Not specified | ❌ No | 26% | <a href="https://job-boards.greenhouse.io/komodohealth/jobs/8584991002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Engineer Associate | American Institutes for Research | US-VA-Arlington | 2 | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/americaninstitutesforresearch/jobs/5263560008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Full Stack Engineer, Mobile | Shift Robotics | Austin, Texas, United States | Not specified | ❌ No | 15% | <a href="https://jobs.workable.com/view/mArW32FUAj3w4ukYsS6Mox/full-stack-engineer%2C-mobile-in-austin-at-shift-robotics"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer Intern/Co-Op - Fall 2026 | SoloPulse | Peachtree Corners, GA | Not specified | ❌ No | 15% | <a href="https://jobs.lever.co/solopulseco/00fbde18-a387-4c9f-97d4-77059aec7b56"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Operations Data Analyst II (Healthcare Claims Processing) | Healthcare Management Administrators | Bellevue, Washington, United States | Not specified | ❌ No | 11% | <a href="https://jobs.workable.com/view/9ohuQsnP4ZncteV8EAekKQ/remote-operations-data-analyst-ii-(healthcare-claims-processing)-in-bellevue-at-healthcare-management-administrators"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer (Fullstack) - Core Applications Workflows | Addepar | New York, NY | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/addepar1/jobs/8590337002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Platform Engineer - Remote | Mindex | Rochester, New York, United States | Not specified | ❌ No | 7% | <a href="https://jobs.workable.com/view/hpSAtM9LXs6duy8B16uH6S/data-platform-engineer---remote-in-rochester-at-mindex"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Embedded Software Engineer - Research And Development (R&D) | Silvus Technologies | Los Angeles | 2 | ❌ No | 7% | <a href="https://job-boards.greenhouse.io/silvus/jobs/5263735008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Fullstack Engineer | Picogrid | El Segundo, CA | Not specified | ❌ No | 7% | <a href="https://jobs.ashbyhq.com/picogrid/406a5209-a27c-4340-83a0-ea3c26b515f3"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer | FairCom | Sandy, Utah, United States | Not specified | ❌ No | 7% | <a href="https://jobs.workable.com/view/iJQs5LjRLmDSDguWW2FoeL/hybrid-software-engineer-in-sandy-at-faircom"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer | FairCom | Columbia, Missouri, United States | Not specified | ❌ No | 7% | <a href="https://jobs.workable.com/view/nwEYQ1waB7NZ9G6yfzLWYH/hybrid-software-engineer-in-columbia-at-faircom"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer II | Sony Interactive Entertainment | United States, San Mateo, CA | Not specified | ❌ No | 7% | <a href="https://job-boards.greenhouse.io/sonyinteractiveentertainmentglobal/jobs/6018473004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer II | Mediavine | Atlanta, Georgia, United States | Not specified | ❌ No | 7% | <a href="https://jobs.workable.com/view/qnVTMAAGgeD2VYXdEGtMTb/remote-software-engineer-ii-in-atlanta-at-mediavine"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-06-15 · 13 roles · 1 H-1B sponsor match

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Full-Stack Engineer | Stripe | San Francisco | 1 | ✅ Yes | 15% | <a href="https://stripe.com/jobs/search?gh_jid=8003382"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Scientist 1 | Adswerve | United States - Remote | Not specified | ❌ No | 30% | <a href="https://job-boards.greenhouse.io/adswerveinc/jobs/5159086007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| People Research Data Scientist, AI Fairness & Bias | OpenAI | San Francisco | Not specified | ❌ No | 30% | <a href="https://jobs.ashbyhq.com/openai/cadb7c24-2aea-4b98-a793-65ae9388b5d6"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Junior AI/ML Engineer | Node.Digital | Herndon, Virginia, United States | 0-2 | ❌ No | 26% | <a href="https://jobs.workable.com/view/tnF3oMi9HKzzNrZnKqZ6et/hybrid-junior-ai%2Fml-engineer-in-herndon-at-node.digital"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Full Stack Software Engineer, ChatGPT Finances | OpenAI | San Francisco | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/openai/39e06ef9-5e62-425d-81e2-e8690188011f"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Developer With .Net & AI | qode.world | South Carolina, South Carolina, United States | Not specified | ❌ No | 19% | <a href="https://apply.workable.com/j/CD0A6BEB90"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Embedded Software Engineer | Silvus Technologies | Los Angeles | 2 | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/silvus/jobs/5263661008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Embedded Software Engineer | Silvus Technologies | Irvine CA | 2 | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/silvus/jobs/5263637008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Quality Engineering Intern, AI/ML | Rocket Lawyer | Arizona ; California; Colorado ; North Carolina ; Utah | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/rocketlawyer/jobs/5263173008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Salesforce Ads Systems Engineer | OpenAI | San Francisco | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/openai/da45caa7-461d-478f-a862-82120dd80e19"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer II | Pinterest | City, State, Country; Remote, CA, US | Not specified | ❌ No | 11% | <a href="https://www.pinterestcareers.com/jobs/?gh_jid=7958766"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Junior Business & Data Analyst | Upgrade | United States (Remote) | 2 | ❌ No | 7% | <a href="https://job-boards.greenhouse.io/upgrade/jobs/4706312005"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Analyst 4 | TOMORROW HIRE | Richmond, Virginia, United States | Not specified | ❌ No | 4% | <a href="https://jobs.workable.com/view/442UC7hD3HsSH98ZrtX9ZS/data-analyst-4-in-richmond-at-tomorrow-hire"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-06-14 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer, Knowledge Systems | Exa Labs | San Francisco, California | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/exa/1f90ebb9-0f74-4a52-822a-d0ea6acdef4f"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-06-13 · 4 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| AI Product Engineer | Brain Co. | New York City, NY | 2 | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/brainco/39660079-dc7e-4974-8ab1-900c45198bcf"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Intern, Production Data Analytics | Harbinger Motors | Garden Grove, CA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/harbingermotors/jobs/5164341007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Product Marketing Intern - AI & Automation | Eulerity | New York, NY | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/eulerity/jobs/4689231006"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer Full Stack | Faro Health Inc. | San Diego, United States | Not specified | ❌ No | 11% | <a href="https://jobs.workable.com/view/aaZAevGisCEsAcbmNoVieb/hybrid-software-engineer-full-stack-in-san-diego-at-faro-health-inc."><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-06-12 · 21 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Data Engineer | PlusAI | Santa Clara, CA | 1 | ❌ No | 33% | <a href="https://jobs.lever.co/plus-2/083142f4-70ed-40f4-8726-a5f99ea52e36"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, GeniusIQ | Genius Sports | Los Angeles, California, United States | Not specified | ❌ No | 33% | <a href="https://boards.greenhouse.io/geniussports/jobs/7765006003?gh_jid=7765006003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Developer | Atlas Energy Solutions | Austin TX | Not specified | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/atlassand/jobs/8589983002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Research Internship - WM | Institute of Foundation Models | Sunnyvale, CA | Not specified | ❌ No | 22% | <a href="https://jobs.lever.co/ifm-us/3eec355c-6dde-4a3e-8cdf-b2a8930d5678"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data & Software Engineer | Avalore, LLC | Chantilly, Virginia, United States | Not specified | ❌ No | 22% | <a href="https://jobs.workable.com/view/h5W4UFTThjon6AUd4doS1b/data-%26-software-engineer-in-chantilly-at-avalore%2C-llc"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Analyst | Alpaca | Remote - Americas | Not specified | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/alpaca/jobs/6020810004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| IC Layout Automation Software Engineer | Rigetti | Fremont, CA | Not specified | ❌ No | 22% | <a href="https://jobs.lever.co/rigetti/515ec1e2-bbdc-4488-b062-32f6f124c239"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer - Data Movement Platform | Reddit | Remote - United States | 2 | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/reddit/jobs/7997866"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Analytics Associate (Marketing Science) | LG Ad Solutions | New York, NY | 2 | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/lgads/c049db92-3ae6-4022-84fa-821e4fed3253"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer (Java) (f/m/d) | Sonar | Bochum | Not specified | ❌ No | 19% | <a href="https://jobs.lever.co/sonarsource/cc369955-e130-48c1-bc1a-160df00e0e4b"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Computer Use & Frontier Interfaces | OpenAI | San Francisco | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/openai/39a709f3-6e9e-45e9-94eb-43a1c2aaaeaf"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Automation and Controls Software Engineer | Varda Space | El Segundo, California, United States | 2 | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/vardaspace/jobs/7770810003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Frontend Software Engineer | Hawk-Eye Innovations | Hungary, Budapest | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/hawkeyeinnovations/fbfe24c9-3f8d-46f1-859b-463e3fa3c97a"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Frontend Software Engineer | Hawk-Eye Innovations | Hungary, Budapest | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/hawkeyeinnovations/71414dbb-1123-4f42-9ae3-405060eecec0"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Frontend Software Engineer | Hawk-Eye Innovations | Hungary, Budapest | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/hawkeyeinnovations/bdc84b0b-3a5b-4610-a022-bc4dc2adde30"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Jr Software Engineer | LG Electronics | Alpharetta, GA | 1 | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/lgelectronics/jobs/5255339008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Platform Engineer | Defense Unicorns | Remote | Not specified | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/defenseunicorns/jobs/5163507007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Equities Data Engineer | DRW | Chicago, New York | Not specified | ❌ No | 7% | <a href="https://job-boards.greenhouse.io/drweng/jobs/8003321"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer II, Strategic Integrations | Attentive | United States | Not specified | ❌ No | 7% | <a href="https://job-boards.greenhouse.io/attentive/jobs/4260923009"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Business Partner | Atlas Energy Solutions | Austin TX | Not specified | ❌ No | 4% | <a href="https://job-boards.greenhouse.io/atlassand/jobs/8589859002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Remote Web Developer & Digital Analytics Specialist | Datamark, Inc. | El Paso, Texas, United States | Not specified | ❌ No | 4% | <a href="https://jobs.workable.com/view/aPiTahJfHgkzuTYfXVkLDe/remote-web-developer-%26-digital-analytics-specialist-in-el-paso-at-datamark%2C-inc."><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-06-11 · 21 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Co-op, Machine Learning for Digital Twins | Lila Sciences | Cambridge, MA USA | Not specified | ❌ No | 30% | <a href="https://job-boards.greenhouse.io/lilasciences/jobs/4280809009"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Applied AI Engineer | Bandwidth | Raleigh, NC | Not specified | ❌ No | 26% | <a href="https://job-boards.greenhouse.io/bandwidth/jobs/8001620"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer II, Backend (ML Training & Serving) | Affirm | Remote US | 1.5 | ❌ No | 26% | <a href="https://job-boards.greenhouse.io/affirm/jobs/7762568003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, X-Scientist | Xaira Therapeutics | South San Francisco, California, United States | Not specified | ❌ No | 26% | <a href="https://job-boards.greenhouse.io/xairatherapeutics/jobs/5161853007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| 2027 Early Career Software Engineer | Anduril | Atlanta, Georgia, United States; Boston, Massachusetts, United States; Costa Mesa, California, United States; Irvine, California, United States; Reston, Virginia, United States; Seattle, Washington, United States | 0-2 | ❌ No | 22% | <a href="https://boards.greenhouse.io/andurilindustries/jobs/5162263007?gh_jid=5162263007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Co-Op, AI Security | Lila Sciences | Cambridge, MA USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/lilasciences/jobs/4280945009"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Full Stack Software Engineer, Codex | OpenAI | San Francisco | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/openai/5ebd5f66-75db-4a96-8d39-babc14f1c582"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Web Layer | OpenAI | San Francisco | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/openai/915a325b-55f6-44e2-8314-34ec0d8bb2c9"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Founders Initiatives, AI Agents | Retell AI | San Francisco Bay Area | 2 | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/retell-ai/21cf0117-6b44-40df-96ea-0fb2d1d0892f"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer II | Verisign | Reston,Virginia,United States | 2 | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/verisign/jobs/7765684003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer in Test – C# / WPF | CaseGuard | Arlington, VA | 2 | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/caseguard/jobs/5255159008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer – Motion & Behavioral Planning | DiDi Global | San Jose, CA | Not specified | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/didi/jobs/8001908"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Engineer - Bilingual Mandarin required | CWILL | Cary, North Carolina, United States | Not specified | ❌ No | 11% | <a href="https://jobs.workable.com/view/pAyfkTDdUnDLvdvcGtRo8t/hybrid-data-engineer---bilingual-mandarin-required-in-cary-at-cwill"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Engineer - Bilingual Mandarin required | CWILL | Los Angeles, California, United States | Not specified | ❌ No | 11% | <a href="https://jobs.workable.com/view/rgZcfgC87aAFZUAR5LPsjz/hybrid-data-engineer---bilingual-mandarin-required-in-los-angeles-at-cwill"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer (Embedded) | Freeform | Los Angeles, CA (On-site) | 2 | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/freeformfuturecorp/jobs/7770777003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Core Infrastructure | Poshmark | Redwood City, California, USA | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/poshmark/1ad97af4-ef83-4e6d-be50-f966d4520f58"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Analyst | Sand Cherry Associates | Denver, Colorado, United States | Not specified | ❌ No | 7% | <a href="https://jobs.workable.com/view/sQsiwhu7rvJpRqEL9xKwof/hybrid-data-analyst-in-denver-at-sand-cherry-associates"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Analyst | Panelmatic | Houston, Texas, United States | Not specified | ❌ No | 7% | <a href="https://jobs.workable.com/view/eeVKoRYh1kvsuYnkWcAtKC/data-analyst-in-houston-at-panelmatic"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Hiring our Heroes Fellowship (12-week program) - AI & Engineering | Deloitte | Multiple Locations | 2 | ❌ No | 7% | <a href="https://apply.deloitte.com/en_US/careers/JobDetail/Hiring-our-Heroes-Fellowship-12-week-program-AI-Engineering/356045"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Strategy & Ops Associate, Applied AI | Clipboard Health | Remote (Non-U.S.) | Not specified | ❌ No | 4% | <a href="https://jobs.ashbyhq.com/clipboard/48b39937-d8fa-467b-beb0-4fdebfe7bd9f"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Strategy & Ops Associate, Applied AI | Clipboard Health | U.S. (Remote) | Not specified | ❌ No | 4% | <a href="https://jobs.ashbyhq.com/clipboard/f9ec8cfe-9eb2-4b10-9942-a36c2fe0cc20"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-06-10 · 12 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer, Test Infrastructure (Application Software) | SpaceX | Hawthorne, CA | 2 | ❌ No | 26% | <a href="https://boards.greenhouse.io/spacex/jobs/8585072002?gh_jid=8585072002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| 2027 Software Engineer Intern | Anduril | Atlanta, Georgia, United States; Boston, Massachusetts, United States; Costa Mesa, California, United States; Irvine, California, United States; Reston, Virginia, United States; Seattle, Washington, United States | Not specified | ❌ No | 22% | <a href="https://boards.greenhouse.io/andurilindustries/jobs/5148079007?gh_jid=5148079007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Machine Learning Engineer, LLM Post-Training | NewsBreak | Mountain View, California, United States | Not specified | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/newsbreak/jobs/4688409006"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer | Codes Health | New York | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/codes-health/c7e866ec-6abe-4fcb-a472-47b1b4a7ee18"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Applications Engineer | Seeq | United States | Not specified | ❌ No | 15% | <a href="https://jobs.workable.com/view/7UzCV6woTxYU8fXQfWft1q/remote-ai-applications-engineer-in-united-states-at-seeq"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Onboard Infrastructure | Nuro | Mountain View, California (HQ) | 2 | ❌ No | 15% | <a href="https://nuro.ai/careersitem?gh_jid=7998328"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Systems Engineer | FTE Factory Advisors | Detroit, Michigan, United States | Not specified | ❌ No | 11% | <a href="https://jobs.workable.com/view/9FuzDcthEaFMma4Di8j1gR/hybrid-ai-systems-engineer-in-detroit-at-fte-factory-advisors"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Postdoctoral Research Scientist, Ocean CDR Atlas | Cultivarium | Boulder, CO | 2 | ❌ No | 11% | <a href="https://jobs.lever.co/convergentresearch/07147ace-4d67-47de-9a0a-c7add68bbb68"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Frontend Engineer | Newcode.ai | New York, New York, United States | Not specified | ❌ No | 7% | <a href="https://jobs.workable.com/view/8AhhkqHUtnj65vz3p7UV3u/hybrid-frontend-engineer-in-new-york-at-newcode.ai"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Postdoctoral Research Scientist, OAE Process-Model Testbed | Cultivarium | Boulder, CO | 2 | ❌ No | 7% | <a href="https://jobs.lever.co/convergentresearch/e62d0373-df49-42f2-ad4d-73d99329d781"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer II | The Trade Desk | Sydney | Not specified | ❌ No | 7% | <a href="https://job-boards.greenhouse.io/thetradedesk/jobs/5159472007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Analyst/PowerBI Engineer | ProArch | Atlanta, Georgia, United States | Not specified | ❌ No | 4% | <a href="https://jobs.workable.com/view/5rd3KMBknkXa8SYEezhNdN/remote-data-analyst%2Fpowerbi-engineer-in-atlanta-at-proarch"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-06-09 · 44 roles · 1 H-1B sponsor match

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Vice President, AI & Machine Learning Engineering | ServiceNow | Santa Clara, CALIFORNIA, United States | Not specified | ✅ Yes | 11% | <a href="https://jobs.smartrecruiters.com/ServiceNow/744000131183509"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Scientist, AI Solutions | DataVisor | Mountain View, California, United States | 1 | ❌ No | 41% | <a href="https://apply.workable.com/j/FC5ABB4A50"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer Intern | Centerfield | Los Angeles, California | Not specified | ❌ No | 41% | <a href="https://jobs.ashbyhq.com/centerfield/3279e803-56ab-4e12-8168-c2fd60bc8e60"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, New Grad | Foxglove | San Francisco, CA | 0-2 | ❌ No | 37% | <a href="https://jobs.ashbyhq.com/foxglove/def61478-8b86-43e5-b27b-be7b76900449"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Full Stack Software Engineer, ChatGPT ImageGen | OpenAI | San Francisco | Not specified | ❌ No | 30% | <a href="https://jobs.ashbyhq.com/openai/6b47238e-025a-4350-b270-2f3564002fcc"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| ML Research Scientist, Co-Folding and Affinity | SandboxAQ | United States | Not specified | ❌ No | 26% | <a href="https://jobs.ashbyhq.com/sandboxaq/bc3c5f17-0306-4525-a7cf-f24d4997a78d"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer - Platform Security | Neo4j | Malmö | Not specified | ❌ No | 26% | <a href="https://boards.greenhouse.io/neo4j/jobs/4687943006?gh_jid=4687943006"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Science Intern | iSpot.tv | Bellevue, WA | Not specified | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/ispottv/jobs/4703297005"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Scientist, AI Solutions | DataVisor | Mountain View, California, United States | Not specified | ❌ No | 22% | <a href="https://jobs.workable.com/view/bFXmb176VoDHZwksE4PQvz/hybrid-data-scientist%2C-ai-solutions-in-mountain-view-at-datavisor"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Backend Software Engineer, ChatGPT ImageGen | OpenAI | San Francisco | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/openai/e7a4ee23-138a-4004-916e-72a452e7d115"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Business Intelligence Engineer (GTM), In-Store Data & Analytics | DoorDash | New York, NY | 2 | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/doordashusa/jobs/7991290"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Platform Engineer | Worth AI | Miami, Florida, United States | Not specified | ❌ No | 19% | <a href="https://jobs.workable.com/view/23dFkEksGRwczvCtdYUqQK/remote-data-platform-engineer-in-miami-at-worth-ai"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Platform Engineer | Worth AI | Tampa, Florida, United States | Not specified | ❌ No | 19% | <a href="https://jobs.workable.com/view/fAqD87DmEhyc1m3g3q1K1t/remote-data-platform-engineer-in-tampa-at-worth-ai"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Platform Engineer | Worth AI | Atlanta, Georgia, United States | Not specified | ❌ No | 19% | <a href="https://jobs.workable.com/view/aK4AuMaAga8jSRdbqf3h3E/remote-data-platform-engineer-in-atlanta-at-worth-ai"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Platform Engineer | Worth AI | Orlando, Florida, United States | Not specified | ❌ No | 19% | <a href="https://jobs.workable.com/view/q5f5HZTTyjcb2PHCFNjBBn/remote-data-platform-engineer-in-orlando-at-worth-ai"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Full Stack AI Engineer | MLabs | New York, New York, United States | Not specified | ❌ No | 19% | <a href="https://jobs.workable.com/view/2EHuzRJQSwBVho9z67XYhU/hybrid-full-stack-ai-engineer-in-new-york-at-mlabs"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Development Engineer, Platform Engineering | PitchBook | Seattle, Washington, United States | 2 | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/pitchbookdata/jobs/4687618006"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Internal Applications - Enterprise | OpenAI | San Francisco | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/openai/db053b0e-c1a5-4b7a-bcb6-6e766629e7b1"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Analyst, In-Store | DoorDash | United States - Remote | 2 | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/doordashusa/jobs/7990832"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Scientist | TickPick | New York, New York, United States | Not specified | ❌ No | 15% | <a href="https://jobs.workable.com/view/qM4uD31Z8C1jLFjYtPBvpQ/hybrid-data-scientist-in-new-york-at-tickpick"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Scientist (Payments Risk Analytics) | Nuvei | United States | Not specified | ❌ No | 15% | <a href="https://jobs.workable.com/view/mvHXaYDZ3VmAF3juBU63FZ/remote-data-scientist-(payments-risk-analytics)-in-united-states-at-nuvei"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Site Reliability Engineer, Client Platform | Hadrian | Los Angeles, CA | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/hadrian-automation/620632cd-94f6-4cb5-8dea-3c62de1f20f7"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Product Engineer, Internal Tools | PlanetArt | Calabasas, California, United States | Not specified | ❌ No | 11% | <a href="https://jobs.workable.com/view/ePEveSmDcyr2Ccdhj7f6bk/hybrid-ai-product-engineer%2C-internal-tools-in-calabasas-at-planetart"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Embedded Software Engineer II | CesiumAstro | El Segundo, CA | 2 | ❌ No | 11% | <a href="https://jobs.lever.co/CesiumAstro/84a45ed6-1890-43f8-bce1-5ae23e986939"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Embedded Software Engineer II | CesiumAstro | Austin, TX | 2 | ❌ No | 11% | <a href="https://jobs.lever.co/CesiumAstro/1c793184-7d93-49e8-9e4c-ee2372c23096"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Embedded Software Engineer II | CesiumAstro | Westminster, CO | 2 | ❌ No | 11% | <a href="https://jobs.lever.co/CesiumAstro/32a8d559-91ad-40ba-b4d5-15422133c898"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| GTM Sales Engineer and AI Automation Specialist | Squiz | New York, New York, United States | Not specified | ❌ No | 11% | <a href="https://jobs.workable.com/view/j6EqWMBwwxwbuCMwpk1JbU/hybrid-gtm-sales-engineer-and-ai-automation-specialist-in-new-york-at-squiz"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| GTM Sales Engineer and AI Automation Specialist | Squiz | Los Angeles, California, United States | Not specified | ❌ No | 11% | <a href="https://jobs.workable.com/view/jWEZW5Y6ExBfbomFhyQRg3/hybrid-gtm-sales-engineer-and-ai-automation-specialist-in-los-angeles-at-squiz"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Implementation Specialist, Upsells AI Receptionist | Weave | Weave - Headquarters (Lehi, UT) | 2 | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/weave/a74db075-6a6e-4e1c-b756-008d65a1b410"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Systems Engineer | M\|R Walls | Santa Monica, California, United States | Not specified | ❌ No | 7% | <a href="https://jobs.workable.com/view/6gbsb57Qb9u7UTxLUQbHie/hybrid-ai-systems-engineer-in-santa-monica-at-m%7Cr-walls"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Embedded Software Engineer, Laser Mesh Routing (Starlink) | SpaceX | Redmond, WA | 2 | ❌ No | 7% | <a href="https://boards.greenhouse.io/spacex/jobs/8578936002?gh_jid=8578936002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Embedded Software Engineer, Laser Mesh Routing (Starlink) | SpaceX | Palo Alto, CA | 2 | ❌ No | 7% | <a href="https://boards.greenhouse.io/spacex/jobs/8578934002?gh_jid=8578934002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Beam Planning (Starlink) | SpaceX | Redmond, WA | 2 | ❌ No | 7% | <a href="https://boards.greenhouse.io/spacex/jobs/8578929002?gh_jid=8578929002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Beam Planning (Starlink) | SpaceX | Palo Alto, CA | 2 | ❌ No | 7% | <a href="https://boards.greenhouse.io/spacex/jobs/8578907002?gh_jid=8578907002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, High Performance Computing (Starlink) | SpaceX | Redmond, WA | 2 | ❌ No | 7% | <a href="https://boards.greenhouse.io/spacex/jobs/8578931002?gh_jid=8578931002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, High Performance Computing (Starlink) | SpaceX | Palo Alto, CA | 2 | ❌ No | 7% | <a href="https://boards.greenhouse.io/spacex/jobs/8578909002?gh_jid=8578909002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Low Latency Computing (Starlink) | SpaceX | Redmond, WA | 2 | ❌ No | 7% | <a href="https://boards.greenhouse.io/spacex/jobs/8578923002?gh_jid=8578923002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Low Latency Computing (Starlink) | SpaceX | Palo Alto, CA | 2 | ❌ No | 7% | <a href="https://boards.greenhouse.io/spacex/jobs/8578910002?gh_jid=8578910002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Speech AI Evaluation Specialist - Chinese Simplified (USA) | RWS | Remote | Not specified | ❌ No | 7% | <a href="https://jobs.lever.co/rws/b6ae34f4-57e5-4bb8-8f29-4c69cf25ecbd"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Speech AI Evaluation Specialist - Vietnamese (USA) | RWS | Remote | Not specified | ❌ No | 7% | <a href="https://jobs.lever.co/rws/6488833f-86c3-480c-9dd1-1667f27a372c"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Translation Evaluator; Russian-English | CrowdGen by Appen | Any | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/appen/dc1ac915-13e6-4258-9fe5-203553c345c4"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| IT Asset Management Data Analyst | Gritter Francona | District of Columbia, United States | Not specified | ❌ No | 4% | <a href="https://jobs.workable.com/view/khGNMtALhnZGKy6yLTEkVC/remote-it-asset-management-data-analyst-in-district-of-columbia-at-gritter-francona"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| IT Asset Management Data Analyst | Gritter Francona | Texas, United States | Not specified | ❌ No | 4% | <a href="https://jobs.workable.com/view/84o8sm6eFcD9wixNuyiRhf/remote-it-asset-management-data-analyst-in-texas-at-gritter-francona"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| IT Asset Management Data Analyst | Gritter Francona | Florida, United States | Not specified | ❌ No | 4% | <a href="https://jobs.workable.com/view/uwJidtKHyYaFFvaez4zyGb/remote-it-asset-management-data-analyst-in-florida-at-gritter-francona"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-06-08 · 29 roles · 2 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer | Stripe | Seattle | 2 | ✅ Yes | 26% | <a href="https://stripe.com/jobs/search?gh_jid=7991636"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Deployments Software Engineer | Physical Intelligence | San Francisco | Not specified | ✅ Yes | 11% | <a href="https://jobs.ashbyhq.com/physicalintelligence/1e8a741a-d415-4c34-9ac8-eda4c5393e41"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Engineer – SFL Scientific | Deloitte | Multiple Locations | 2 | ❌ No | 52% | <a href="https://apply.deloitte.com/en_US/careers/JobDetail/AI-Engineer-SFL-Scientific/355403"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Science Fellow - AI/NLP | Axle | Remote | Not specified | ❌ No | 37% | <a href="https://job-boards.greenhouse.io/axle/jobs/5158529007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Embedded Agentic AI | Roku | Austin, Texas | 2 | ❌ No | 37% | <a href="https://www.weareroku.com/jobs/7991641?gh_jid=7991641"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Fullstack Engineer, Health Intelligence | Oura | Hybrid - Helsinki, Uusimaa | 2 | ❌ No | 30% | <a href="https://job-boards.greenhouse.io/oura/jobs/4273399009"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Machine Learning Engineer II - Autonomous Driving Performance Evaluation | May Mobility | Anywhere, USA | 2 | ❌ No | 30% | <a href="https://job-boards.greenhouse.io/maymobility/jobs/8187068002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Research Scientist, Agentic Data & Benchmarking | Institute of Foundation Models | Sunnyvale, CA | 2 | ❌ No | 30% | <a href="https://jobs.lever.co/ifm-us/ab7fbd2c-f809-4f08-ab53-3e666c9792eb"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Engineer | Chime Financial | San Francisco, CA, USA | 2 | ❌ No | 26% | <a href="https://boards.greenhouse.io/chime/jobs/8569368002?gh_jid=8569368002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| CPU/AI Workload Analysis Intern | Tenstorrent | Santa Clara, California, United States | Not specified | ❌ No | 26% | <a href="https://job-boards.greenhouse.io/tenstorrentuniversity/jobs/5158533007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Machine Learning Engineer II - Autonomous Driving & Inference Runtime | May Mobility | Anywhere, USA | 2 | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/maymobility/jobs/8502419002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Onboarding | Ramp | New York, NY (HQ) | 2 | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/ramp/f1b3ca8d-d55f-4159-9a3b-f69ad0d981bc"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Engineer | V4C.ai | United States | 2 | ❌ No | 19% | <a href="https://jobs.workable.com/view/abuBNzmRKx3R6odAcyRrBs/remote-data-engineer-in-united-states-at-v4c.ai"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Operations Data Analyst II (Contract) | Latitude AI | Pittsburgh, PA, Detroit, MI | 2 | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/latitude/jobs/7991041"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer II (Java) | Sony Interactive Entertainment | United States, Madison, WI | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/sonyinteractiveentertainmentglobal/jobs/5987690004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Data Labeler | Mashgin | Remote | 2 | ❌ No | 15% | <a href="https://jobs.lever.co/mashgin/e3c8c967-68d2-41d0-8ecc-218b88e9ca65"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Factory Software Engineer (Starlink) | SpaceX | Bastrop, TX | 2 | ❌ No | 15% | <a href="https://boards.greenhouse.io/spacex/jobs/8574053002?gh_jid=8574053002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Frontend Engineer | Assembled | United States | 2 | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/assembledhq/81c159cf-ad96-46af-97a1-c08eb415dbfb"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Frontend Engineer | Assembled | San Francisco, CA | 2 | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/assembledhq/dcc6f951-237d-451e-a5ea-4c503ce9ab00"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Junior Software Engineer, AI-Forward | Texas Sports Academy Main | Austin, Texas, United States | 0-2 | ❌ No | 15% | <a href="https://jobs.workable.com/view/qCTXyeSoKVUGAcb1NjraCT/junior-software-engineer%2C-ai-forward-in-austin-at-texas-sports-academy-main"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer | Nox Metals | Windsor, ON | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/nox-metals/507178b6-7190-4e32-b29c-a1d1bbb3a021"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Compute Infrastructure | Glean | Mountain View, CA | Not specified | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/gleanwork/jobs/4704106005"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Analytics Engineer | Loop | Chicago | 2 | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/loop/jobs/6016433004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Digital Marketing Intern (SEO and AI Focus) - Fall 2026 | RF-SMART | Jacksonville, Florida, United States | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/rfsmart/jobs/5248299008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Applied AI Engineer | SOCOTEC Global | New York, NY, United States | Not specified | ❌ No | 7% | <a href="https://jobs.smartrecruiters.com/Socotec/744000130845740"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer Planning | Deeproute.ai | Fremont, California, United States | Not specified | ❌ No | 7% | <a href="https://jobs.workable.com/view/ocxiH9xmM3t3MoVyJ4nDuW/software-engineer-planning-in-fremont-at-deeproute.ai"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Multimedia Producer | AppDirect | United States | Not specified | ❌ No | 4% | <a href="https://job-boards.greenhouse.io/appdirect/jobs/8556740002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Analytics / Data Engineer | Prop Firm Match Global – FZCO | United States | Not specified | ❌ No | 4% | <a href="https://jobs.workable.com/view/iSjb5XBTscbLNPmPQwoZab/remote-analytics-%2F-data-engineer-in-united-states-at-prop-firm-match-global-%E2%80%93-fzco"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Junior Web Application Developer | Idea Entity | San Antonio, Texas, United States | 0-2 | ❌ No | 4% | <a href="https://jobs.workable.com/view/fpT22gH28osG7GmnCZ1xtR/hybrid-junior-web-application-developer-in-san-antonio-at-idea-entity"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-06-07 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Applied AI Product Engineer | Spur | New York City | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/spur/3e021029-67f0-4574-a1b2-8517fa531529"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-06-06 · 4 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| AI Builder Intern | Scale AI | San Francisco, CA; New York, NY | Not specified | ❌ No | 26% | <a href="https://job-boards.greenhouse.io/scaleai/jobs/4703343005"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Research Intern (PhD), Machine Learning | Output Biosciences | New York HQ 🗽 | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/output/da2723ca-a418-49f1-b7da-a4f383dd8239"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Propulsion Simulation & Data Analysis | SpaceX | Hawthorne, CA | 1 | ❌ No | 19% | <a href="https://boards.greenhouse.io/spacex/jobs/8581299002?gh_jid=8581299002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Infra Onboard Performance Intern | XPENG Motors | Santa Clara, CA | Not specified | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/xpengmotors/jobs/8581353002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-06-05 · 19 roles · 1 H-1B sponsor match

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Machine Learning Engineer, Agentic Product - Moveworks | ServiceNow | Mountain View, CALIFORNIA, United States | Not specified | ✅ Yes | 7% | <a href="https://jobs.smartrecruiters.com/ServiceNow/744000130554339"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Full Stack SDET (Software Development Engineer in Test) | Hawk-Eye Innovations | Budapest, Hungary | Not specified | ❌ No | 30% | <a href="https://jobs.ashbyhq.com/hawkeyeinnovations/e6112b92-b862-4f65-b4ea-ed231e5d34df"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Research Robotics/Computer Vision Engineer | Skild AI | San Mateo | Not specified | ❌ No | 30% | <a href="https://job-boards.greenhouse.io/skildai-careers/jobs/5248733008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, COOP | Solink | Ottawa Office | Not specified | ❌ No | 30% | <a href="https://jobs.ashbyhq.com/solink/df855bdc-1d59-4af5-b7dc-5e23801aeb30"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Machine Learning Engineer II - Autonomous Driving Training Infrastructure | May Mobility | Remote, USA | 2 | ❌ No | 26% | <a href="https://job-boards.greenhouse.io/maymobility/jobs/8580411002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Professional Service Engineer - AI Security | Zscaler | Split, HRV; Zagreb, HRV | Not specified | ❌ No | 26% | <a href="https://job-boards.greenhouse.io/zscaler/jobs/5151897007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, COOP | Solink | Ottawa Office | Not specified | ❌ No | 26% | <a href="https://jobs.ashbyhq.com/solink/a9faf14b-6e54-4127-89b6-795011a025ef"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Developer - SAD con | Valsoft Corporation | Beirut, Beirut Governorate, Lebanon | Not specified | ❌ No | 22% | <a href="https://apply.workable.com/j/71EC34C4BC"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Clinical AI Product Specialist | Hippocratic AI | Palo Alto | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/Hippocratic%20AI/d6499382-8441-4872-a996-45268fb5885b"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Forward Deployed (All Levels) | Zip | San Francisco | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/zip/3b54f98b-c0a7-4c6b-8a8b-b34a224db0ad"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Engineer (Mid) | Northramp LLC | Washington, District of Columbia, United States | Not specified | ❌ No | 15% | <a href="https://jobs.workable.com/view/hYYj5VJfPVJrt6TBh2Mr6E/remote-ai-engineer-(mid)-in-washington-at-northramp-llc"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Engineer II | Mediavine | Atlanta, Georgia, United States | Not specified | ❌ No | 15% | <a href="https://jobs.workable.com/view/mkV3PpUkzftJE2FTmEwgBP/remote-data-engineer-ii-in-atlanta-at-mediavine"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Full-Stack Engineer (Identity & Security Engineer) | Servant | United States | Not specified | ❌ No | 15% | <a href="https://jobs.workable.com/view/w4y9KPYrTX6Pshv61j3eHH/remote-full-stack-engineer-(identity-%26-security-engineer)-in-united-states-at-servant"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Security Software Engineer (Starlink) | SpaceX | Hawthorne, CA | 2 | ❌ No | 15% | <a href="https://boards.greenhouse.io/spacex/jobs/8577408002?gh_jid=8577408002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Site Reliability Engineer / Production Support Analyst | mthree | Salt Lake City, Utah, United States | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/mthreerecruitingportal/jobs/4687363006"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| DevOps Engineer (Weekend) | MEMX | United States | 2 | ❌ No | 7% | <a href="https://job-boards.greenhouse.io/memx/jobs/5249316008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Forward Deployed Engineer (AI Deployment) | CloudFactory | Dallas, United States | Not specified | ❌ No | 7% | <a href="https://jobs.workable.com/view/rSqWvxbrQ6J2afCWEjbmSJ/hybrid-forward-deployed-engineer-(ai-deployment)-in-dallas-at-cloudfactory"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Networking (Dataplane) | Tailscale | Remote (United States) | Not specified | ❌ No | 7% | <a href="https://job-boards.greenhouse.io/tailscale/jobs/4703138005"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Analyst BI Architecture, Client Facing Experience Must | AssistRx | Florida, United States | Not specified | ❌ No | 4% | <a href="https://jobs.workable.com/view/oCjrUxZfqVhCef7DunPw4k/remote-data-analyst-bi-architecture%2C-client-facing-experience-must-in-florida-at-assistrx"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-06-04 · 12 roles · 2 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Data Scientist, Economic Insights & Research | Stripe | US | Not specified | ✅ Yes | 15% | <a href="https://stripe.com/jobs/search?gh_jid=7980402"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Agentic Systems - Moveworks | ServiceNow | Mountain View, CALIFORNIA, United States | Not specified | ✅ Yes | 4% | <a href="https://jobs.smartrecruiters.com/ServiceNow/744000130257420"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer II, Forward Deployment | Flock Safety | Remote - USA | Not specified | ❌ No | 33% | <a href="https://jobs.ashbyhq.com/Flock%20Safety/5083671c-8a9a-409b-8e1a-f85b462fa2dd"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Test Engineer II | Trend Health Partners | Remote | Not specified | ❌ No | 22% | <a href="https://jobs.lever.co/Trend-Health-Partners/ab55dae4-517e-4037-af1c-913875064331"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Cloud Software Engineer - Database | TP-Link Systems Inc. | Irvine, California, United States | Not specified | ❌ No | 15% | <a href="https://jobs.workable.com/view/9SSaWQWNhAXhPCdob8htNV/cloud-software-engineer---database-in-irvine-at-tp-link-systems-inc."><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Analyst | Modern Health | Remote - US | 2 | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/modernhealth/jobs/8550544002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Full Stack Software Engineer, Cybersecurity Products | OpenAI | San Francisco | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/openai/88654e7f-4e23-4e75-8e54-18c10d09b093"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Infrastructure Engineer – DevOps, Kubernetes & Automation | TensorWave | Las Vegas, Nevada | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/tensorwave/83fccd48-0587-4f82-8041-d75062f172e1"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer II, Frontend - Service Monetization | Crunchyroll | Los Angeles, California, United States | 2 | ❌ No | 15% | <a href="https://boards.greenhouse.io/crunchyroll/jobs/7980329?gh_jid=7980329"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Engineer / Data Scientist | American Operations Corporation | Montgomery, Alabama, United States | Not specified | ❌ No | 11% | <a href="https://jobs.workable.com/view/bvu6Mjg7kDTsq4q69nYnfB/ai%2Fml-engineer-%2F-data-scientist-in-montgomery-at-american-operations-corporation"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer / Application Developer | American Operations Corporation | Montgomery, Alabama, United States | Not specified | ❌ No | 7% | <a href="https://jobs.workable.com/view/uFAgmbP3y6nHoQcAPRfQRS/software-engineer-%2F-application-developer-in-montgomery-at-american-operations-corporation"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Spanish Conversational-AI Specialist | Prodigal | Remote - Global | Not specified | ❌ No | 4% | <a href="https://job-boards.greenhouse.io/prodigal/jobs/5155937007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-06-03 · 18 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| AI Engineer | Sony Interactive Entertainment | United States, San Diego, CA | 2 | ❌ No | 37% | <a href="https://job-boards.greenhouse.io/sonyinteractiveentertainmentglobal/jobs/6007946004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Computer Vision AI & ML Engineer | Skild AI | San Mateo, CA | Not specified | ❌ No | 30% | <a href="https://job-boards.greenhouse.io/skildai-careers/jobs/5239930008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| ML Engineer | Mach9 | San Francisco | Not specified | ❌ No | 30% | <a href="https://jobs.ashbyhq.com/mach9/51061973-9726-4e8e-bba4-4bfa9e3ef004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Core Platform Engineer, Data and Algo (All Levels) | Oura | Hybrid - Helsinki, Uusimaa | Not specified | ❌ No | 26% | <a href="https://job-boards.greenhouse.io/oura/jobs/4259790009"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Machine Learning Researcher | Jane Street | New York, New York, United States | Not specified | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/janestreet/jobs/8576928002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer (Cloud, Cross-Platform & .NET Systems) | Altom Transport | Houston, Texas, United States | Not specified | ❌ No | 22% | <a href="https://jobs.workable.com/view/azuwQfc4TyCWpApUsX8YRB/software-engineer-(cloud%2C-cross-platform-%26-.net-systems)-in-houston-at-altom-transport"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer (Cloud, Cross-Platform & .NET Systems) | Altom Transport | Chicago, Illinois, United States | Not specified | ❌ No | 22% | <a href="https://jobs.workable.com/view/474qkqh3tGXm8G6TzM1UPw/software-engineer-(cloud%2C-cross-platform-%26-.net-systems)-in-chicago-at-altom-transport"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Host Systems Software Engineer | OpenAI | San Francisco | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/openai/87e5f8c3-3337-480a-9db2-e4cef5db909b"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Engineer | Pereview Software | Dallas, Texas, United States | Not specified | ❌ No | 15% | <a href="https://jobs.workable.com/view/5nrPq2ipU8DJVTNtdKyiWX/ai-engineer-in-dallas-at-pereview-software"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Full Stack Software Engineer, Codex Cloud Apps | OpenAI | San Francisco | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/openai/130a5389-83e1-493f-9205-542d3ff53afb"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Scientist, GTM | Cursor | San Francisco | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/cursor/7bc441a4-9bb6-45cb-a9e0-5ae1b9c7ac5b"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Junior Software Engineer | Clearstory | Walnut Creek, California, United States | 0-2 | ❌ No | 11% | <a href="https://jobs.workable.com/view/acDDakVq9eEvcT8UZjmS7a/junior-software-engineer-in-walnut-creek-at-clearstory"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Distributed Systems | Discord | San Francisco Bay Area | 2 | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/discord/jobs/8545663002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Performance | Nuro | Mountain View, California (HQ) | 2 | ❌ No | 11% | <a href="https://nuro.ai/careersitem?gh_jid=7978428"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Performance - New Grad | Nuro | Mountain View, California (HQ) | 0-2 | ❌ No | 11% | <a href="https://nuro.ai/careersitem?gh_jid=7978432"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Systems Engineer - R&D | SoloPulse | Peachtree Corners, GA | Not specified | ❌ No | 7% | <a href="https://jobs.lever.co/solopulseco/1847aeec-f19d-46ee-812b-be16c8505753"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Management Engineer II” ETL / IICS Developer | Deloitte | Multiple Locations | Not specified | ❌ No | 4% | <a href="https://apply.deloitte.com/en_US/careers/JobDetail/Data-Management-Engineer-II-ETL-IICS-Developer/354704"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Management Engineer II” ETL / IICS Developer | Deloitte | Multiple Locations | Not specified | ❌ No | 4% | <a href="https://apply.deloitte.com/en_US/careers/JobDetail/Data-Management-Engineer-II-ETL-IICS-Developer/354706"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-06-02 · 34 roles · 2 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Research Intern (AI) - 2026 | Snowflake | PL-Warsaw | Not specified | ✅ Yes | 26% | <a href="https://jobs.ashbyhq.com/snowflake/e2412cd5-19dd-44f8-addd-c9ef3c99ff82"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer Intern (AI/ML) - 2026 | Snowflake | PL-Warsaw | Not specified | ✅ Yes | 26% | <a href="https://jobs.ashbyhq.com/snowflake/897e1850-c590-4462-b187-0516b65b2034"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Applied AI Engineering Intern | d-Matrix | Santa Clara | Not specified | ❌ No | 44% | <a href="https://jobs.ashbyhq.com/d-Matrix/93a6e6ee-3391-4437-8459-e28eb05eace7"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Machine Learning Engineer II | Tinder | Palo Alto, California | 1 | ❌ No | 44% | <a href="https://jobs.lever.co/matchgroup/613fab0e-1e84-4604-9fae-08785c3a792e"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Machine Learning Engineer | Robinhood | Bellevue, WA | Not specified | ❌ No | 37% | <a href="https://boards.greenhouse.io/robinhood/jobs/7960680?t=gh_src=&amp;gh_jid=7960680"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Engineer - Data Intelligence | Clarium | Remote/US | Not specified | ❌ No | 33% | <a href="https://jobs.ashbyhq.com/clarium/83332693-7e11-41db-8b62-8225cb818abf"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Scientist (Looker / AI / BI) | Northramp LLC | Washington, District of Columbia, United States | Not specified | ❌ No | 33% | <a href="https://jobs.workable.com/view/8m9Ro5UhgNCuSQuUvgABnV/hybrid-data-scientist-(looker-%2F-ai-%2F-bi)-in-washington-at-northramp-llc"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Agentic AI | Robinhood | Bellevue, WA | Not specified | ❌ No | 33% | <a href="https://boards.greenhouse.io/robinhood/jobs/7975477?t=gh_src=&amp;gh_jid=7975477"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer | Robinhood | Menlo Park, CA | 1 | ❌ No | 26% | <a href="https://boards.greenhouse.io/robinhood/jobs/7975558?t=gh_src=&amp;gh_jid=7975558"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer | Robinhood | Menlo Park, CA | Not specified | ❌ No | 26% | <a href="https://boards.greenhouse.io/robinhood/jobs/7975531?t=gh_src=&amp;gh_jid=7975531"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer | Robinhood | Menlo Park, CA | Not specified | ❌ No | 26% | <a href="https://boards.greenhouse.io/robinhood/jobs/7975530?t=gh_src=&amp;gh_jid=7975530"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Ads Product | xAI | Palo Alto, CA | Not specified | ❌ No | 26% | <a href="https://job-boards.greenhouse.io/xai/jobs/5152408007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Automation Engineer - Scientific Data, AI/ML Pipelines & Integration Dev | Zifo | Boston, Massachusetts, United States | Not specified | ❌ No | 22% | <a href="https://jobs.workable.com/view/h5Ucj6jyfu9Q6a2Du1cr2e/hybrid-automation-engineer---scientific-data%2C-ai%2Fml-pipelines-%26-integration-dev-in-boston-at-zifo"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Engineer (BigQuery / Cloud Data Platforms) | Northramp LLC | Washington, District of Columbia, United States | Not specified | ❌ No | 22% | <a href="https://jobs.workable.com/view/9bbjv52q9rembbYKSFbDTs/hybrid-data-engineer-(bigquery-%2F-cloud-data-platforms)-in-washington-at-northramp-llc"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Machine Learning Scientist, Reinforcement Learning | Profluent | Emeryville, California, United States; Hybrid (2-3 days on-site) | Not specified | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/profluent/jobs/5238462008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer | Robinhood | Menlo Park, CA | 1 | ❌ No | 22% | <a href="https://boards.greenhouse.io/robinhood/jobs/7975507?t=gh_src=&amp;gh_jid=7975507"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer II - MES | Rocket Lab USA | Long Beach, CA | 2 | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/rocketlab/jobs/7737073003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer II, Backend (Capital Orchestration) | Affirm | Remote US | 1.5 | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/affirm/jobs/7749755003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Applied AI Engineer | Becoming | San Francisco, California, United States | Not specified | ❌ No | 19% | <a href="https://jobs.workable.com/view/552gk9ZtEAqSNJVzUKiPM4/applied-ai-engineer-in-san-francisco-at-becoming"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer | Robinhood | Menlo Park, CA | Not specified | ❌ No | 19% | <a href="https://boards.greenhouse.io/robinhood/jobs/7975550?t=gh_src=&amp;gh_jid=7975550"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer | Robinhood | Menlo Park, CA | Not specified | ❌ No | 19% | <a href="https://boards.greenhouse.io/robinhood/jobs/7975549?t=gh_src=&amp;gh_jid=7975549"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer | Robinhood | Menlo Park, CA | 1 | ❌ No | 19% | <a href="https://boards.greenhouse.io/robinhood/jobs/7975516?t=gh_src=&amp;gh_jid=7975516"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer | Robinhood | Menlo Park, CA | Not specified | ❌ No | 19% | <a href="https://boards.greenhouse.io/robinhood/jobs/7960734?t=gh_src=&amp;gh_jid=7960734"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Full Stack | EverDriven | Greenwood Village, Colorado, United States | 2 | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/everdriven/jobs/5238306008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer- BIS (Baseten Inference Stack) | Baseten | San Francisco | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/baseten/c8701794-bdc1-4932-bffa-a444ce57ed73"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Full Stack Engineer (AI Platform & Product) | Riot Hospitality Group | Scottsdale, Arizona, United States | Not specified | ❌ No | 15% | <a href="https://jobs.workable.com/view/uXZNCZmTfCNCiUfoB375aC/hybrid-full-stack-engineer-(ai-platform-%26-product)-in-scottsdale-at-riot-hospitality-group"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer | Robinhood | Menlo Park, CA | Not specified | ❌ No | 15% | <a href="https://boards.greenhouse.io/robinhood/jobs/7975529?t=gh_src=&amp;gh_jid=7975529"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer | Robinhood | Menlo Park, CA | Not specified | ❌ No | 15% | <a href="https://boards.greenhouse.io/robinhood/jobs/7975526?t=gh_src=&amp;gh_jid=7975526"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer (Computational Geometry) | Layup Parts | Huntington Beach, CA | Not specified | ❌ No | 15% | <a href="https://jobs.lever.co/layup/b2ab778f-63bb-482c-83ab-19961b7fe6b5"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| MDM Platform Engineer (DE) | ShyftLabs | Noida, Uttar Pradesh | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/shyftlabs/a37782bd-e533-4843-8c58-27c8d58de317"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer | Checkr | Santiago, Región Metropolitana, Chile | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/checkr/jobs/7927124"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Hardware Systems Engineer | Lumafield | Boston, MA | Not specified | ❌ No | 7% | <a href="https://jobs.lever.co/lumafield/309cb9df-0b93-4fc6-a495-e64264dc8eea"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Language Annotator - Chinese Traditional | RWS | Taipei | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/rws/f7caddcc-e1ca-477d-80c8-cd43c0557705"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Full Stack Engineer | Pensar | New York, New York, United States | Not specified | ❌ No | 4% | <a href="https://jobs.workable.com/view/ccoYXwYbMn6fWwcTHDG61b/full-stack-engineer-in-new-york-at-pensar"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-06-01 · 19 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Data Engineer (Starship) | SpaceX | Starbase, TX | 2 | ❌ No | 37% | <a href="https://boards.greenhouse.io/spacex/jobs/8569186002?gh_jid=8569186002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer (Starship) | SpaceX | Hawthorne, CA | 2 | ❌ No | 37% | <a href="https://boards.greenhouse.io/spacex/jobs/8569160002?gh_jid=8569160002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer (Starship) | SpaceX | Starbase, TX | 2 | ❌ No | 37% | <a href="https://boards.greenhouse.io/spacex/jobs/8569125002?gh_jid=8569125002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Machine Learning Engineer | Multi Media LLC | United States | Not specified | ❌ No | 33% | <a href="https://jobs.workable.com/view/bqkqSAJN2W35yHL1WmQ5C9/remote-machine-learning-engineer-in-united-states-at-multi-media-llc"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Engineer (Starlink Network Analytics, Wi-Fi) | SpaceX | Redmond, WA | 1 | ❌ No | 22% | <a href="https://boards.greenhouse.io/spacex/jobs/8573711002?gh_jid=8573711002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| DevOps / Infrastructure Engineer | MLabs | United States | Not specified | ❌ No | 22% | <a href="https://apply.workable.com/j/D12F9E3EDA"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Wireless Software Engineer | Skydio | San Mateo, California, United States | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/skydio/c0c38168-badc-4dd7-96ed-99deb22149fc"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Graduate Software Engineer, Open Source and Linux, Canonical Ubuntu | Canonical | Home based - Worldwide | 0-2 | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/canonical/jobs/7957239"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Research Marketing Intern - Summer 2026 | Lambda | San Francisco Office (Second St) | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/lambda/1c764f96-966d-4560-8087-35452480d330"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Infrastructure Engineer | Flint | San Francisco | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/flint/9347be1d-49bd-40bc-9308-acca85ee1117"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Engineer - Roamly Labs | Roamly | Austin, Texas, United States | Not specified | ❌ No | 11% | <a href="https://jobs.workable.com/view/jyWeVQes3kL4tmmHw47UGu/ai-engineer---roamly-labs-in-austin-at-roamly"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Learning Scientist | Kira | New York | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/kira/0c05824e-f107-4766-ac2e-2adcc7643c14"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Market Infrastructure Engineer | Base Power | Austin, TX | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/base-power/53924682-e6c8-4c3b-9a39-19905ea16e5b"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Physical Security Systems Engineer | OpenAI | San Francisco | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/openai/78a3351e-55db-40dc-9655-4739f31d7ef7"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Product Data Analyst - Acquiring Operations | NMI | Remote, US | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/nmi/jobs/5232258008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Roamly Labs - AI Engineer | The Ride Platform | Austin, Texas, United States | Not specified | ❌ No | 11% | <a href="https://jobs.workable.com/view/9yaLrLuHLvMcNmSEHWU1Qb/roamly-labs---ai-engineer-in-austin-at-the-ride-platform"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer - Core Strategist | prosource.it- Americas | Houston, Texas, United States | Not specified | ❌ No | 11% | <a href="https://jobs.workable.com/view/acuxPemNm9WXAuWj4rnUoM/hybrid-software-engineer---core-strategist-in-houston-at-prosource.it--americas"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| DevOps Engineer (11 PM - 8 AM) | MEMX | United States | 2 | ❌ No | 7% | <a href="https://job-boards.greenhouse.io/memx/jobs/5238249008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Copywriter | Socure | Hybrid - US | 2 | ❌ No | 4% | <a href="https://jobs.ashbyhq.com/socure/0b83a57d-2566-48c3-a700-e36df48ec9dc"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-05-31 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer | Vector | HQ | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/vector/96a4906c-1bc2-469f-b9c0-7cb06cc1982b"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Diagnostics Software Engineer | Arista Networks | Nashua, NH, United States | Not specified | ❌ No | 4% | <a href="https://jobs.smartrecruiters.com/AristaNetworks/744000129323999"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-05-30 · 4 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Data Scientist/Machine Learning Engineer (req-253) | CATHEXIS | Tysons, Virginia, United States | Not specified | ❌ No | 19% | <a href="https://jobs.workable.com/view/pUsr7LK3ps1Ro5nTcss7Pi/data-scientist%2Fmachine-learning-engineer-(req-253)-in-tysons-at-cathexis"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Video Trainer - Hebrew | Wing Assistant | Haifa | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/getwingapp/2d508f71-74b3-43c2-bf2b-31cb90674ed1"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Video Trainer - Hebrew | Wing Assistant | Tel-Aviv | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/getwingapp/29f8f5d2-2437-4fb1-b0e8-ff32f6e97c27"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Video Trainer - Hebrew | Wing Assistant | United States | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/getwingapp/a79aec5d-210f-4303-a542-f0158bdcf275"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-05-29 · 21 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Open-Source Machine Learning Engineer - US Remote | Hugging Face | New York, New York, United States | Not specified | ❌ No | 41% | <a href="https://jobs.workable.com/view/8UbCFFqNjvdNUKZBYdFAMR/open-source-machine-learning-engineer---us-remote-in-new-york-at-hugging-face"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Research Scientist - Vision Language Model | Institute of Foundation Models | Sunnyvale, CA | Not specified | ❌ No | 33% | <a href="https://jobs.lever.co/ifm-us/1f5c0611-5364-4155-91f8-6884e6757385"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Machine Learning Engineer - Reinforcement Learning | pony.ai | Fremont, California, United States | Not specified | ❌ No | 30% | <a href="https://apply.workable.com/j/B61A865299"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Machine Learning Engineer - Reinforcement Learning | pony.ai | Fremont, California, United States | Not specified | ❌ No | 22% | <a href="https://jobs.workable.com/view/k8DRDpnZgUmVpNfZooCWe1/machine-learning-engineer---reinforcement-learning-in-fremont-at-pony.ai"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Research Scientist - Frontier Benchmarks | Snorkel AI | San Francisco, CA (Hybrid) | Not specified | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/snorkelai/jobs/6009489004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| IT Controls Data Engineer | OpenAI | San Francisco | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/openai/5bc79fde-2f1d-4bb2-8186-4a700ecff37c"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer - Risk | DRW | Chicago, New York | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/drweng/jobs/7942728"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Operational/ Process Efficiency | Waymo | Mountain View, CA, US | Not specified | ❌ No | 19% | <a href="https://careers.withwaymo.com/jobs?gh_jid=7926526"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Engineer | GitLab | Remote, US | Not specified | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/gitlab/jobs/8565469002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Associate Software Engineer, Embedded Development | Relay | Raleigh, NC | Not specified | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/relaypro/jobs/7968124"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer | SpaceX | McGregor, TX | 1 | ❌ No | 11% | <a href="https://boards.greenhouse.io/spacex/jobs/8563110002?gh_jid=8563110002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer Intern - Generalist | pony.ai | Fremont, California, United States | Not specified | ❌ No | 11% | <a href="https://apply.workable.com/j/BA5FFDBC71"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Network | Persona | Remote | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/persona/fc9e26c9-0123-4cd1-a8da-c1836ab68a0b"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Traffic | Persona | Remote | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/persona/247b0dec-3fe3-41f7-a1b6-76e51cbc8ab5"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Engineer — Workforce Reinvention | OpenSesame | Remote | Not specified | ❌ No | 7% | <a href="https://boards.greenhouse.io/opensesame/jobs/7967740?gh_jid=7967740"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Applied AI Engineer | WS Development | Chestnut Hill, Massachusetts, United States | Not specified | ❌ No | 7% | <a href="https://jobs.workable.com/view/5MxDZf1Jn86Ykwcuov7AYi/applied-ai-engineer-in-chestnut-hill-at-ws-development"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Engineer - Remote | Mindex | Rochester, New York, United States | Not specified | ❌ No | 7% | <a href="https://jobs.workable.com/view/uBFf3vWb9By2AJn9t9XtdF/data-engineer---remote-in-rochester-at-mindex"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Power Systems Engineer | Base Power | Austin, TX | Not specified | ❌ No | 7% | <a href="https://jobs.ashbyhq.com/base-power/14254957-3c64-4e0b-9714-7adda026736e"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| SAS Data Engineer- Linux, bilingual in Korean | Cesna Recruitment | Austin, Texas, United States | Not specified | ❌ No | 7% | <a href="https://jobs.workable.com/view/sC9MNiM4MEHoExLe7p8oU9/sas-data-engineer--linux%2C-bilingual-in-korean-in-austin-at-cesna-recruitment"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer Intern - Generalist | pony.ai | Fremont, California, United States | Not specified | ❌ No | 7% | <a href="https://jobs.workable.com/view/fMNdv7wiX6977RgdBwZGEp/software-engineer-intern---generalist-in-fremont-at-pony.ai"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Jr. Web Developer (AI-Powered) | eJam | Santa Ana, California, United States | 0-2 | ❌ No | 4% | <a href="https://jobs.workable.com/view/gaLzLxCymosWafMiJNuoPf/jr.-web-developer-(ai-powered)-in-santa-ana-at-ejam"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-05-28 · 37 roles · 2 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Machine Learning Engineer, GAI Search Relevance - Moveworks | ServiceNow | Mountain View, CALIFORNIA, United States | Not specified | ✅ Yes | 11% | <a href="https://jobs.smartrecruiters.com/ServiceNow/744000129017632"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Agentic AI Systems - Moveworks | ServiceNow | Mountain View, CALIFORNIA, United States | Not specified | ✅ Yes | 7% | <a href="https://jobs.smartrecruiters.com/ServiceNow/744000128997739"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Junior Software Engineer, Full-Stack | Epic Kids | Remote, US | 0-2 | ❌ No | 33% | <a href="https://job-boards.greenhouse.io/epickids/jobs/7751646003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Machine Learning Engineer, App SW | Wayve | Detroit | Not specified | ❌ No | 33% | <a href="https://wayve.firststage.co/jobs?gh_jid=8568694002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Machine Learning Engineer | Silvus Technologies | Los Angeles CA | 2 | ❌ No | 30% | <a href="https://job-boards.greenhouse.io/silvus/jobs/5233544008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Research Intern - Deep Learning | pony.ai | Fremont, California, United States | Not specified | ❌ No | 22% | <a href="https://apply.workable.com/j/4C1F53EF5D"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer - AI | Promise | Washington, D.C. | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/Promise/ea0b2ad0-7270-413a-91f9-0be0b99052e1"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer II, Big Data, tvScientific | Pinterest | San Francisco, CA, US; Remote, US | Not specified | ❌ No | 22% | <a href="https://www.pinterestcareers.com/jobs/?gh_jid=7782546"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Associate Software Engineer, Site Reliability | Relay | Raleigh, NC | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/relaypro/jobs/7950142"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Helix AI Engineer, Android | Figure | San Jose, CA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/figureai/jobs/4685209006"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Helix AI Engineer, Backend Infrastructure | Figure | San Jose, CA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/figureai/jobs/4685172006"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer I | Axon | Sterling, Virginia, United States | 2 | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/axon/jobs/7738253003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Strategic Projects | Tailscale | Remote (United States) | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/tailscale/jobs/4700280005"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| iOS Software Engineer, AI Engineering | TWG Global AI | Santa Monica, California, United States | Not specified | ❌ No | 15% | <a href="https://jobs.workable.com/view/m7z76Y7Rkg4Xt84SXpSthz/ios-software-engineer%2C-ai-engineering-in-santa-monica-at-twg-global-ai"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| iOS Software Engineer, AI Engineering | TWG Global AI | New York, New York, United States | Not specified | ❌ No | 15% | <a href="https://jobs.workable.com/view/qnWzxLw3geBYuRMPWdscCR/ios-software-engineer%2C-ai-engineering-in-new-york-at-twg-global-ai"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Research Intern - Deep Learning | pony.ai | Fremont, California, United States | Not specified | ❌ No | 15% | <a href="https://jobs.workable.com/view/dg7mE62ASKJNz8hiNyQd13/research-intern---deep-learning-in-fremont-at-pony.ai"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer (Starlink Mobile) | SpaceX | Sunnyvale, CA | 2 | ❌ No | 15% | <a href="https://boards.greenhouse.io/spacex/jobs/8567634002?gh_jid=8567634002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer (Starlink Mobile) | SpaceX | Redmond, WA | 2 | ❌ No | 15% | <a href="https://boards.greenhouse.io/spacex/jobs/8568939002?gh_jid=8568939002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Financial & Data Analyst | Pavago | United States | 2 | ❌ No | 11% | <a href="https://jobs.workable.com/view/hzcjV3StwoDC5wnC2LJA8Q/remote-financial-%26-data-analyst-in-united-states-at-pavago"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Fluid Systems Engineer II | Relativity Space | Long Beach, California | 2 | ❌ No | 7% | <a href="https://boards.greenhouse.io/relativity/jobs/8568918002?gh_jid=8568918002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Trainer - Dutch | Wing Assistant | Rotterdam | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/getwingapp/499322ed-71b9-4ec4-af7e-8b8ff60c9c06"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Trainer - Khmer | Wing Assistant | Cambodia | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/getwingapp/1410f93f-c9bf-4c57-b42e-f6fa73f7943d"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Trainer - Khmer | Wing Assistant | Phnom Penh | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/getwingapp/7d9f2963-311c-427b-9dfb-1f2557c61586"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Trainer - Malay | Wing Assistant | Penang | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/getwingapp/3aadfc2c-2712-49a8-9709-f4074e7a6f91"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Trainer - Mandarin/Cantonese | Wing Assistant | Taipei | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/getwingapp/8ae4e386-a2c5-448a-b0f1-4d1e53ec1dfb"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Trainer - Swahili | Wing Assistant | Uganda | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/getwingapp/f40cd750-e3e0-4910-9937-1521c5b75b39"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Trainer - Swahili | Wing Assistant | Tanzania | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/getwingapp/67757b58-0ff7-4d1b-a7b3-a96f6a87a22d"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Trainer - Thai | Wing Assistant | Chiang Mai | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/getwingapp/0291d341-b7d3-4c22-9ed8-bab1d9b38e7b"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Trainer - Turkish | Wing Assistant | Ankara | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/getwingapp/6cb9e5d5-a50f-4f72-b7db-4005ca6312df"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Trainer - Turkish | Wing Assistant | Istanbul | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/getwingapp/2acf9729-1055-4e08-902b-f6c02aeabff8"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Video Trainer | Wing Assistant | Pune | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/getwingapp/0250acbb-38fb-4859-9010-3b74a43a4378"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Video Trainer - Korean | Wing Assistant | Busan | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/getwingapp/de52732e-9016-4f5f-b9bf-84626d40fd33"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Video Trainer - Korean | Wing Assistant | Seongnam, Gyeonggi Province | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/getwingapp/310a2e39-34c5-408f-985c-e917310d6b1f"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Video Trainer - Spanish | Wing Assistant | Valencia | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/getwingapp/2a56acf2-9453-4ec9-9d9d-270a138edab5"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Video Trainer - Spanish | Wing Assistant | Madrid | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/getwingapp/445b76cc-7359-482a-85c0-d9ae4350935a"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Voice Trainer | Wing Assistant | Madhya Pradesh | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/getwingapp/52335021-831d-4c8c-88f3-d222036a67d0"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Infrastructure Engineer | Scientech Research | Shanghai | Not specified | ❌ No | 4% | <a href="https://jobs.ashbyhq.com/scientech-research/4f4324c3-879a-48fa-aa22-35b6906a3c32"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-05-27 · 30 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer, Data Migration | MongoDB | California; Oregon; Washington | 2 | ❌ No | 37% | <a href="https://www.mongodb.com/careers/job/?gh_jid=7523834"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Distributed LLM Inference Engineer | Anyscale | San Francisco | Not specified | ❌ No | 30% | <a href="https://jobs.ashbyhq.com/anyscale/1cf38233-8aa0-47f8-9d85-65ce27bc3047"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| 2026 Fall Intern, Computer Vision/AI | Samsung Research America | 665 Clyde Avenue, Mountain View, CA, USA | Not specified | ❌ No | 26% | <a href="https://job-boards.greenhouse.io/samsungresearchamericainternship/jobs/8560657002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Intermediate Full Stack Software Engineer | impact.com | Columbus, OH | 2 | ❌ No | 26% | <a href="https://job-boards.greenhouse.io/impact/jobs/8557055002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Full Stack Engineer, AgentControl | LaunchDarkly | Remote - US | Not specified | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/launchdarkly/jobs/7750116003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer | Harvey | San Francisco | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/harvey/581cd358-0186-48a6-b76f-c76946c5c7a7"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer (Cloud, Cross-Platform & .NET Systems) | Altom Transport | Houston, Texas, United States | Not specified | ❌ No | 22% | <a href="https://jobs.workable.com/view/nGXhLiC91Jpsa8rjUUhY4r/software-engineer-(cloud%2C-cross-platform-%26-.net-systems)-in-houston-at-altom-transport"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer (Cloud, Cross-Platform & .NET Systems) | Altom Transport | Chicago, Illinois, United States | Not specified | ❌ No | 22% | <a href="https://jobs.workable.com/view/rvVK93rjQXKpJ2pWEi7ooD/software-engineer-(cloud%2C-cross-platform-%26-.net-systems)-in-chicago-at-altom-transport"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Cyber Frontier | OpenAI | San Francisco | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/openai/b7f46b2e-dfc7-4b06-8e5e-8468555c102b"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Engineer, Agent Platform | NewsBreak | Mountain View, California, United States | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/newsbreak/jobs/4683873006"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| C++ Software Engineer | Hawk-Eye Innovations | Hungary, Budapest | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/hawkeyeinnovations/ceef33cc-d064-47a2-bb12-9705c6b01f7e"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer | InterImage | Arlington, Virginia, United States | Not specified | ❌ No | 19% | <a href="https://jobs.workable.com/view/ungBMgsaUnHyo1dxiRrNx4/remote-software-engineer-in-arlington-at-interimage"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer - Infrastructure | Skydio | San Mateo, California, United States | 2 | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/skydio/cb958101-ede8-4f50-bf30-b3272d33f25f"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Hardware Test & Automation (Starlink) | SpaceX | Redmond, WA | 2 | ❌ No | 19% | <a href="https://boards.greenhouse.io/spacex/jobs/8565155002?gh_jid=8565155002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Red Teamer, LLM Generalist | Handshake | Seattle, WA | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/handshake/1e3a9711-d13c-4b79-8599-34dfb3133621"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Clinical Product Specialist, AI Development | Lyra Health | United States | 1 | ❌ No | 15% | <a href="https://jobs.lever.co/lyrahealth/b2f04e56-7db2-4615-bf1d-436ec628e92d"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Engineer | Habitat Energy | Austin, United States | Not specified | ❌ No | 15% | <a href="https://jobs.workable.com/view/oj4dvHpVechQNtyXNoiRDQ/hybrid-data-engineer-in-austin-at-habitat-energy"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Manufacturing Data Analyst Intern | Zone 5 Technologies | San Luis Obispo, California, United States | Not specified | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/zone5technologies/jobs/5231405008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Integrations | SchooLinks | United States | Not specified | ❌ No | 15% | <a href="https://jobs.workable.com/view/4pFkZxMHDXnfAipKZ59uG5/remote-software-engineer%2C-integrations-in-united-states-at-schoolinks"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| C++ Software Engineer | Hawk-Eye Innovations | Hungary, Budapest | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/hawkeyeinnovations/c2955797-b0c8-4794-83ba-b3b49f6ead96"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Salesforce & Business Systems Engineer | Betterment | Betterment HQ - New York City | Not specified | ❌ No | 11% | <a href="https://www.betterment.com/careers/current-openings/job?gh_jid=7958111&amp;gh_jid=7958111"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Site Reliability Engineer, Robotics | Hadrian | Los Angeles, CA | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/hadrian-automation/44db308b-2d21-409f-8589-3ab6319b02ec"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer | Waymo | PERM - N/A | Not specified | ❌ No | 11% | <a href="https://careers.withwaymo.com/jobs?gh_jid=7960666"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer | Waymo | PERM - N/A | Not specified | ❌ No | 11% | <a href="https://careers.withwaymo.com/jobs?gh_jid=7960517"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Accounting AI Intern - Summer 2026 | Lambda | San Francisco Office (Second St) | Not specified | ❌ No | 7% | <a href="https://jobs.ashbyhq.com/lambda/d84c4397-8b15-414b-b488-99ea0180bf18"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Development Engineer in Test II - Contractor | Sony Interactive Entertainment | United States, San Mateo, CA | Not specified | ❌ No | 7% | <a href="https://job-boards.greenhouse.io/sonyinteractiveentertainmentglobal/jobs/5993032004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer | Waymo | PERM - N/A | Not specified | ❌ No | 7% | <a href="https://careers.withwaymo.com/jobs?gh_jid=7960496"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Video Trainer - Spanish | Wing Assistant | Barcelona | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/getwingapp/df3ad5a3-2c3a-4a14-9644-7199e5dd07e3"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Full Stack Engineer | Phia | New York City | 1 | ❌ No | 4% | <a href="https://jobs.ashbyhq.com/phia/d0e5df80-ebc7-4abb-8b0b-2d1d152c482f"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Full Stack Engineer Intern | Phia | New York City | Not specified | ❌ No | 4% | <a href="https://jobs.ashbyhq.com/phia/71c26b8b-86cd-446d-a63f-8cd8c2a3f162"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-05-26 · 18 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer, I - Data Engineering | Torc Robotics | Ann Arbor, MI | Not specified | ❌ No | 37% | <a href="https://job-boards.greenhouse.io/torcrobotics/jobs/8560188002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Agentic Software Engineer II | Deloitte | Multiple Locations | 2 | ❌ No | 30% | <a href="https://apply.deloitte.com/en_US/careers/JobDetail/Agentic-Software-Engineer-II/352139"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Full-Stack Software Engineer, Compute Foundations | OpenAI | San Francisco | Not specified | ❌ No | 30% | <a href="https://jobs.ashbyhq.com/openai/1312f55e-ff56-4dab-9bf7-a91e2c157572"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Scientist | Parafin | San Francisco, CA | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/parafin/cb15e569-764f-4304-a2cd-41a11fe9e008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer II - MES | Rocket Lab USA | Albuquerque, NM | 2 | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/rocketlab/jobs/7738610003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Calibration | Woven | Ann Arbor, MI | Not specified | ❌ No | 22% | <a href="https://jobs.lever.co/woven-by-toyota/43bdae02-424e-48f2-9648-b5aa16abcfc3"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Simulation | PlusAI | Santa Clara, CA | 2 | ❌ No | 22% | <a href="https://jobs.lever.co/plus-2/3e6f5196-a87d-402a-8bbf-b6dd14a82c78"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer - Vector Index | Neo4j | Malmö | Not specified | ❌ No | 19% | <a href="https://boards.greenhouse.io/neo4j/jobs/4684177006?gh_jid=4684177006"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Technical AI Instructor and Forward-Deployed Engineer III | Deloitte | Multiple Locations | 2 | ❌ No | 19% | <a href="https://apply.deloitte.com/en_US/careers/JobDetail/Technical-AI-Instructor-and-Forward-Deployed-Engineer-III/352277"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Marketing Performance Data Analyst | Filevine | Salt Lake City, Utah | Not specified | ❌ No | 15% | <a href="https://jobs.lever.co/filevine/a93b5d03-3185-41b9-a6d6-dc91b28167d6"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Compute | Persona | San Francisco | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/persona/25defcf7-530d-4cca-8faa-498e517401e6"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Founding Software Engineer - Backend | Hypercubic | San Francisco | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/hypercubic/497e109c-23cb-4d9a-a00c-14d0ebb86684"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Platform Engineer | Farfetch | Porto | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/farfetch/141b5d17-54ea-448e-8a09-7b26fdf47651"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Clinical AI Intern | Anterior | New York | Not specified | ❌ No | 7% | <a href="https://jobs.ashbyhq.com/anterior/550c48f9-eb2e-4d5e-80ff-8db076b4e52d"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer - AI & Cloud Engineering (Early to Mid Career, WI Based) | Flexcompute Inc. | Madison, Wisconsin, United States | Not specified | ❌ No | 7% | <a href="https://jobs.workable.com/view/spVeHyZgsnwdVggEU5V8qy/software-engineer---ai-%26-cloud-engineering-(early-to-mid-career%2C-wi-based)-in-madison-at-flexcompute-inc."><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Voice Trainer - Ilocano | Wing Assistant | Ilocos | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/getwingapp/3e0f8a2e-f525-4670-bfca-be8bbae64a62"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Voice Trainer - Malayalam | Wing Assistant | Kerala | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/getwingapp/b038516e-0825-4900-8325-0a391fe7a43b"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Voice Trainer - Punjabi | Wing Assistant | Punjab | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/getwingapp/854058f6-15b7-476b-9293-76a605393e5f"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-05-25 · 3 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Machine Learning Engineer II (Servicing ML) | Affirm | Remote US | 2 | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/affirm/jobs/7719651003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Analytics Engineer | Octopus Energy | Milan (IT) | Not specified | ❌ No | 19% | <a href="https://jobs.lever.co/octoenergy/5e3bbc9a-a2ea-4ad9-a81f-6ccedf175ce2"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Infrastructure Engineer | Triumph | San Francisco HQ | Not specified | ❌ No | 4% | <a href="https://jobs.ashbyhq.com/triumph-arcade/60b13af3-b81f-4e92-8914-ca4aba599f22"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-05-23 · 3 roles · 1 H-1B sponsor match

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer - Secret, Cryptographic and Identity Infrastructure | Snowflake | US-WA-Bellevue | Not specified | ✅ Yes | 15% | <a href="https://jobs.ashbyhq.com/snowflake/eb704210-4c4a-4ab7-8838-8ba7abd55af3"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, RL Training Infra | OpenAI | San Francisco | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/openai/13995549-e8cc-498f-9eaa-1869067ac35b"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Robotics Software Engineer, SLAM & 3D Mapping | Field AI | Irvine, CA | Not specified | ❌ No | 15% | <a href="https://jobs.lever.co/field-ai/8f3af86b-ded0-4c8a-a657-b89e50256bdd"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-05-22 · 25 roles · 1 H-1B sponsor match

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer | Stripe | Seattle, WA | 2 | ✅ Yes | 7% | <a href="https://stripe.com/jobs/search?gh_jid=7922832"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer (Sweep) | IntraFi | Arlington, VA | Not specified | ❌ No | 26% | <a href="https://jobs.lever.co/intrafi/eeae9603-9abb-4815-8a67-a2ffa00e9aca"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Computer Vision Engineer Intern | PlusAI | Santa Clara, CA | Not specified | ❌ No | 22% | <a href="https://jobs.lever.co/plus-2/c143df6e-66c2-4498-b19b-8323f9954ca9"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Deep Learning Intern | PlusAI | Santa Clara, CA | Not specified | ❌ No | 22% | <a href="https://jobs.lever.co/plus-2/58d77886-bf3a-4707-8af8-e1af47162e2e"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, ML Systems & Training Architecture | OpenAI | San Francisco | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/openai/9117987a-7a59-449e-a702-89e8d0e8cb60"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Intern, Data Analytics | EV Realty | San Francisco, CA | Not specified | ❌ No | 19% | <a href="https://jobs.lever.co/evrealty-us/0274f48f-9b19-4bed-bf6a-5e02a2b1e865"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Inference Engineer Intern - Model Pruning | Quadric | Burlingame, California, United States | Not specified | ❌ No | 15% | <a href="https://apply.workable.com/j/870833317E"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Scientist, Planetary Science | Relativity Space | Long Beach, California | Not specified | ❌ No | 15% | <a href="https://boards.greenhouse.io/relativity/jobs/8561541002?gh_jid=8561541002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Deep Learning Research Intern | PlusAI | Santa Clara, CA | 2 | ❌ No | 15% | <a href="https://jobs.lever.co/plus-2/2f2c1cd9-f099-483a-9717-0da83a391333"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Kernel Engineer Intern - Kernel Optimization | Quadric | Burlingame, California, United States | Not specified | ❌ No | 11% | <a href="https://apply.workable.com/j/6BEF4752B5"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| DevOps Engineer | Hawk-Eye Innovations | Hungary, Budapest | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/hawkeyeinnovations/8ad1131f-16ab-4c3f-971b-dab7d4d9000c"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| MacOS Software Engineer | Jane Street | New York, New York, United States | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/janestreet/jobs/8555588002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer (Thermal & Fluid Analysis) | SpaceX | Starbase, TX | 1 | ❌ No | 11% | <a href="https://boards.greenhouse.io/spacex/jobs/8562437002?gh_jid=8562437002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer - Postgres Internals | PlanetScale | San Francisco Bay Area or Remote | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/planetscale/jobs/4257174009"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Flight Software (Starship) | SpaceX | Hawthorne, CA | 2 | ❌ No | 11% | <a href="https://boards.greenhouse.io/spacex/jobs/8562450002?gh_jid=8562450002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Flight Software (Starship) | SpaceX | Starbase, TX | 2 | ❌ No | 11% | <a href="https://boards.greenhouse.io/spacex/jobs/8562284002?gh_jid=8562284002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Manufacturing Test Systems | Skild AI | San Mateo, California | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/skildai-careers/jobs/5228757008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Inference Engineer Intern - Model Pruning | quadric, Inc | Burlingame, California, United States | Not specified | ❌ No | 7% | <a href="https://jobs.workable.com/view/nPGayDLL6isV6eDWhcmuDp/ai-inference-engineer-intern---model-pruning-in-burlingame-at-quadric%2C-inc"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Kernel Engineer Intern - Kernel Optimization | quadric, Inc | Burlingame, California, United States | Not specified | ❌ No | 7% | <a href="https://jobs.workable.com/view/8BNznuLGqsVJHm8yoZZQv7/ai-kernel-engineer-intern---kernel-optimization-in-burlingame-at-quadric%2C-inc"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Linguistic AI Auditor (Italian) | RWS | Rome | Not specified | ❌ No | 7% | <a href="https://jobs.lever.co/rws/34a9ada3-28fb-4358-9a50-c4b56cfe9b93"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Linguistic AI Auditor (Simplified Chinese) | RWS | California | Not specified | ❌ No | 7% | <a href="https://jobs.lever.co/rws/3eb7a900-5409-43fa-9604-27463f84df8e"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Linguistic AI Auditor (Vietnamese) | RWS | California | Not specified | ❌ No | 7% | <a href="https://jobs.lever.co/rws/bc381fc4-b943-4006-a989-7a5f3356d2e5"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Engineer | Security Risk Advisors | Philadelphia, Pennsylvania, United States | Not specified | ❌ No | 4% | <a href="https://jobs.workable.com/view/9RtjZRJyENTQKB3sXX2qXq/hybrid-data-engineer-in-philadelphia-at-security-risk-advisors"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Ground Station Systems Engineer - Mission Operations | Lynk | Chantilly, VA | Not specified | ❌ No | 4% | <a href="https://jobs.ashbyhq.com/Lynk/1af67704-9c8d-47a4-a48c-7a50dabef6e1"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer | SOCOTEC Global | New York, NY, United States | Not specified | ❌ No | 4% | <a href="https://jobs.smartrecruiters.com/Socotec/744000127899832"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-05-21 · 31 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Data Scientist Engineer – SFL Scientific | Deloitte | Multiple Locations | 2 | ❌ No | 59% | <a href="https://apply.deloitte.com/en_US/careers/JobDetail/Data-Scientist-Engineer-SFL-Scientific/350764"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Scientist I | Axon | Seattle, Washington, United States | 1 | ❌ No | 41% | <a href="https://job-boards.greenhouse.io/axon/jobs/7746492003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Engineer (in person) | SEP | Westfield, IN | 2 | ❌ No | 22% | <a href="https://jobs.lever.co/sep/2eb79283-b3fd-4316-9e93-e80dbebfba05"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Middleware Software Engineer Intern - Fall 2026 | Skydio | San Mateo, California, United States | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/skydio/7d9dbb60-4ca1-4ba8-8bae-5ebfded4a915"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, AI-Native | Libra Solutions | Las Vegas, Nevada, United States | Not specified | ❌ No | 22% | <a href="https://jobs.workable.com/view/oDkz6stLxB2dukGoN8Bzmp/remote-software-engineer%2C-ai-native-in-las-vegas-at-libra-solutions"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Consultant, Data Analytics | Beghou Consulting | Emeryville, California | 2 | ❌ No | 19% | <a href="https://jobs.lever.co/beghouconsulting/73489eb8-5a3b-4bcf-b845-dce4b14f8cd2"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Consultant, Data Analytics | Beghou Consulting | Boston, Massachusetts | 2 | ❌ No | 19% | <a href="https://jobs.lever.co/beghouconsulting/13eb87a7-fe04-4138-af80-96b116e514cc"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Consultant, Data Analytics | Beghou Consulting | Rockville, Maryland | 2 | ❌ No | 19% | <a href="https://jobs.lever.co/beghouconsulting/825b2364-e8b5-4dff-8a09-54d4b620e789"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Consultant, Data Analytics | Beghou Consulting | San Diego, California | 2 | ❌ No | 19% | <a href="https://jobs.lever.co/beghouconsulting/d3205455-ad93-4285-8097-1eea5e27734f"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Cryptography Research Scientist, FHE | LG Electronics | Santa Clara, CA | 2 | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/lgelectronics/jobs/5226811008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer (Platform Team) | SpaceX | Bastrop, TX | 2 | ❌ No | 19% | <a href="https://boards.greenhouse.io/spacex/jobs/8560546002?gh_jid=8560546002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer (Platform Team) | SpaceX | Starbase, TX | 2 | ❌ No | 19% | <a href="https://boards.greenhouse.io/spacex/jobs/8560537002?gh_jid=8560537002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer - Product (New Grad) | Julius AI | San Francisco, CA | 0-2 | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/julius/5e0b677a-f677-44de-93c6-f7848ab5a8e6"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, ASIC | Neuralink | South San Francisco, California, United States | Not specified | ❌ No | 19% | <a href="https://boards.greenhouse.io/neuralink/jobs/7743087003?gh_jid=7743087003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Quality & Developer Tools \| Consumer Devices | OpenAI | San Francisco | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/openai/1ba666a4-0be2-4bd0-ad51-39ed7164c241"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Engineer Intern | Great Question | San Francisco | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/greatquestion/c533196c-75d5-43b8-b1c8-dedf2437d544"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| DC Devops Engineer | Pure Storage | Dallas, Texas | Not specified | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/purestorage/jobs/7944064"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Part-Time Student Worker AI & Automation: Supply Chain, Quality & Reliability | Zoox | Foster City, CA | Not specified | ❌ No | 15% | <a href="https://jobs.lever.co/zoox/e6aeeac7-f809-4679-b72c-effa5a39223d"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Quality Engineer, AI-Native | Libra Solutions | Las Vegas, Nevada, United States | Not specified | ❌ No | 15% | <a href="https://jobs.workable.com/view/1UkvYSQxe8wqtBynWoZ33a/remote-quality-engineer%2C-ai-native-in-las-vegas-at-libra-solutions"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, CI/CD | Neuralink | Austin, Texas, United States; South San Francisco, California, United States | Not specified | ❌ No | 15% | <a href="https://boards.greenhouse.io/neuralink/jobs/7743089003?gh_jid=7743089003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Engineer | OPPO US Research Center | Palo Alto, California, United States | Not specified | ❌ No | 11% | <a href="https://jobs.workable.com/view/4yYaFRoy7SqpvMEn23JGjk/ai-engineer-in-palo-alto-at-oppo-us-research-center"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Cloud Security Consultant – Azure Infrastructure & AI | Deloitte | Multiple Locations | 2 | ❌ No | 11% | <a href="https://apply.deloitte.com/en_US/careers/JobDetail/Cloud-Security-Consultant-Azure-Infrastructure-AI/353511"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Embedded Software Engineer, OS/Platform (Starlink) | SpaceX | Redmond, WA | 2 | ❌ No | 11% | <a href="https://boards.greenhouse.io/spacex/jobs/8552893002?gh_jid=8552893002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| OS/Platform Software Engineer (Starlink) | SpaceX | Redmond, WA | 2 | ❌ No | 11% | <a href="https://boards.greenhouse.io/spacex/jobs/8552882002?gh_jid=8552882002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Embedded Software (Starlink) | SpaceX | Redmond, WA | 2 | ❌ No | 11% | <a href="https://boards.greenhouse.io/spacex/jobs/8552752002?gh_jid=8552752002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Flight Software (Starlink) | SpaceX | Redmond, WA | 2 | ❌ No | 11% | <a href="https://boards.greenhouse.io/spacex/jobs/8551932002?gh_jid=8551932002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Content Creator (Contract) | Sleeper | Remote, United States | Not specified | ❌ No | 7% | <a href="https://jobs.ashbyhq.com/sleeper/fd7c8e44-caa4-4dff-b2d9-3a3365aae706"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Research Data Engineer | Alphatec Spine | Carlsbad, California, United States | Not specified | ❌ No | 7% | <a href="https://jobs.workable.com/view/oy2LFJjFvT65MxkjTJLiSH/research-data-engineer-in-carlsbad-at-alphatec-spine"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Voice Trainer - Bengali | Wing Assistant | West Bengal | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/getwingapp/92a250c1-bae0-4d04-b5af-95bffe4131df"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/Electrical Engineer (R&D) | AMAX | Fremont, California, United States | Not specified | ❌ No | 4% | <a href="https://jobs.workable.com/view/93jsoSaXZJPz6cyRT7n4qm/ai%2Felectrical-engineer-(r%26d)-in-fremont-at-amax"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Occupational Safety and Health Data Analyst | Eastern Research Group | Fairfax, VA | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/erg/55e6dfc9-fe22-4dec-80ae-8d4ec6e46b39"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-05-20 · 25 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Data Scientist, New Grad - Model Optimization | Quadric | Burlingame, California, United States | 0-2 | ❌ No | 33% | <a href="https://apply.workable.com/j/5A15DE8CCE"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Deployed Software Engineer (all levels) | Fieldguide | San Francisco, CA or Remote (USA) | Not specified | ❌ No | 30% | <a href="https://jobs.ashbyhq.com/fieldguide/5147ad09-1d4e-4cbf-93b0-b584ff46ce74"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Instructor - Generative AI in Data Analytics | Fullstack Academy | United States | Not specified | ❌ No | 30% | <a href="https://jobs.workable.com/view/dWLbaPJorv3rKjUynFMek9/remote-instructor---generative-ai-in-data-analytics-in-united-states-at-fullstack-academy"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Machine Learning Engineer Intern - Scenario Simulation | PlusAI | Santa Clara, CA | Not specified | ❌ No | 30% | <a href="https://jobs.lever.co/plus-2/b4f750e7-0148-41f0-b2b1-ff054450a320"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Machine Learning Engineer Intern - Scenario Generation | PlusAI | Santa Clara, CA | Not specified | ❌ No | 26% | <a href="https://jobs.lever.co/plus-2/1432ed29-d5e2-4348-acc4-9c42bf0897e2"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Computer Vision Engineer | BrightAI | Palo Alto, California | Not specified | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/brightai/jobs/6002012004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Machine Learning Engineer Intern | PlusAI | Santa Clara, CA | Not specified | ❌ No | 22% | <a href="https://jobs.lever.co/plus-2/5d71c173-fef1-409f-b3f0-750e3b828266"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Machine Learning Researcher | Scientech Research | New Jersey | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/scientech-research/b1eb5fed-4753-463d-9e3f-7683edc93522"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer II, Customer Lifecycle Engineering | Attentive | United States | 2 | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/attentive/jobs/4251552009"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Machine Learning Engineer Intern - Planning | PlusAI | Santa Clara, CA | Not specified | ❌ No | 19% | <a href="https://jobs.lever.co/plus-2/91a07eb1-2244-48bf-a65b-dc166a327ddc"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer (Platform Team) | SpaceX | Palo Alto, CA | 2 | ❌ No | 19% | <a href="https://boards.greenhouse.io/spacex/jobs/8558859002?gh_jid=8558859002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer (Platform Team) | SpaceX | Sunnyvale, CA | 2 | ❌ No | 19% | <a href="https://boards.greenhouse.io/spacex/jobs/8558858002?gh_jid=8558858002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer (Platform Team) | SpaceX | Redmond, WA | 2 | ❌ No | 19% | <a href="https://boards.greenhouse.io/spacex/jobs/8558857002?gh_jid=8558857002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Software Engineer (Fullstack) | Clearstory | Walnut Creek, California, United States | Not specified | ❌ No | 15% | <a href="https://jobs.workable.com/view/otth3Lrmad9kSaNNY5V6Tt/ai-software-engineer-(fullstack)-in-walnut-creek-at-clearstory"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Scientist, New Grad - Model Optimization | quadric, Inc | Burlingame, California, United States | 0-2 | ❌ No | 15% | <a href="https://jobs.workable.com/view/fdK9zefjzwnJCpfP5nTxCT/data-scientist%2C-new-grad---model-optimization-in-burlingame-at-quadric%2C-inc"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Site Reliability Engineer (Pacific timezone | PostHog | Remote | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/posthog/1464036f-94d5-4dbd-aef8-fe99246a26d4"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Full Stack | Exa Labs | San Francisco, California | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/exa/98a8bab6-4cbf-4d39-a5a7-0867addc4086"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Applied AI Engineer | Salient | SF Headquarters | 2 | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/salient/5bef27e7-17b3-4ad0-93e0-9e430409acd4"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer Intern - Robotics | PlusAI | Santa Clara, CA | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/plus-2/7a1afea9-b468-4b7c-a508-185e8e4032db"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Flight Software Engineer (Starlink Mobile) | SpaceX | Redmond, WA | Not specified | ❌ No | 7% | <a href="https://boards.greenhouse.io/spacex/jobs/8556909002?gh_jid=8556909002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer II (Security) | Aurora Innovation | Pittsburgh, Pennsylvania | 2 | ❌ No | 7% | <a href="https://aurora.tech/jobs/8557485002?gh_jid=8557485002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer II (Security) | Aurora Innovation | Seattle, Washington | 2 | ❌ No | 7% | <a href="https://aurora.tech/jobs/8557484002?gh_jid=8557484002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer II (Security) | Aurora Innovation | Mountain View, California | 2 | ❌ No | 7% | <a href="https://aurora.tech/jobs/8555225002?gh_jid=8555225002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer Intern- Runtime, Robotics | PlusAI | Santa Clara, CA | Not specified | ❌ No | 7% | <a href="https://jobs.lever.co/plus-2/a3bcdba6-b0d0-46ba-9af3-a387926a6fb4"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Web Developer & Digital Marketing Specialist: Full-Time - Onsite | Grapevine MSP Technology Services | Bakersfield, California, United States | Not specified | ❌ No | 4% | <a href="https://jobs.workable.com/view/o1sHqL5oaXenXL9BS3jSS1/web-developer-%26-digital-marketing-specialist%3A-full-time---onsite-in-bakersfield-at-grapevine-msp-technology-services"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-05-19 · 18 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| AI Engineer, Generative AI Agents | LG Ad Solutions | Denver, CO | Not specified | ❌ No | 37% | <a href="https://jobs.ashbyhq.com/lgads/e4f63ec6-ac22-471d-8e08-dc52fa9f8d6d"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Forward Deployment Engineer - Gen AI | Tiger Analytics Inc. | United States | Not specified | ❌ No | 22% | <a href="https://jobs.workable.com/view/kovTU4Pvj7DUvvdzabwvis/remote-forward-deployment-engineer---gen-ai-in-united-states-at-tiger-analytics-inc."><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Machine Learning Researcher | Scientech Research | Shanghai | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/scientech-research/c1672c16-dbea-4ea1-a427-07587fef886b"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Semantic Data and AI Engineer | Enterprise Knowledge | Arlington, Virginia, United States | Not specified | ❌ No | 22% | <a href="https://jobs.workable.com/view/bcwSzuHHfEQHtqjqCzpcYa/remote-semantic-data-and-ai-engineer-in-arlington-at-enterprise-knowledge"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Enterprise AI Platform | OpenAI | San Francisco | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/openai/a6363571-e090-43a7-b758-ee3386a096c1"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Analyst | CharterUP | Austin, Texas, United States | 2 | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/charterup/jobs/5225364008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer - Distributed Simulation Systems | Astera | Emeryville HQ | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/astera/147c1f34-98e6-40dd-91d8-f4da5475690c"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Accelerator Software Engineer | Etched.ai | San Jose | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/Etched/8e280db7-f954-4467-b3ea-b9b4386d6632"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Embedded Software Engineer II | Flock Safety | Remote - USA | 2 | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/Flock%20Safety/0d874965-3f92-4ad8-b4bd-5dc20cdc2d11"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer (Components) | SpaceX | Hawthorne, CA | 2 | ❌ No | 11% | <a href="https://boards.greenhouse.io/spacex/jobs/8557032002?gh_jid=8557032002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Systems Engineer I | Sony Interactive Entertainment | United States, Bellevue, WA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/sonyinteractiveentertainmentglobal/jobs/6000422004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| IT Systems Engineer II | BioAgilytix | Durham, NC | Not specified | ❌ No | 7% | <a href="https://jobs.lever.co/bioagilytix/6df451fd-8f6a-421c-8b4c-e2a6d8466432"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Voice Trainer - Gujarati | Wing Assistant | Gujarat | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/getwingapp/71b2452b-af0d-4d42-97bb-678bfc0baa6b"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Voice Trainer - Kannada | Wing Assistant | Karnataka | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/getwingapp/9c523521-5fdf-4390-8b25-77729c200bb8"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Voice Trainer - Marathi | Wing Assistant | Maharashtra | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/getwingapp/f4c055f5-2719-4178-83b1-aa09ad744c33"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Voice Trainer - Tamil | Wing Assistant | Tamil Nadu | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/getwingapp/d273363f-e5c3-408b-8b2c-f7fda1fb1ae1"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Voice Trainer - Telugu | Wing Assistant | Andhra Pradesh | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/getwingapp/d49227dd-1046-4c2f-a258-2261657d0e38"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Voice Trainer - Telugu | Wing Assistant | Telangana | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/getwingapp/f9128d22-a75a-4b4f-ad9e-ebd5858c8c9f"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-05-18 · 12 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Forward Deployed Engineer (Generative AI) | Tiger Analytics Inc. | United States | Not specified | ❌ No | 22% | <a href="https://jobs.workable.com/view/wEqeNpJrFHC2U67C9NhzhT/remote-forward-deployed-engineer-(generative-ai)-in-united-states-at-tiger-analytics-inc."><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Platform Engineer, Training and Inference | Saviynt | Milpitas, California | Not specified | ❌ No | 19% | <a href="https://jobs.lever.co/saviynt/9a8661ce-8856-4977-87f4-b06567125e28"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Scientist II, Experimentation | Pinterest | San Francisco, CA, US; Remote, US | 2 | ❌ No | 19% | <a href="https://www.pinterestcareers.com/jobs/?gh_jid=7896291"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Scientist II, Infrastructure | Pinterest | San Francisco, CA, US; Remote, US | Not specified | ❌ No | 19% | <a href="https://www.pinterestcareers.com/jobs/?gh_jid=7816424"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Founding AI Engineer | Bild AI | San Francisco | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/bild-ai/45434dce-1d56-4433-bade-38568e1fa979"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Research Scientist, Safety Post Training | Scale AI | San Francisco, CA; New York, NY | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/scaleai/jobs/4696595005"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Security Researcher, Agentic AI Threats | OpenAI | San Francisco | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/openai/e0eef869-cd4d-4737-b7af-75c5a1970aeb"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| App Engineer (AI & Automation) | LaunchDarkly | Hybrid - Bangalore; Hybrid - Mumbai | Not specified | ❌ No | 7% | <a href="https://job-boards.greenhouse.io/launchdarkly/jobs/7738141003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Associate Research Scientist, Evidence Generation | Precision AQ | Remote, United States | 2 | ❌ No | 7% | <a href="https://job-boards.greenhouse.io/precisionaq/jobs/5996348004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Scientist - Healthcare (Hybrid / New York Metro) | AssistRx | New York, United States | Not specified | ❌ No | 7% | <a href="https://jobs.workable.com/view/x3FDwceY9ZiJZz2D1Nbpb8/hybrid-data-scientist---healthcare-(hybrid-%2F-new-york-metro)-in-new-york-at-assistrx"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Full Stack Software Engineer I or II | CVector - Industrial AI | New York, New York, United States | Not specified | ❌ No | 7% | <a href="https://jobs.workable.com/view/hJXCVjxkp3j1botSahusmy/full-stack-software-engineer-i-or-ii-in-new-york-at-cvector---industrial-ai"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Founding AI Research Engineer - Robot Learning | Origin | San Francisco, California, United States | Not specified | ❌ No | 4% | <a href="https://jobs.workable.com/view/eMCJdYC7KZA618n5Aup9px/founding-ai-research-engineer---robot-learning-in-san-francisco-at-origin"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-05-17 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Laser Systems Engineer | QuEra Computing | Boston, MA, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/queracomputinginc/jobs/5223167008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-05-16 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Full Stack Software Engineer, Data | SpaceX | Starbase, TX | 2 | ❌ No | 41% | <a href="https://boards.greenhouse.io/spacex/jobs/8553080002?gh_jid=8553080002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, User Operations | Cursor | Remote | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/cursor/1d6dbbb2-a5af-41a6-a70a-ca97690d9313"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-05-15 · 26 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Machine Learning Engineer (I-III) | True Anomaly | Denver, CO or Long Beach, CA | Not specified | ❌ No | 48% | <a href="https://job-boards.greenhouse.io/trueanomalyinc/jobs/5138856007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Infrastructure Engineer | Roboflow | NY, SF or Remote | Not specified | ❌ No | 41% | <a href="https://jobs.ashbyhq.com/roboflow/6aca5391-3bbc-4d49-a8ff-952903d3cc3c"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Embedded Agentic AI | Roku | San Jose, California | 2 | ❌ No | 37% | <a href="https://www.weareroku.com/jobs/7868793?gh_jid=7868793"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Engineer | Makai Labs | New York | Not specified | ❌ No | 30% | <a href="https://jobs.ashbyhq.com/makai-labs/a350e730-8d80-4528-9d41-497acbd01223"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Scientist, Safety | OpenAI | San Francisco | Not specified | ❌ No | 26% | <a href="https://jobs.ashbyhq.com/openai/90c711dc-5f50-46e3-a5ab-82359a56d683"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Generative AI - ML System Engineering | Meshy | Shanghai | Not specified | ❌ No | 26% | <a href="https://jobs.ashbyhq.com/meshy/f05f55f9-8996-4ccf-bab7-b99e087648fa"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer (L2) Segment Team | Twilio | Remote - US | 2 | ❌ No | 26% | <a href="https://job-boards.greenhouse.io/twilio/jobs/7767263"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Engineer - Remote | Huzzle | United States | 2 | ❌ No | 22% | <a href="https://jobs.workable.com/view/43GzkzjdyV2AkVLa384SD1/ai-engineer---remote-in-united-states-at-huzzle"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Systems Engineer, Codex Agents | OpenAI | San Francisco | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/openai/de06790a-7243-4e33-a6f1-e7bd34009588"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Scientist | Doximity | San Francisco, CA or Remote (U.S.) | Not specified | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/doximity/jobs/7909273"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer II (Backend, Enterprise) | Whoop | Boston, MA | 2 | ❌ No | 22% | <a href="https://jobs.lever.co/whoop/5bb99b67-fac6-416e-b992-2a37ca2c7ee8"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer Intern - Data | PlusAI | Santa Clara, CA | Not specified | ❌ No | 22% | <a href="https://jobs.lever.co/plus-2/012a2134-8a6a-4982-8f25-f906178a24e4"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Applied AI Engineer, Ops | Alloy | New York City | Not specified | ❌ No | 19% | <a href="https://www.alloy.com/about/jobs/detail?gh_jid=8552760002&amp;gh_jid=8552760002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Full Stack Engineer Intern | PlusAI | Santa Clara, CA | Not specified | ❌ No | 19% | <a href="https://jobs.lever.co/plus-2/b69c9b6d-483f-41d4-b487-97c99332ca40"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Full-Stack Developer (Nextjs / Python / AI) | Valsoft Corporation | Beirut, Beirut Governorate, Lebanon | Not specified | ❌ No | 19% | <a href="https://apply.workable.com/j/00A2198F76"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Machine Learning Infrastructure Engineer Intern | PlusAI | Santa Clara, CA | Not specified | ❌ No | 19% | <a href="https://jobs.lever.co/plus-2/30dd9b9b-48c8-4777-97f6-8edb30db12e4"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Researcher Intern | GenScript | United States | Not specified | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/genscript/jobs/5138842007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Research Scientist I/II, Multiscale & Multiphysics Simulations | Lila Sciences | Cambridge, MA USA | Not specified | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/lilasciences/jobs/4243144009"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Development Engineer In Test | Sony Interactive Entertainment | United States, San Mateo, CA | Not specified | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/sonyinteractiveentertainmentglobal/jobs/5993042004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Tech Ops | ZipRecruiter | Los Angeles, CA | 2 | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/ziprecruiter/jobs/7927670"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer Intern - Data Infrastructure and Tools | PlusAI | Santa Clara, CA | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/plus-2/06b808df-85a1-4ddd-863c-3e1cbe61eda9"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Product & AI Quality Intern, Technical Projects Group | Schmidt Sciences | New York, NY | Not specified | ❌ No | 7% | <a href="https://jobs.lever.co/schmidt-entities/5b4bf839-143f-4399-89fe-097c4690c18c"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Implementation Associate | Highbeam | New York | Not specified | ❌ No | 4% | <a href="https://jobs.ashbyhq.com/highbeam/60b69921-b805-4a8d-a6ef-bba2a3aba05d"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data & Control Systems Engineer | SpaceX | Cape Canaveral, FL | Not specified | ❌ No | 4% | <a href="https://boards.greenhouse.io/spacex/jobs/8552660002?gh_jid=8552660002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Linguistics Experts in the US — Contribute to AI Speech Annotation! | CrowdGen by Appen | Any | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/appen/2ffcfdbc-a973-4176-9fdc-74c0e820315f"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Research Infrastructure and Software Engineer | Harvard University | Cambridge, MA, United States | Not specified | ❌ No | 4% | <a href="https://jobs.smartrecruiters.com/HarvardUniversity/3743990013167156"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-05-14 · 16 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer, Backend (Warsaw) | Mistral AI | Warsaw | Not specified | ❌ No | 33% | <a href="https://jobs.lever.co/mistral/126f59ee-2ad3-4dea-ab16-337c84fec561"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Product Engineer | Lightfield | HQ: San Francisco | Not specified | ❌ No | 30% | <a href="https://jobs.ashbyhq.com/Lightfield/b32dc57b-ffa0-4bb7-99c8-f469c3876002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Agent Data Pipeline Intern | XPENG Motors | Santa Clara, CA | Not specified | ❌ No | 26% | <a href="https://job-boards.greenhouse.io/xpengmotors/jobs/8548990002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Full Stack Engineer, Product & Systems | Lightfield | HQ: San Francisco | 2 | ❌ No | 26% | <a href="https://jobs.ashbyhq.com/Lightfield/412ff3ec-19d5-41d9-847c-0a93a80ed191"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Full Stack AI Engineer | OpusClip | Mountain View | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/opusclip/02c5fdd5-5818-4a7f-999c-6071ddbe00fe"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, News Multimodal | The New York Times | New York, NY | 2 | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/thenewyorktimes/jobs/4693057005"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Business Strategist (Contractor) | SK hynix | San Jose, CA | 2 | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/skhynixamerica/jobs/5219921008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| GenAI Data Engineer | Tiger Analytics Inc. | Hartford, Connecticut, United States | Not specified | ❌ No | 15% | <a href="https://jobs.workable.com/view/594JtwD4tA2kwRhqwbdt2D/remote-genai-data-engineer-in-hartford-at-tiger-analytics-inc."><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Security Software Engineer (Starlink) | SpaceX | Redmond, WA | 2 | ❌ No | 15% | <a href="https://boards.greenhouse.io/spacex/jobs/8543668002?gh_jid=8543668002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Business Intelligence Analyst | LaBella Associates | Rochester, New York, United States | Not specified | ❌ No | 11% | <a href="https://jobs.workable.com/view/wvrfZ86UVbSnRDhNqNmpn6/hybrid-business-intelligence-analyst-in-rochester-at-labella-associates"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Cloud Infrastructure Engineer | Thunder Compute | San Francisco | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/thundercompute/927a922b-c607-4b0e-a6f2-451571a537f4"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Systems Software Engineer (C++) | Thunder Compute | San Francisco | 1 | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/thundercompute/2efae53b-817c-43e7-9da3-72694813f608"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Artist | OpusClip | Mountain View | Not specified | ❌ No | 7% | <a href="https://jobs.ashbyhq.com/opusclip/69bb7a1e-6ff0-47df-8ffb-c3bed216307f"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer - Microsoft Dynamics 365FO | Farfetch | Porto | Not specified | ❌ No | 7% | <a href="https://jobs.lever.co/farfetch/d27f5520-4f45-46eb-ab64-8245acddfd39"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Driven Verification CAD Engineer | Sandisk | Milpitas, CA, United States | Not specified | ❌ No | 4% | <a href="https://jobs.smartrecruiters.com/Sandisk/744000126555309"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Revenue AI Solutions Analyst | Sandisk | Milpitas, CA, United States | Not specified | ❌ No | 4% | <a href="https://jobs.smartrecruiters.com/Sandisk/744000126587280"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-05-13 · 16 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| AI/ML Infrastructure Engineer | Zensors | San Francisco | Not specified | ❌ No | 33% | <a href="https://jobs.ashbyhq.com/zensors/d00b1704-5330-4af3-99e6-03ea02df8026"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Engineer I | ClimateAI | San Francisco, California, United States | Not specified | ❌ No | 26% | <a href="https://job-boards.greenhouse.io/climateai/jobs/5137357007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Scientist, Core Experimentation | OpenAI | Seattle | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/openai/e90a44a7-fc2e-49bf-aec4-d43b9e3d8e92"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Credit | Ramp | New York, NY (HQ) | 2 | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/ramp/5598f7b8-4ae2-4105-a2b4-2d0f55c54c40"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Chip Simulation Software Engineer | Etched.ai | San Jose | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/Etched/29b303b2-f1a5-4799-a0b2-e86e28289a9b"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Engineer | Perpay | Philadelphia, Pennsylvania, United States | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/perpay/jobs/4089104007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Sales AI Engineer | Figma | San Francisco, CA • New York, NY • United States | Not specified | ❌ No | 19% | <a href="https://boards.greenhouse.io/figma/jobs/5991176004?gh_jid=5991176004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Analytics Engineer II | Spotify | Stockholm | 2 | ❌ No | 15% | <a href="https://jobs.lever.co/spotify/08d82da1-0c72-44d1-91eb-7fa22dee3d39"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Security Software Engineer (Starlink) | SpaceX | Redmond, WA | 2 | ❌ No | 15% | <a href="https://boards.greenhouse.io/spacex/jobs/8543784002?gh_jid=8543784002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Security Software Engineer (Starlink) | SpaceX | Hawthorne, CA | 2 | ❌ No | 15% | <a href="https://boards.greenhouse.io/spacex/jobs/8543817002?gh_jid=8543817002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer II | Sony Interactive Entertainment | United States, San Diego, CA | 2 | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/sonyinteractiveentertainmentglobal/jobs/5995645004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Applied AI Engineer | Tolan | San Francisco | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/tolan/84c0dc1d-de28-40f0-b1ef-b8af5f18c8e4"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| DevOps Engineer | DRW | Chicago, Austin | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/drweng/jobs/7913994"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer- Backend Intern (Fall 2026) | Astranis | San Francisco, CA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/astranis/jobs/4681183006"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Analytics Consultant, Journeyman - Financial Emphasis | Aretum | McLean, Virginia, United States | Not specified | ❌ No | 7% | <a href="https://jobs.workable.com/view/oyEBXJCRosCBxrLmwqs7KN/remote-data-analytics-consultant%2C-journeyman---financial-emphasis-in-mclean-at-aretum"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Instructional Designer, HBS AI Institute | Harvard University | Boston, MA, United States | Not specified | ❌ No | 4% | <a href="https://jobs.smartrecruiters.com/HarvardUniversity/3743990013111626"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-05-12 · 19 roles · 2 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer - Snowflake Postgres | Snowflake | US-CA-Menlo Park | 2 | ✅ Yes | 19% | <a href="https://jobs.ashbyhq.com/snowflake/19ff5740-e678-4f43-a6c6-29bab94fbc21"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer Intern - Zurich (2026) | Snowflake | CH-Zurich-Observe | Not specified | ✅ Yes | 15% | <a href="https://jobs.ashbyhq.com/snowflake/26a0ae52-97a6-4a46-9216-3c382570d89b"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Machine Learning Engineer, LLM Evals & Observability | Glean | Mountain View, CA | 2 | ❌ No | 33% | <a href="https://job-boards.greenhouse.io/gleanwork/jobs/4694716005"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Applied AI & Analytics Associate Opportunities | SharkNinja | Needham, MA, United States | 2 | ❌ No | 30% | <a href="https://job-boards.greenhouse.io/sharkninjaoperatingllc/jobs/4680287006"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer II Python | Onapsis | Dallas, Texas, United States | 2 | ❌ No | 26% | <a href="https://job-boards.greenhouse.io/onapsis/jobs/8545473002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Systems Engineer II | ExtraHop | Seattle, WA | 2 | ❌ No | 26% | <a href="https://job-boards.greenhouse.io/extrahopnetworks/jobs/5993893004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer - Human Motion Data | Apptronik | Austin, TX | 2 | ❌ No | 22% | <a href="https://boards.greenhouse.io/apptronik/jobs/5994540004?gh_jid=5994540004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Developer Marketer - AI observability | PostHog | Remote | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/posthog/068ba58d-0143-4263-b83a-7b389c4d77e6"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| People Analytics & AI Specialist | Faire | New York City, NY; San Francisco, CA | Not specified | ❌ No | 11% | <a href="https://boards.greenhouse.io/faire/jobs/8545972002?gh_jid=8545972002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer - Ride and Fleet Services | Zoox | San Diego, CA | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/zoox/2783987b-5ab8-4447-a9e4-77745439e7ba"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Hardware Test & Automation (Optical Payloads) | SpaceX | Redmond, WA | 2 | ❌ No | 11% | <a href="https://boards.greenhouse.io/spacex/jobs/8545930002?gh_jid=8545930002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Next.js | Vercel | Hybrid - San Francisco | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/vercel/jobs/5993753004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Product | Salient | SF Headquarters | 2 | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/salient/a213eea8-ef18-40cb-b693-67ca3900c7fb"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| WebApp Offensive Security Software Engineer | Horizon3.ai | US, Remote | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/horizon3ai/3a664c46-88f2-4367-8aa1-4413d29acd19"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI 数据平台产品经理｜标注 / 评测方向 | Creatify | Palo Alto, CA | Not specified | ❌ No | 7% | <a href="https://jobs.ashbyhq.com/embedding-vc/c3ce1f94-b566-4b72-9342-0a617ae18b53"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Cloud Platform Engineer | Accenture | Arlington, VA | Not specified | ❌ No | 7% | <a href="https://boards.greenhouse.io/accenturefederalservices/jobs/4681156006?gh_jid=4681156006"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Embedded Systems Engineer-Federal | Field AI | Irvine, CA | Not specified | ❌ No | 7% | <a href="https://jobs.lever.co/field-ai/5aa0a3ef-b693-4404-829a-63d8b9dad776"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Research Scientist | Cogent Security | San Francisco, CA | Not specified | ❌ No | 7% | <a href="https://jobs.ashbyhq.com/cogent-security/ce972e7a-d724-46a5-873c-9b2ba8397bb8"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Hardware Deployment Technician (AI & Robotics) | Treeswift | San Francisco | Not specified | ❌ No | 4% | <a href="https://jobs.ashbyhq.com/treeswift/caf13558-a4f8-48cf-8823-94965fcc5e01"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-05-11 · 13 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Machine Learning Engineer, Underwriting | Bree | Remote | Not specified | ❌ No | 44% | <a href="https://jobs.ashbyhq.com/bree/f33dd42a-6a68-495d-baa6-2830ca9e5834"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Engineer | AI Fund | Mountain View, CA | Not specified | ❌ No | 33% | <a href="https://jobs.lever.co/AIFund/273af06c-9114-4b9c-83c9-a3627f4b875f"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Founding Software Engineer | Tamarind Bio | San Francisco | Not specified | ❌ No | 33% | <a href="https://jobs.ashbyhq.com/tamarindbio/fac142a8-4ade-432b-a3e5-e8a6b33ce20d"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer (AI-Driven Billing Automation) | ArteraAI | Remote-US | 2 | ❌ No | 30% | <a href="https://jobs.lever.co/artera/cc5cbc4d-c7e7-4573-993f-526cb33f5a81"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Engineer - Remote | Huzzle | United States | Not specified | ❌ No | 19% | <a href="https://jobs.workable.com/view/rwrMWhX66jmNMYk8dQ9p1i/ai-engineer---remote-in-united-states-at-huzzle"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Prompt Developer | DoubleVerify | NYC Global HQ | 2 | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/doubleverify/jobs/8539964002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Embedded Systems Software Engineer | REGENT | North Kingstown, Rhode Island, USA | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/regent/f8d421ad-93ae-4b99-873e-65892f0f083e"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Security Software Engineer II, Security Operations | Pinterest | Chicago, IL, US; Remote, US | Not specified | ❌ No | 15% | <a href="https://www.pinterestcareers.com/jobs/?gh_jid=7816431"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer - Federal Mission Workflows | Field AI | Irvine, CA | Not specified | ❌ No | 15% | <a href="https://jobs.lever.co/field-ai/d3ca1d03-e67c-440a-9061-14437e870663"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer - Fleet | Lambda | San Francisco Office (Fremont St) | 2 | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/lambda/d96f72bd-d78e-4a2b-9d9f-faa10b9ec883"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Development Engineer in Test Contractor (SDET Contractor) | Sony Interactive Entertainment | United States, San Mateo, CA | Not specified | ❌ No | 7% | <a href="https://job-boards.greenhouse.io/sonyinteractiveentertainmentglobal/jobs/5993055004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer | Midwestern Software Solutions, LLC ("MS2") | Ann Arbor, Michigan, United States | Not specified | ❌ No | 7% | <a href="https://jobs.workable.com/view/qFV11TkrgVc18srLjpcZS3/hybrid-software-engineer-in-ann-arbor-at-midwestern-software-solutions%2C-llc-(%22ms2%22)"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Sensor Systems Engineer-Federal | Field AI | Irvine, CA | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/field-ai/c0932811-6a6e-45b4-bced-4d0efe50d427"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-05-10 · 4 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Agentic AI Engineer | Trilagen | New York, New York, United States | Not specified | ❌ No | 22% | <a href="https://jobs.workable.com/view/13kDzVtFSKZX6cmS2RY5Vp/hybrid-agentic-ai-engineer-in-new-york-at-trilagen"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Agentic AI Engineer | Trilagen | McLean, Virginia, United States | Not specified | ❌ No | 22% | <a href="https://jobs.workable.com/view/ePrX7icinZAooumVnxu9Cs/hybrid-agentic-ai-engineer-in-mclean-at-trilagen"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Agentic AI Engineer | Trilagen | Bethesda, Maryland, United States | Not specified | ❌ No | 22% | <a href="https://jobs.workable.com/view/k1Q1pyjoekxSavuLDThJRw/hybrid-agentic-ai-engineer-in-bethesda-at-trilagen"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Productivity - Inference Runtime | OpenAI | San Francisco | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/openai/9d48e2e6-41a9-4a90-8b3b-6cc960e95c2f"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-05-09 · 4 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Last Minute AI-Machine Learning Summer Internship (Gen AI - Multimodal) | Eluvio | Berkeley, California, United States | Not specified | ❌ No | 41% | <a href="https://apply.workable.com/j/F70F3473E7"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Machine Learning Engineer | Human Archive | San Francisco | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/humanarchive/98291570-1c51-4517-93f8-845fea602f43"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Site Reliability Engineer | Cognition | San Francisco | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/cognition/d50d94b0-60c8-4dae-9c36-234f072ee4e3"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Research Engineer | Cogent Security | San Francisco, CA | Not specified | ❌ No | 7% | <a href="https://jobs.ashbyhq.com/cogent-security/d0b45843-f1d7-4711-8e0d-9cd180d336d7"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-05-08 · 11 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| 2026 Fall Intern, ML/NLP Research | Samsung Research America | 665 Clyde Avenue, Mountain View, CA, USA | Not specified | ❌ No | 37% | <a href="https://job-boards.greenhouse.io/samsungresearchamericainternship/jobs/8541339002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Full Stack Software Engineer, Data (Starlink) | SpaceX | Hawthorne, CA | 2 | ❌ No | 30% | <a href="https://boards.greenhouse.io/spacex/jobs/8540435002?gh_jid=8540435002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Artificial Intelligence Analyst, I | Pathward | Remote | 2 | ❌ No | 26% | <a href="https://job-boards.greenhouse.io/pathward/jobs/5992061004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer - Forecasting & Scheduling | Assembled | United States | Not specified | ❌ No | 26% | <a href="https://jobs.ashbyhq.com/assembledhq/935215f5-7699-42ba-b102-52f385279d3d"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer - Forecasting & Scheduling | Assembled | San Francisco, CA | Not specified | ❌ No | 26% | <a href="https://jobs.ashbyhq.com/assembledhq/c66054bb-694f-4077-8012-f71dd0a61a0c"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer II - Mobile | Alarm.com | Tysons, Virginia | 2 | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/alarmcom/jobs/8538618002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Site Reliability Engineer III, Aviation | Flock Safety | Remote - USA | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/Flock%20Safety/8f4dd66b-9051-44c0-b192-54041d715e7c"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Android | Zoox | Foster City, CA | 1 | ❌ No | 15% | <a href="https://jobs.lever.co/zoox/d48270e1-81e0-4f04-ab9e-d1fc25313f76"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Developer Productivity | MongoDB | New York City | Not specified | ❌ No | 15% | <a href="https://www.mongodb.com/careers/job/?gh_jid=7851388"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Embedded Software Engineer III | ALTEN Technology | Greensboro, North Carolina, United States | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/altentechnologyusa/jobs/5126464007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer (Video Player) | Genius Sports | Medellín, Antioquia, Colombia | Not specified | ❌ No | 7% | <a href="https://boards.greenhouse.io/geniussports/jobs/7727686003?gh_jid=7727686003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-05-07 · 14 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Data Science Intern (Customer Success) | Cresta | United States (Remote) | Not specified | ❌ No | 56% | <a href="https://job-boards.greenhouse.io/cresta/jobs/5213417008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer II - Data Engineering | Rocket Lab USA | Auckland, NZ | Not specified | ❌ No | 37% | <a href="https://job-boards.greenhouse.io/rocketlab/jobs/7727892003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Scientist, Supply | Anthropic | San Francisco, CA \| New York City, NY | Not specified | ❌ No | 26% | <a href="https://job-boards.greenhouse.io/anthropic/jobs/5212119008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Analytics Engineer I | Oscar Health | New York, New York, United States | 1 | ❌ No | 22% | <a href="http://www.hioscar.com/careers/7872595?gh_jid=7872595"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Autonomy Engineer - ML & DL Infrastructure | Skydio | San Mateo, California, United States | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/skydio/b6be08f7-89c0-48dd-b427-f587f23dbf34"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Backend Software Engineer, Applied Foundations | OpenAI | San Francisco | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/openai/b398e1c6-0c32-4464-bb34-6ccda901b688"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Platform Engineer | WebAI | Austin, TX | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/webai/82459a75-50a2-4fbb-a631-e057e0c4396a"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Full Stack Software Engineer - Alts & Data Management | Addepar | New York, NY | 2 | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/addepar1/jobs/8538666002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Frontend Engineer II, AI Experiences | Box | Redwood City, CA | 1 | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/boxinc/jobs/7886709"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Full-Stack Software Engineer, Applied Foundations | OpenAI | San Francisco | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/openai/f873dd71-46c9-4be1-8580-bc67c56b4cad"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Platform Engineer | Base Power | Austin, TX | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/base-power/10772e1c-dfad-4161-9e9e-5f34728c4745"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Applied Scientist | Clipboard Health | Hybrid (San Francisco, CA) | Not specified | ❌ No | 7% | <a href="https://jobs.ashbyhq.com/clipboard/8e59b9ee-5e85-49f8-9750-1c9c1e9bb52a"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Distributed Systems Engineer | Dedalus Labs | San Francisco | Not specified | ❌ No | 4% | <a href="https://jobs.ashbyhq.com/dedalus-labs/e71ec106-a376-42cb-88de-264c95d423ed"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Junior Engineer, AI | BME Strategies | United States | 0-2 | ❌ No | 4% | <a href="https://jobs.workable.com/view/qjrGNapN75tbumDBMFisdm/remote-junior-engineer%2C-ai-in-united-states-at-bme-strategies"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-05-06 · 13 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Clinical Data Engineer | Eight Sleep | Boston Area | 2 | ❌ No | 37% | <a href="https://jobs.ashbyhq.com/eightsleep/63be4811-838b-4075-8828-718603c11eba"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Machine Learning Scientist — Agentic data pipelines | Iambic Therapeutics | Boston Office | Not specified | ❌ No | 33% | <a href="https://jobs.ashbyhq.com/iambic-therapeutics/deb88095-f8c6-4cbc-bd79-de8984a30846"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Machine Learning Scientist — Large multimodal models | Iambic Therapeutics | Boston Office | Not specified | ❌ No | 33% | <a href="https://jobs.ashbyhq.com/iambic-therapeutics/bccc58b8-6022-49d4-865b-931176a88b8e"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Deep Learning Compiler Engineer (New Grad) | Quadric | Burlingame, California, United States | 0-2 | ❌ No | 22% | <a href="https://apply.workable.com/j/43779C9213"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Core Network Engineering | OpenAI | San Francisco | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/openai/1fec5ecd-5b7b-45bc-bc8c-ac7184565551"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Infrastructure | CLEAR | New York, New York, United States | 2 | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/clear/jobs/7901600"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Kernel Engineer (New Grad) | Quadric | Burlingame, California, United States | 0-2 | ❌ No | 15% | <a href="https://apply.workable.com/j/B8F898E1F5"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Associate Software Engineer-Data and Integrations | City of Philadelphia | Philadelphia, PA, United States | Not specified | ❌ No | 15% | <a href="https://jobs.smartrecruiters.com/CityofPhiladelphia/744000124984721"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Deep Learning Compiler Engineer (New Grad) | quadric, Inc | Burlingame, California, United States | 0-2 | ❌ No | 15% | <a href="https://jobs.workable.com/view/qhRxgq75LzsLDMVVv26bSb/hybrid-deep-learning-compiler-engineer-(new-grad)-in-burlingame-at-quadric%2C-inc"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Kernel Engineer (New Grad) | quadric, Inc | Burlingame, California, United States | 0-2 | ❌ No | 11% | <a href="https://jobs.workable.com/view/uwW8jmkcMXLmTqtNUj4gsK/hybrid-ai-kernel-engineer-(new-grad)-in-burlingame-at-quadric%2C-inc"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Associate Software Engineer-Applications & Automation | City of Philadelphia | Philadelphia, PA, United States | Not specified | ❌ No | 11% | <a href="https://jobs.smartrecruiters.com/CityofPhiladelphia/744000124986404"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer (Range Systems) | Saalex | Corona, California, United States | Not specified | ❌ No | 7% | <a href="https://jobs.workable.com/view/6xTLdEWhVmDa1cvU2KqDjJ/hybrid-software-engineer-(range-systems)-in-corona-at-saalex"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Associate Systems Engineer | City of Philadelphia | Philadelphia, PA, United States | 2 | ❌ No | 4% | <a href="https://jobs.smartrecruiters.com/CityofPhiladelphia/744000124984059"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-05-05 · 29 roles · 6 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Data Scientist, Algorithms, Optimization - Fulfillment | Lyft | San Francisco, CA | 2 | ✅ Yes | 26% | <a href="https://app.careerpuck.com/job-board/lyft/job/8536085002?gh_jid=8536085002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer | Stripe | San Francisco, California | 2 | ✅ Yes | 19% | <a href="https://stripe.com/jobs/search?gh_jid=7895344"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Distinguished Software Engineer, Machine Learning (Growth) | LinkedIn | Mountain View, CA, United States | Not specified | ✅ Yes | 7% | <a href="https://jobs.smartrecruiters.com/LinkedIn3/744000124684984"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Distinguished Software Engineer, Systems Infrastructure | LinkedIn | Mountain View, CA, United States | Not specified | ✅ Yes | 4% | <a href="https://jobs.smartrecruiters.com/LinkedIn3/744000124685990"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Distinguished Software Engineer, Systems Infrastructure - Core Infra | LinkedIn | Bellevue, WA, United States | Not specified | ✅ Yes | 4% | <a href="https://jobs.smartrecruiters.com/LinkedIn3/744000124729737"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Distinguished Software Engineer, Systems Infrastructure - Core Infra | LinkedIn | Mountain View, CA, United States | Not specified | ✅ Yes | 4% | <a href="https://jobs.smartrecruiters.com/LinkedIn3/744000124688119"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Engineer | Nimble Gravity | LATAM (Remote), US (Remote) | Not specified | ❌ No | 37% | <a href="https://job-boards.greenhouse.io/nimblegravity/jobs/4692556005"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Backend Software Engineer | Lumafield | San Francisco, CA | 2 | ❌ No | 37% | <a href="https://jobs.lever.co/lumafield/a162ca4e-4beb-4f6f-94ac-44e327e481b0"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Ray Serve | Anyscale | Bengaluru, Karnataka | Not specified | ❌ No | 30% | <a href="https://jobs.ashbyhq.com/anyscale/c35b6d34-710d-4943-85b6-2073ff4eecd1"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Intern – VLA Deployment | XPENG Motors | Santa Clara, CA | Not specified | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/xpengmotors/jobs/8535409002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Graduate Engineer - AI Agents | LiveFlow | San Francisco | 2 | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/liveflow/93a4d132-b68c-42d7-ace0-7975661130ba"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Machine Learning Computer Vision Intern | Syntiant | Redwood City, California, United States | Not specified | ❌ No | 22% | <a href="https://jobs.workable.com/view/cEpLQBCRMUXE3rDnEMhnmY/machine-learning-computer-vision-intern-in-redwood-city-at-syntiant"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer (Cloud, Cross-Platform & .NET Systems) | Altom Transport | Houston, Texas, United States | Not specified | ❌ No | 22% | <a href="https://jobs.workable.com/view/a2AiLUiAJ2CodNg53eftuv/software-engineer-(cloud%2C-cross-platform-%26-.net-systems)-in-houston-at-altom-transport"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer (Cloud, Cross-Platform & .NET Systems) | Altom Transport | Chicago, Illinois, United States | Not specified | ❌ No | 22% | <a href="https://jobs.workable.com/view/wcBNSmsxwPuC1NPQRmUMDv/software-engineer-(cloud%2C-cross-platform-%26-.net-systems)-in-chicago-at-altom-transport"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer - AI Agents | LiveFlow | San Francisco | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/liveflow/e1ba2bad-030a-4bc2-9bbd-f1375f712a57"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer Intern Fall 2026/Winter 2027 | Skydio | San Mateo, California, United States | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/skydio/f6320e9b-4eed-408d-8d37-d509fb0406ee"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Research Scientist | Oura | Remote - United States | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/oura/jobs/4239300009"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Data Platform | Nuro | Mountain View, California (HQ) | 1 | ❌ No | 19% | <a href="https://nuro.ai/careersitem?gh_jid=7895644"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, ML Data Infrastructure | Nuro | Mountain View, California (HQ) | 1 | ❌ No | 19% | <a href="https://nuro.ai/careersitem?gh_jid=7895818"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Scientist/AI Engineer (Contingent) | KIHOMAC | Aberdeen Proving Ground, Maryland, United States | Not specified | ❌ No | 15% | <a href="https://jobs.workable.com/view/hWH5DGSX4BSZYP93HcZGtY/data-scientist%2Fai-engineer-(contingent)-in-aberdeen-proving-ground-at-kihomac"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| SAP AI Developer | Accenture | Washington, DC | 2 | ❌ No | 15% | <a href="https://boards.greenhouse.io/accenturefederalservices/jobs/4679087006?gh_jid=4679087006"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer (Full Stack) | Quantcast | San Francisco, CA | 1 | ❌ No | 15% | <a href="https://jobs.lever.co/quantcast/4c579231-9b59-425b-a32f-68b31413e5f8"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Instructor | AI Fund | Mountain View, CA | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/AIFund/3460a600-c1bf-4f69-bfd8-6ca9720452c2"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Analytics Engineer II | Home Chef | Chicago, IL | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/homechef/jobs/5209446008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Autonomy Visualization | Nuro | Mountain View, California (HQ) | 1 | ❌ No | 11% | <a href="https://nuro.ai/careersitem?gh_jid=7896063"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Operator - Platform Delivery | Distyl | San Francisco | Not specified | ❌ No | 7% | <a href="https://jobs.ashbyhq.com/distyl/966ec457-55c4-44a2-a4c4-803fcbba6cc5"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Full Stack Engineer - Podcast | Spotify | New York, NY | Not specified | ❌ No | 7% | <a href="https://jobs.lever.co/spotify/69524356-88f8-4a8e-b543-0198670e4ceb"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| GTME Ecosystem - GTME & AI Teacher | Clay | New York | Not specified | ❌ No | 7% | <a href="https://jobs.ashbyhq.com/claylabs/1b1c004f-0e6a-41b6-bac3-971448b63a07"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer - 3D Mapping | Zoox | Foster City, CA | Not specified | ❌ No | 7% | <a href="https://jobs.lever.co/zoox/fae3a833-35de-4258-8618-d9878b69a9ab"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-05-04 · 8 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Machine Learning Engineer III | TeleTracking | Pittsburgh, PA | Not specified | ❌ No | 63% | <a href="https://job-boards.greenhouse.io/teletrackingtechnologiesinc/jobs/5207632008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Scientist - Biomedical Multimodal Modeling | Xaira Therapeutics | South San Francisco, California, United States | Not specified | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/xairatherapeutics/jobs/5036777007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Scientist II | The Trade Desk | Irvine | Not specified | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/thetradedesk/jobs/5127530007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Delivery / CD | OpenAI | San Francisco | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/openai/e14fc37c-7ae5-4a6b-ba0d-a36860cf9bb2"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Ground Systems Engineer II – Instrumentation and Controls | Rocket Lab USA | Wallops Island, VA | 2 | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/rocketlab/jobs/7719796003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Operator, Implementation Delivery | Distyl | San Francisco | Not specified | ❌ No | 7% | <a href="https://jobs.ashbyhq.com/distyl/ad8ea524-bfeb-4c6f-a642-eadd988fb191"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer - Desktop Frontend Developer (C#/Winforms) | Virtu Financial | New York | Not specified | ❌ No | 7% | <a href="https://job-boards.greenhouse.io/virtu/jobs/8516902002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI & Performance Marketing Intern | Dapper Labs | Rotterdam | Not specified | ❌ No | 4% | <a href="https://jobs.ashbyhq.com/dapper/57fbd995-59d2-4905-a84c-3511e20457fd"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-05-02 · 4 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Founding Software Engineer | Lance | San Francisco | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/lance/0f86cbc1-f89e-49e7-bf31-c112b223c87d"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Continuous Integration (Starship) | SpaceX | Hawthorne, CA | 2 | ❌ No | 15% | <a href="https://boards.greenhouse.io/spacex/jobs/8533853002?gh_jid=8533853002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Continuous Integration (Starship) | SpaceX | Starbase, TX | 2 | ❌ No | 11% | <a href="https://boards.greenhouse.io/spacex/jobs/8533859002?gh_jid=8533859002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer | Nox Metals | Los Angeles | Not specified | ❌ No | 7% | <a href="https://jobs.ashbyhq.com/nox-metals/82698f55-d4d2-4fbf-8951-181c28103dc5"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-05-01 · 14 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Platform Engineer, GenAI/ML | Strava | Strava SF | Not specified | ❌ No | 37% | <a href="https://jobs.ashbyhq.com/strava/70e03b74-28b9-4603-9d0f-2deff6876794"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Performance & Systems Engineer, Codex | OpenAI | San Francisco | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/openai/8a9d680c-5122-4ffe-ab4b-e1de7e806500"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Robotics Software Engineer - ML and Grasping | Pickle Robot | Charlestown, MA | Not specified | ❌ No | 19% | <a href="https://jobs.lever.co/picklerobot/4c70de3a-9059-4a0c-a92c-19677ef57b32"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| OS / K8s Systems Engineer | Baseten | San Francisco | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/baseten/dd166491-a4a2-4fb8-b42a-6a60e4049d15"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer | Texas Sports Academy Main | United States | Not specified | ❌ No | 11% | <a href="https://jobs.workable.com/view/ebTDwg5Q71DcEYTaDsM4zK/remote-software-engineer-in-united-states-at-texas-sports-academy-main"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Growth | Garage | New York City | 2 | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/garage/dba79415-f4eb-48fd-acf8-9c2086d58a54"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Frontend Design Systems Engineer | Seeq | United States | Not specified | ❌ No | 7% | <a href="https://jobs.workable.com/view/k7bnEJVCnkHYwNzfGQszvE/remote-frontend-design-systems-engineer-in-united-states-at-seeq"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Labeler / Annotator – AI Response Evaluation (French) | Blueprint Technologies | Remote | Not specified | ❌ No | 7% | <a href="https://job-boards.greenhouse.io/bpcs/jobs/7867327"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Labeler / Annotator – AI Response Evaluation (French) | Blueprint Technologies | Remote | Not specified | ❌ No | 7% | <a href="https://job-boards.greenhouse.io/bpcs/jobs/7867287"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Labeler / Annotator – AI Response Evaluation (German) | Blueprint Technologies | Remote | Not specified | ❌ No | 7% | <a href="https://job-boards.greenhouse.io/bpcs/jobs/7867333"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Labeler / Annotator – AI Response Evaluation (German) | Blueprint Technologies | Remote | Not specified | ❌ No | 7% | <a href="https://job-boards.greenhouse.io/bpcs/jobs/7867297"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Labeler / Annotator – AI Response Evaluation (German) | Blueprint Technologies | Remote | Not specified | ❌ No | 7% | <a href="https://job-boards.greenhouse.io/bpcs/jobs/7867171"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| SoC Platform Engineer | E-Space | Saratoga, CA | Not specified | ❌ No | 7% | <a href="https://jobs.lever.co/espace/c687b07c-2f4f-4ca2-8ea0-06ad313b9ae8"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Systems Engineer, Flight Safety | Varda Space | El Segundo, California, United States | Not specified | ❌ No | 4% | <a href="https://job-boards.greenhouse.io/vardaspace/jobs/7679461003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-04-30 · 10 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Forward Deployed Machine Learning Engineer | Federato | Remote | 2 | ❌ No | 30% | <a href="https://job-boards.greenhouse.io/federato/jobs/5206958008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Junior Research Scientist | EliseAI | San Francisco | 0-2 | ❌ No | 26% | <a href="https://jobs.ashbyhq.com/EliseAI/0fb4a3ab-1472-4180-8f0c-9f898260f3bd"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Full Stack Software Engineer | Northslope Technologies | New York | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/northslope-technologies/de39253f-7733-43ac-b92a-43aa52814786"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Ground Station Systems Software Engineer | Lynk | Chantilly, VA | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/Lynk/194cba01-5321-436d-b191-4867a4729645"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer II, Backend, tvScientific | Pinterest | San Francisco, CA, US; Remote, US | Not specified | ❌ No | 22% | <a href="https://www.pinterestcareers.com/jobs/?gh_jid=7782552"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer \| Seattle | Grid | Seattle, Washington | 1 | ❌ No | 19% | <a href="https://jobs.lever.co/Grid/82e6f8eb-0567-466e-93da-b4806d0b15c1"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Internal Systems Engineer (Applied AI) | impact.com | Columbus; New York City, Santa Barbara; Remote | Not specified | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/impact/jobs/8532453002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Development Test (Starlink) | SpaceX | Redmond, WA | 2 | ❌ No | 11% | <a href="https://boards.greenhouse.io/spacex/jobs/8532395002?gh_jid=8532395002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Network and Systems Engineer | Neuralink | South San Francisco, California, United States | Not specified | ❌ No | 7% | <a href="https://boards.greenhouse.io/neuralink/jobs/7720290003?gh_jid=7720290003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Integrations | Juicebox | San Francisco | Not specified | ❌ No | 7% | <a href="https://jobs.ashbyhq.com/juicebox/ac503cfb-e98b-4681-ae73-3dabce4d340c"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-04-29 · 24 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer - Data | xAI | Palo Alto, CA | 2 | ❌ No | 33% | <a href="https://job-boards.greenhouse.io/xai/jobs/5124616007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer (Applied AI) | Centralize | Remote, SF, NYC | Not specified | ❌ No | 30% | <a href="https://jobs.ashbyhq.com/centralize/03f64297-a8b8-4090-8bf7-7a2883dc5615"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Research Scientist, Robotics | The Allen Institute for AI | Seattle, WA | Not specified | ❌ No | 26% | <a href="https://job-boards.greenhouse.io/thealleninstitute/jobs/7848623"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer | PAR Tech | Champaign, IL | 2 | ❌ No | 26% | <a href="https://jobs.ashbyhq.com/PAR%20Technology/da5217c9-9b0e-493a-847e-96028574d107"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer - Core Services | Snorkel AI | Redwood City, CA (Hybrid); San Francisco, CA (Hybrid) | 2 | ❌ No | 26% | <a href="https://job-boards.greenhouse.io/snorkelai/jobs/5984577004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Productivity - Model Performance | OpenAI | San Francisco | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/openai/6d403ec9-d5d3-4754-9092-8fd5e659562a"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Frontend Engineer | Eudia | Palo Alto, CA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/eudia/jobs/4232678009"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Post-Training Research | OpenAI | San Francisco | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/openai/f381868f-7b0a-4b22-b215-71c7f5c1b498"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer (Product) | Centralize | Remote, SF, NYC | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/centralize/c231e810-3517-4b9f-a0b1-ebbb1bc7cb7e"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Analyst, Reporting Partnerships | Doximity | San Francisco, CA or Remote (U.S.) | 2 | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/doximity/jobs/7787892"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Distributed Systems Engineer | MLabs | United States | Not specified | ❌ No | 11% | <a href="https://apply.workable.com/j/F597E8028F"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Full Stack Web Developer | RevStar | Texas, United States | Not specified | ❌ No | 11% | <a href="https://jobs.workable.com/view/exXsv9DpYBUzkN2UhyAbg6/remote-full-stack-web-developer-in-texas-at-revstar"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Full Stack Web Developer | RevStar | Florida, United States | Not specified | ❌ No | 11% | <a href="https://jobs.workable.com/view/wSaosuEWMDJCxawtShRLAm/remote-full-stack-web-developer-in-florida-at-revstar"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Full Stack Web Developer | RevStar | Arizona, United States | Not specified | ❌ No | 11% | <a href="https://jobs.workable.com/view/bWuh9XYu6xrrgnZ79zgmGD/remote-full-stack-web-developer-in-arizona-at-revstar"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Product Management, Human Data Platform | Anthropic | San Francisco, CA \| New York City, NY | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/anthropic/jobs/5195866008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer (Infrastructure) | Centralize | Remote, SF, NYC | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/centralize/79ee0fab-fbd7-4268-8244-a4a228262d99"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer (Product / Design) | Centralize | Remote, SF, NYC | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/centralize/217e243b-878f-44c0-a50f-12b8359331f3"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer II, Data Warehouse | Amplitude | San Francisco, CA | 2 | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/amplitude/jobs/8530635002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Dev Tools | Polymarket | Remote | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/polymarket/6010bab5-8446-4834-a484-18e6a893230b"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Research Fellowship, (Summer and Fall 2026) | DoorDash | San Francisco, CA | Not specified | ❌ No | 7% | <a href="https://job-boards.greenhouse.io/doordashusa/jobs/7848317"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer (Starlink) | SpaceX | Redmond, WA | Not specified | ❌ No | 7% | <a href="https://boards.greenhouse.io/spacex/jobs/8525359002?gh_jid=8525359002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Marketing Strategist Intern – San Francisco | Uplane | San Francisco | Not specified | ❌ No | 4% | <a href="https://jobs.ashbyhq.com/uplane/81f8563e-1159-4600-9167-99279b570e05"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Tutor - Hungarian | xAI | Remote | Not specified | ❌ No | 4% | <a href="https://job-boards.greenhouse.io/xai/jobs/5123518007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Tutor - Russian | xAI | Remote | Not specified | ❌ No | 4% | <a href="https://job-boards.greenhouse.io/xai/jobs/5123528007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-04-28 · 60 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| DevOps Engineer | Eight Sleep | Shenzhen | Not specified | ❌ No | 26% | <a href="https://jobs.ashbyhq.com/eightsleep/227e8352-9128-4bf3-8928-bf9d7518dd9f"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Machine Learning Engineer, Robot Learning, Loco-Manipulation | Path Robotics | Columbus, Ohio | 2 | ❌ No | 22% | <a href="https://boards.greenhouse.io/pathrobotics/jobs/8501710002?gh_jid=8501710002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| ML Scientist I / II, Foundation Models for Life Sciences | Lila Sciences | San Francisco, CA USA | Not specified | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/lilasciences/jobs/4222051009"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Agents | Benchling | San Francisco, CA | 2 | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/benchling/815d941c-dff6-40cb-8307-57695acb37a7"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| (FALL) Data Scientist Intern - PhD | Integra FEC | Austin, Texas | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/integra/jobs/5134592008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Data Engineer | C the Signs | Rhode Island, United States | Not specified | ❌ No | 19% | <a href="https://jobs.workable.com/view/7kPcqzBwVfD6AuyLASShrL/remote-ai-data-engineer-in-rhode-island-at-c-the-signs"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Data Engineer | C the Signs | New Hampshire, United States | Not specified | ❌ No | 19% | <a href="https://jobs.workable.com/view/eYCkqWwMFbEtc5SRVFzF36/remote-ai-data-engineer-in-new-hampshire-at-c-the-signs"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Data Engineer | C the Signs | New Jersey, United States | Not specified | ❌ No | 19% | <a href="https://jobs.workable.com/view/mi3DChCAcdM6KswQp9wd5i/remote-ai-data-engineer-in-new-jersey-at-c-the-signs"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Data Engineer | C the Signs | New York, United States | Not specified | ❌ No | 19% | <a href="https://jobs.workable.com/view/ikpLP8ch6Fdyw3LVBVEnWF/remote-ai-data-engineer-in-new-york-at-c-the-signs"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Data Engineer | C the Signs | New York, New York, United States | Not specified | ❌ No | 19% | <a href="https://jobs.workable.com/view/r8DFFQ5nQaR4WM3iNPhbM6/remote-ai-data-engineer-in-new-york-at-c-the-signs"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Data Engineer | C the Signs | Boston, Massachusetts, United States | Not specified | ❌ No | 19% | <a href="https://jobs.workable.com/view/m854CgFteiU5uwJz4rdfvq/remote-ai-data-engineer-in-boston-at-c-the-signs"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Finance Applications | Block | Bay Area, CA, United States of America | Not specified | ❌ No | 19% | <a href="http://block.xyz/careers/jobs/4888459008?gh_jid=4888459008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Productivity - Networking | OpenAI | San Francisco | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/openai/17daedbd-b3fb-4e8c-a17c-8bbc9ec1d0b5"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| (FALL) Data Analyst Intern | Integra FEC | Austin, Texas | Not specified | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/integra/jobs/5134522008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | Philadelphia, PA | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/51bc310b-ac25-40d3-9832-e26259b4cf6f"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | Philadelphia, PA | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/5c4a626d-bf2f-4bf8-b1b5-ef1143adaa2d"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | Philadelphia, PA | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/5a00851e-46e1-4db4-8fea-d3ed78e4a1a6"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | Philadelphia, PA | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/4b5a0293-dae6-4337-95d1-6ee1d65c4420"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | Cheyenne, WY | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/e8176a34-e6ae-4f6e-a87b-1ae4c15fe237"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | Cheyenne, WY | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/a77f5ec6-24ed-4d1e-99b5-d4e8dfe14c6a"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | Cheyenne, WY | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/2ece8304-fd3a-4f63-a141-0f02364e8a50"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | Cheyenne, WY | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/076f06cf-a89a-4170-b57d-060a33c0d50a"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | Fargo, ND | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/a055fd65-1aa9-44f3-bb6d-09735a2f51b8"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | Fargo, ND | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/39f06a64-c14b-4cd5-b04b-da9dc90555a9"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | Fargo, ND | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/01de5fe4-2e79-47ee-9230-55fe4631f52d"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | Fargo, ND | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/65b6f67c-1d26-48e0-804b-a298208478ee"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | Boise, ID | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/a856e2a6-3da4-4598-ae13-ce238c2d8798"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | Boise, ID | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/89b4549a-a33a-4f35-8437-e982d4142c78"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | Boise, ID | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/50798152-60be-4d75-ac36-c44fd13b67d4"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | Boise, ID | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/85647f4a-a772-4831-8c3f-49171f0d64ab"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | Des Moines, IA | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/700aff37-e971-4ca9-bbbe-e8e47c1d679c"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | Des Moines, IA | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/b36fc46a-9d5c-49ec-9aa0-9a4cb901d5e2"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | Des Moines, IA | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/8a0dbc98-5181-410b-86c5-219c44b9fa4d"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | Des Moines, IA | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/e9b7d0c3-b758-4946-b3cf-c765744dafd9"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | Wichita, KS | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/c96710ce-6f83-47d0-8f79-78024b242640"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | Wichita, KS | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/2307e8f5-4382-41a5-8be5-cb8420e36009"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | Wichita, KS | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/9016b5b0-602a-4123-9bd6-7b1620561a50"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | Oklahoma City, OK | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/09870d41-3dec-4614-be8a-b98c9a3b675c"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | Oklahoma City, OK | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/401c169a-5b21-4dda-a65b-ac78c2f4e605"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | Oklahoma City, OK | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/712b9a1a-6520-4d67-b458-a1fdfd69dd5b"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | Oklahoma City, OK | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/bf29e9b9-a02e-49cd-b6ca-e4ba4ca2cba5"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | Salt Lake City, UT | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/2fd20dab-fa52-4502-8287-7b33859486b8"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | Salt Lake City, UT | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/1457c2ea-1939-4de9-8e79-0bcbed43d69f"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | Salt Lake City, UT | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/20d2f6f6-f99f-4a83-88e4-274f436753c0"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | Salt Lake City, UT | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/e97d3d71-57eb-486b-bafa-7a538c5433de"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | Milwaukee, WI | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/a799a0e4-47e7-46b0-a5db-d3faf6892417"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | Milwaukee, WI | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/499bb7b0-f54b-4ac0-ba26-c1baf05f6382"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | Milwaukee, WI | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/dbd5baeb-f2df-4bfd-8d8b-04537470921d"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | Milwaukee, WI | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/93786b61-e086-40cb-ab6c-a2acce7f298b"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | Louisville, KY | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/8f46c222-0458-4b6b-a92d-afe00a00aa3a"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | Louisville, KY | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/59c697cd-2635-4d2f-a9d2-b31c3fabd61e"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | Louisville, KY | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/cccc16be-312f-4410-88f7-8e3d13044671"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | Louisville, KY | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/334eb9e3-601b-4bc1-b48d-77df8e34fbba"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | Jackson, MS | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/c186e891-93bf-4d49-af99-07e75276424c"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer | Latent | San Francisco | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/latent/37081ba7-cd44-4a40-bc5f-4a2829c0d079"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Edge | Persona | Remote | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/persona/c41805eb-ca15-4020-9058-ea44539389b8"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Analyst - 3056-03 | Delaware Nation Industries | Joint Base Andrews, Maryland, United States | Not specified | ❌ No | 7% | <a href="https://jobs.workable.com/view/1DdFnBAYWUTbeRRpPM9PrJ/data-analyst---3056-03-in-joint-base-andrews-at-delaware-nation-industries"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Core Platform | Cribl | Remote - United States | Not specified | ❌ No | 7% | <a href="https://cribl.io/job-detail/?gh_jid=5844014004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Partnerships | Box | Redwood City, CA, United States, San Francisco, CA, United States | Not specified | ❌ No | 4% | <a href="https://job-boards.greenhouse.io/boxinc/jobs/7862815"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Frontend Platform Engineer | Harvey | New York | Not specified | ❌ No | 4% | <a href="https://jobs.ashbyhq.com/harvey/24f9a3fa-476a-490f-87bf-e8cebb7b3928"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-04-27 · 37 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer, New Grad (AI) | Notion | San Francisco, California | 0-2 | ❌ No | 30% | <a href="https://jobs.ashbyhq.com/notion/7e6dc7fe-7ddd-42c1-8928-13f7bddb9ec9"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Associate Software Engineer | Major League Baseball | San Francisco, California | Not specified | ❌ No | 26% | <a href="https://www.mlb.com/careers/opportunities?gh_jid=7842178"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Research Engineer - The Diffusion LLM Team | Institute of Foundation Models | Sunnyvale, CA | Not specified | ❌ No | 19% | <a href="https://jobs.lever.co/ifm-us/00c6696f-ae36-46b4-9efa-8c1fba3bfa77"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Compute Infrastructure | OpenAI | San Francisco | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/openai/ca300a6d-a2a7-4580-aad7-323fbdfee7b1"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Tokens-as-a-Service (Taas) Software Engineer | OpenAI | San Francisco | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/openai/f3ddd41c-541f-485e-90d6-86c26e018e9f"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Early Career | Mirage | Union Square, New York City | 0-2 | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/mirage/cbf278fd-84ec-48d9-8052-b76abb035ac7"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Production Engineering | Ramp | New York, NY (HQ) | 2 | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/ramp/be496b52-cfbf-494e-b862-61fb4a188b24"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | Jackson, MS | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/c13cdaad-aca2-4371-8e4e-7cb31de3a704"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | Jackson, MS | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/e016f1c8-963a-4125-b4ec-46de2feaeef4"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | Jackson, MS | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/96e79e8c-0ff9-472d-ab98-acf805aebd7f"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | Columbia, SC | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/839fe24e-01d2-4a40-b941-a0c77371d54a"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | Columbia, SC | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/d238afc4-2921-4232-9aa7-80ed6dff08eb"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | Columbia, SC | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/b4b0b415-7b2f-4e8d-a84f-fae1a77179fe"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | Columbia, SC | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/f85b0f7f-a94a-4a07-a52f-c0f87f9f074c"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | New Orleans, LA | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/e4935321-a771-42d5-bf4e-00e948f90c99"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | New Orleans, LA | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/cd20c304-7f85-4f95-954b-fae59b2a6329"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | New Orleans, LA | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/dd8454d7-4cc0-45ba-9a51-c406e861ee49"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | New Orleans, LA | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/c20b5577-6319-4650-a288-c2875d6e92db"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | Birmingham, AL | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/9619eee7-2ed0-4cfb-a44c-a86442df59bf"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | Birmingham, AL | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/2a7a951b-6ae3-4c95-88bf-e4814c2875da"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | Birmingham, AL | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/316671bc-7176-4c0b-8ab5-73fc842eabbe"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | Birmingham, AL | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/c9d05fa2-69a2-4742-bf53-dc31c351ce18"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | Los Angeles, CA | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/e8be46cc-28ed-458c-889c-dba89798f2b0"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | Los Angeles, CA | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/3711bbf5-483b-4d99-b881-5413ffd7f0b7"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | Los Angeles, CA | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/f3dea37e-6cbf-4acc-bac8-37646c469681"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | Los Angeles, CA | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/aec0a9a8-4326-4c6d-9ebb-6e101daec002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | Chicago, IL | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/5bfba953-b65d-417c-8641-da24a9846aad"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | Chicago, IL | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/7b997458-177f-45cc-819f-90b594179b45"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | Chicago, IL | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/fccbb1fc-3f0b-4c05-bc20-b506c2ef88b4"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | Chicago, IL | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/b80e56d1-2580-435a-9d07-d4a0ef1bb36f"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | Chicago, IL | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/c49b8f14-2f2e-4c56-9261-eca4619b6997"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | New York, NY | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/c245df6e-29f8-4aa5-8998-93bbeab402f3"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | New York, NY | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/5350901e-f041-4e2f-9704-190e98d6ab1c"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | New York State | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/70e2bc0e-551a-4ec4-a3dd-9601f3b19239"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | New York, NY | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/de70c40e-55dc-43a8-a86f-f32f0495a524"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Engineering Platform | Ramp | New York, NY (HQ) | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/ramp/198150d6-789a-4ef8-999f-93a49656d4f1"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Machine Learning Engineer | Harvard University | Boston, MA, United States | Not specified | ❌ No | 7% | <a href="https://jobs.smartrecruiters.com/HarvardUniversity/3743990012837047"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-04-26 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer II (Backend, Hardware Accelerate) | Whoop | Boston, MA | Not specified | ❌ No | 19% | <a href="https://jobs.lever.co/whoop/3bc68bdd-3a23-42cc-b334-26338431ab0a"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-04-25 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer I, Ad Supply Experiences | Twitch | San Francisco, CA | 2 | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/twitch/jobs/8519628002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Inference - Performance Optimization | OpenAI | San Francisco | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/openai/85fceac9-fb8a-4d71-a524-a8e5f1e9b01b"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-04-24 · 15 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Data Engineer | xAI | Palo Alto, CA | 1 | ❌ No | 30% | <a href="https://job-boards.greenhouse.io/xai/jobs/5120884007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Intern - Applications, AI and Machine Learning (Fall 2026) (ET26021) | TMEIC | Roanoke, Virginia, United States | Not specified | ❌ No | 19% | <a href="https://apply.workable.com/j/FD4C9770FF"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer | Mach Industries | Huntington Beach, CA | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/mach/777f664d-77e9-408e-ae65-f6a2183d3bb4"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Flight Software Engineer | Mach Industries | Huntington Beach, CA | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/mach/70315deb-00a9-433b-8b9b-9958ffb8ee29"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Intern - Applications, AI and Machine Learning (Fall 2026) (ET26021) | TMEIC Corporation Americas | Roanoke, Virginia, United States | Not specified | ❌ No | 15% | <a href="https://jobs.workable.com/view/g1R8VBCDnj96gfLREyP7aF/intern---applications%2C-ai-and-machine-learning-(fall-2026)-(et26021)-in-roanoke-at-tmeic-corporation-americas"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Machine Learning & Operations Engineer | OptiTrack | Arlington, Virginia, United States | Not specified | ❌ No | 15% | <a href="https://jobs.workable.com/view/iXrrWdnNpL3Gvg4CbgwkTW/remote-machine-learning-%26-operations-engineer-in-arlington-at-optitrack"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Machine Learning & Operations Engineer | OptiTrack | Durham, North Carolina, United States | Not specified | ❌ No | 15% | <a href="https://jobs.workable.com/view/gGNqrN4yvBTGBpEeFeWEgn/remote-machine-learning-%26-operations-engineer-in-durham-at-optitrack"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Machine Learning & Operations Engineer | OptiTrack | Atlanta, Georgia, United States | Not specified | ❌ No | 15% | <a href="https://jobs.workable.com/view/mhY4y3LMFSGiTwWmbtQpXt/remote-machine-learning-%26-operations-engineer-in-atlanta-at-optitrack"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Machine Learning & Operations Engineer | OptiTrack | Miami, Florida, United States | Not specified | ❌ No | 15% | <a href="https://jobs.workable.com/view/2xQZ2BxEBM3GZqvWZSHWYX/remote-machine-learning-%26-operations-engineer-in-miami-at-optitrack"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Machine Learning & Operations Engineer | OptiTrack | Corvallis, Oregon, United States | Not specified | ❌ No | 15% | <a href="https://jobs.workable.com/view/skBHDWaX7bc81c1QycULdL/remote-machine-learning-%26-operations-engineer-in-corvallis-at-optitrack"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer II | The Trade Desk | Madrid | 2 | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/thetradedesk/jobs/5120396007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer – General (new grad / early career) | Northwood Space | Torrance, CA | 2 | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/NorthwoodSpace/b960b661-e1cc-40d0-bde3-290cd1b58ede"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Site Reliability Engineer, Cloud Cost Utilization | GitLab | Remote, US | Not specified | ❌ No | 7% | <a href="https://job-boards.greenhouse.io/gitlab/jobs/8515080002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Automation Engineer | Novig | New York, New York | Not specified | ❌ No | 4% | <a href="https://jobs.ashbyhq.com/novig/1bc54185-7095-4499-b291-7076192a865e"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Education Intern | Leland | Leland HQ - Lehi, UT | Not specified | ❌ No | 4% | <a href="https://jobs.ashbyhq.com/leland/94347c0b-273b-4c17-9987-563912629633"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-04-23 · 20 roles · 3 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer (Civil Aviation) | Airspace Intelligence | Boston, US | Not specified | ✅ Yes | 19% | <a href="https://jobs.ashbyhq.com/airspace-intelligence.com/1336c828-21b1-48a0-bbce-8c6e2d061124"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer - Trust Center | Snowflake | US-WA-Bellevue | Not specified | ✅ Yes | 19% | <a href="https://jobs.ashbyhq.com/snowflake/9268cbbb-f6a5-44bc-9c84-cb354cd8090f"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Cloud Platform Engineer (Civil Aviation) | Airspace Intelligence | Boston, US | Not specified | ✅ Yes | 11% | <a href="https://jobs.ashbyhq.com/airspace-intelligence.com/07797dd1-ea25-4fa5-8d8b-bc8528e0b2b1"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Scientist II - Big Data R&D, Identity Graph & KYC | Socure | Hybrid - US | 2 | ❌ No | 37% | <a href="https://jobs.ashbyhq.com/socure/df93769c-ab37-4741-88bb-0f9d1ff4954b"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Scientist Operations | Kikoff | San Francisco | 2 | ❌ No | 30% | <a href="https://job-boards.greenhouse.io/kikoff/jobs/4231306009"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Scientist, Core Data - PhD (2026) | Figma | San Francisco, CA • New York, NY | Not specified | ❌ No | 30% | <a href="https://boards.greenhouse.io/figma/jobs/5976930004?gh_jid=5976930004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer - Voice AI (Inference Runtime) | Baseten | San Francisco | Not specified | ❌ No | 30% | <a href="https://jobs.ashbyhq.com/baseten/6e396eb7-acb3-436a-89ec-05e755c477f2"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Scientist | FanDuel | Jersey City | 1 | ❌ No | 26% | <a href="https://www.fanduel.careers/open-positions?gh_jid=7848571"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Research Engineer, Machine Learning (RL Velocity) | Anthropic | Remote-Friendly (Travel-Required) \| San Francisco, CA \| New York City, NY | Not specified | ❌ No | 26% | <a href="https://job-boards.greenhouse.io/anthropic/jobs/5198108008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Research Engineer, Machine Learning Systems | Deepgram | USA \| Remote | 0 | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/deepgram/9a030b32-d671-43e0-a221-4653bb73ba29"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, New Grad | Notion | San Francisco, California | 0-2 | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/notion/a6311f97-4850-4674-a5f3-d9fe5f6f2555"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data & AI Engineer | RevStar | Arizona, United States | Not specified | ❌ No | 19% | <a href="https://jobs.workable.com/view/h9V7LrDHLa8NqDzEpYUDEq/remote-data-%26-ai-engineer-in-arizona-at-revstar"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data & AI Engineer | RevStar | Texas, United States | Not specified | ❌ No | 19% | <a href="https://jobs.workable.com/view/r3DXgDqh3s96RFEDTeAU1K/remote-data-%26-ai-engineer-in-texas-at-revstar"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data & AI Engineer | RevStar | Florida, United States | Not specified | ❌ No | 19% | <a href="https://jobs.workable.com/view/vS8MwphAPJuHUKriGfoaHY/remote-data-%26-ai-engineer-in-florida-at-revstar"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Backend Engineer - API | xAI | Palo Alto, CA | Not specified | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/xai/jobs/5119111007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Analytics Engineer | One Park Financial | Miami, Florida, United States | Not specified | ❌ No | 11% | <a href="https://jobs.workable.com/view/5ZwMX1MQkQcNnFSpks6A85/analytics-engineer-in-miami-at-one-park-financial"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Software Engineer | UpSmith | United States | Not specified | ❌ No | 7% | <a href="https://jobs.workable.com/view/snskeFrHDohZuwCejy9V5u/remote-ai-software-engineer-in-united-states-at-upsmith"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Builder | F. Schumacher & Co. | Soho, New York | Not specified | ❌ No | 4% | <a href="https://job-boards.greenhouse.io/fschumacherco/jobs/5198571008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Factory, Value Engineer | Armada | United States (Remote) | Not specified | ❌ No | 4% | <a href="https://job-boards.greenhouse.io/armada/jobs/5182555008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Vehicle Platform Systems Engineer | Aurora Innovation | Dallas, Texas | Not specified | ❌ No | 4% | <a href="https://aurora.tech/jobs/8508606002?gh_jid=8508606002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-04-22 · 7 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Machine Learning Research Engineer | Roboflow | Remote | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/roboflow/40c3389e-c7ea-4054-8c90-05b1beb38bff"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Resident | RoboForce | Milpitas, CA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/roboforce/jobs/5196164008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Scientific Software Engineer — Emulation & Application | QuEra Computing | Boston, MA, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/queracomputinginc/jobs/5196318008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer | Mach Industries | San Francisco, CA | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/mach/f55cee73-55aa-47f3-9baf-8292817c70dc"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Warfighter Systems - SkillBridge | Anduril | Bellevue, Washington, United States | Not specified | ❌ No | 19% | <a href="https://boards.greenhouse.io/andurilindustries/jobs/5117558007?gh_jid=5117558007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Analyst | Gallup | Omaha Riverfront | Not specified | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/gallup/jobs/4217886009"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Developer Experience | Replit | Foster City, CA | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/replit/d0e0dd7d-59d1-4de8-afbb-54aea680b51d"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-04-21 · 12 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer (Flight Reliability) | SpaceX | Hawthorne, CA | 2 | ❌ No | 33% | <a href="https://boards.greenhouse.io/spacex/jobs/8512876002?gh_jid=8512876002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Scientist, New Grad | SentiLink | United States | 0-2 | ❌ No | 30% | <a href="https://jobs.ashbyhq.com/sentilink/3cb2885e-7a58-4a14-94d5-b7b851053408"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Autonomy Engineer Intern - Deep Learning (Computational Photography) | Skydio | San Mateo, California, United States | Not specified | ❌ No | 26% | <a href="https://jobs.ashbyhq.com/skydio/d13e3179-e646-4873-84a6-d492a692bc25"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| ML Postdoc Researcher - Healthcare AI Innovation | Truveta | Seattle, WA | Not specified | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/truveta/jobs/5978375004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Solutions Engineer | Baseten | San Francisco | 1 | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/baseten/508b792d-57a0-467e-9a89-76fe72e84433"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Applied AI Inference Engineer | Baseten | San Francisco | 1 | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/baseten/90e9ff4e-1225-4b1b-b0b4-2362e36d9cfa"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Backend Software Engineer (Robotics Systems) | Intrinsic | Mountain View, California | Not specified | ❌ No | 15% | <a href="https://boards.greenhouse.io/intrinsicrobotics/jobs/5973679004?gh_jid=5973679004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, ChatGPT Infrastructure | OpenAI | San Francisco | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/openai/e6981259-c1d0-46de-8376-56bde28cfb10"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Embedded Software Engineer, OS/Platform (Starlink) | SpaceX | Bastrop, TX | 2 | ❌ No | 11% | <a href="https://boards.greenhouse.io/spacex/jobs/8511391002?gh_jid=8511391002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Hardware Systems Engineer | Lumafield | San Francisco, CA | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/lumafield/0f3a5bc8-f285-4291-9e5b-3a1bd2d2f62e"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| PCIe Software Engineer | Arista Networks | Austin, TX, United States | Not specified | ❌ No | 4% | <a href="https://jobs.smartrecruiters.com/AristaNetworks/744000122124136"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| PCIe Software Engineer | Arista Networks | Santa Clara, CA, United States | Not specified | ❌ No | 4% | <a href="https://jobs.smartrecruiters.com/AristaNetworks/744000122122337"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-04-20 · 10 roles · 1 H-1B sponsor match

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Frontend Engineer (Defense) | Airspace Intelligence | Boston, US | Not specified | ✅ Yes | 11% | <a href="https://jobs.ashbyhq.com/airspace-intelligence.com/ed6d7999-1e12-4819-9ee9-c86fef2a65d8"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| PhD Fall Machine Learning Intern (ATG — Visual, Multimodal, and Recommender Systems) | Pinterest | San Francisco, CA, US; Palo Alto, CA, US; Seattle, WA, US; New York, NY, US | Not specified | ❌ No | 48% | <a href="https://www.pinterestcareers.com/jobs/?gh_jid=7255640"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Training Infrastructure Engineer – Humanoid Whole Body Control | Figure | San Jose, CA | Not specified | ❌ No | 26% | <a href="https://job-boards.greenhouse.io/figureai/jobs/4674754006"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Full-Stack | Loop | New York, NY, USA | Not specified | ❌ No | 26% | <a href="https://job-boards.greenhouse.io/loop/jobs/5977189004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer - Site Reliability Engineering | Neo4j | Malmö | Not specified | ❌ No | 22% | <a href="https://boards.greenhouse.io/neo4j/jobs/4674495006?gh_jid=4674495006"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Engineer | Vooma | San Francisco Office | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/vooma/5396e567-964c-46f7-b798-f41688e6c220"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Infrastructure | Tavus | Remote | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/tavus/2cdc9932-1140-42d6-9fce-ee7e26192b15"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Research Scientist / Engineer, Two-Photon Imaging & Holographic Optogenetics | Astera | Emeryville HQ | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/astera/64521b48-51dd-4e59-82e8-c10f4e90bed6"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| French-Speaking AI Evaluation Specialist | Blueprint Technologies | Remote | Not specified | ❌ No | 7% | <a href="https://job-boards.greenhouse.io/bpcs/jobs/7832253"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Human-Centered AI Intern: Human-Computer Interaction | Toyota Research Institute | Los Altos, CA | Not specified | ❌ No | 7% | <a href="https://jobs.lever.co/tri/000be2f3-b77c-4719-8476-0718c4c49a19"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-04-17 · 16 roles · 1 H-1B sponsor match

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Cloud Platform Engineer (Defense) | Airspace Intelligence | Boston, US | Not specified | ✅ Yes | 22% | <a href="https://jobs.ashbyhq.com/airspace-intelligence.com/3ef9d056-4216-4b80-9c13-80a8b8badab0"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Scientist I | GumGum | Santa Monica, California, United States | 2 | ❌ No | 52% | <a href="https://job-boards.greenhouse.io/gumgum/jobs/7703520003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Fullstack Engineer Intern | Meshy | Bay Area Office | Not specified | ❌ No | 26% | <a href="https://jobs.ashbyhq.com/meshy/262d74c7-8aab-474e-9fc6-8c8c48ec6572"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, UI/UX | Lightship RV | Broomfield, CO | 2 | ❌ No | 26% | <a href="https://jobs.lever.co/lightship/d04d7685-024f-4927-a584-c917e991d0ce"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, UI/UX | Lightship RV | South San Francisco, CA | 2 | ❌ No | 26% | <a href="https://jobs.lever.co/lightship/b9612499-1296-4cc8-9b98-1abc602816c8"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Quantitative Research and Strategy, Healthcare AI Associate | RA Capital Management | Boston, MA | 2 | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/racapitalmanagementllc/jobs/5192268008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Back-end Engineer | TripAdvisor | Reykjavik, Iceland | Not specified | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/tripadvisor/jobs/7825805"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| PT Student Worker-AI Driven Trouble Shooting | Zoox | Foster City, CA | Not specified | ❌ No | 15% | <a href="https://jobs.lever.co/zoox/0bb2dd41-e6a9-41a5-bafc-8a438f0a7cca"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Site Reliability Engineer | Peloton | New York, New York | Not specified | ❌ No | 15% | <a href="https://careers.onepeloton.com/en/all-jobs/?gh_jid=7785741"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Kernel Performance & AI Tooling | OpenAI | San Francisco | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/openai/e9627fa6-ac76-4899-9a93-9251419e61a0"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Middleware | Nuro | Mountain View, California (HQ) | 2 | ❌ No | 15% | <a href="https://nuro.ai/careersitem?gh_jid=7825886"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Onboard Systems | Nuro | Mountain View, California (HQ) | 2 | ❌ No | 15% | <a href="https://nuro.ai/careersitem?gh_jid=7809136"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Development Engineer in Test (Peripheral Driver, Embedded SDET) | Sony Interactive Entertainment | United States, San Mateo, CA | Not specified | ❌ No | 7% | <a href="https://job-boards.greenhouse.io/sonyinteractiveentertainmentglobal/jobs/5969889004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Talent Systems and Recruiting Generalist | Giga AI | San Francisco | Not specified | ❌ No | 4% | <a href="https://jobs.ashbyhq.com/gigaml/7f70df01-8b1f-4368-a51a-801ed21833f3"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Engineer | SZNS Solutions LLC | Reston, Virginia, United States | Not specified | ❌ No | 4% | <a href="https://jobs.workable.com/view/qicTgBYubkk7KqMEF6zKKJ/hybrid-data-engineer-in-reston-at-szns-solutions-llc"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| SF Platform & Media Cloud Engineer | MARGO | Warsaw | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/margo-group/019a1823-5b2f-4365-87e4-a41e53578a77"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-04-16 · 11 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| AI / Embedded ML Engineer | E-Space | Saratoga, CA | 2 | ❌ No | 37% | <a href="https://jobs.lever.co/espace/bd11a952-26a0-40e9-8d2f-17b98f22f233"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Associate Data Scientist - Originations | PrizePicks | Atlanta, GA preferred, Remote | Not specified | ❌ No | 22% | <a href="http://prizepicks.com/position?gh_jid=7702028003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer Intern (AI-Native) — Summer 2026 | Kognitos | San Jose - HQ | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/Kognitos/a3c5bd4c-f6fb-4eb0-b943-e0e1a1d878c5"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Research Data Platform | Anthropic | San Francisco, CA \| New York City, NY | Not specified | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/anthropic/jobs/5191226008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Ground Systems Engineer II, Automation Controls | Rocket Lab USA | Stennis Space Center, MS | 2 | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/rocketlab/jobs/7703264003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Junior Software Engineer | Rokt | New York, New York, United States | 0-2 | ❌ No | 15% | <a href="https://apply.workable.com/j/783A754DDB"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Hybrid Mobile Developer | RP Pro Services | Springfield, Virginia, United States | Not specified | ❌ No | 11% | <a href="https://jobs.workable.com/view/pwfF2DijbDNpuCcVgQGFrx/remote-hybrid-mobile-developer-in-springfield-at-rp-pro-services"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Cellular | Flock Safety | Atlanta, GA | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/Flock%20Safety/7c4eaafe-802d-489b-895f-1ed87c0a5c48"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Wireless Software Engineer (Starlink) | SpaceX | Sunnyvale, CA | 2 | ❌ No | 11% | <a href="https://boards.greenhouse.io/spacex/jobs/8511186002?gh_jid=8511186002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Backend Software Engineer (Robotics Data) | Rovex Technologies Corporation | Gainesville, Florida, United States | Not specified | ❌ No | 7% | <a href="https://jobs.workable.com/view/6awuEHc3NkFzcvTzn7aw6V/backend-software-engineer-(robotics-data)-in-gainesville-at-rovex-technologies-corporation"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Communication Systems Engineer III - (Data Transmission Systems) | Aetos Systems | Merritt Island, Florida, United States | Not specified | ❌ No | 4% | <a href="https://jobs.workable.com/view/67e4BkjhwDnQu6cXMBUKXa/communication-systems-engineer-iii---(data-transmission-systems)-in-merritt-island-at-aetos-systems"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-04-15 · 9 roles · 1 H-1B sponsor match

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Full Stack Engineer (Defense) | Airspace Intelligence | Boston, US | Not specified | ✅ Yes | 22% | <a href="https://jobs.ashbyhq.com/airspace-intelligence.com/c97b6f01-a032-49dc-9ad1-c897912baab8"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Applied AI, Forward Deployed Machine Learning Engineer - Palo Alto | Mistral AI | Palo Alto | 2 | ❌ No | 48% | <a href="https://jobs.lever.co/mistral/0b476d3a-5f0c-4dda-9a5e-bd5ed8515328"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Scientist, Finance Forecasting | ClickHouse | San Francisco, USA (Hybrid) | Not specified | ❌ No | 30% | <a href="https://job-boards.greenhouse.io/clickhouse/jobs/5970141004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Applied AI Engineer | General Matter | Los Angeles, CA | Not specified | ❌ No | 26% | <a href="https://job-boards.greenhouse.io/generalmatter/jobs/5190258008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Backend Engineer II | HackerRank Careers | Hybrid in Santa Clara, CA | 2 | ❌ No | 26% | <a href="https://job-boards.greenhouse.io/hackerrank/jobs/7729186"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Security Observability | OpenAI | San Francisco | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/openai/1e4e9985-babf-4bd9-8fe8-a2016250780d"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Engineer II | Garner Health | New York City, New York | 2 | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/garnerhealth/jobs/5844340004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Safety | Twitch | San Francisco, CA | 1 | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/twitch/jobs/8504990002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Electrical Systems Engineer | SunSource | Hartland, WI 53029 | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/sunsrce/74413faf-f498-4eef-ac81-5b73c4b837f9"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-04-14 · 16 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Full-Stack Software Engineer, Reinforcement Learning | Anthropic | San Francisco, CA \| New York City, NY | Not specified | ❌ No | 33% | <a href="https://job-boards.greenhouse.io/anthropic/jobs/5186067008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Engineer | EQL Tech | San Francisco, California, United States | Not specified | ❌ No | 19% | <a href="https://jobs.workable.com/view/9epyFt3QJccXCuk7ZcZZ5x/ai-engineer-in-san-francisco-at-eql-tech"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Engineer | EQL Tech | Phoenix, Arizona, United States | Not specified | ❌ No | 19% | <a href="https://jobs.workable.com/view/eF5nz3sbGXSGg4YsBGNDM6/ai-engineer-in-phoenix-at-eql-tech"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Scientist | Forward Networks | Santa Clara, CA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/forwardnetworks/jobs/7695301003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Research Scientist - Audio | Retell AI | San Francisco Bay Area | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/retell-ai/7dbe5404-e08c-4c62-99dc-ef050534d029"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Research Scientist - LLM | Retell AI | San Francisco Bay Area | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/retell-ai/b0d780eb-df25-49d0-859a-915de204a2f2"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Security Software Engineer II, Detection and Response | Pinterest | San Francisco, CA, US; Remote, US | Not specified | ❌ No | 19% | <a href="https://www.pinterestcareers.com/jobs/?gh_jid=7770914"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Backend | Base Power | Austin, TX | 2 | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/base-power/23bc4e94-d63c-4933-926b-edcb69138410"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Foundations Search | OpenAI | San Francisco | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/openai/40ed6975-ef61-4807-b748-37c2fa2b76c7"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Engineer | Aviator | New York City | 2 | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/aviator/a5682392-8403-434b-aca4-47108a6f6709"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Research Scientist - Frontier Data | AfterQuery | San Francisco | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/afterquery/4e0d6e12-23b5-4a46-9ea5-63cbc2659ac8"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Research Scientist - Post Training | AfterQuery | San Francisco | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/afterquery/41a7fe68-6892-4d98-bb0e-857d63bd721d"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer | Polymath | San Francisco | Not specified | ❌ No | 7% | <a href="https://jobs.ashbyhq.com/polymath/44812b4a-b41c-4288-8232-e0131da6eefe"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer I (Quality) | Whoop | Boston, MA | Not specified | ❌ No | 7% | <a href="https://jobs.lever.co/whoop/b7f75849-b5c0-49fe-8d24-50cbb39d284d"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Research Resident | Polymath | San Francisco | Not specified | ❌ No | 4% | <a href="https://jobs.ashbyhq.com/polymath/feac8f33-2e28-4434-bff5-cf26c849f270"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Diagnostics Software Engineer | Arista Networks | Santa Clara, CA, United States | Not specified | ❌ No | 4% | <a href="https://jobs.smartrecruiters.com/AristaNetworks/744000120765457"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-04-13 · 17 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer - Fluency | The Job Sauce | San Francisco | Not specified | ❌ No | 33% | <a href="https://jobs.ashbyhq.com/The%20Job%20Sauce/c9113750-4dfc-4cdd-9f98-416a9df6cba3"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Machine Learning Engineer | Latent | San Francisco | Not specified | ❌ No | 30% | <a href="https://jobs.ashbyhq.com/latent/233bbaac-d589-49f4-a8eb-6bb16673b060"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Research Scientist | Latent | San Francisco | Not specified | ❌ No | 30% | <a href="https://jobs.ashbyhq.com/latent/648fa6e1-52b8-4c43-8cf9-ab80260ecb1d"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer | Major League Baseball | Los Angeles, California | 2 | ❌ No | 30% | <a href="https://www.mlb.com/careers/opportunities?gh_jid=7811682"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Scientist | BlueLabs Analytics | Washington D.C. or Remote | 2 | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/bluelabsanalyticsinc/jobs/5106844007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Forward Deployed Research Scientist | Labelbox | San Francisco Bay Area | Not specified | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/labelbox/jobs/5101375007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer | Maybern | New York Office | 2 | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/maybern/b9df4d9a-7247-4a3c-b94a-dd1e23ee1c22"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer (New Grads 2025-2026) | EliseAI | New York City | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/EliseAI/1ffbd278-a5fe-443c-984f-521d61a97353"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Agent Evaluation and Quality | Cursor | San Francisco | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/cursor/2bbe9f02-83a5-4173-98be-9085d1cb5693"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Flight Dynamics | Muon Space | San Jose, CA | 2 | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/muonspace/jobs/5090219007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Backend Engineer, Integrations | Pylon | Palo Alto | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/pylon/23ee52df-cd68-42c9-bf27-5b844ae8e2c6"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Backend Engineer, Underwriting | Pylon | Palo Alto | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/pylon/2ed1cad6-d4c7-48a4-bf8a-f66ce884a0ea"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Fullstack Engineer, Customer Success | Pylon | Palo Alto | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/pylon/fd573bb0-d06c-401f-97b5-b73d030662d4"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Infrastructure Engineer, Foundation | Pylon | Palo Alto | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/pylon/5e3de934-d746-4753-8436-ea70143baeae"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Backend Engineer, API | Pylon | Palo Alto | Not specified | ❌ No | 7% | <a href="https://jobs.ashbyhq.com/pylon/d1ef993a-9d43-432c-8700-f185de00a1e4"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Analyst Consultant (m/w/d) - Quereinsteiger willkommen! DSDE 14 - 01. März 2027 | The Information Lab | Hamburg | Not specified | ❌ No | 7% | <a href="https://jobs.lever.co/theinformationlab/851d2d0b-b554-4d7c-8dc0-aa390366b6ea"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Business Development Representative, Emerging AI Products | Intercom | Chicago, Illinois | 1 | ❌ No | 4% | <a href="https://job-boards.greenhouse.io/intercom/jobs/7807509"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-04-11 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer, Infrastructure - Analytics Platform | OpenAI | San Francisco | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/openai/e44bfa94-0b82-4d0c-b224-02155b76eea9"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-04-10 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Intern, AI Engineering | Workato | San Francisco, California | Not specified | ❌ No | 30% | <a href="https://www.workato.com/careers?gh_jid=8492935002#open-roles"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Site Infrastructure Engineer – Networking & Compute | Avride | Austin, TX | Not specified | ❌ No | 7% | <a href="https://job-boards.greenhouse.io/avride/jobs/4215813009"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-04-09 · 10 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Helix AI Engineer, Generative AI | Figure | San Jose, CA | Not specified | ❌ No | 41% | <a href="https://job-boards.greenhouse.io/figureai/jobs/4671699006"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Helix AI Engineer, Modeling | Figure | San Jose, CA | Not specified | ❌ No | 41% | <a href="https://job-boards.greenhouse.io/figureai/jobs/4671712006"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Helix AI Engineer, Pretraining | Figure | San Jose, CA | Not specified | ❌ No | 41% | <a href="https://job-boards.greenhouse.io/figureai/jobs/4671704006"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Helix AI Engineer, Video Pretraining | Figure | San Jose, CA | Not specified | ❌ No | 37% | <a href="https://job-boards.greenhouse.io/figureai/jobs/4671703006"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Helix AI Engineer, Reinforcement Learning | Figure | San Jose, CA | Not specified | ❌ No | 30% | <a href="https://job-boards.greenhouse.io/figureai/jobs/4671707006"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Infrastructure Engineer Intern | Sezzle | Colombia, Remote | Not specified | ❌ No | 26% | <a href="https://job-boards.greenhouse.io/sezzle/jobs/7694238003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Science Leader | Tiger Analytics Inc. | California City, California, United States | Not specified | ❌ No | 22% | <a href="https://jobs.workable.com/view/fbxfdBmCBvDryyqx4vLgUi/data-science-leader-in-california-city-at-tiger-analytics-inc."><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Power Systems Engineer | Carbon Direct | United States - Remote | Not specified | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/carbondirect/jobs/5096071007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer | Kitware | Clifton Park, New York | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/kitware/3bf971c6-93d9-4ba3-8946-54fc7741c2b0"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer - Cumberland/FICCO Tools Engineering | DRW | Chicago | 2 | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/drweng/jobs/7797373"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-04-08 · 15 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Applied Scientist II | The Trade Desk | Irvine | 2 | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/thetradedesk/jobs/5102136007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer (New Grad) | Zettabyte | United States | 2 | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/zettabyte-space/50a9c6dc-7225-4ff0-a914-69d1dd325d6a"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Frontend Software Engineer | Hadrian | Los Angeles, CA | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/hadrian-automation/af629fd3-1162-4a8c-bab6-0083bd7f20fc"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer II | The Trade Desk | San Francisco | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/thetradedesk/jobs/5102422007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Windows AI Automation | Sola | Remote | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/sola/9a9c39a9-6a15-4b76-b538-f7d219fdb92e"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Robotics Software Engineer | RoboForce | Milpitas, CA | 2 | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/roboforce/jobs/5181554008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer 3 | MongoDB | Sydney | 2 | ❌ No | 15% | <a href="https://www.mongodb.com/careers/job/?gh_jid=7744404"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Deployed | Serval | San Francisco | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/Serval/37e2985b-a7bf-4c02-bd71-b5d906292814"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Systems Engineer II, Compute | Crusoe | San Francisco, CA - US | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/Crusoe/39e3cfc5-c0fd-44ad-b5de-ffde8080c099"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| BIOS Software Engineer | Arista Networks | Austin, TX, United States | Not specified | ❌ No | 4% | <a href="https://jobs.smartrecruiters.com/AristaNetworks/744000119389508"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| BIOS Software Engineer | Arista Networks | Santa Clara, CA, United States | Not specified | ❌ No | 4% | <a href="https://jobs.smartrecruiters.com/AristaNetworks/744000119391376"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Linux Kernel Software Engineer | Arista Networks | Austin, TX, United States | Not specified | ❌ No | 4% | <a href="https://jobs.smartrecruiters.com/AristaNetworks/744000119379088"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Linux Kernel Software Engineer | Arista Networks | Santa Clara, CA, United States | Not specified | ❌ No | 4% | <a href="https://jobs.smartrecruiters.com/AristaNetworks/744000119379037"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Layer1 | Arista Networks | Santa Clara, CA, United States | Not specified | ❌ No | 4% | <a href="https://jobs.smartrecruiters.com/AristaNetworks/744000119449582"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Layer1 | Arista Networks | Austin, TX, United States | Not specified | ❌ No | 4% | <a href="https://jobs.smartrecruiters.com/AristaNetworks/744000119446993"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-04-07 · 12 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| AI Sorcerer | Anduril | Costa Mesa, California, United States | Not specified | ❌ No | 33% | <a href="https://boards.greenhouse.io/andurilindustries/jobs/5101597007?gh_jid=5101597007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer (Platform Team) | SpaceX | Hawthorne, CA | 2 | ❌ No | 19% | <a href="https://boards.greenhouse.io/spacex/jobs/8495882002?gh_jid=8495882002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer in Test (SET) | Allegiant Air | Las Vegas, NV | Not specified | ❌ No | 15% | <a href="https://jobs.lever.co/allegiantair/11d8e500-6164-4f13-b17d-b5d75546d793"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Infrastructure | Cursor | San Francisco | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/cursor/6d576a09-f30d-4e5e-bb58-5d7ef56cb511"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Storage | Cursor | San Francisco | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/cursor/515926c1-f044-4aff-9d5f-0bb84cb7eca2"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Android Developer Intern | Eulerity | New York, New York | 1 | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/eulerity/jobs/4671031006"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Analytics Engineer I | dv01 | Remote - USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/dv01/jobs/8497282002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Scientist | RightsHelper | United States | Not specified | ❌ No | 11% | <a href="https://jobs.workable.com/view/rzbLSJxdU8pcXNE61J27dB/remote-data-scientist-in-united-states-at-rightshelper"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Core Services | Cursor | San Francisco | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/cursor/77bf35db-119c-4533-8187-1e8d5ae08c45"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Model Routing & Inference | Cursor | New York | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/cursor/45c815b0-5100-4934-8558-0e750b8aed79"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Services Platform | Cursor | San Francisco | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/cursor/0863d184-1b2f-42cd-9fca-37fa90efe2eb"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Mobile iOS Developer Intern | Eulerity | New York, New York | 1 | ❌ No | 7% | <a href="https://job-boards.greenhouse.io/eulerity/jobs/4671025006"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-04-06 · 16 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Application Software Engineer | SpaceX | Bastrop, TX | 2 | ❌ No | 26% | <a href="https://boards.greenhouse.io/spacex/jobs/8494240002?gh_jid=8494240002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Application Software Engineer | SpaceX | Hawthorne, CA | 2 | ❌ No | 26% | <a href="https://boards.greenhouse.io/spacex/jobs/8494238002?gh_jid=8494238002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Full Stack Software Engineer (Application Software) | SpaceX | Bastrop, TX | 2 | ❌ No | 26% | <a href="https://boards.greenhouse.io/spacex/jobs/8495180002?gh_jid=8495180002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Full Stack Software Engineer (Application Software) | SpaceX | Hawthorne, CA | 2 | ❌ No | 26% | <a href="https://boards.greenhouse.io/spacex/jobs/8495131002?gh_jid=8495131002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Full Stack Cloud Engineer (AI Security Platform) | HiddenLayer | Remote- US | Not specified | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/hiddenlayer/jobs/5100067007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Marketing Data Scientist | Kikoff | San Francisco | 2 | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/kikoff/jobs/4209451009"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer (New Grad Program) | Sigma Computing | San Francisco, CA and New York City, NY | 0-2 | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/sigmacomputing/jobs/7690411003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer Intern (Fall 2026) | Notion | San Francisco, California | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/notion/5b15697c-fa91-4511-9482-c98a6ff29f90"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Web Product | Mirage | Union Square, New York City | 2 | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/mirage/961e9a66-7574-4e0a-bff1-95312b7d6cab"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Applied ML Engineer | Foxglove | San Francisco, CA | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/foxglove/2780d1fb-5afc-40b2-9a11-8d8d9ad44760"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Junior Full Stack Engineer | MLabs | New York, New York, United States | 0-2 | ❌ No | 15% | <a href="https://apply.workable.com/j/DDD1E9AF26"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer - Back End | Farfetch | Porto | Not specified | ❌ No | 15% | <a href="https://jobs.lever.co/farfetch/3aa69044-5ad4-4323-ad4d-33a714aef3f7"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Full-Stack Engineer | Vironix AI | Austin, Texas, United States | Not specified | ❌ No | 11% | <a href="https://jobs.workable.com/view/48KDWXBasXyvXMG1PcrPDt/hybrid-full-stack-engineer-in-austin-at-vironix-ai"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Full-Stack Engineer (Backend Focused) | Vironix AI | Austin, Texas, United States | Not specified | ❌ No | 7% | <a href="https://jobs.workable.com/view/6t4yqFrHY98XmU9Aw1avrh/hybrid-full-stack-engineer-(backend-focused)-in-austin-at-vironix-ai"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer | Freeform | Los Angeles, CA (On-site) | Not specified | ❌ No | 7% | <a href="https://job-boards.greenhouse.io/freeformfuturecorp/jobs/7691540003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Tutor - Audio Editing | xAI | Remote | Not specified | ❌ No | 4% | <a href="https://job-boards.greenhouse.io/xai/jobs/5098930007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-04-05 · 6 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Data Scientist | KDA Consulting Inc | McLean, Virginia, United States | Not specified | ❌ No | 30% | <a href="https://jobs.workable.com/view/mKFf6YvVZGEUKLaiw1y4PG/data-scientist-in-mclean-at-kda-consulting-inc"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Scientist | KDA Consulting Inc | Herndon, Virginia, United States | Not specified | ❌ No | 30% | <a href="https://jobs.workable.com/view/knFZBmcV8JLHTWmUK6PtGz/data-scientist-in-herndon-at-kda-consulting-inc"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Scientist | KDA Consulting Inc | Chantilly, Virginia, United States | Not specified | ❌ No | 30% | <a href="https://jobs.workable.com/view/upgcpGZRswdMLoeyHNawNb/data-scientist-in-chantilly-at-kda-consulting-inc"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Engineer | KDA Consulting Inc | McLean, Virginia, United States | Not specified | ❌ No | 15% | <a href="https://jobs.workable.com/view/onEq6iaBk54JDYNdnLxqrf/data-engineer-in-mclean-at-kda-consulting-inc"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Engineer | KDA Consulting Inc | Herndon, Virginia, United States | Not specified | ❌ No | 15% | <a href="https://jobs.workable.com/view/41FsKi9JCo9nYgEDr6CCRr/data-engineer-in-herndon-at-kda-consulting-inc"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Engineer | KDA Consulting Inc | Chantilly, Virginia, United States | Not specified | ❌ No | 15% | <a href="https://jobs.workable.com/view/inU6em2xS1RPj9STLPEnVm/data-engineer-in-chantilly-at-kda-consulting-inc"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-04-03 · 5 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer - New Grad | Realm | Remote | 0-2 | ❌ No | 41% | <a href="https://jobs.ashbyhq.com/realmalliance/56d8b433-31ad-43a2-997e-b8538f5f2c9f"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Generative AI Integration Engineer | Anduril | Costa Mesa, California, United States | Not specified | ❌ No | 37% | <a href="https://boards.greenhouse.io/andurilindustries/jobs/4792948007?gh_jid=4792948007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Pre-Sales Systems Engineer, SLED (New Jersey) | Pure Storage | Remote, New Jersey | Not specified | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/purestorage/jobs/7776197"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Full-Stack Developer (AI-Augmented) | Texas Sports Academy | Austin, Texas, United States | Not specified | ❌ No | 11% | <a href="https://jobs.workable.com/view/1w9FY2ARpNSA4rXzJ3KFgG/full-stack-developer-(ai-augmented)-in-austin-at-texas-sports-academy"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Business Development Representative \| AI Pentesting | Escape | NYC Office | Not specified | ❌ No | 7% | <a href="https://jobs.ashbyhq.com/escape/87c1ee66-3495-4aef-8615-ccd23e8cc6a7"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-04-02 · 9 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| AI Engineer | InterImage | Annapolis Junction, Maryland, United States | Not specified | ❌ No | 30% | <a href="https://jobs.workable.com/view/2e6kCgKWXUs6uEiDJEQAZW/ai-engineer-in-annapolis-junction-at-interimage"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Fall 2026: SharkByte Applied AI & Analytics Co-op (July to December) | SharkNinja | Miami, Florida, United States; Needham, MA, United States | Not specified | ❌ No | 30% | <a href="https://job-boards.greenhouse.io/sharkninjaoperatingllc/jobs/4669676006"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Network Data Analyst | LG Electronics | Huntsville, AL | Not specified | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/lgelectronics/jobs/5174223008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Scientist - Model Optimization | quadric, Inc | Burlingame, California, United States | Not specified | ❌ No | 19% | <a href="https://jobs.workable.com/view/2yyHXVnCA6q5byg5nicZCV/data-scientist---model-optimization-in-burlingame-at-quadric%2C-inc"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Machine Learning Research Scientist, Mechanical Intuition in Multimodal Models | Toyota Research Institute | Los Altos, CA; Cambridge, MA | Not specified | ❌ No | 19% | <a href="https://jobs.lever.co/tri/8851c6af-6a0f-4fc2-8805-8d8b266d1dd3"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| ML Platform Engineer | Foxglove | San Francisco, CA | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/foxglove/3ab47403-b3b6-4e9b-bb89-6e225b16799f"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Platform Engineer - KLPTK | Valsoft Corporation | Beirut, Beirut Governorate, Lebanon | Not specified | ❌ No | 15% | <a href="https://apply.workable.com/j/CEFE96455F"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Applied AI | Auctor | New York | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/auctor/ca5b0c44-cafb-48ad-99fa-84aa3cfc5179"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Geophysicist - AI Trainer | Handshake | Remote (USA) | 1 | ❌ No | 4% | <a href="https://jobs.ashbyhq.com/handshake/7ee2585c-2aab-421a-aff3-29a85f83bd15"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-04-01 · 36 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Postdoctoral Researcher, Real-Time Generative AI for Automotive XR | Toyota Research Institute | Los Altos, CA | Not specified | ❌ No | 30% | <a href="https://jobs.lever.co/tri/f1f3a5a2-8aaa-41e1-914c-0453489bea1e"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer - AI Platforms and Products (Frontend) | The New York Times | New York, NY | 2 | ❌ No | 26% | <a href="https://job-boards.greenhouse.io/thenewyorktimes/jobs/4680447005"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Autonomy Systems Software Engineer | Kodiak Robotics | San Francisco Bay Area | Not specified | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/kodiak/jobs/4204664009"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Scientist | Triumph | San Francisco HQ | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/triumph-arcade/f1cbbcbd-8e9b-472e-8fc1-4459e5e6cbca"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Generative AI Applications Engineer (Agents & RAG) | Accenture | Fairfield, CA | Not specified | ❌ No | 22% | <a href="https://boards.greenhouse.io/accenturefederalservices/jobs/4669273006?gh_jid=4669273006"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Generative AI Applications Engineer (Agents & RAG) | Accenture | Seattle, WA | Not specified | ❌ No | 22% | <a href="https://boards.greenhouse.io/accenturefederalservices/jobs/4669272006?gh_jid=4669272006"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Generative AI Applications Engineer (Agents & RAG) | Accenture | Washington, DC | Not specified | ❌ No | 22% | <a href="https://boards.greenhouse.io/accenturefederalservices/jobs/4669270006?gh_jid=4669270006"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Postdoctoral Researcher, CAD Generation Machine Learning | Toyota Research Institute | Los Altos, CA | Not specified | ❌ No | 22% | <a href="https://jobs.lever.co/tri/8255ca2d-c400-40ac-8676-c9aaef9e8cea"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Research Scientist, Agents for Science | The Allen Institute for AI | Seattle, WA | Not specified | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/thealleninstitute/jobs/7723570"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Intern (Summer 2027) | Aquatic Capital Management | Chicago | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/aquaticcapitalmanagement/jobs/8489233002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Engineer | Teserac, Inc. | Sunnyvale, California, United States | Not specified | ❌ No | 15% | <a href="https://jobs.workable.com/view/cH6pMyDMEWVnSSi6hgW3c5/ai-engineer-in-sunnyvale-at-teserac%2C-inc."><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Network Infrastructure Engineer (DevOps) | MLabs | Ashburn, Virginia, United States | Not specified | ❌ No | 15% | <a href="https://apply.workable.com/j/074C9E61C8"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer | MLabs | San Francisco, California, United States | Not specified | ❌ No | 15% | <a href="https://jobs.workable.com/view/wLsRBAB2BQpfj4LGVRhPRw/software-engineer-in-san-francisco-at-mlabs"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer | MLabs | New York, New York, United States | Not specified | ❌ No | 15% | <a href="https://jobs.workable.com/view/rKMj32TAfeZbKkBhrX4g7G/software-engineer-in-new-york-at-mlabs"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer – ML Platform | Avride | Austin, TX | Not specified | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/avride/jobs/4205615009"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Tutor - Chinese | xAI | Remote | Not specified | ❌ No | 4% | <a href="https://job-boards.greenhouse.io/xai/jobs/5090180007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Tutor - Finnish | xAI | Remote | Not specified | ❌ No | 4% | <a href="https://job-boards.greenhouse.io/xai/jobs/5090199007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Tutor - French | xAI | Remote | Not specified | ❌ No | 4% | <a href="https://job-boards.greenhouse.io/xai/jobs/5090202007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Tutor - German | xAI | Remote | Not specified | ❌ No | 4% | <a href="https://job-boards.greenhouse.io/xai/jobs/5090120007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Tutor - Hebrew | xAI | Remote | Not specified | ❌ No | 4% | <a href="https://job-boards.greenhouse.io/xai/jobs/5090206007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Tutor - Indonesian | xAI | Remote | Not specified | ❌ No | 4% | <a href="https://job-boards.greenhouse.io/xai/jobs/5095657007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Tutor - Korean | xAI | Remote | Not specified | ❌ No | 4% | <a href="https://job-boards.greenhouse.io/xai/jobs/5090210007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Tutor - Marathi | xAI | Remote | Not specified | ❌ No | 4% | <a href="https://job-boards.greenhouse.io/xai/jobs/5090213007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Tutor - Norwegian | xAI | Remote | Not specified | ❌ No | 4% | <a href="https://job-boards.greenhouse.io/xai/jobs/5090215007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Tutor - Polish | xAI | Remote | Not specified | ❌ No | 4% | <a href="https://job-boards.greenhouse.io/xai/jobs/5090218007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Tutor - Portuguese | xAI | Remote | Not specified | ❌ No | 4% | <a href="https://job-boards.greenhouse.io/xai/jobs/5090221007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Tutor - Punjabi | xAI | Remote | Not specified | ❌ No | 4% | <a href="https://job-boards.greenhouse.io/xai/jobs/5090246007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Tutor - Spanish | xAI | Remote | Not specified | ❌ No | 4% | <a href="https://job-boards.greenhouse.io/xai/jobs/5090264007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Tutor - Swedish | xAI | Remote | Not specified | ❌ No | 4% | <a href="https://job-boards.greenhouse.io/xai/jobs/5090265007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Tutor - Tagalog | xAI | Remote | Not specified | ❌ No | 4% | <a href="https://job-boards.greenhouse.io/xai/jobs/5090268007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Tutor - Tamil | xAI | Remote | Not specified | ❌ No | 4% | <a href="https://job-boards.greenhouse.io/xai/jobs/5090269007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Tutor - Telugu | xAI | Remote | Not specified | ❌ No | 4% | <a href="https://job-boards.greenhouse.io/xai/jobs/5090270007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Tutor - Thai | xAI | Remote | Not specified | ❌ No | 4% | <a href="https://job-boards.greenhouse.io/xai/jobs/5090272007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Tutor - Turkish | xAI | Remote | Not specified | ❌ No | 4% | <a href="https://job-boards.greenhouse.io/xai/jobs/5095662007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Tutor - Urdu | xAI | Remote | Not specified | ❌ No | 4% | <a href="https://job-boards.greenhouse.io/xai/jobs/5090273007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Tutor - Vietnamese | xAI | Remote | Not specified | ❌ No | 4% | <a href="https://job-boards.greenhouse.io/xai/jobs/5090274007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-03-31 · 9 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| BioMedical AI Research Engineer | Xaira Therapeutics | South San Francisco, California, United States | Not specified | ❌ No | 37% | <a href="https://job-boards.greenhouse.io/xairatherapeutics/jobs/5005200007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Scientist | Dropbox | Remote - US: Select locations | Not specified | ❌ No | 15% | <a href="https://jobs.dropbox.com/listing/7762004?gh_jid=7762004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Generative AI Platform Engineer | Accenture | Washington, DC | Not specified | ❌ No | 15% | <a href="https://boards.greenhouse.io/accenturefederalservices/jobs/4668930006?gh_jid=4668930006"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Security Software Engineer II, Corporate Security | Pinterest | San Francisco, CA, US; Remote, US | Not specified | ❌ No | 15% | <a href="https://www.pinterestcareers.com/jobs/?gh_jid=7494666"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, User Sharing | Roblox | San Mateo, CA, United States | 1 | ❌ No | 15% | <a href="https://careers.roblox.com/jobs/7767204?gh_jid=7767204"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| GenAI Platform Engineer | Accenture | Seattle, WA | Not specified | ❌ No | 11% | <a href="https://boards.greenhouse.io/accenturefederalservices/jobs/4668945006?gh_jid=4668945006"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Full-Stack Engineer | Parspec | Hybrid - San Mateo, California | Not specified | ❌ No | 7% | <a href="https://jobs.ashbyhq.com/parspec/7a8cbb41-0a10-47ac-ae1f-bda12b53d62b"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Simulation Software Engineer (Application Software) | SpaceX | Hawthorne, CA | 2 | ❌ No | 7% | <a href="https://boards.greenhouse.io/spacex/jobs/8488034002?gh_jid=8488034002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Simulations (Application Software) | SpaceX | Hawthorne, CA | 2 | ❌ No | 7% | <a href="https://boards.greenhouse.io/spacex/jobs/8487534002?gh_jid=8487534002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-03-30 · 8 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Data Engineer | Tavus | Remote | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/tavus/a29d6e98-3a83-461c-b651-fc0dc387c4c7"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Machine Learning Engineer | Meshy | Shenzhen | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/meshy/de962b0e-0da4-4928-9750-e8c5ab63c84c"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer | Circleback | San Francisco | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/circleback/c0cb575f-b1b8-4c0b-9f51-9521469f7f5d"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer I | Sony Interactive Entertainment | United States, Los Angeles, CA | Not specified | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/sonyinteractiveentertainmentglobal/jobs/5840958004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer II, SDN Networking | Crusoe | San Francisco, CA - US | 2 | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/Crusoe/14d58b1a-74a9-4779-882a-043889f726a8"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Engineer | Northstrat | Sterling, Virginia, United States | Not specified | ❌ No | 7% | <a href="https://jobs.workable.com/view/4Awu8s6i3ebFmaTFd5WpEw/hybrid-data-engineer-in-sterling-at-northstrat"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Robotics Software Engineer – Robot Integrations | Field AI | Irvine, CA | Not specified | ❌ No | 7% | <a href="https://jobs.lever.co/field-ai/b5f58151-9a46-441f-badf-2e91244bfd39"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer - Runtime Platform, Robot Software | Wayve | Sunnyvale | Not specified | ❌ No | 7% | <a href="https://wayve.firststage.co/jobs?gh_jid=8482117002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-03-29 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Machine Learning Researcher - Springtail | Astera | Emeryville HQ | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/astera/62476521-abff-42eb-9b23-61d5a5fd0aed"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-03-28 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer II | DiDi Global | San Jose, CA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/didi/jobs/7762773"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-03-27 · 20 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Machine Learning Engineer: LLM Interpretability & Systems | CTGT | San Francisco | Not specified | ❌ No | 44% | <a href="https://jobs.ashbyhq.com/ctgt/c6916802-4158-4f24-b4b1-ac978157b6d9"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Machine Learning Scientist (Financial Scoring) | Lendbuzz | Boston, MA | 2 | ❌ No | 37% | <a href="https://jobs.lever.co/lendbuzz/7f05f28b-8a0f-45cd-92c4-24f44994f85a"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Engineer, Web Scraping | 10a Labs | Washington D.C. | 2 | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/10alabs/jobs/4203151009"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Junior DevOps Engineer | Trading212 | Sofia | 0-2 | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/trading212/4892b112-efce-425d-a5ca-3645e8961474"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer (Entry) | Pattern Data | Richmond, VA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/patterndata/jobs/5092337007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Product | Prelim | New York | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/prelim/62449307-e366-4c92-8d22-9a9f8ec11afa"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer (L1) | Twilio | Remote - US | Not specified | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/twilio/jobs/7681338"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| World Model Research Scientist- Physical AI | Kodiak Robotics | Mountain View, CA | Not specified | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/kodiak/jobs/4203253009"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | Miami, FL | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/0b46895a-59ab-4dbc-80ef-7ed0b4978d90"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | Miami, FL | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/0f23c215-67a9-4404-befc-85a4529f4457"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | Miami, FL | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/53cd93fa-4de6-4234-bddf-23db810089be"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | Miami, FL | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/7042fe74-d1ef-4177-bee2-311c5b1b8256"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | Indianapolis, IN | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/05604e2d-bbf8-48bf-abf4-92d7f20fc5fe"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | Indianapolis, IN | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/9a13f02a-15f5-466b-b914-a1f1c74de174"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | Indianapolis, IN | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/d4e2fdea-dd37-4b57-b71e-3eb5113b22d7"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Data Contributor | TSMG | Indianapolis, IN | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/tsmg/8c1d7435-6779-4b04-848a-7b314fef7a68"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer II, Storage | Crusoe | San Francisco, CA - US | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/Crusoe/00fb8ce3-aaee-41c3-8016-18829f6b80ff"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Tutor - Arabic | xAI | Remote | Not specified | ❌ No | 4% | <a href="https://job-boards.greenhouse.io/xai/jobs/5090171007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Tutor - Danish | xAI | Remote | Not specified | ❌ No | 4% | <a href="https://job-boards.greenhouse.io/xai/jobs/5090189007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Tutor - Dutch | xAI | Remote | Not specified | ❌ No | 4% | <a href="https://job-boards.greenhouse.io/xai/jobs/5090197007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-03-26 · 17 roles · 2 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Systems PhD - Software Engineer | Databricks | Bellevue, Washington; Seattle, Washington | Not specified | ✅ Yes | 15% | <a href="https://databricks.com/company/careers/open-positions/job?gh_jid=8482086002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Systems PhD - Software Engineer | Databricks | Mountain View, California; San Francisco, California | Not specified | ✅ Yes | 15% | <a href="https://databricks.com/company/careers/open-positions/job?gh_jid=8482037002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Applied AI Engineer, Codex Core Agent | OpenAI | San Francisco | Not specified | ❌ No | 37% | <a href="https://jobs.ashbyhq.com/openai/577e6673-0a4a-491b-9a0d-facbdd3bdf3c"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Research Engineer | Creatify | Mountain View, CA | Not specified | ❌ No | 30% | <a href="https://jobs.ashbyhq.com/embedding-vc/925e9460-e2db-45ee-86d3-69d497106272"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer - 2027 Interns | Ellipsis Labs | New York, New York | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/ellipsislabs/02136b22-35b1-4b3d-8bef-567c3380a849"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer - 2027 New Grads | Ellipsis Labs | New York, New York | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/ellipsislabs/256c2ec2-01c8-4ff6-9ad0-b926fe40472d"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Codex Core Agents | OpenAI | San Francisco | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/openai/7ade7a12-845c-4e3a-af23-c028420bd181"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Backend Engineer, Oasis, Music | Spotify | New York, NY | Not specified | ❌ No | 19% | <a href="https://jobs.lever.co/spotify/52fe2b49-3c85-4479-b1db-2c5ab74cbcfc"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Field Data Analyst | Field AI | Irvine, CA | Not specified | ❌ No | 15% | <a href="https://jobs.lever.co/field-ai/acfba278-5f04-4639-ae26-c85e607eebce"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer | Northstrat | Herndon, Virginia, United States | Not specified | ❌ No | 15% | <a href="https://jobs.workable.com/view/qMCbanU2qCEV53tbXthcgS/hybrid-software-engineer-in-herndon-at-northstrat"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI 3D Dataset Engineer | Meshy | Shanghai | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/meshy/60206200-a633-493c-8bb5-4749593c4d58"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Social Content Creator (full-time) | Creatify | San Francisco Bay Area | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/embedding-vc/56302113-f87d-44ba-8687-dabfec3ce3d4"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Autonomy Integration Software Engineer | Glydways | Remote | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/glydways/jobs/5091394007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Java Software Engineer TNG | Northstrat | Aurora, Colorado, United States | Not specified | ❌ No | 7% | <a href="https://jobs.workable.com/view/3SD4vfbiN2TBTmEo8vhDhK/java-software-engineer-tng-in-aurora-at-northstrat"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Java Software Engineer TNG | Northstrat | Sterling, Virginia, United States | Not specified | ❌ No | 7% | <a href="https://jobs.workable.com/view/wNB6r79tQRAwcQGxFJfUkj/java-software-engineer-tng-in-sterling-at-northstrat"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer II | Sony Interactive Entertainment | United States, San Mateo, CA | Not specified | ❌ No | 7% | <a href="https://job-boards.greenhouse.io/sonyinteractiveentertainmentglobal/jobs/5838328004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Creator — Video & Generative Media | Creatify | Mountain View, CA | 1 | ❌ No | 4% | <a href="https://jobs.ashbyhq.com/embedding-vc/5098ed48-7d8d-4deb-9f34-daa407358351"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-03-25 · 12 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Research Scientist, Frontier Risk Evaluations | Scale AI | San Francisco, CA; New York, NY | Not specified | ❌ No | 26% | <a href="https://job-boards.greenhouse.io/scaleai/jobs/4677657005"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer - AI Engineering | Applied Intuition | Sunnyvale | 2 | ❌ No | 26% | <a href="https://jobs.ashbyhq.com/applied/981054d6-d6d9-4553-9db8-38e56939d3b8"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| 0->1 Engineer, Open Source AI | Mozilla | Remote US | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/mozilla/jobs/7747603"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI in Residence | Xaira Therapeutics | South San Francisco, California, United States | Not specified | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/xairatherapeutics/jobs/5089321007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Flight Software Infrastructure Engineer (Starlink) | SpaceX | Redmond, WA | 2 | ❌ No | 15% | <a href="https://boards.greenhouse.io/spacex/jobs/8477451002?gh_jid=8477451002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Platform Engineer, Flight Software (Starlink) | SpaceX | Redmond, WA | 2 | ❌ No | 15% | <a href="https://boards.greenhouse.io/spacex/jobs/8478286002?gh_jid=8478286002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Security Software Engineer (Starlink) | SpaceX | Bastrop, TX | 2 | ❌ No | 15% | <a href="https://boards.greenhouse.io/spacex/jobs/8479234002?gh_jid=8479234002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer I, Commerce Engineering | Twitch | Seattle, WA | Not specified | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/twitch/jobs/8459320002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer I, Commerce Engineering | Twitch | San Francisco, CA | Not specified | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/twitch/jobs/8457711002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Infrastructure Engineer, Flight Software (Starlink) | SpaceX | Redmond, WA | 2 | ❌ No | 15% | <a href="https://boards.greenhouse.io/spacex/jobs/8478283002?gh_jid=8478283002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, C++ (Starlink) | SpaceX | Redmond, WA | 2 | ❌ No | 7% | <a href="https://boards.greenhouse.io/spacex/jobs/8477124002?gh_jid=8477124002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Starlink Network | SpaceX | Redmond, WA | 2 | ❌ No | 7% | <a href="https://boards.greenhouse.io/spacex/jobs/8477137002?gh_jid=8477137002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-03-24 · 13 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer, Data (Starlink) | SpaceX | Hawthorne, CA | 2 | ❌ No | 30% | <a href="https://boards.greenhouse.io/spacex/jobs/8476427002?gh_jid=8476427002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Machine Learning Researcher | Virtu Financial | New York | 2 | ❌ No | 26% | <a href="https://job-boards.greenhouse.io/virtu/jobs/8477580002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Agent Engineer - US Remote | TRM Labs | United States | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/trm-labs/828b60b2-ac8f-407d-92a0-8b794c8cf391"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer - AI Agents | LiveFlow | New York, New York | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/liveflow/44a4e8f8-76fc-433e-963f-f5ffcfdccd46"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Astro Core Services | Astronomer | New York City | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/astronomer/de75aa5e-82f9-4348-9122-4cc83138a569"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Motion & AI Video Designer (Via, Remix, Citymapper) | Via | New York City | Not specified | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/via/jobs/8478199002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| RF Systems Engineer II - Operations | Rocket Lab USA | Auckland, NZ | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/rocketlab/jobs/7671545003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Systems Engineer, MAPS | Cloudflare | Hybrid | Not specified | ❌ No | 11% | <a href="https://boards.greenhouse.io/cloudflare/jobs/7742773?gh_jid=7742773"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Backend Engineer | Maxana | Seattle, Washington, United States | Not specified | ❌ No | 7% | <a href="https://jobs.workable.com/view/7rjNz9y11ZZrFohoHYfist/hybrid-backend-engineer-in-seattle-at-maxana"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Backend Engineer | Maxana | San Francisco, California, United States | Not specified | ❌ No | 7% | <a href="https://jobs.workable.com/view/7t79S3VnGGX9cESwCKfePJ/hybrid-backend-engineer-in-san-francisco-at-maxana"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Backend Engineer | Maxana | New York, New York, United States | Not specified | ❌ No | 7% | <a href="https://jobs.workable.com/view/nBTwZSZXXoXMgg9K9du3Xa/hybrid-backend-engineer-in-new-york-at-maxana"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Mid-level Systems Engineer | Geneva Trading | Chicago Office | Not specified | ❌ No | 7% | <a href="https://job-boards.greenhouse.io/genevatrading/jobs/5088592007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Investor and Fund Administration Technology | Point72 | United States | Not specified | ❌ No | 4% | <a href="https://boards.greenhouse.io/point72/jobs/8372893002?gh_jid=8372893002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-03-23 · 9 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| AI Engineer - SDLC Process Improvement | Pierce Technology Corp | United States | Not specified | ❌ No | 19% | <a href="https://jobs.workable.com/view/8sMq5kU4QphNLwr58hMm39/remote-ai-engineer---sdlc-process-improvement-in-united-states-at-pierce-technology-corp"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer II | Alarm.com | Tysons, Virginia | 2 | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/alarmcom/jobs/8455660002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Site Reliability Engineer II | Illumio | Sunnyvale, California - HQ | 2 | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/illumio/3a3bf906-2223-49e5-a7b4-c71e549f2eb5"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Cloud Security | Illumio | Sunnyvale, California - HQ | 2 | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/illumio/3b98af67-5d7d-47b7-8ab3-296fdfd45de5"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Research – Cumberland Systematic | DRW | New York City | Not specified | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/drweng/jobs/7743648"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Analyst - SQL, Excel, Tableau/Power BI, with Salesforce | AssistRx | Orlando, Florida, United States | Not specified | ❌ No | 7% | <a href="https://jobs.workable.com/view/n9oZ1hYxEHMjS1bJuSbNyQ/remote-data-analyst---sql%2C-excel%2C-tableau%2Fpower-bi%2C-with-salesforce-in-orlando-at-assistrx"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Automation Engineer | Valsoft Corporation | United States | Not specified | ❌ No | 4% | <a href="https://apply.workable.com/j/0556AD4228"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Automation Engineer | Valsoft Corporation | United States | Not specified | ❌ No | 4% | <a href="https://jobs.workable.com/view/k9rTzDTy4TqSqLwKjvubsH/remote-ai-automation-engineer-in-united-states-at-valsoft-corporation"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Vice President, Enterprise Architecture & AI | Vuori | Carlsbad, CA, United States | Not specified | ❌ No | 4% | <a href="https://jobs.smartrecruiters.com/vuoriinc/744000116261378"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-03-20 · 7 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Generative AI - 3D Foundation Model | Meshy | Shanghai | Not specified | ❌ No | 30% | <a href="https://jobs.ashbyhq.com/meshy/ceedf3f8-be1b-42b5-b593-07bacecdd739"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI-Forward Engineer | NimbleRx | Redwood City, CA | 2 | ❌ No | 26% | <a href="https://jobs.lever.co/nimblerx/a4c29cab-9446-4bb8-82f9-bb6325e1cb18"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Research Engineer | Xaira Therapeutics | Seattle, Washington, United States; South San Francisco, California, United States | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/xairatherapeutics/jobs/5084981007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Scientist, Underwriting | Parafin | San Francisco, CA | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/parafin/92807f0c-0c67-4516-bbf2-dc809516de14"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Research Scientist, Agent Robustness | Scale AI | San Francisco, CA; New York, NY | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/scaleai/jobs/4675684005"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Research Scientist, AI Controls and Monitoring | Scale AI | San Francisco, CA; New York, NY | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/scaleai/jobs/4675694005"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Junior Software Engineer | Geneva Trading | Chicago Office | 0-2 | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/genevatrading/jobs/5085231007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-03-19 · 6 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Computational Geometry Software Engineer | Hadrian | Los Angeles, CA | Not specified | ❌ No | 26% | <a href="https://jobs.ashbyhq.com/hadrian-automation/3e8d001a-5df7-49ee-ab64-79c3c914545b"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Machine Learning Engineer | Spotify | New York, NY | Not specified | ❌ No | 26% | <a href="https://jobs.lever.co/spotify/e68ad741-4c4e-4b06-ae11-9cf1e36dd40f"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Scoop Core | The New York Times | New York, NY | 2 | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/thenewyorktimes/jobs/4673616005"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Engineer | HockeyStack | San Francisco | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/hockeystack/449b62dd-434d-4f42-b005-cf2bc74dba4d"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Site Reliability Engineer | Pico | New York City, NY | Not specified | ❌ No | 7% | <a href="https://job-boards.greenhouse.io/picoquantitativetrading/jobs/4664671006"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Benchmark & Datasets Engineer / Researcher | Pathway | Palo Alto, California, United States | Not specified | ❌ No | 4% | <a href="https://jobs.workable.com/view/knKPmxCM1nUE2VB85ZbMpc/hybrid-ai-benchmark-%26-datasets-engineer-%2F-researcher-in-palo-alto-at-pathway"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-03-18 · 16 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| AI Research Engineer | TRM Labs | North America | Not specified | ❌ No | 37% | <a href="https://jobs.ashbyhq.com/trm-labs/b9733033-ed7b-409b-8881-855f49002177"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Scientist / Engineer | Shift | US - Boston | Not specified | ❌ No | 33% | <a href="https://job-boards.greenhouse.io/shifttechnology/jobs/7668168003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer Intern 2026 | Creatify Lab | Mountain View | Not specified | ❌ No | 33% | <a href="https://jobs.ashbyhq.com/creatify/75a1f1ad-13d2-4513-952c-71b6dfcaa84f"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Localization | OpenAI | San Francisco | Not specified | ❌ No | 30% | <a href="https://jobs.ashbyhq.com/openai/deff9215-217d-4392-825e-7788cb8205f3"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Design Software (Starship) | SpaceX | Hawthorne, CA | 2 | ❌ No | 26% | <a href="https://boards.greenhouse.io/spacex/jobs/8466905002?gh_jid=8466905002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Design Software (Starship) | SpaceX | Starbase, TX | 2 | ❌ No | 26% | <a href="https://boards.greenhouse.io/spacex/jobs/8466837002?gh_jid=8466837002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer II | Alarm.com | Boston, Massachusetts | 2 | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/alarmcom/jobs/8432004002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Engineer | Baseten | San Francisco | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/baseten/c2ba6c50-d282-4478-98e9-668f94facde8"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer - Python | Applied Intuition | Sunnyvale | 1 | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/applied/32e39ce9-9c09-4dd9-9ad1-4ee0b0cf7907"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI & ML Engineering Coaches (Contract) | Leland | Remote - USA | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/leland/203589d3-86b4-4788-b130-eb9ae2399f67"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Core Product (Early Career)- San Francisco HQ | Orb | HQ-San Francisco | 2 | ❌ No | 7% | <a href="https://jobs.ashbyhq.com/orb/b39f70d0-aaa9-46c1-896a-b064a1d3b2cc"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Automation & Agents Coach (Contract) | Leland | Remote - USA | Not specified | ❌ No | 4% | <a href="https://jobs.ashbyhq.com/leland/1312ec97-2931-4ff7-9b37-e6876da19b03"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI for Data & Analytics Coach (Contract) | Leland | Remote - USA | Not specified | ❌ No | 4% | <a href="https://jobs.ashbyhq.com/leland/1f85224b-02d5-46af-9dcf-2a8b46595ae4"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI for Finance Coach (Contract) | Leland | Remote - USA | Not specified | ❌ No | 4% | <a href="https://jobs.ashbyhq.com/leland/981b806f-390e-4e21-8078-f6062f4c9cbd"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI for Sales & Marketing Coach (Contract) | Leland | Remote - USA | Not specified | ❌ No | 4% | <a href="https://jobs.ashbyhq.com/leland/4ddc80c9-8ca9-4603-b4fc-df1ccbf727ce"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Strategy & Transformation Coach (Contract) | Leland | Remote - USA | Not specified | ❌ No | 4% | <a href="https://jobs.ashbyhq.com/leland/6eb04f9c-8da4-47b7-8099-c55d9bb48f88"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-03-17 · 8 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Machine Learning Engineer, Integrity | OpenAI | San Francisco | Not specified | ❌ No | 48% | <a href="https://jobs.ashbyhq.com/openai/ecf1abec-898c-4acb-a984-42858836a1ff"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Machine Learning Engineer | Freedom Technology Solutions Group | Chantilly, VA | Not specified | ❌ No | 30% | <a href="https://job-boards.greenhouse.io/freedomconsulting/jobs/5081498007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Resident - Learning From Videos (LFV) | Toyota Research Institute | Los Altos, CA | Not specified | ❌ No | 19% | <a href="https://jobs.lever.co/tri/07910a65-9ab3-4d48-85a8-44cd187afafd"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer I | Aurora Innovation | Mountain View, California | 2 | ❌ No | 15% | <a href="https://aurora.tech/jobs/8159549002?gh_jid=8159549002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Post-Training Research Scientist | Baseten | San Francisco | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/baseten/7c9d2bb0-ac03-4a3c-86c3-cf720cd314e8"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer - Cumberland/FICCO Tools Engineering | DRW | New York City | 2 | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/drweng/jobs/7728094"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer - Prediction Markets (Python) | DRW | New York City | 2 | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/drweng/jobs/7728142"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Analyst | Healthix | New York, New York, United States | Not specified | ❌ No | 7% | <a href="https://jobs.workable.com/view/ntvTeA2yuASJwvvJNkxNVm/hybrid-data-analyst-in-new-york-at-healthix"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-03-16 · 9 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Machine Learning Eval Engineer | Reducto | San Francisco Office | Not specified | ❌ No | 26% | <a href="https://jobs.ashbyhq.com/reducto/2b978fe8-b009-4dea-acd6-c4111440b7e5"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer I (Frontend, Growth) | Whoop | Boston, MA | Not specified | ❌ No | 15% | <a href="https://jobs.lever.co/whoop/27101f2d-abc5-4cf3-aa86-f164e66ecdd8"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Developer Experience (AI) | Clay | New York | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/claylabs/9b008b26-189b-45cf-83d8-fee117d32874"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer - Cumberland/FICCO Tools Engineering | DRW | Greenwich | 2 | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/drweng/jobs/7713717"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Product Development Coach (Contract) | Leland | Remote - USA | Not specified | ❌ No | 7% | <a href="https://jobs.ashbyhq.com/leland/59e7df43-6745-464c-af21-18eed2238f75"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Frontend Engineer - Music | Spotify | New York, NY | Not specified | ❌ No | 7% | <a href="https://jobs.lever.co/spotify/a8606ee6-84b9-4677-af2f-b57f1e71fd91"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Support Platform Engineer | Gigs | New York | Not specified | ❌ No | 7% | <a href="https://gigs.com/careers?gh_jid=4811744101"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Break Into AI Careers Coach (Contract) | Leland | Remote - USA | Not specified | ❌ No | 4% | <a href="https://jobs.ashbyhq.com/leland/fdd4759a-44a5-4bfe-8d58-860f906d2f1b"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Systems Engineer | LayerZero Labs | Vancouver, BC | 2 | ❌ No | 4% | <a href="https://job-boards.greenhouse.io/layerzerolabs/jobs/5826155004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-03-14 · 3 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Machine Learning Engineer | Orchard | San Francisco | 2 | ❌ No | 41% | <a href="https://jobs.ashbyhq.com/orchard/58cc4c3f-3ef2-4fe3-a81f-160916e67aaa"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| New Grad Software Engineer, Product | Secureframe | New York, NY | 0-2 | ❌ No | 19% | <a href="https://jobs.lever.co/secureframe/5138ce50-65dc-4818-8940-a78b3d0bbd4f"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Product Engineer | Samba TV | San Francisco, California | Not specified | ❌ No | 15% | <a href="https://jobs.lever.co/sambatv/a0a1f3cc-9b2e-4440-b5c1-45ea050cf0b1"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-03-13 · 12 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Bioinformatics Data Engineer | GenBio AI | Abu Dhabi | Not specified | ❌ No | 37% | <a href="https://jobs.lever.co/genbio/ba9d68d4-b928-42e9-a442-b5c03f0c95b6"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Application Engineer, AI Physics | Rescale | Remote (North America) | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/rescale/89c969e2-d677-494a-9c75-30d04516931f"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Robotics Software Engineer (Perception & Localization) | Orchard | San Francisco | 2 | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/orchard/4f81b000-c82a-4285-b05d-a7861a576d6f"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Android Software Engineer Co-op | Notability | San Francisco | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/gingerlabsinc/jobs/5129674008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, User Co-Experience | Roblox | San Mateo, CA, United States | 2 | ❌ No | 11% | <a href="https://careers.roblox.com/jobs/7711780?gh_jid=7711780"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Cartographer/Digital Cartographer - AI Trainer | Handshake | Remote (USA) | 1 | ❌ No | 7% | <a href="https://jobs.ashbyhq.com/handshake/9ec77bf2-bc68-4f0f-a235-7e774cbc41a6"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Electrical Design Engineer - AI Trainer | Handshake | Remote (USA) | 1 | ❌ No | 4% | <a href="https://jobs.ashbyhq.com/handshake/7e7702f6-750e-44e1-8f12-caf26fcc85f4"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Medical Image Analyst - AI Trainer | Handshake | Remote (USA) | 1 | ❌ No | 4% | <a href="https://jobs.ashbyhq.com/handshake/670b5472-0855-4339-9d72-d09f264ea0c8"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Music Producer - AI Trainer | Handshake | Remote (USA) | 1 | ❌ No | 4% | <a href="https://jobs.ashbyhq.com/handshake/d1fb64ba-750e-43da-8f1b-2cb4ae78da65"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| UI/UX Visual Designer - AI Trainer | Handshake | Remote (USA) | 1 | ❌ No | 4% | <a href="https://jobs.ashbyhq.com/handshake/8e9ee351-7149-40fa-851a-c4fb35fbc61d"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Video Content Producer - AI Trainer | Handshake | Remote (USA) | 1 | ❌ No | 4% | <a href="https://jobs.ashbyhq.com/handshake/d1b973a5-1726-4898-9356-607f63da5c20"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Video Editor - AI Trainer | Handshake | Remote (USA) | 1 | ❌ No | 4% | <a href="https://jobs.ashbyhq.com/handshake/de06e664-497e-438a-9e28-1387fa06d4d9"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-03-12 · 11 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| AI Solutions Engineer | Pinterest | San Francisco, CA, US; Remote, US | Not specified | ❌ No | 30% | <a href="https://www.pinterestcareers.com/jobs/?gh_jid=7714127"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Research Scientist, Gemini Safety | DeepMind | Mountain View, California, US | Not specified | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/deepmind/jobs/7421111"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer in Test (SET) | Machina Labs | Chatsworth, CA | Not specified | ❌ No | 19% | <a href="https://jobs.lever.co/MachinaLabs/8658cfcf-5fcc-411d-82d1-7187cbd38633"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Bugbot | Cursor | San Francisco | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/cursor/88d47f97-0bea-448c-9abb-4720e4acf17a"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Cloud Software Engineer - DevOps | TP-Link Systems Inc. | Irvine, California, United States | Not specified | ❌ No | 11% | <a href="https://jobs.workable.com/view/2LkUKyzgFxuqZZHDMGKFKE/cloud-software-engineer---devops-in-irvine-at-tp-link-systems-inc."><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Robotics Software Engineer, Embedded Systems | Shift Robotics | Austin, Texas, United States | Not specified | ❌ No | 11% | <a href="https://jobs.workable.com/view/a7RiNRbjWdDMjK9DRAU9wq/robotics-software-engineer%2C-embedded-systems-in-austin-at-shift-robotics"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer - Prediction Markets (Python) | DRW | Chicago | 2 | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/drweng/jobs/7713854"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Billing | Cursor | Remote | Not specified | ❌ No | 7% | <a href="https://jobs.ashbyhq.com/cursor/47994d20-cc6a-436b-8da0-2eceabfd413e"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, C++ (Starlink) | SpaceX | Sunnyvale, CA | 2 | ❌ No | 7% | <a href="https://boards.greenhouse.io/spacex/jobs/8451960002?gh_jid=8451960002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Enterprise Platform | Cursor | San Francisco | Not specified | ❌ No | 7% | <a href="https://jobs.ashbyhq.com/cursor/b6807f07-c4b7-4435-8c4c-0bef35865ad7"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Starlink Network | SpaceX | Sunnyvale, CA | 2 | ❌ No | 7% | <a href="https://boards.greenhouse.io/spacex/jobs/8458001002?gh_jid=8458001002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-03-11 · 4 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer, Data Platform | Ramp | New York, NY (HQ) | Not specified | ❌ No | 33% | <a href="https://jobs.ashbyhq.com/ramp/bca0346c-b843-4795-96df-6091f51e421b"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer II, Data Engineer | LG Ad Solutions | New York, NY | 2 | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/lgads/c26a2bee-e3ab-4d38-aa18-e44721d3d20b"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Transformative AI Research Economist, Economic Research | Anthropic | San Francisco, CA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/anthropic/jobs/5149802008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| IT Network Infrastructure Engineer, Launch | SpaceX | Starbase, TX | Not specified | ❌ No | 7% | <a href="https://boards.greenhouse.io/spacex/jobs/8458745002?gh_jid=8458745002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-03-10 · 10 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| AI Engineer | DataVisor | Mountain View, California, United States | 2 | ❌ No | 48% | <a href="https://apply.workable.com/j/5F7109B03C"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Engineer | DataVisor | Mountain View, California, United States | Not specified | ❌ No | 33% | <a href="https://jobs.workable.com/view/ooAokaoHEf3mZchbKcsk2G/hybrid-ai-engineer-in-mountain-view-at-datavisor"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Scientist - (Knowledge Graph & Identity) | Samba TV | San Francisco, California | 2 | ❌ No | 30% | <a href="https://jobs.lever.co/sambatv/7810c712-4c27-4161-9c1b-96353a210421"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Machine Learning Engineer II, Computer Vision Applied Science | Pinterest | San Francisco, CA, US; Remote, US | 2 | ❌ No | 30% | <a href="https://www.pinterestcareers.com/jobs/?gh_jid=7697137"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer - AI | Promise | San Francisco | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/Promise/aed7d514-6a36-498b-9659-4fb6ae38dca4"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Machine Learning Infrastructure | Bot Auto | Houston, TX or San Francisco Bay Area Based | Not specified | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/botauto/jobs/5148468008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Telemetry (Starlink) | SpaceX | Hawthorne, CA | 2 | ❌ No | 15% | <a href="https://boards.greenhouse.io/spacex/jobs/8451998002?gh_jid=8451998002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Platform Engineer, C/FICCO | DRW | Chicago | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/drweng/jobs/7696484"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Marketer Intern - USA | Valsoft Corporation | United States | Not specified | ❌ No | 4% | <a href="https://apply.workable.com/j/AA9D496F9D"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Web Application Developer (Magento/Adobe Commerce Experience Required) | Latitude | Montgomery Village, MD | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/latitudeinc/81cfcb80-c175-4bc8-a5d4-c09d2373d3b4"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-03-09 · 8 roles · 1 H-1B sponsor match

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Infrastructure Engineer, Observe by Snowflake | Snowflake | US-CA-Menlo Park | 2 | ✅ Yes | 11% | <a href="https://jobs.ashbyhq.com/snowflake/143a2248-564b-4cfa-85f5-d47bac911d74"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Research Scientist, Multimodal Alignment, Safety, and Fairness | DeepMind | Kirkland, Washington, US; Mountain View, California, US; New York City, New York, US | Not specified | ❌ No | 33% | <a href="https://job-boards.greenhouse.io/deepmind/jobs/7680885"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Forward Deployed Software Engineer, New Grad | Northslope Technologies | New York | 0-2 | ❌ No | 7% | <a href="https://jobs.ashbyhq.com/northslope-technologies/7ccd126f-b127-4526-87f1-57408919c30a"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Game Developer - AI Trainer | Handshake | Remote (USA) | 1 | ❌ No | 7% | <a href="https://jobs.ashbyhq.com/handshake/7d4f5006-c35d-48ae-bebf-fd1dc7acc870"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Architectural Designer - AI Trainer | Handshake | Remote (USA) | 1 | ❌ No | 4% | <a href="https://jobs.ashbyhq.com/handshake/1b468be6-e784-4a63-b771-a75603e9d2bb"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Digital Artist - AI Trainer | Handshake | Remote (USA) | 1 | ❌ No | 4% | <a href="https://jobs.ashbyhq.com/handshake/ceaeb07c-c943-4d6e-8357-2e5d37d62a03"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Hardware Engineer - AI Trainer | Handshake | Remote (USA) | 1 | ❌ No | 4% | <a href="https://jobs.ashbyhq.com/handshake/a2005298-96da-46f6-8809-231008720bd9"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Industrial Designer - AI Trainer | Handshake | Remote (USA) | 1 | ❌ No | 4% | <a href="https://jobs.ashbyhq.com/handshake/faeedef2-db4f-4a8a-8e30-2808908e7a40"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-03-08 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| PhD Autonomy Engineer Intern - Deep Learning or Computer Vision | Skydio | San Mateo, California, United States | Not specified | ❌ No | 30% | <a href="https://jobs.ashbyhq.com/skydio/8d3979a8-c791-4825-8cf4-9b25479b9519"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-03-07 · 3 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer - Systems Engineering AI Tooling | Applied Intuition | Sunnyvale | 2 | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/applied/6cce20b1-2250-4350-9952-9691f58fb074"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer – Autonomy Tooling | Applied Intuition | Sunnyvale | 2 | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/applied/453ad7e5-92dd-4517-bfac-3bc74d389663"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Pathology and Digital Imaging | Neuralink | Austin, Texas, United States | Not specified | ❌ No | 15% | <a href="https://boards.greenhouse.io/neuralink/jobs/7656401003?gh_jid=7656401003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-03-06 · 6 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Associate Data Scientist - Operations Research | Wheely | Λευκωσία, Nicosia, Cyprus | Not specified | ❌ No | 22% | <a href="https://boards.greenhouse.io/wheely/jobs/7655287003?gh_jid=7655287003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer - Sharding | Neo4j | Malmö | Not specified | ❌ No | 22% | <a href="https://boards.greenhouse.io/neo4j/jobs/4660616006?gh_jid=4660616006"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Frontend | Sim | San Francisco | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/sim/53142439-6fd6-4adf-ae61-438cd49afe82"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Robot Manufacturing | Neuralink | South San Francisco, California, United States | Not specified | ❌ No | 11% | <a href="https://boards.greenhouse.io/neuralink/jobs/7655221003?gh_jid=7655221003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer | Infleqtion | Louisville, Colorado, United States | Not specified | ❌ No | 7% | <a href="https://jobs.workable.com/view/k84mGXDVS65HKjUW4ykwgt/software-engineer-in-louisville-at-infleqtion"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Engineer | Elve Inc | Davis, California, United States | Not specified | ❌ No | 4% | <a href="https://jobs.workable.com/view/mseW1yLKF47MNrZaRvneUU/data-engineer-in-davis-at-elve-inc"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-03-05 · 23 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Infrastructure Engineer | Tamarind Bio | San Francisco | Not specified | ❌ No | 33% | <a href="https://jobs.ashbyhq.com/tamarindbio/2aecc18f-ab25-4560-9245-63c90174f333"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Machine Learning Engineer, LLM Evals & Observability | Glean | San Francisco, CA | 2 | ❌ No | 33% | <a href="https://job-boards.greenhouse.io/gleanwork/jobs/4669417005"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Scientist, Integrity Measurement | OpenAI | San Francisco | Not specified | ❌ No | 26% | <a href="https://jobs.ashbyhq.com/openai/be4e1098-f7ac-46f4-babe-44ef08f47fcb"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Full Stack | Verse Medical | New York City | 1 | ❌ No | 26% | <a href="https://jobs.ashbyhq.com/versemedical/42612785-ae5f-4bd3-b82c-c7f0fe872938"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Full Stack - Emerging Talent | Verse Medical | New York City | Not specified | ❌ No | 26% | <a href="https://jobs.ashbyhq.com/versemedical/af511a89-f716-4e51-9ad1-bf4e68dbdcaa"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Agentic Developer, LLM‑Native / Enterprise (Contractor), West Coast/ NYC | ION Group | Los Angeles | Not specified | ❌ No | 19% | <a href="https://jobs.lever.co/ion/f7bf6c5b-b70e-44d9-92b7-d9593f8220e6"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Operations Associate | Loop | San Francisco, New York, Chicago | 1 | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/loop/jobs/5819779004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Commercial Data Analyst, Poker | FanDuel | New York City | 2 | ❌ No | 15% | <a href="https://www.fanduel.careers/open-positions?gh_jid=7684414"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer II (Frontend), Social | Sony Interactive Entertainment | United States, Los Angeles, CA | 2 | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/sonyinteractiveentertainmentglobal/jobs/5712558004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Analog Engineer - AI Trainer | Handshake | Remote (USA) | 1 | ❌ No | 7% | <a href="https://jobs.ashbyhq.com/handshake/385dcfca-d3c2-4638-bc4f-de7108ca1a17"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| RF Engineer - AI Trainer | Handshake | Remote (USA) | 1 | ❌ No | 7% | <a href="https://jobs.ashbyhq.com/handshake/48bec46c-c1c6-4305-8511-250a1f1c5837"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Spatial Data Analyst - AI Trainer | Handshake | Remote (USA) | 1 | ❌ No | 7% | <a href="https://jobs.ashbyhq.com/handshake/8330e86c-9f22-47bc-8c68-b9fc9fee9b37"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| VLA for Physical AI (Talent pool) | 42dot | Sunnyvale, United States | Not specified | ❌ No | 7% | <a href="https://jobs.ashbyhq.com/42dot/c1ca75b1-d79e-4ed9-8be6-43d0055ffc2d"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Audio Editor - AI Trainer | Handshake | Remote (USA) | 1 | ❌ No | 4% | <a href="https://jobs.ashbyhq.com/handshake/32375272-3ef5-48a2-b995-458acb147997"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| BIM Coordinator - AI Trainer | Handshake | Remote (USA) | 1 | ❌ No | 4% | <a href="https://jobs.ashbyhq.com/handshake/bedfe1ee-5d52-4db5-8b91-50fac3f0ed5c"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Computational Fluid Dynamics Engineer - AI Trainer | Handshake | Remote (USA) | 1 | ❌ No | 4% | <a href="https://jobs.ashbyhq.com/handshake/218d9072-dd6a-474f-8de8-08d6748e4f56"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Content Video Editor - AI Trainer | Handshake | Remote (USA) | 1 | ❌ No | 4% | <a href="https://jobs.ashbyhq.com/handshake/f4034203-76ef-48c6-bb0e-31b63814977a"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Film & Video Editor - AI Trainer | Handshake | Remote (USA) | 1 | ❌ No | 4% | <a href="https://jobs.ashbyhq.com/handshake/ac76968b-cbc9-4c79-97c4-1421630e5057"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Indie Game Developer - AI Trainer | Handshake | Remote (USA) | 1 | ❌ No | 4% | <a href="https://jobs.ashbyhq.com/handshake/3cb4bb3b-9c8c-4f0d-9509-4891d76fc3d2"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Mechanical Drafter - AI Trainer | Handshake | Remote (USA) | 1 | ❌ No | 4% | <a href="https://jobs.ashbyhq.com/handshake/8b8cb6bc-f06f-429f-92dd-01225d634654"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Mechanical Engineer - AI Trainer | Handshake | Remote (USA) | 1 | ❌ No | 4% | <a href="https://jobs.ashbyhq.com/handshake/c966fa72-d8c8-40ec-8688-4772ea56f0dd"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Medical Imaging Specialist - AI Trainer | Handshake | Remote (USA) | 1 | ❌ No | 4% | <a href="https://jobs.ashbyhq.com/handshake/4a1d14cd-1aec-4974-aa0b-bb911d200c97"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Structural Engineer - AI Trainer | Handshake | Remote (USA) | 1 | ❌ No | 4% | <a href="https://jobs.ashbyhq.com/handshake/b416cb5d-661a-4793-8d5b-071e6ca4475b"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-03-04 · 8 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Forward Deployed Software Engineer | Northslope Technologies | Dubai | Not specified | ❌ No | 26% | <a href="https://jobs.ashbyhq.com/northslope-technologies/4bc4c6db-dd4c-489a-a569-a65ccfaca9f4"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer - Cloud Simulation & Full-Stack | Skydio | San Mateo, California, United States | Not specified | ❌ No | 26% | <a href="https://jobs.ashbyhq.com/skydio/7d7dfadc-c6fd-4958-8d59-004a91bff55e"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer - Simulation & Robotics Engineer | Skydio | San Mateo, California, United States | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/skydio/7a8f3e6c-d576-41af-a81e-bf4fe20da12a"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Fullstack Software Engineer | Hadrian | Los Angeles, CA | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/hadrian-automation/68286f52-3ea7-412e-a85f-04ab21c91994"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Systems Engineer – Oracle ERP | Tessera Labs | Remote in the U.S. | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/tessera-labs/1c2ae8fb-9bd1-409f-bfde-2e960c77a605"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer - C++ | Applied Intuition | Sunnyvale | 1 | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/applied/c9473dcb-f651-47bb-9a59-4150bddcdaa8"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Platform Systems Engineer; Motion Planning and Control | Waabi | Phoenix, AZ | Not specified | ❌ No | 7% | <a href="https://jobs.lever.co/waabi/5fcde68c-577a-4fed-b532-793fec8de175"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, CDN (Starlink) | SpaceX | Redmond, WA | 2 | ❌ No | 7% | <a href="https://boards.greenhouse.io/spacex/jobs/8448505002?gh_jid=8448505002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-03-03 · 9 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer II | Garner Health | New York City, New York | 2 | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/garnerhealth/jobs/5816889004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Agent Engineer | Pelago | New York, NY | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/pelago/jobs/5067557007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer | DataVisor | Mountain View, California, United States | Not specified | ❌ No | 19% | <a href="https://jobs.workable.com/view/65W1msW6ZHXXnAXei2dj4q/hybrid-software-engineer-in-mountain-view-at-datavisor"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Forward Deployed Engineer - ML | Modal | Stockholm | 2 | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/modal/0d9c249b-f305-4b0e-b325-3242ac7274e7"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data & AI Specialist | Windfall | San Francisco | 2 | ❌ No | 11% | <a href="https://jobs.lever.co/windfalldata/aa919b80-9247-4135-a356-c3f638c391d1"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer (Junior/Intermediate) | Automat | San Francisco | 0-2 | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/automat/a4172515-0353-47ec-9c71-631a294aa137"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Systems Engineer | Whoop | Boston, MA | Not specified | ❌ No | 7% | <a href="https://jobs.lever.co/whoop/2392c72b-6e86-4ce3-95b8-cebb4b8b48fe"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Platform Engineer - Application Networking | Sony Interactive Entertainment | United States, San Diego, CA | Not specified | ❌ No | 4% | <a href="https://job-boards.greenhouse.io/sonyinteractiveentertainmentglobal/jobs/5818262004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Platform Engineer - Application Networking | Sony Interactive Entertainment | United States, Aliso Viejo, CA | Not specified | ❌ No | 4% | <a href="https://job-boards.greenhouse.io/sonyinteractiveentertainmentglobal/jobs/5812444004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-03-02 · 10 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Helix AI Engineer, Agentic Systems | Figure | San Jose, CA | Not specified | ❌ No | 33% | <a href="https://job-boards.greenhouse.io/figureai/jobs/4659175006"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| New Grad Software Engineer | Confido | NYC Office | 0-2 | ❌ No | 26% | <a href="https://jobs.ashbyhq.com/confido/69c0e572-b2f4-442f-beb8-1240155c629e"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Platform Engineer | E-Space | Arlington, TX | Not specified | ❌ No | 22% | <a href="https://jobs.lever.co/espace/6495e784-f56b-4e64-8a35-032048b5dd31"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| University 2026 Talent Acquisition/ HR AI Intern | ID.me | Mountain View, CA | Not specified | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/idmeuniversityrecruiting/jobs/7648978003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform | Sim | San Francisco | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/sim/ea59bdb4-cfd5-41be-8220-27320195876c"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Instructor, AI/Machine Learning - NLP & Audio Analytics, Simplilearn (Part time | Fullstack Academy | United States | Not specified | ❌ No | 15% | <a href="https://jobs.workable.com/view/vN92eTz6jGU6Y46XMyxvYa/remote-instructor%2C-ai%2Fmachine-learning---nlp-%26-audio-analytics%2C-simplilearn-(part-time-in-united-states-at-fullstack-academy"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Agents | Sim | San Francisco | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/sim/c04eccb8-cbd8-4dc7-8299-b1f4c8aa1225"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Innovation Internship | Fundwell | New York, NY | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/fundwell/2d91136d-b54d-4ed0-93de-22c7839a3982"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Instructor, Microsoft AI Machine Learning, Simplilearn (Part time) | Fullstack Academy | United States | Not specified | ❌ No | 11% | <a href="https://jobs.workable.com/view/x1V9bNx5CuvVMcBVoHcoCh/remote-instructor%2C-microsoft-ai-machine-learning%2C-simplilearn-(part-time)-in-united-states-at-fullstack-academy"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| RF Silicon Software Engineer (RFIC Engineering) | SpaceX | Redmond, WA | 1 | ❌ No | 11% | <a href="https://boards.greenhouse.io/spacex/jobs/8439627002?gh_jid=8439627002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-03-01 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Robotics Software Engineer | Scout AI | Sunnyvale, CA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/scoutai/jobs/5137118008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-02-28 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer, Infrastructure Security | Resolve | San Francisco | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/Resolve%20AI/2aa8ba5e-9678-4693-9821-a7ff92e27862"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-02-27 · 9 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Machine Learning Engineer, App SW | Wayve | Sunnyvale | Not specified | ❌ No | 33% | <a href="https://wayve.firststage.co/jobs?gh_jid=8435254002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Research Engineer / Research Scientist, Pre-training | Anthropic | Zürich, CH | Not specified | ❌ No | 33% | <a href="https://job-boards.greenhouse.io/anthropic/jobs/5135168008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Web Interface Software Engineer | Silvus Technologies | Los Angeles CA | 1 | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/silvus/jobs/5136468008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Infrastructure Engineer | MatX | Mountain View, CA | Not specified | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/matx/jobs/5136264008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer - Billing and Internal Tooling | Baseten | San Francisco | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/baseten/d073254f-729c-471e-9a33-520358ead183"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Embedded Software Engineer | Silvus Technologies | Irvine CA | 2 | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/silvus/jobs/5136557008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Embedded Software Engineer | Silvus Technologies | Los Angeles | 2 | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/silvus/jobs/5135358008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Business Internship | Bitmovin | Klagenfurt; Vienna | Not specified | ❌ No | 4% | <a href="https://bitmovin.com/careers/8441631002?gh_jid=8441631002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Full Stack Web Developer (WordPress, Shopify, CRM) | Huzzle | United States | Not specified | ❌ No | 4% | <a href="https://jobs.workable.com/view/3kd7rvxbXCBC4Dfm1HzxKB/remote-full-stack-web-developer-(wordpress%2C-shopify%2C-crm)-in-united-states-at-huzzle"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-02-26 · 8 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Data Scientist, Preparedness | OpenAI | San Francisco | Not specified | ❌ No | 26% | <a href="https://jobs.ashbyhq.com/openai/efcc3430-14c8-4022-8350-8146ffb867ab"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Quantum Software Engineer - Machine Learning | Infleqtion | Chicago, Illinois, United States | Not specified | ❌ No | 26% | <a href="https://apply.workable.com/j/8CE62AF14C"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Scientist/Machine Learning Engineer | CATHEXIS | Redwood City, California, United States | Not specified | ❌ No | 22% | <a href="https://jobs.workable.com/view/vixRYXtyEUEVu6uJrDCKRD/data-scientist%2Fmachine-learning-engineer-in-redwood-city-at-cathexis"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Tutor - Software Engineering Specialist | xAI | Remote | Not specified | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/xai/jobs/5063490007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Instructor, AI/Machine Learning, Simplilearn (Part time) | Fullstack Academy | United States | Not specified | ❌ No | 11% | <a href="https://jobs.workable.com/view/2gwnMdxjrTz88E4sN9E6nm/remote-instructor%2C-ai%2Fmachine-learning%2C-simplilearn-(part-time)-in-united-states-at-fullstack-academy"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Postdoctoral Fellow - Applied Machine Learning in Quantum Systems | QuEra Computing | Boston, MA USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/queracomputinginc/jobs/5135036008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Quantum Software Engineer - Machine Learning | Infleqtion | Chicago, Illinois, United States | Not specified | ❌ No | 11% | <a href="https://jobs.workable.com/view/1y2DiU9FV1aLUP9npaveWS/hybrid-quantum-software-engineer---machine-learning-in-chicago-at-infleqtion"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Marketing Strategist - San Francisco | Uplane | San Francisco | Not specified | ❌ No | 4% | <a href="https://jobs.ashbyhq.com/uplane/7c2e963a-01bb-4007-8b66-4e46521049f4"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-02-25 · 10 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer II, Simulation, tvScientific | Pinterest | San Francisco, CA, US; Remote, US | Not specified | ❌ No | 26% | <a href="https://www.pinterestcareers.com/jobs/?gh_jid=7642265"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer | Salvo Health | New York, NY | 2 | ❌ No | 22% | <a href="https://jobs.lever.co/salvohealth/285d6b09-7961-490b-8927-3b24698affe9"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Engineer - Thorin | 8VC | San Francisco, CA | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/8vc/5ef2f020-4296-4bbc-89a0-7ffd578f421e"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Research Scientist/Engineer | Astera | Emeryville HQ | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/astera/1dd75b2d-8562-4411-9d22-ac35415debcf"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Research Scientist: Energy Based Models | Astera | Emeryville HQ | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/astera/6574807b-68f1-4eab-89d7-302467b5c77c"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Research Scientist: Hierarchical RL Agents | Astera | Emeryville HQ | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/astera/642a99d7-8cbd-4568-ae86-8844d3db5f48"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Research Scientist: Hierarchical Sensorimotor Perception | Astera | Emeryville HQ | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/astera/b13d16fa-415c-42fc-b624-7228c65ed0d3"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer | Braven | Chicago, Illinois, United States | Not specified | ❌ No | 15% | <a href="https://jobs.workable.com/view/4AohJ458dX6mwrd5LiR8pY/hybrid-software-engineer-in-chicago-at-braven"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Onboarding Specialist - Home Services | Podium | Lehi, Utah | 2 | ❌ No | 7% | <a href="https://job-boards.greenhouse.io/podium81/jobs/7654696"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Onboarding Specialist - Medspa | Podium | Lehi, Utah | 2 | ❌ No | 7% | <a href="https://job-boards.greenhouse.io/podium81/jobs/7654693"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-02-24 · 4 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer - AI Enablement | Baseten | San Francisco | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/baseten/b88a68b7-d2bc-4a30-a79a-3ef292ad7c26"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Digital Illustrator - AI Trainer | Handshake | Remote (USA) | 1 | ❌ No | 4% | <a href="https://jobs.ashbyhq.com/handshake/20045018-6294-4943-b010-95af96c6fba0"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Game Artist - AI Trainer | Handshake | Remote (USA) | 1 | ❌ No | 4% | <a href="https://jobs.ashbyhq.com/handshake/23dcd797-44b9-4ac5-856e-05d78a7aadcd"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Graphic Designer - AI Trainer | Handshake | Remote (USA) | 1 | ❌ No | 4% | <a href="https://jobs.ashbyhq.com/handshake/1c09f77c-f51f-43b2-913a-dc58d3aa68d8"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-02-23 · 7 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| ML Research Engineer, Interpretable AI for End-to-End Automated Driving | Toyota Research Institute | Los Altos, CA | Not specified | ❌ No | 26% | <a href="https://jobs.lever.co/tri/84dfcb59-8368-481c-acdb-50df883eadd4"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Recruiter, AI/ML Research | OpenAI | San Francisco | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/openai/ed871ac9-44ae-47fa-beaa-b9ab7ff31012"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer — GPU Networking & Distributed Systems | Baseten | San Francisco | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/baseten/1f7d7fda-5540-4205-890b-cdbf774f0814"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Forward Deployed Engineer - ML | Modal | New York | 2 | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/modal/9fadb51f-ce11-41b1-84d5-470e66cc8ee9"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, New Grad | 8VC | San Francisco, CA | 0-2 | ❌ No | 7% | <a href="https://jobs.ashbyhq.com/8vc/4fea7270-2409-4701-b147-fc961d95588d"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Bioinformatics Software Engineer | Harvard University | Boston, MA, United States | Not specified | ❌ No | 4% | <a href="https://jobs.smartrecruiters.com/HarvardUniversity/3743990011801881"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Power Systems Engineer | ALTEN Technology | Pittsburgh, Pennsylvania, United States | Not specified | ❌ No | 4% | <a href="https://job-boards.greenhouse.io/altentechnologyusa/jobs/5057906007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-02-21 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer | PermitFlow | New York City, NY | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/permitflow/8d780d11-57e8-4570-a599-b8dc3d4377a1"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-02-20 · 13 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Data Analyst | Clay | New York | 2 | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/claylabs/31d3597f-400e-4c12-9692-a5fb6f5e0d03"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Scientific Software Engineer- Shuttle Compilation | QuEra Computing | Boston, MA USA | Not specified | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/queracomputinginc/jobs/5128197008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Applied AI Strategist, New Ventures | Valon | Remote | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/Valon/7dbac7a9-78bd-4a27-b057-e39cd5124a2d"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Scientific Software Engineer - Hardware Compilation | QuEra Computing | Boston, MA USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/queracomputinginc/jobs/5128092008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer (Golang backend) | Verneek | New York, New York, United States | Not specified | ❌ No | 11% | <a href="https://jobs.workable.com/view/jmGk9zdyAh7W6itdCGjXzy/software-engineer-(golang-backend)-in-new-york-at-verneek"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI / Video Engineer | Uare.ai | Los Altos, CA | Not specified | ❌ No | 7% | <a href="https://job-boards.greenhouse.io/uareai/jobs/4140560009"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Data Specialist - Farsi | RWS | Tashkent | Not specified | ❌ No | 7% | <a href="https://jobs.lever.co/rws/8b9e8d0f-645e-4084-8d59-f5e58fcc0fbb"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Data Specialist - Polish | RWS | Warsaw | Not specified | ❌ No | 7% | <a href="https://jobs.lever.co/rws/7a524781-6bda-4b0c-bba5-980be1587772"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Data Specialist - Russian | RWS | Bukhara | Not specified | ❌ No | 7% | <a href="https://jobs.lever.co/rws/e73419d1-7720-48dc-892a-e384b8cf6667"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Data Specialist - Slovak | RWS | Bratislava | Not specified | ❌ No | 7% | <a href="https://jobs.lever.co/rws/e581ee4a-db1a-4de3-9fee-c2550f142557"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Data Specialist - Swedish | RWS | Stockholm | Not specified | ❌ No | 7% | <a href="https://jobs.lever.co/rws/8636c284-ef55-4336-bc0c-5449e334c175"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Data Specialist - Turkish | RWS | Sofia | Not specified | ❌ No | 7% | <a href="https://jobs.lever.co/rws/98a26563-10a6-4efd-a97e-06f215ed19be"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer (New Grads) | Giga AI | New York | Not specified | ❌ No | 7% | <a href="https://jobs.ashbyhq.com/gigaml/7314c5c1-e3d0-4439-ad9f-b3b09d4dde51"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-02-19 · 9 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer, (L2) CDP | Twilio | Remote - US | Not specified | ❌ No | 26% | <a href="https://job-boards.greenhouse.io/twilio/jobs/7602727"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| ML Research Scientist, Prediction & Smart Agents | Nuro | Mountain View, California (HQ) | 2 | ❌ No | 22% | <a href="https://nuro.ai/careersitem?gh_jid=7439020"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer I (Backend) | Whoop | Boston, MA | Not specified | ❌ No | 22% | <a href="https://jobs.lever.co/whoop/3b94218d-3a5a-4dd1-91c7-5f18655c93a8"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Backend | Sola | New York City | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/sola/8ae775b2-e137-4d93-8d54-4ce876c7afe0"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Offboard Infrastructure | Nuro | Mountain View, California (HQ) | 2 | ❌ No | 19% | <a href="https://nuro.ai/careersitem?gh_jid=7638789"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Development Engineer in Test, Platform Safety Assurance | Zoox | Foster City, CA | Not specified | ❌ No | 15% | <a href="https://jobs.lever.co/zoox/8914da26-af12-40ce-8819-bfc9fbf98cf2"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Observability | OpenAI | San Francisco | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/openai/d4dcd344-40cf-44d6-a7dd-172118eb0842"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Trainer: Code Generation | Creatify | Palo Alto, CA | Not specified | ❌ No | 7% | <a href="https://jobs.ashbyhq.com/embedding-vc/5b38ad5c-ea98-46af-92e9-b4e01f746c41"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Backend Engineer | Rescale | Remote (United States) | 2 | ❌ No | 7% | <a href="https://jobs.ashbyhq.com/rescale/ef94f670-e2df-4d4f-97ae-26cc9a5befdc"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-02-18 · 7 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Frontend Software Engineer, Codex App | OpenAI | San Francisco | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/openai/5f6685ad-2fba-4e60-8982-fa142b33e194"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| ML Infrastructure Engineer | AppLovin | Palo Alto, CA | 2 | ❌ No | 22% | <a href="https://boards.greenhouse.io/applovin/jobs/4655740006?gh_jid=4655740006"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer | Mechanize | San Francisco | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/mechanize/1ef28bb2-6251-4da6-a590-a4a7606368cb"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Research Data Scientist | Swayable | Remote | Not specified | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/swayable/jobs/5056114007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Research Data Scientist | Swayable | SF | Not specified | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/swayable/jobs/5056112007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Codex App | OpenAI | San Francisco | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/openai/60e52bb7-3418-447c-8767-a6bb8e7dedd8"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Frontend Engineer | Verneek | New York, New York, United States | Not specified | ❌ No | 7% | <a href="https://jobs.workable.com/view/eSsRVhFq19TaZQmjQS1FLz/frontend-engineer-in-new-york-at-verneek"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-02-17 · 5 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Data Science Analyst | Tatari | San Francisco, California, United States | 2 | ❌ No | 26% | <a href="https://job-boards.greenhouse.io/tatari/jobs/8350484002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Science Analyst | Tatari | Los Angeles, California, United States | 2 | ❌ No | 26% | <a href="https://job-boards.greenhouse.io/tatari/jobs/8350482002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Cloud Software Engineer, Backend - Enterprise | TP-Link Systems Inc. | Irvine, California, United States | Not specified | ❌ No | 15% | <a href="https://jobs.workable.com/view/trZ6MZgmnpu3fXdoW5vrdc/cloud-software-engineer%2C-backend---enterprise-in-irvine-at-tp-link-systems-inc."><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer Grad | Pure Storage | Santa Clara, California | Not specified | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/purestorage/jobs/7258968"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Founding Engineer (AI-Native) | AI Fund | San Francisco, California | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/AIFund/3606216b-19c1-4a8d-8602-f830f5e75997"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-02-16 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| The Ride Platform - AI Data Engineer | The Ride Platform | Austin, Texas, United States | Not specified | ❌ No | 11% | <a href="https://jobs.workable.com/view/cqN5W2YETLk3eeEVuBQLzP/the-ride-platform---ai-data-engineer-in-austin-at-the-ride-platform"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-02-13 · 4 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Machine Learning Engineer - Computer Vision | CaseGuard | Arlington, VA | Not specified | ❌ No | 70% | <a href="https://job-boards.greenhouse.io/caseguard/jobs/5120675008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Research Scientist - 3D Vision and Generation, Self-Driving | Applied Intuition | Sunnyvale | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/applied/26947f44-f658-4999-8ed8-77320ef458de"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Forward Deployed Software Engineer | Hive | San Francisco | 1 | ❌ No | 15% | <a href="https://jobs.lever.co/hive/e91c1a5a-fd0d-434e-a912-017e6231ce50"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Research Data Scientist | Swayable | NYC | Not specified | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/swayable/jobs/5053179007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-02-12 · 5 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Application Software Engineer, Data | SpaceX | Starbase, TX | 2 | ❌ No | 41% | <a href="https://boards.greenhouse.io/spacex/jobs/8420526002?gh_jid=8420526002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Full Stack Software Engineer (Components) | SpaceX | Hawthorne, CA | 2 | ❌ No | 22% | <a href="https://boards.greenhouse.io/spacex/jobs/8421359002?gh_jid=8421359002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Research Scientist - Simplex | Astera | Emeryville HQ | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/astera/ddd85583-1890-42c0-9505-775c03606789"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Devops Engineer, Federal | Cognition | Washington DC | 2 | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/cognition/589326d3-9dc0-447e-ae0c-972b808f831d"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| System Software Engineer - GCC/LLVM compiler, tooling, and ecosystem | Canonical | Home Based - Americas | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/canonical/jobs/7612825"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-02-11 · 5 roles · 2 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Applied Scientist- Pricing, Dynamic Pricing & Offer Selection | Lyft | New York, NY | 2 | ✅ Yes | 19% | <a href="https://app.careerpuck.com/job-board/lyft/job/8403370002?gh_jid=8403370002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Applied Scientist- Pricing, Dynamic Pricing & Offer Selection | Lyft | San Francisco, CA | 2 | ✅ Yes | 19% | <a href="https://app.careerpuck.com/job-board/lyft/job/8402813002?gh_jid=8402813002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer – Autonomy Stack | Applied Intuition | Sunnyvale | 2 | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/applied/cac3c985-67a6-4268-a398-a5430529abb3"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Analytics & AI Intern / Analyst - Castle Park Investments | Castle Park Investments, LLC | New York, New York, United States | Not specified | ❌ No | 19% | <a href="https://jobs.workable.com/view/f3hDYBNf2SbJbTzXToNVbB/data-analytics-%26-ai-intern-%2F-analyst---castle-park-investments-in-new-york-at-castle-park-investments%2C-llc"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| People Team Intern - HR Operations & AI Innovation (Fall 2026) | Cloudflare | In-Office | Not specified | ❌ No | 19% | <a href="https://boards.greenhouse.io/cloudflare/jobs/7606240?gh_jid=7606240"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-02-10 · 4 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Data Scientist | Solace Health | United States | Not specified | ❌ No | 44% | <a href="https://jobs.ashbyhq.com/solace/94e34d8e-264f-4cd6-a3d8-12492aa3c203"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Engineer | qode.world | New Jersey, New Jersey, United States | Not specified | ❌ No | 15% | <a href="https://apply.workable.com/j/12BA4B7B0E"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Platform Engineer | Defense Unicorns | Remote, United States | Not specified | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/defenseunicorns/jobs/5049314007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Forward Deployed Autonomous Systems Engineer | Mach Industries | Huntington Beach, CA | 2 | ❌ No | 7% | <a href="https://jobs.ashbyhq.com/mach/9b244fc7-5bcc-4bc8-917f-81f73a04ba9d"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-02-08 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer (New Grads) | Giga AI | San Francisco | Not specified | ❌ No | 7% | <a href="https://jobs.ashbyhq.com/gigaml/cb74c445-322b-47fc-804c-b0565e18ca3a"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-02-07 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Site Reliability Engineer II | Illumio | Sunnyvale, California - HQ | 2 | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/illumio/e76ff883-448c-40ff-9b7a-121075b3d289"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Creator — Video & Generative Media | Creatify Lab | Mountain View | 1 | ❌ No | 4% | <a href="https://jobs.ashbyhq.com/creatify/fa1a7606-6703-4fd5-a6a4-c7fa07e22cb9"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-02-06 · 3 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Machine Learning Engineer, Distributed Data Systems - Robotics | OpenAI | San Francisco | Not specified | ❌ No | 30% | <a href="https://jobs.ashbyhq.com/openai/4a13c764-18c3-4076-ac87-29e05491be07"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Human Data Interface | Anthropic | San Francisco, CA \| New York City, NY | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/anthropic/jobs/5109273008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Onboarding Specialist | Podium | Lehi, Utah | 2 | ❌ No | 7% | <a href="https://job-boards.greenhouse.io/podium81/jobs/7597038"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-02-05 · 9 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| AI/CAD Software Engineer | Falcomm | Atlanta, Georgia, United States | 2 | ❌ No | 41% | <a href="https://apply.workable.com/j/B282B3FABB"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| ML Ops Engineer, Machine Learning & AI | The New York Times | New York, NY | 2 | ❌ No | 41% | <a href="https://job-boards.greenhouse.io/thenewyorktimes/jobs/4655096005"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, GPU Infrastructure - HPC | OpenAI | San Francisco | Not specified | ❌ No | 30% | <a href="https://jobs.ashbyhq.com/openai/f58cb1eb-9642-4a4d-a14d-d7a57d583a11"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Identity Infrastructure Engineering | OpenAI | San Francisco | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/openai/551b0d0d-46c2-42fb-bb05-46e2fba8d4db"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/CAD Software Engineer | Falcomm | Atlanta, Georgia, United States | Not specified | ❌ No | 19% | <a href="https://jobs.workable.com/view/c4s9H7bUwQP8wrKTUjpV4B/ai%2Fcad-software-engineer-in-atlanta-at-falcomm"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Full-Stack + AI Engineer | Alchemy Worx | New York, New York, United States | Not specified | ❌ No | 19% | <a href="https://jobs.workable.com/view/4f5yBwDwVJnrM3KZPDKvUc/full-stack-%2B-ai-engineer-in-new-york-at-alchemy-worx"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| New Graduate Software Engineer - Sunnyvale | Cerebras Systems | Sunnyvale | 0-2 | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/earlytalentcerebras/jobs/7621174003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer Internship - Sunnyvale | Cerebras Systems | Sunnyvale | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/earlytalentcerebras/jobs/7621006003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Technical Solutions Engineer - Cloud, Hyperscalers and AI networks | Arista Networks | Santa Clara, CA, United States | Not specified | ❌ No | 4% | <a href="https://jobs.smartrecruiters.com/AristaNetworks/744000107618375"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-02-04 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| 1.10 Software Engineer, Human-Robot Interaction | Field AI | Boston, MA | Not specified | ❌ No | 15% | <a href="https://jobs.lever.co/field-ai/d702dd2b-3acd-4b0d-865a-e973a2f6ea90"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-02-03 · 8 roles · 1 H-1B sponsor match

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Backend Engineer, Payments and Risk | Stripe | US | 2 | ✅ Yes | 22% | <a href="https://stripe.com/jobs/search?gh_jid=7232592"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Application Software Engineer | SpaceX | Redmond, WA | 2 | ❌ No | 26% | <a href="https://boards.greenhouse.io/spacex/jobs/8402778002?gh_jid=8402778002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Frontend Engineer, ChatGPT Engineering | OpenAI | San Francisco | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/openai/5bde9af5-df78-460e-ae9c-5c49ac778640"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Machine Learning Scientist I/II, Multi-Modal Scientific Reasonings | Lila Sciences | Cambridge, MA USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/lilasciences/jobs/4116672009"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Robotics AI Engineer – Calibration, Localization, and Mapping | Field AI | Irvine, CA | Not specified | ❌ No | 15% | <a href="https://jobs.lever.co/field-ai/ca85d200-ee59-4d7f-93ac-655e7077b398"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer 3, Atlas Search Systems | MongoDB | San Francisco | 2 | ❌ No | 15% | <a href="https://www.mongodb.com/careers/job/?gh_jid=7523920"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, AI & Developer Acceleration | Cartesia | *HQ - San Francisco, CA | 2 | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/cartesia/cdf453af-7035-45f6-a93c-5cacd332d31e"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Content Creator & Social Strategist | Box | Redwood City, California | Not specified | ❌ No | 7% | <a href="https://job-boards.greenhouse.io/boxinc/jobs/7586013"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-02-02 · 4 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Backend Software Engineer, GNC (Starlink) | SpaceX | Redmond, WA | 2 | ❌ No | 19% | <a href="https://boards.greenhouse.io/spacex/jobs/8398679002?gh_jid=8398679002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Applied AI / ML Scientist - Ads Bidding | Faire | San Francisco, CA | 2 | ❌ No | 15% | <a href="https://boards.greenhouse.io/faire/jobs/8400765002?gh_jid=8400765002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer II (Backend, Business Systems) | Whoop | Boston, MA | 2 | ❌ No | 15% | <a href="https://jobs.lever.co/whoop/ce1d5c5e-3fda-4884-8135-d98dce39877b"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| DevOps Engineer | Freedom Technology Solutions Group | Annapolis Junction, MD | Not specified | ❌ No | 7% | <a href="https://job-boards.greenhouse.io/freedomconsulting/jobs/5040789007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-01-30 · 6 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Helix AI Engineer, Robot Learning | Figure | San Jose, CA | Not specified | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/figureai/jobs/4649851006"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Full Stack Software Engineer, Growth | OpenAI | San Francisco | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/openai/77bc0b3a-35c1-4ecf-99c7-1b3b19d959ca"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Engineer | qode.world | New Jersey, New Jersey, United States | Not specified | ❌ No | 15% | <a href="https://apply.workable.com/j/93348C2C62"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Engineer | qode.world | New Jersey, New Jersey, United States | Not specified | ❌ No | 15% | <a href="https://apply.workable.com/j/407642AB47"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Developer Relations | Exa Labs | San Francisco, California | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/exa/22804c28-3daa-48b5-afc9-d048132482bf"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Healthcare Data Analyst | Scalepex | Dallas, Texas, United States | Not specified | ❌ No | 7% | <a href="https://jobs.workable.com/view/v1U9o5MPD2ERFSTbTZMgj2/remote-healthcare-data-analyst-in-dallas-at-scalepex"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-01-29 · 5 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer, Fundamental Research Tools | Point72 | New York | Not specified | ❌ No | 22% | <a href="https://boards.greenhouse.io/point72/jobs/8377045002?gh_jid=8377045002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Site Reliability Engineer | Astera | Emeryville HQ | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/astera/413b72ac-e039-4627-8f12-7659954a4a15"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer - MeritFirst | 8VC | Austin, TX | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/8vc/143acb7e-6342-48b3-9310-9caa68db9307"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Power Systems Controls (Starlink) | SpaceX | Redmond, WA | 2 | ❌ No | 11% | <a href="https://boards.greenhouse.io/spacex/jobs/8395307002?gh_jid=8395307002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer - Android | ether.fi | Dubai | Not specified | ❌ No | 7% | <a href="https://jobs.ashbyhq.com/ether.fi/d4c8f715-15da-42d5-bee6-083e80ea8414"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-01-28 · 4 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Data Engineer, Analytics Data Products | The New York Times | New York, NY | 2 | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/thenewyorktimes/jobs/4653104005"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Replit Cloud | Replit | Foster City, CA | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/replit/7fa1826e-d7fd-4837-8485-97de895ba7fc"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Infrastructure Administrator I, Cloud AI | Illumio | HQ - Sunnyvale (Office) | 1 | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/illumio/fd85f4f7-77df-4a65-933e-152203bf0576"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Web Application Developer | Latitude | Orlando, FL | Not specified | ❌ No | 7% | <a href="https://jobs.lever.co/latitudeinc/6bff1276-d68a-4923-be13-28d92dea5b72"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-01-27 · 5 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer, Machine Learning Platform | The New York Times | New York, NY | 2 | ❌ No | 41% | <a href="https://job-boards.greenhouse.io/thenewyorktimes/jobs/4653129005"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Fullstack | Sola | New York City | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/sola/0c859bfa-c3e1-429d-876d-0542f5358c17"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, ML Infrastructure | Cursor | San Francisco | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/cursor/c66cde5e-9cb6-4a2e-a330-9323e1edf2a9"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Research Scientist | Cursor | San Francisco | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/cursor/cd4bad0a-e2f6-4a8d-9b57-ce1780efedae"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, ML Research | Cursor | San Francisco | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/cursor/0aa0650b-f93c-416e-9e2f-4fdf1556fd14"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-01-26 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| AI Scientist, BioMedical AI | Xaira Therapeutics | South San Francisco, California, United States | Not specified | ❌ No | 26% | <a href="https://job-boards.greenhouse.io/xairatherapeutics/jobs/4987432007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Frontend Engineer | Aleph | Americas | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/aleph/00b1e5f7-146f-4f95-8fa3-286de1d1bd1d"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-01-25 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| AI GTM, Fellowship Program | Obvious | Atlanta, GA | 1 | ❌ No | 7% | <a href="https://jobs.ashbyhq.com/obvious/32e103bf-5782-4b27-922a-eb964672dc70"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-01-24 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer, Enterprise | Replit | Foster City, CA | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/replit/b7f12834-78d2-424d-bf83-0c942815fbf7"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-01-23 · 16 roles · 1 H-1B sponsor match

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| ML Infra Engineer (TPU/Jax/Optimization) | Physical Intelligence | San Francisco | Not specified | ✅ Yes | 22% | <a href="https://jobs.ashbyhq.com/physicalintelligence/4e547c5a-e4ee-40a7-b14b-c4daf9c072eb"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Applied Scientist- AI/ML Intern | Wealth.com | Remote, United States | 1 | ❌ No | 37% | <a href="https://jobs.ashbyhq.com/wealth-com/1899d513-4c4a-43b2-a307-8c8e4b877622"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Analyst / Associate Data Scientist | Integra FEC | Austin, Texas | 2 | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/integra/jobs/5083082008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Full Stack Engineer - Python+React | Creative Chaos | United States | Not specified | ❌ No | 19% | <a href="https://jobs.workable.com/view/dSNx9gJPWG3F6ZYCYBFRq3/remote-full-stack-engineer---python%2Breact-in-united-states-at-creative-chaos"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Research - Human Data | OpenAI | San Francisco | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/openai/4d6a5951-9838-434c-830a-22cb938ea228"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Analyst | Arcana | Coimbatore/Bangalore/Remote | Not specified | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/arcanaanalytics/jobs/4110676009"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform Systems | OpenAI | San Francisco | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/openai/5e4ed6d1-2417-4bf5-bae0-905931c488e3"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Research Scientist I/II, AI for Process Engineering | Lila Sciences | Cambridge, MA USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/lilasciences/jobs/4110163009"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Data Specialist - Armenian | RWS | Tbilisi | Not specified | ❌ No | 7% | <a href="https://jobs.lever.co/rws/ef2f95b6-8ff8-45c2-9126-d77baee053af"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Data Specialist - Estonian | RWS | Tallinn | Not specified | ❌ No | 7% | <a href="https://jobs.lever.co/rws/0c672c6a-9cf6-429b-b892-a2916743ff06"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Data Specialist - Finnish | RWS | Helsinki | Not specified | ❌ No | 7% | <a href="https://jobs.lever.co/rws/6ae45dac-02be-4300-b11d-b93a3fe9f116"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Data Specialist - Georgian | RWS | Tbilisi | Not specified | ❌ No | 7% | <a href="https://jobs.lever.co/rws/54bce139-73f9-4a81-a56d-a83f9bf0ac6d"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Data Specialist - Icelandic | RWS | Reykjavik | Not specified | ❌ No | 7% | <a href="https://jobs.lever.co/rws/258dae74-9b32-42ff-98a4-1c8860749fb3"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Data Specialist - Latvian | RWS | Riga | Not specified | ❌ No | 7% | <a href="https://jobs.lever.co/rws/c66d3e2b-e682-4760-aca4-b68b1d750c34"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Data Specialist - Oromo | RWS | Nairobi | Not specified | ❌ No | 7% | <a href="https://jobs.lever.co/rws/85b64ace-32f0-4347-b6ad-6797857d67d1"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, GPU | Waymo | Mountain View, CA, USA; New York, NY, USA | Not specified | ❌ No | 7% | <a href="https://careers.withwaymo.com/jobs?gh_jid=7554830"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-01-22 · 4 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer, Machine Learning | Roku | San Jose, California | 1 | ❌ No | 30% | <a href="https://www.weareroku.com/jobs/7555263?gh_jid=7555263"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Generative AI Researcher Intern | Meshy | Shanghai | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/meshy/00b6328d-8c32-4b91-aafa-51434e965f37"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Backend Engineer, Domains Registrar | Squarespace | Aveiro | 2 | ❌ No | 19% | <a href="http://www.squarespace.com/about/careers?gh_jid=7557125"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Onboarding Specialist - Automotive | Podium | Lehi, Utah | 2 | ❌ No | 7% | <a href="https://job-boards.greenhouse.io/podium81/jobs/7557676"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-01-21 · 6 roles · 1 H-1B sponsor match

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer - SnowConvert AI | Snowflake | US-CA-Menlo Park | Not specified | ✅ Yes | 22% | <a href="https://jobs.ashbyhq.com/snowflake/2a928b93-a5d4-4285-a92c-032fb389faa2"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Machine Learning Engineer (Foundation Models & Personalization) | Eight Sleep | San Francisco | 2 | ❌ No | 37% | <a href="https://jobs.ashbyhq.com/eightsleep/ef81d491-6991-49f7-8195-d3de86d951b0"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Early Career AI/ML Engineer | Brain Co. | San Francisco Bay Area | 2 | ❌ No | 33% | <a href="https://jobs.ashbyhq.com/brainco/bb6e555b-8bb1-4cd7-9813-4f82a5ebe839"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform Infrastructure | Verkada | San Mateo, CA United States | 1 | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/verkada/jobs/5029725007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Strategist (All Levels) | Distyl | San Francisco | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/distyl/18ce7c79-a1d5-4c87-8ae0-dc71d5623ddd"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Avionics Systems Engineer (Starship) | SpaceX | Hawthorne, CA | 1 | ❌ No | 7% | <a href="https://boards.greenhouse.io/spacex/jobs/8377628002?gh_jid=8377628002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-01-20 · 5 roles · 1 H-1B sponsor match

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer - APG | Snowflake | US-CA-Menlo Park | 2 | ✅ Yes | 26% | <a href="https://jobs.ashbyhq.com/snowflake/5f4ae8d3-bf84-430d-8f9f-325f14ddf947"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Core Product | Ramp | New York, NY (HQ) | 2 | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/ramp/5fe4c64e-9336-4384-9e6f-ff32eeb3fdae"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Frontend Engineer, Financial Web Platform | OpenAI | San Francisco | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/openai/192980b8-b874-4493-a8c1-f7d5660f00f3"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Junior Full Stack Engineer ($250k - $300k salary) | Baton Corporation | New York | 0-2 | ❌ No | 7% | <a href="https://jobs.ashbyhq.com/batoncorporation/bb3ab630-5e59-48b5-9794-00a225879a66"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Facilities Infrastructure Engineer | SpaceX | Hawthorne, CA | 1 | ❌ No | 4% | <a href="https://boards.greenhouse.io/spacex/jobs/8381785002?gh_jid=8381785002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-01-18 · 3 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer – Performance Profiling | Etched.ai | San Jose | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/Etched/610c3836-9798-46ea-931a-02bb95b29467"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, ML Data Systems | Cursor | San Francisco | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/cursor/8d07fe0f-34aa-458b-88e8-091469a963dc"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Quantum Scientist - Machine Learning and Quantum Error Correction | QuEra Computing | Boston, MA, USA | Not specified | ❌ No | 4% | <a href="https://job-boards.greenhouse.io/queracomputinginc/jobs/5075843008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-01-16 · 6 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Research Engineer, Economic Research Data Platform | Anthropic | San Francisco, CA | Not specified | ❌ No | 26% | <a href="https://job-boards.greenhouse.io/anthropic/jobs/5071132008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Research Engineer/Research Scientist, Audio | Anthropic | San Francisco, CA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/anthropic/jobs/5074815008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Junior Software Engineer | mthree | USA | 0-2 | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/mthreerecruitingportal/jobs/4622899006"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Core Software Engineer (C++) - Remote | ClickHouse | United States (remote) | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/clickhouse/jobs/5755093004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer (Frontend) | Latent | San Francisco | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/latent/c54c96d7-2776-41be-b74c-b2beaad99634"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Localization, Calibration & Mapping | AeroVect | Remote | 2 | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/AeroVect/73a42f00-af59-4439-8ff5-531b7c355745"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-01-15 · 5 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| AI Researcher - Thorin | 8VC | San Francisco, CA | Not specified | ❌ No | 30% | <a href="https://jobs.ashbyhq.com/8vc/28fa497f-a408-4555-a786-2a6b264d4bf7"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Science Intern | Faire | San Francisco, CA | Not specified | ❌ No | 19% | <a href="https://boards.greenhouse.io/faire/jobs/8376377002?gh_jid=8376377002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Network Performance & Reliability | Cloudflare | Hybrid | Not specified | ❌ No | 15% | <a href="https://boards.greenhouse.io/cloudflare/jobs/7446310?gh_jid=7446310"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Quality Systems Engineer (Starlink Aviation) | SpaceX | Woodinville, WA | 1 | ❌ No | 7% | <a href="https://boards.greenhouse.io/spacex/jobs/8372252002?gh_jid=8372252002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Analyst, Data & Analytics | Atria Health and Research Institute | New York, New York, United States | Not specified | ❌ No | 4% | <a href="https://jobs.workable.com/view/dxW3YVUZpXNYb75SWxyd7n/data-analyst%2C-data-%26-analytics-in-new-york-at-atria-health-and-research-institute"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-01-14 · 8 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer, Backend (New-York) | Mistral AI | New York | Not specified | ❌ No | 26% | <a href="https://jobs.lever.co/mistral/f2e8ba75-bf5a-4976-bb96-c5d3e0f99366"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Kernel Driver Software Engineer | Etched.ai | San Jose | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/Etched/283c88a9-0031-4232-a5b3-1103c2af4100"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Computer Vision Engineer (C++) | Shield AI | Melbourne | Not specified | ❌ No | 19% | <a href="https://jobs.lever.co/shieldai/2cfe6692-a266-4d27-8832-ef652fa57ee4"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Engineer - Delivery | Beghou Consulting | Hyderabad, Telangana | 2 | ❌ No | 19% | <a href="https://jobs.lever.co/beghouconsulting/f36a3ca5-5457-4619-a064-05af607d0a6f"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Biological Safety Research Scientist | Anthropic | San Francisco, CA | Not specified | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/anthropic/jobs/5066977008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Forward Deployed Engineer - Software Engineer | ElevenLabs | San Francisco | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/elevenlabs/6c4c57c1-ec72-42ba-af3a-eb7aebbde2e6"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Machine Learning Engineer | Tiger Analytics Inc. | Plano, Texas, United States | Not specified | ❌ No | 15% | <a href="https://jobs.workable.com/view/8vGP48rmjhGSV9EtyYXRag/hybrid-machine-learning-engineer-in-plano-at-tiger-analytics-inc."><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Backend Engineer | Bevel | New York | 2 | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/Bevel/3d4b2b63-a119-4917-89da-f9ceb365dab1"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-01-13 · 8 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Machine Learning PhD Intern, Economics (Fall) | Instacart | United States - Remote | Not specified | ❌ No | 33% | <a href="https://instacart.careers/job/?gh_jid=7532267"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Research Scientist - Agents | Institute of Foundation Models | Sunnyvale, CA | 2 | ❌ No | 30% | <a href="https://jobs.lever.co/ifm-us/9ae2a6dc-39bd-4dbe-aa0b-d99e656f8b04"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| ML Research Engineer - Hardware Codesign | OpenAI | San Francisco | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/openai/5931abef-191b-417e-89f1-1d06f00e908c"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Engineer - Delivery | Beghou Consulting | Hyderabad, Telangana | 2 | ❌ No | 19% | <a href="https://jobs.lever.co/beghouconsulting/bd1d1550-21aa-4970-b1c9-fe983dcd2886"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Scientist | Point72 | Chicago, New York | Not specified | ❌ No | 19% | <a href="https://boards.greenhouse.io/point72/jobs/8372544002?gh_jid=8372544002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Site Reliability Engineer | Wheely | Λευκωσία, Nicosia, Cyprus | Not specified | ❌ No | 19% | <a href="https://boards.greenhouse.io/wheely/jobs/7588282003?gh_jid=7588282003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Security Infrastructure Engineer | Tailscale | Remote (United States) | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/tailscale/jobs/4648933005"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Security Software Engineer | Tailscale | Remote (United States) | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/tailscale/jobs/4648916005"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-01-12 · 4 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Backend Engineer - Seattle | Revefi | Seattle, WA | 2 | ❌ No | 19% | <a href="https://jobs.lever.co/revefi/6eddfb74-7ad4-4fcb-bcfa-6ebb435dc9ab"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer | Pivot Robotics | San Francisco | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/pivotrobotics/75fa67bb-a087-47d4-aa5c-3aec0a17f1b1"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Applied AI Engineer | Ramp | New York, NY (HQ) | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/ramp/d204e136-2749-42de-82b4-88a0dd352090"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Founding Applied AI Engineer | Wilson | San Francisco | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/wilson/901651b2-76a5-4d4c-a3a7-f0d9453c7389"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-01-09 · 7 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Full-Stack Engineer, AI Data Platform | Labelbox | San Francisco Bay Area | 2 | ❌ No | 41% | <a href="https://job-boards.greenhouse.io/labelbox/jobs/5019254007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Generative AI - 3D Foundation Model | Meshy | Shanghai | Not specified | ❌ No | 33% | <a href="https://jobs.ashbyhq.com/meshy/32cd6686-606b-462c-a64f-00e56b595637"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Codex Enterprise | OpenAI | San Francisco | Not specified | ❌ No | 26% | <a href="https://jobs.ashbyhq.com/openai/89f58eb2-519f-4a36-8be0-2e594724e1bc"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Applied AI Engineer | Luminai | SF Bay Area | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/luminai/4b580dd6-0675-4f55-86c7-6d694285b6d8"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Embedded UI | Roku | San Jose, California | Not specified | ❌ No | 19% | <a href="https://www.weareroku.com/jobs/7527300?gh_jid=7527300"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer II (Backend, Growth) | Whoop | Boston, MA | Not specified | ❌ No | 15% | <a href="https://jobs.lever.co/whoop/ec4522b6-8ffc-44f0-801c-c7cd47d25d5b"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Generative AI - Graphics Engineer | Meshy | Shanghai | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/meshy/1806f5d3-9f34-4e7e-8238-4e53fc4e579b"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-01-08 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer, Productivity - Training Runtime | OpenAI | San Francisco | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/openai/c02b35b2-af37-4740-a702-2ed3b5dc3cf1"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-01-07 · 5 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer, Model Performance Systems | Baseten | San Francisco | Not specified | ❌ No | 30% | <a href="https://jobs.ashbyhq.com/baseten/75d7beac-0298-40fa-b206-2e0c0c08a64f"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer (All Levels) | Fieldguide | San Francisco, CA or Remote (USA) | Not specified | ❌ No | 26% | <a href="https://jobs.ashbyhq.com/fieldguide/47a2afc4-1075-4378-83bb-714543b6c272"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Cooperative AI | OpenAI | San Francisco | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/openai/7613aca3-9dd8-41cd-b114-06ef4de967a9"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer | Socket | United States | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/socket/a1be82e9-bbe4-44ad-b05a-c03075e47af1"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Engineer | Cooperidge Consulting Firm | San Francisco, California, United States | Not specified | ❌ No | 7% | <a href="https://jobs.workable.com/view/nscUhpK7CGFN3QdUgAY9fu/ai-engineer-in-san-francisco-at-cooperidge-consulting-firm"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-01-06 · 4 roles · 1 H-1B sponsor match

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Robotics Software Engineer | Physical Intelligence | San Francisco | Not specified | ✅ Yes | 15% | <a href="https://jobs.ashbyhq.com/physicalintelligence/f6bee7a7-57ae-4ec1-9276-ae3bcbdc7327"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Full-Stack Software Engineer (New Grad) – Remote | SpruceID | REMOTE | 0-2 | ❌ No | 22% | <a href="https://jobs.lever.co/sprucesystems/c683a712-7a5a-4bed-b580-f899998f044a"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| DevOps Engineer - Infrastructure | Kodiak Robotics | Mountain View, CA | Not specified | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/kodiak/jobs/4090717009"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Founding AI Deployment Strategist | Dust | San Francisco | Not specified | ❌ No | 7% | <a href="https://jobs.ashbyhq.com/dust/c97de2e4-93e8-4c24-b237-61ff3b16ce3c"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-01-05 · 4 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Web3 / Full-stack Software Engineer | stakefish | United States | Not specified | ❌ No | 22% | <a href="https://jobs.workable.com/view/xrDqeUuM7zqVgji5kFVZgw/remote-web3-%2F-full-stack-software-engineer-in-united-states-at-stakefish"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Full-Stack Software Engineer – Remote | SpruceID | United States | 2 | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/spruceid/491c3062-8aae-425f-bcc7-9451ff180997"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Device - Software Engineer (Firmware) | Span | Bengaluru | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/span/fed58386-54fd-4e5f-ab22-9dc142d0bf8b"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Founding Account Executive - Rime Ai | Unusual | San Francisco Bay Area | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/unusual/f9330de7-e064-4788-9bd7-6ea97a419480"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-01-02 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Data Engineer | Solace Health | United States | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/solace/f19207b3-5fad-4cd4-9a7e-5dd64fb78401"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Avionics Systems Engineer (Starship) | SpaceX | Starbase, TX | 1 | ❌ No | 7% | <a href="https://boards.greenhouse.io/spacex/jobs/8356336002?gh_jid=8356336002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-12-31 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer | Aircall | Madrid Office | Not specified | ❌ No | 26% | <a href="https://jobs.lever.co/aircall/7eec7634-230e-4f21-a0b4-0e2da7e78f7f"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-12-30 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Power Systems Engineer (Starship Avionics) | SpaceX | Hawthorne, CA | 1 | ❌ No | 4% | <a href="https://boards.greenhouse.io/spacex/jobs/8355513002?gh_jid=8355513002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-12-27 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Founding Engineer (AI / ML) | Pax Historia | San Francisco | Not specified | ❌ No | 7% | <a href="https://jobs.ashbyhq.com/pax-historia/d497ab5f-a364-4bce-b7ae-5f2fe9c381c4"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-12-23 · 3 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Full-stack Software Engineer | Nick AI | United States | Not specified | ❌ No | 30% | <a href="https://jobs.workable.com/view/37quUoKsDu7UNMqPD8ZEYH/remote-full-stack-software-engineer-in-united-states-at-nick-ai"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Camera Software Engineer, Consumer Devices | OpenAI | San Francisco | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/openai/1dc05fc7-ceb7-4827-a905-9d1beb77a4a0"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer | Flint | San Francisco | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/flint/0f65ed4b-2de8-4603-8295-8c2ea9438a88"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-12-22 · 6 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Data Science Analyst | Tatari | New York, New York, United States | 2 | ❌ No | 26% | <a href="https://job-boards.greenhouse.io/tatari/jobs/8350483002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Scientist - Perception Verification and Validation | Zoox | Boston, MA | Not specified | ❌ No | 22% | <a href="https://jobs.lever.co/zoox/9ab192af-3480-40a7-9ff3-f81061ac6301"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Research Scientist, Dexterous Manipulation & Robot Learning | Lila Sciences | Cambridge, MA USA | Not specified | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/lilasciences/jobs/4087170009"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Scenario Modeling | Maybern | New York Office | 2 | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/maybern/0e6d43a6-a5f9-44fb-be3e-78a160a8fb11"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Blockchain Site Reliability Engineer | InfStones | Texas | Not specified | ❌ No | 15% | <a href="https://jobs.lever.co/infstones/193a69fc-5191-4042-841c-1f3cb08a9f53"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Scientist Fellow | Major League Baseball | Baltimore, MD | Not specified | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/baltimoreorioles/jobs/5742975004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-12-19 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Site Reliability Engineer | SingleStore | Seattle | 2 | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/singlestore/jobs/7432205"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Distributed Data Systems | Exa Labs | San Francisco, California | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/exa/5f10cc28-bcad-4ce4-8fa1-996a59c59e65"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-12-18 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Fluids Systems Engineer, Solar Cell Factory (Starlink) | SpaceX | Bastrop, TX | 2 | ❌ No | 4% | <a href="https://boards.greenhouse.io/spacex/jobs/8346155002?gh_jid=8346155002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-12-17 · 3 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| 2026 Fall Health AI Scholar, Digital Health Algorithms | Samsung Research America | 665 Clyde Avenue, Mountain View, CA, USA | Not specified | ❌ No | 26% | <a href="https://job-boards.greenhouse.io/samsungresearchamericainternship/jobs/8342576002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Routing | Nuro | Mountain View, California (HQ) | 2 | ❌ No | 22% | <a href="https://nuro.ai/careersitem?gh_jid=7482347"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Device Software Engineer, Gateway/Embedded Linux | Span | San Francisco | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/span/05030431-e289-4428-a55f-337fe69b559c"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-12-16 · 7 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| [2026] Data Scientist, Social | Roblox | San Mateo, CA, United States | 2 | ❌ No | 30% | <a href="https://careers.roblox.com/jobs/7463634?gh_jid=7463634"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Autonomy Engineer - Deep Learning | Skydio | San Mateo, California, United States | Not specified | ❌ No | 26% | <a href="https://jobs.ashbyhq.com/skydio/cc83824e-a1cd-4bc7-9206-7264da9fbd61"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Forward Deployed Marketing Data Scientist | Hightouch | Remote (North America) | Not specified | ❌ No | 26% | <a href="https://job-boards.greenhouse.io/hightouch/jobs/5718912004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Quantitative Evaluations | Waymo | Mountain View, CA, USA; San Francisco, CA, USA | 1 | ❌ No | 26% | <a href="https://careers.withwaymo.com/jobs?gh_jid=7466534"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Full Stack Software Engineer - 2026 Summer Intern | Symmetry Systems | Remote | Not specified | ❌ No | 19% | <a href="https://jobs.lever.co/SymmetrySystems/dbca271b-a99b-48ab-83f2-b596a037ad65"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| System Software Engineer, Consumer Devices | OpenAI | San Francisco | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/openai/20f525b7-f958-4c95-a055-f914ab3adb95"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Annotator for AI Models - Dutch in USA | RWS | Florida | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/rws/dc05ba5b-2d0f-49d6-87ba-40046d6aa158"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-12-15 · 9 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Autonomy Engineer Intern - Computer Vision/Deep Learning Fall 2026 | Skydio | San Mateo, California, United States | Not specified | ❌ No | 33% | <a href="https://jobs.ashbyhq.com/skydio/c84945f0-b8e0-4272-b636-265d6611a8eb"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Autonomy Software Engineer | Skydio | San Mateo, California, United States | 1 | ❌ No | 30% | <a href="https://jobs.ashbyhq.com/skydio/a48fe41b-030b-4f11-bf25-df7446151854"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Autonomy Engineer - Deep Learning Infrastructure | Skydio | San Mateo, California, United States | Not specified | ❌ No | 26% | <a href="https://jobs.ashbyhq.com/skydio/dcb04687-9b4f-425d-8c37-1111cf3ccf3d"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Autonomy Engineer - Deep Learning Model Acceleration | Skydio | San Mateo, California, United States | Not specified | ❌ No | 26% | <a href="https://jobs.ashbyhq.com/skydio/cd6d8410-419b-4713-8d4d-7eb72b134d5a"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Treasury | Lithic | Remote | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/lithic/jobs/5737189004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Annotator for AI Models - Italian in USA | RWS | Florida | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/rws/63092333-9a5d-4fe1-8072-aa8f4246bd6a"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Developer Productivity | Cursor | San Francisco | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/cursor/010063bd-6083-4fc0-a455-e6f0193b5347"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Backend Engineer - AI | Anything | San Francisco | Not specified | ❌ No | 4% | <a href="https://jobs.ashbyhq.com/anything/f4123aa5-855a-4b82-b762-66fb4a77f493"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Platform Engineer | Anything | San Francisco | Not specified | ❌ No | 4% | <a href="https://jobs.ashbyhq.com/anything/6af7ed92-2390-4ef8-a9b3-3be3935307c5"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-12-14 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Ground Systems Engineer I/II- Mechanical | Rocket Lab USA | Auckland, NZ | 1 | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/rocketlab/jobs/7554078003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-12-12 · 4 roles · 2 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Data Scientist, Algorithms, Optimization - Fulfillment | Lyft | New York, NY | 2 | ✅ Yes | 26% | <a href="https://app.careerpuck.com/job-board/lyft/job/8335733002?gh_jid=8335733002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Scientist, Algorithms, Optimization - Fulfillment | Lyft | Seattle, WA | 2 | ✅ Yes | 26% | <a href="https://app.careerpuck.com/job-board/lyft/job/8335715002?gh_jid=8335715002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Legal Specialist | Filevine | Bratislava | Not specified | ❌ No | 26% | <a href="https://jobs.lever.co/filevine/6f189fd8-dab4-441b-87df-9aeca90ecaec"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Deployment Strategist - Marseille | Mistral AI | Marseille | 2 | ❌ No | 19% | <a href="https://jobs.lever.co/mistral/0cde829a-c9b9-4ee1-827f-9bd30c1810fc"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-12-11 · 4 roles · 1 H-1B sponsor match

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Forward Deployed Software Engineer, Internship - US Government | Palantir | Honolulu, HI | Not specified | ✅ Yes | 19% | <a href="https://jobs.lever.co/palantir/315f695d-04d1-4a9a-848e-cb2bec7a997e"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| New Grad Software Engineer (Full Stack) | N1 | New York City | 0-2 | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/n1/73724fe2-9a93-4a60-b349-4fd3d2efa94a"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Perception Scaling Evaluation | Waymo | Mountain View, CA, USA; San Francisco, CA, USA | 2 | ❌ No | 11% | <a href="https://careers.withwaymo.com/jobs?gh_jid=7449712"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Analyst | RxSense | Princeton, NJ or Remote | 2 | ❌ No | 7% | <a href="https://job-boards.greenhouse.io/rxsense/jobs/4640025005"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-12-10 · 5 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer, Context Platform | Glean | Mountain View, CA | 1 | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/gleanwork/jobs/4638008005"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Applied Research Scientist | Cartesian | Cambridge, MA | Not specified | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/cartesiansystems/jobs/4076723009"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer Intern | Caddi | Seattle, Washington, United States | Not specified | ❌ No | 15% | <a href="https://jobs.workable.com/view/gGEiMa8iZUsKnGUcyB5VxT/software-engineer-intern-in-seattle-at-caddi"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Research Engineer – Machine Learning | Avride | Austin, TX | Not specified | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/avride/jobs/4075884009"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Strategy & Governance Leader | Accenture | Washington, DC | Not specified | ❌ No | 11% | <a href="https://boards.greenhouse.io/accenturefederalservices/jobs/4624780006?gh_jid=4624780006"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-12-09 · 3 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Quantum Software Engineer | Infleqtion | Chicago, Illinois, United States | Not specified | ❌ No | 33% | <a href="https://apply.workable.com/j/00EC28A7E5"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Machine Learning Engineer | Tiger Analytics Inc. | United States | Not specified | ❌ No | 15% | <a href="https://jobs.workable.com/view/s3oWU3nc483Jkxwgff7CfA/remote-machine-learning-engineer-in-united-states-at-tiger-analytics-inc."><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Quantum Software Engineer | Infleqtion | Chicago, Illinois, United States | Not specified | ❌ No | 11% | <a href="https://jobs.workable.com/view/c9qisBantgwr97xTnrS8Cm/hybrid-quantum-software-engineer-in-chicago-at-infleqtion"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-12-06 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer, Vehicle Platforms C++ | Waymo | Mountain View, CA, US | 2 | ❌ No | 11% | <a href="https://careers.withwaymo.com/jobs?gh_jid=7429873"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-12-05 · 3 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Data Scientist | Newton Research | Greater Boston Area | Not specified | ❌ No | 37% | <a href="https://job-boards.greenhouse.io/newtonresearch/jobs/5020783008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Power Systems Engineer, Energy Storage | Redwood Materials | San Francisco, California, United States | Not specified | ❌ No | 19% | <a href="https://boards.greenhouse.io/redwoodmaterials/jobs/5731003004?gh_jid=5731003004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Site Reliability Engineer | Latent | San Francisco | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/latent/bbd1a8e3-b943-4c8c-b239-e87951504f71"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-12-03 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer | Modern Treasury | San Francisco | 2 | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/moderntreasury/f2ff4c9c-0c2f-4bb8-b446-77cab281126a"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-12-02 · 3 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer II (Frontend), Social | Sony Interactive Entertainment | United States, San Diego, CA | 2 | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/sonyinteractiveentertainmentglobal/jobs/5712556004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Agent Software Engineer | Assort Health | San Francisco | 1 | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/assorthealth/753aba51-eddf-42f7-920f-e04d12d02515"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Workflow Engineer | Alpaca VC | New York, New York, United States | Not specified | ❌ No | 4% | <a href="https://jobs.workable.com/view/i2Xu2xtzEZbqr1yCtea7cm/remote-ai-workflow-engineer-in-new-york-at-alpaca-vc"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-12-01 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Research Engineer / Research Scientist- Personal AGI (Post Training) | OpenAI | San Francisco | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/openai/1c516e9f-c97d-4a40-8529-9871dac615a5"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-11-28 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer, Early Career | Affirm | San Francisco, California, United States | 0-2 | ❌ No | 7% | <a href="https://job-boards.greenhouse.io/affirm/jobs/7485068003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-11-27 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Middle Software Engineer (PHP) | Xsolla | CIS | Not specified | ❌ No | 15% | <a href="https://jobs.lever.co/xsolla/164a8740-d61a-41ee-9d10-8892b60ac0cb"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Automation Engineer | Prop Firm Match Global – FZCO | United States | Not specified | ❌ No | 11% | <a href="https://jobs.workable.com/view/aUTfLxQhw2oT7DrieizFdA/remote-ai-automation-engineer-in-united-states-at-prop-firm-match-global-%E2%80%93-fzco"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-11-25 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Machine Learning Engineer | Reducto | San Francisco Office | 2 | ❌ No | 26% | <a href="https://jobs.ashbyhq.com/reducto/aac35219-c38c-4490-8050-cee52e7dcf6b"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Backend/AI Engineer | Reducto | San Francisco Office | 2 | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/reducto/66e1299c-aaa9-4bee-b326-26afbd8b86ea"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-11-24 · 5 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| DevOps Engineer | Aquabyte | Puerto Varas | 2 | ❌ No | 22% | <a href="https://jobs.lever.co/aquabyte/79fb132f-07f0-4c66-9492-d34cc3d0cd88"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Machine Learning Scientist | Cartesian | Cambridge, MA | Not specified | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/cartesiansystems/jobs/4067461009"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Media Software Engineer, Speech (All Levels) | Cantina | San Francisco | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/cantina/e8019c96-0f59-4b2d-9871-867a854dfa43"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Inference Engineer | quadric, Inc | Burlingame, California, United States | Not specified | ❌ No | 11% | <a href="https://jobs.workable.com/view/f9jiyuftM23Boi7Nky2LtV/hybrid-ai-inference-engineer-in-burlingame-at-quadric%2C-inc"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Kernel Engineer | quadric, Inc | Burlingame, California, United States | Not specified | ❌ No | 11% | <a href="https://jobs.workable.com/view/46Ue11vgj8SvbzujvrGTTk/hybrid-ai-kernel-engineer-in-burlingame-at-quadric%2C-inc"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-11-23 · 4 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Data Engineer, Platform | Basis Research Institute | New York Office | Not specified | ❌ No | 26% | <a href="https://jobs.ashbyhq.com/basis-research/97ff8c58-b594-44b8-886c-21cf631dad1c"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Research Scientist, Program Synthesis & Neuro-symbolic Methods | Basis Research Institute | New York Office | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/basis-research/2b5fcfdb-0017-4e05-9ed3-1d65a6c44cc6"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| ML Systems Engineer, Infrastructure & Cloud | Basis Research Institute | New York Office | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/basis-research/51ebb571-246c-4913-84da-b924341f8a26"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Research Scientist, Reinforcement Learning | Basis Research Institute | New York Office | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/basis-research/f3bf27eb-f5fe-4b7d-9964-2eebe22b4ecd"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-11-21 · 6 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer, Backend | Clay | New York | Not specified | ❌ No | 30% | <a href="https://jobs.ashbyhq.com/claylabs/248aa0c7-034f-47d3-a57e-ce16736eeab6"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Analyst | TLA-LLC | McLean, Virginia, United States | Not specified | ❌ No | 26% | <a href="https://jobs.workable.com/view/sEYoBJe4Bo458kq9ypG2ma/data-analyst-in-mclean-at-tla-llc"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer Intern | TENEX.AI | San Jose, CA | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/tenex/fbfefd5c-ae95-4a71-8a75-e2b61facb304"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Robotics Software Engineer | Pivot Robotics | San Francisco | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/pivotrobotics/2bcbd79e-2570-4450-98cf-a0a74f67a047"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Engineer Internship | Solva | New York City | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/solva/e336c053-5f6e-4076-ad14-f941ab5096b6"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Product Designer, AI Models | Figma | San Francisco, CA • New York, NY • United States | Not specified | ❌ No | 7% | <a href="https://boards.greenhouse.io/figma/jobs/5711913004?gh_jid=5711913004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-11-20 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Junior Business Scientist, Data Science and Marketing Effectiveness | Ekimetrics | New York | 2 | ❌ No | 15% | <a href="https://jobs.lever.co/ekimetrics/d9d64766-3d42-4ba9-94d4-f74cdaf20065"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Electrical Systems Engineer | Pendar Technologies | Cambridge, MA | Not specified | ❌ No | 4% | <a href="https://job-boards.greenhouse.io/pendartechnologies/jobs/4994146008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-11-19 · 4 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| ML PhD Intern - LLMs & Generative AI | Truveta | Seattle, WA | 1 | ❌ No | 44% | <a href="https://job-boards.greenhouse.io/truveta/jobs/5712997004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Product Engineer, New Grad | Lightfield | HQ: San Francisco | 0-2 | ❌ No | 26% | <a href="https://jobs.ashbyhq.com/Lightfield/bb758825-5422-46c4-86c3-0be1cc89148f"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Fleet Management | OpenAI | San Francisco | Not specified | ❌ No | 26% | <a href="https://jobs.ashbyhq.com/openai/7809102e-e82a-4678-bf7c-221de8acc0d6"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Client Infrastructure | Cursor | San Francisco | Not specified | ❌ No | 7% | <a href="https://jobs.ashbyhq.com/cursor/e08262e8-c089-488d-9b59-9e21f7702b64"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-11-18 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer | Schonfeld | New York, New York, United States | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/schonfeld/jobs/7381166"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-11-14 · 3 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Applied AI Engineer | Serval | San Francisco | Not specified | ❌ No | 30% | <a href="https://jobs.ashbyhq.com/Serval/2bfaede4-22b2-43b2-a14c-f45e5f398624"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Distributed Data Systems - Robotics | OpenAI | San Francisco | Not specified | ❌ No | 26% | <a href="https://jobs.ashbyhq.com/openai/da07ba71-81fd-47c7-adb1-2b2d1eaed325"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Machine Learning Researcher / Engineer (Foundational Models) | Pathway | Palo Alto, California, United States | Not specified | ❌ No | 11% | <a href="https://jobs.workable.com/view/rwoNCCeB3Ebm8qhveHkm7s/hybrid-machine-learning-researcher-%2F-engineer-(foundational-models)-in-palo-alto-at-pathway"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-11-13 · 7 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer II | Alarm.com | Needham, Massachusetts | Not specified | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/alarmcom/jobs/8284605002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Flight Software Engineer | Hermeus | Los Angeles, CA | 1 | ❌ No | 11% | <a href="https://jobs.lever.co/hermeus/de110c1f-faa3-4442-a5ff-bcffb958608a"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Robotics Software Engineer | Sorting Robotics | Van Nuys, California, United States | Not specified | ❌ No | 11% | <a href="https://jobs.workable.com/view/sN7G1aPg6ruRq5uiVwxjai/robotics-software-engineer-in-van-nuys-at-sorting-robotics"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Backend Software Engineer | Concourse | New York City | 2 | ❌ No | 7% | <a href="https://jobs.ashbyhq.com/concourse/d3f5006c-34c0-4b36-8b11-a8a862435bba"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| UNPAID VOLUNTEER - Web Developer | Blockchain & Climate Institute/ BCI America Inc. | Florida, United States | Not specified | ❌ No | 4% | <a href="https://jobs.workable.com/view/j4RQCgbuWQBUrpurWybfUV/remote-unpaid-volunteer---web-developer-in-florida-at-blockchain-%26-climate-institute%2F-bci-america-inc."><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| UNPAID VOLUNTEER - Web Developer | Blockchain & Climate Institute/ BCI America Inc. | California, United States | Not specified | ❌ No | 4% | <a href="https://jobs.workable.com/view/cSnfoV7Y2PrQQiCsvZSGbC/remote-unpaid-volunteer---web-developer-in-california-at-blockchain-%26-climate-institute%2F-bci-america-inc."><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| UNPAID VOLUNTEER - Web Developer | Blockchain & Climate Institute/ BCI America Inc. | New York, New York, United States | Not specified | ❌ No | 4% | <a href="https://jobs.workable.com/view/8Qs2TRcJ2a6syvo7aPTuj4/remote-unpaid-volunteer---web-developer-in-new-york-at-blockchain-%26-climate-institute%2F-bci-america-inc."><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-11-12 · 5 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer II | The Trade Desk | Sydney | Not specified | ❌ No | 37% | <a href="https://job-boards.greenhouse.io/thetradedesk/jobs/4972481007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Full Stack Engineer, Intelligence Systems | OpenAI | San Francisco | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/openai/52c72cb9-7c44-4cba-b440-e05262a38491"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer (Back-End Oriented) | HelloGov AI | Miami, Florida, United States | Not specified | ❌ No | 22% | <a href="https://jobs.workable.com/view/oTiPRY7YDM8rp6Rz2ijCcK/software-engineer-(back-end-oriented)-in-miami-at-hellogov-ai"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| LLM Inference Engineer | Hippocratic AI | Palo Alto | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/Hippocratic%20AI/eef8a721-23de-4c20-bff0-56088b39afa0"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Cumberland/FICCO Tools Engineering | DRW | New York City | 2 | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/drweng/jobs/7392396"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-11-10 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer II (Backend, Healthcare) | Whoop | Boston, MA | Not specified | ❌ No | 15% | <a href="https://jobs.lever.co/whoop/79aed6aa-56b2-4d6d-9db7-570bb38706e0"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-11-09 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Scientific Software Engineer - Virtual Machine & Emulation | QuEra Computing | Boston, MA USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/queracomputinginc/jobs/4982246008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-11-08 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer | Confido | NYC Office | 2 | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/confido/d5520ce5-bc5f-4947-8912-292615b0c5ac"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-11-07 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Research Scientist, Interpretability | Anthropic | San Francisco, CA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/anthropic/jobs/4980427008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Junior Ubuntu Software Engineer | Canonical | Home based - Worldwide | 0-2 | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/canonical/jobs/6707669"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-11-05 · 3 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer - E2E Autonomy | Applied Intuition | Sunnyvale | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/applied/c3307413-8541-43b3-a854-81b0ac1a3868"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Full-Stack Software Engineer – Remote | SpruceID | REMOTE | 2 | ❌ No | 19% | <a href="https://jobs.lever.co/sprucesystems/b6ed1d39-d3e4-454f-8d8c-a5a65d64651f"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, AI Forward Deployed | Ramp | San Francisco, CA | 2 | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/ramp/deca582c-a1d0-4705-9975-60aed81ba89f"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-11-04 · 4 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Applied AI, Forward Deployed Machine Learning Engineer - Morocco | Mistral AI | Casablanca | 2 | ❌ No | 41% | <a href="https://jobs.lever.co/mistral/cb2137e6-d6b1-47d7-8450-6370a61f2b79"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer - AI Products | Herald | New York, NY | 2 | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/heraldapi/jobs/4976239008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Intern - AI Compilers | Tenstorrent | Austin, Texas, United States | Not specified | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/tenstorrentuniversity/jobs/4968219007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Machine Learning for Physical Design Intern - CPU/AI Hardware | Tenstorrent | Santa Clara, California, United States | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/tenstorrentuniversity/jobs/4968215007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-11-03 · 3 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| ML Research Scientist I/II, Multimodal Data Extraction | Lila Sciences | Cambridge, MA USA | Not specified | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/lilasciences/jobs/4052832009"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Site Reliability Engineer, Frontier Systems Infrastructure | OpenAI | San Francisco | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/openai/ad2cf782-15a4-48c7-9133-1788e3f33bbb"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Deployment Strategist - Morocco | Mistral AI | Casablanca | 2 | ❌ No | 19% | <a href="https://jobs.lever.co/mistral/8f93bac1-1885-41ea-8650-cb5454be97e7"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-11-01 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer, Full Stack | Figma | San Francisco, CA • New York, NY • United States | Not specified | ❌ No | 22% | <a href="https://boards.greenhouse.io/figma/jobs/5691911004?gh_jid=5691911004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-10-31 · 5 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| AI Product Engineer | Bunkerhill Health | SF Office | 2 | ❌ No | 26% | <a href="https://jobs.ashbyhq.com/bunkerhillhealth/8e4b579f-374a-4983-abd2-57b3d68d2ce2"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Hardware | OpenAI | San Francisco | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/openai/778e3a4f-c318-4a79-a745-00e722e5ee47"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Engineer | Joomag | Miami, Florida, United States | Not specified | ❌ No | 15% | <a href="https://jobs.workable.com/view/8Jw3gVHE4zLJNP8X19PRtk/hybrid-ai-engineer-in-miami-at-joomag"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Research Scientist, World Models | Basis Research Institute | New York Office | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/basis-research/a1feef01-9226-4041-ba05-486b596c54c3"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Analyst | Octopus Energy | Ancarano (IT) | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/octoenergy/de906ea2-3442-4fe1-a3b8-e2eb1e994820"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-10-30 · 3 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer, AI Agents | Hightouch | Remote (North America) | Not specified | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/hightouch/jobs/5542602004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Ground Systems Engineer II, Mechanical | Rocket Lab USA | Stennis Space Center, MS | 2 | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/rocketlab/jobs/7513269003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Growth | Cursor | San Francisco | Not specified | ❌ No | 7% | <a href="https://jobs.ashbyhq.com/cursor/0ec39ed7-a5dc-4551-bb26-b7f4f9fb4a74"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-10-29 · 5 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Training: ML Framework Engineer | OpenAI | San Francisco | Not specified | ❌ No | 30% | <a href="https://jobs.ashbyhq.com/openai/d8794980-1d3f-4d82-8b48-811449b6c492"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Machine Learning Engineer | Relace | San Francisco | 2 | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/relace/2deb110b-b848-4316-a120-f1864d788e94"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Machine Learning Scientist | Relace | San Francisco | 2 | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/relace/bc8f030e-157f-44b1-95ac-65fb1d807cc1"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Associate Conversational AI Designer | Cresta | United States (Remote) | Not specified | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/cresta/jobs/4970396008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Infrastructure Engineer | Relace | San Francisco | 2 | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/relace/4c882256-0667-433b-8ffa-2ebf99a0f7ce"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-10-28 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Research Scientist | Snorkel AI | Redwood City, CA (Hybrid); San Francisco, CA (Hybrid); United States (Remote) | Not specified | ❌ No | 56% | <a href="https://job-boards.greenhouse.io/snorkelai/jobs/5690608004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-10-27 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer - Full Stack | Airgoods | New York City | 1.5 | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/airgoods/036e4ed9-9c41-4aaa-9219-3851fb02f8e3"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Agent Harness | Cursor | San Francisco | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/cursor/6e6f5bc2-eb32-40e2-bba9-cfa56479600d"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-10-24 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer | TENEX.AI | Sarasota, FL HQ | Not specified | ❌ No | 37% | <a href="https://jobs.ashbyhq.com/tenex/09a6f900-f1f6-4edb-9296-03c6e5626799"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-10-23 · 4 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Junior Software Engineer with Accounting Experience (Chile) | Sezzle | Chile, Remote | 0-2 | ❌ No | 33% | <a href="https://job-boards.greenhouse.io/sezzle/jobs/6668067003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Junior Software Engineer with Accounting Experience (LATAM) | Sezzle | Colombia, Remote | 0-2 | ❌ No | 33% | <a href="https://job-boards.greenhouse.io/sezzle/jobs/6668068003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| New Grad Software Engineer | PointOne | New York City | 0-2 | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/pointone/1e312db8-6d18-4d07-af99-ed3ba165e7d9"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Exceptional Software Engineer | xAI | Austin, TX; New York, NY; Palo Alto, CA; Seattle, WA | Not specified | ❌ No | 7% | <a href="https://job-boards.greenhouse.io/xai/jobs/4956028007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-10-22 · 3 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer, AI Platform - Intern | Nuro | Mountain View, California (HQ) | Not specified | ❌ No | 26% | <a href="https://nuro.ai/careersitem?gh_jid=7351061"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Frontend Engineer - AI Products | Herald | New York City | 1 | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/heraldapi/jobs/4962979008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, AI Platform - New Grad | Nuro | Mountain View, California (HQ) | 0-2 | ❌ No | 19% | <a href="https://nuro.ai/careersitem?gh_jid=7351066"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-10-20 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Data Engineer | Innovative Rocket Technologies Inc. | Hauppauge, New York, United States | Not specified | ❌ No | 4% | <a href="https://jobs.workable.com/view/sEJ9jHurbRUYgSMhRiwhA6/data-engineer-in-hauppauge-at-innovative-rocket-technologies-inc."><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-10-17 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer, Reliability | OpenAI | San Francisco | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/openai/1faee5e7-3b2f-4d8c-9a6f-ff0f2a4a42a7"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Founding Full-Stack Engineer | truthsystems | San Francisco | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/truthsystems/c1f89831-104e-4731-b870-60239b374b5a"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-10-16 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Connectivity Software Engineer, Consumer Devices | OpenAI | San Francisco | Not specified | ❌ No | 26% | <a href="https://jobs.ashbyhq.com/openai/9b2c68f2-5ce8-44f9-a30c-d8016ac66d86"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-10-15 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Machine Learning Systems Engineer, Research Tools | Anthropic | San Francisco, CA \| New York City, NY \| Seattle, WA | Not specified | ❌ No | 26% | <a href="https://job-boards.greenhouse.io/anthropic/jobs/4952079008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer - Networking Software and Services | xAI | Palo Alto, CA | Not specified | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/xai/jobs/4946696007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-10-14 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| [2026] Applied Scientist - PhD Intern | Roblox | San Mateo, CA, United States | Not specified | ❌ No | 37% | <a href="https://careers.roblox.com/jobs/7142298?gh_jid=7142298"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer | Idler | San Francisco | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/idler/cce9ab39-0ab0-489d-bbf9-4df74c2baeee"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-10-13 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer Intern | Simular | Palo Alto | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/Simular/063f177b-c3f2-44d2-8eeb-622a977e7d5a"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-10-10 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Research Engineer / Research Scientist, Tokens | Anthropic | New York City, NY; New York City, NY \| Seattle, WA; San Francisco, CA | Not specified | ❌ No | 26% | <a href="https://job-boards.greenhouse.io/anthropic/jobs/4951814008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Research Scientist | Simular | Palo Alto | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/Simular/7591c872-aba9-4442-8ee0-816064dbacd8"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-10-09 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| iOS Engineer II (AI Experiences) | Whoop | Boston, MA | Not specified | ❌ No | 19% | <a href="https://jobs.lever.co/whoop/ac5d06b2-ff4a-416c-8e60-bcbbfed730fd"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Cloud Platform Engineer | Baseten | San Francisco Office | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/baseten/916e9d62-492a-4562-971f-3e97e3868392"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-10-08 · 8 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| AI/ML Engineer | Accenture | Washington, DC | Not specified | ❌ No | 30% | <a href="https://boards.greenhouse.io/accenturefederalservices/jobs/4608162006?gh_jid=4608162006"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Research Scientist, Prediction & Planning | Waymo | Mountain View, CA USA; New York, NY USA; San Francisco, CA USA; | Not specified | ❌ No | 26% | <a href="https://careers.withwaymo.com/jobs?gh_jid=7309064"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Applied AI Scientist, Small Language Model and AI Training | Postman | San Francisco, California, United States | Not specified | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/postman/jobs/7452539003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Scientist - Warsaw | Mistral AI | Warsaw | Not specified | ❌ No | 19% | <a href="https://jobs.lever.co/mistral/4e498cbf-151e-483a-b3f7-76ff64a22041"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Scientist - Zurich | Mistral AI | Zurich | Not specified | ❌ No | 19% | <a href="https://jobs.lever.co/mistral/bedfc2aa-f1b6-4136-bd17-b3abe4c06120"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Inference – AMD GPU Enablement | OpenAI | San Francisco | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/openai/9b79406c-89a8-49bd-8a38-e72db80996e9"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Institute Fellow in Residence | Schmidt Sciences | New York, NY | Not specified | ❌ No | 15% | <a href="https://jobs.lever.co/schmidt-entities/c42b4c52-d92a-4bd6-bac6-6b2d94159b35"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| DevOps Engineer/ Production Support Analyst | mthree | USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/mthreerecruitingportal/jobs/4605796006"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-10-07 · 3 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| AI/ML Research Internship | Eight Sleep | San Francisco | Not specified | ❌ No | 30% | <a href="https://jobs.ashbyhq.com/eightsleep/b6c2e6f6-eadd-4d67-93e9-1426be4f2035"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer - Data Platform | Hadrian | Los Angeles, CA | Not specified | ❌ No | 26% | <a href="https://jobs.ashbyhq.com/hadrian-automation/c7953b1a-6672-49b1-9364-79ecb8db638c"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Full Stack Engineer - AI | Walter | New York, New York, United States | Not specified | ❌ No | 11% | <a href="https://jobs.workable.com/view/oA78G45wYUzj8xnmTxgDFR/full-stack-engineer---ai-in-new-york-at-walter"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-10-06 · 7 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| AI Residency Program, Material Science (2026 Cohort) | Lila Sciences | Cambridge, MA USA | Not specified | ❌ No | 26% | <a href="https://job-boards.greenhouse.io/lilasciences/jobs/4031379009"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data/AI Engineer | Sandpiper Productions | United States | Not specified | ❌ No | 22% | <a href="https://jobs.workable.com/view/9VG7jNrVNeT41PvT4RavK2/remote-data%2Fai-engineer-in-united-states-at-sandpiper-productions"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Machine Learning Scientist I/II, Scientific Reasoning | Lila Sciences | Cambridge, MA USA | Not specified | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/lilasciences/jobs/4031437009"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Research Scientist I/II, Statistical Mechanics and Dynamics | Lila Sciences | Cambridge, MA USA | Not specified | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/lilasciences/jobs/4031471009"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Infrastructure Security | OpenAI | Remote - US | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/openai/98ad9beb-4f91-496c-bd16-ac0b2a8d5bb2"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Ray Core | Anyscale | Bengaluru, Karnataka | 2 | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/anyscale/8b29c5e5-d56f-4c52-8887-a6a1827cf042"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Research Scientist, Frontier Capabilities | Lila Sciences | Cambridge, MA USA; San Francisco, CA USA | Not specified | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/lilasciences/jobs/4031326009"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-10-04 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer, Software Update Infrastructure | Nuro | Mountain View, California (HQ) | 2 | ❌ No | 15% | <a href="https://nuro.ai/careersitem?gh_jid=7235419"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-10-03 · 5 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer | Valon | New York | 1 | ❌ No | 26% | <a href="https://jobs.ashbyhq.com/Valon/495b5050-0d48-4ff7-ab21-2a6155d62658"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Backend Engineer | Octopus Energy | Ascoli Piceno (IT) | Not specified | ❌ No | 15% | <a href="https://jobs.lever.co/octoenergy/f8b78b18-1d20-45a8-aa49-ec9e07fa8b8b"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer – DevOps Platform | Wealthfront | Palo Alto, CA (Open to US-based Remote) | 2 | ❌ No | 15% | <a href="https://jobs.lever.co/wealthfront/91c149ed-18fa-4e72-a3a6-386840aae86e"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Product Infrastructure | Notion | San Francisco, California | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/notion/d41b635b-c17b-4efd-89fd-fdb2ddb62e9a"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Healthcare and Administration Tutor | xAI | Remote | Not specified | ❌ No | 4% | <a href="https://job-boards.greenhouse.io/xai/jobs/4931312007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-10-02 · 3 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer, Developer Productivity | Glean | Mountain View, CA | Not specified | ❌ No | 26% | <a href="https://job-boards.greenhouse.io/gleanwork/jobs/4614706005"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Operations Research Scientist | Hadrian | Los Angeles, CA | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/hadrian-automation/2f10c29e-3918-4429-8a65-df5b1ba8ed25"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Scientist | GeoDelphi | Alexandria, Virginia, United States | Not specified | ❌ No | 7% | <a href="https://jobs.workable.com/view/mTKcBccBoonzT43XEYshFP/remote-data-scientist-in-alexandria-at-geodelphi"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-10-01 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer, All Teams | Compa | Orange County HQ / Remote Considered | 2 | ❌ No | 26% | <a href="https://jobs.ashbyhq.com/compa/ffbbc5c1-f8e9-444e-b4fb-89010a4a2398"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-09-30 · 5 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Builder - AI Engineer | Reevo | Santa Clara | 2 | ❌ No | 26% | <a href="https://jobs.ashbyhq.com/reevo/c14a5fc2-8ab5-4585-b84e-8ff0e87227db"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Research – Cumberland Systematic | DRW | Chicago | Not specified | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/drweng/jobs/7283668"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Science Tutor | xAI | Remote | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/xai/jobs/4925835007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Cumberland/FICCO Tools Engineering | DRW | Greenwich | 2 | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/drweng/jobs/7288315"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Data Specialist - Illinois (US) | RWS | Illinois | Not specified | ❌ No | 7% | <a href="https://jobs.lever.co/rws/dd563b7b-74d5-4124-bb0b-89a8d44348ae"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-09-27 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer (Full-stack) | Impiricus | Atlanta, GA \| NYC, NY \| Remote, USA | 2 | ❌ No | 37% | <a href="https://job-boards.greenhouse.io/impiricus/jobs/4936169008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Backend | Robinhood | Menlo Park, CA | 2 | ❌ No | 19% | <a href="https://boards.greenhouse.io/robinhood/jobs/7263592?t=gh_src=&amp;gh_jid=7263592"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-09-26 · 4 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Artificial Intelligence (AI) Engineers | Substance \| Level Up by Substance | United States | Not specified | ❌ No | 52% | <a href="https://jobs.workable.com/view/1YHyxu9kpbCGv17oSnBUt6/remote-artificial-intelligence-(ai)-engineers-in-united-states-at-substance-%7C-level-up-by-substance"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Agentic AI/ML Engineer, Multimodal | Field AI | Irvine, CA | 2 | ❌ No | 26% | <a href="https://jobs.lever.co/field-ai/28935a89-7c6b-4caf-abe7-b83b8a9958e1"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Product Engineer, Deployed | Brain Co. | Abu Dhabi | 2 | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/brainco/d8b1b928-d00e-4516-ba85-398cf9aba690"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Full Stack Engineer (Warsaw) | SalesPatriot | Warsaw Office | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/salespatriot/cf710859-108f-480e-826b-513a4b47a041"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-09-25 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Mobile Application Developer | Major League Baseball | Baltimore, MD | Not specified | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/baltimoreorioles/jobs/5659229004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Analyst | Numeral | HQ - San Francisco, CA | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/numeral/38a5fbbc-2556-499e-991d-e0a9806363d6"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-09-24 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Applied Machine Learning Engineer | Strata Decision Technology | Chicago, IL; Remote | Not specified | ❌ No | 52% | <a href="https://job-boards.greenhouse.io/stratacareers/jobs/7452181003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-09-23 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| AI Data Specialist - North Carolina (US) | RWS | North Carolina | Not specified | ❌ No | 7% | <a href="https://jobs.lever.co/rws/b181fd3b-a1e6-4c95-a2d9-4ec756ccd948"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Data Specialist - Texas (US) | RWS | Texas | Not specified | ❌ No | 7% | <a href="https://jobs.lever.co/rws/edfded6a-6a93-49cd-9b50-d0f74c3a41ac"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-09-22 · 3 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Foundational Research Scientist | AppLovin | Palo Alto, CA | Not specified | ❌ No | 26% | <a href="https://boards.greenhouse.io/applovin/jobs/4601725006?gh_jid=4601725006"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Research Developer Productivity | OpenAI | San Francisco | Not specified | ❌ No | 26% | <a href="https://jobs.ashbyhq.com/openai/e6d5ca02-f30b-4ac5-a69d-c947efb430f9"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, High Performance Computing | Eventual | San Francisco | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/eventualcomputing/9aa3763a-f267-4f19-bbd4-e6f38ab1c71e"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-09-18 · 7 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Data Scientist, Applied AI - Remote | Azumo | United States | Not specified | ❌ No | 48% | <a href="https://jobs.workable.com/view/czghxrEWSvvujrShXZDcng/data-scientist%2C-applied-ai---remote-in-united-states-at-azumo"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Software Engineer - Remote | Azumo | United States | Not specified | ❌ No | 30% | <a href="https://jobs.workable.com/view/7xRPgnRuDPJxP1jtoyCpz9/ai-software-engineer---remote-in-united-states-at-azumo"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Data Infrastructure - Research | OpenAI | San Francisco | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/openai/b7a2e30f-c5f6-4710-b53e-64d64bcce189"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Devops Engineer - I | Netomi | Gurugram | 2 | ❌ No | 15% | <a href="https://jobs.lever.co/netomi/78ceaf47-c13a-4735-a2c6-d7301af7f3fc"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Full Stack Software Engineer | PerformYard | United States | Not specified | ❌ No | 15% | <a href="https://jobs.workable.com/view/8NRBAdqLuht1XpteLSeqFK/remote-full-stack-software-engineer-in-united-states-at-performyard"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Site Reliability Engineer - Cybersecurity | xAI | Palo Alto, CA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/xai/jobs/4803447007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Data Specialist - Yoruba | RWS | Pretoria | Not specified | ❌ No | 7% | <a href="https://jobs.lever.co/rws/0d00557f-063d-47b9-89cc-9fe77311f84c"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-09-17 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer, Perception Evaluation | Waymo | Mountain View, CA, USA | 2 | ❌ No | 26% | <a href="https://careers.withwaymo.com/jobs?gh_jid=7256244"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Experienced Software Engineer (in person) | SEP | Westfield, IN | 2 | ❌ No | 15% | <a href="https://jobs.lever.co/sep/80cd8c15-bafc-49a9-b8f1-5d407e891ec0"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-09-16 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| AI Data Specialist - Italian | RWS | Rome | Not specified | ❌ No | 7% | <a href="https://jobs.lever.co/rws/613a9553-e941-4476-80f1-4dbd00410113"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-09-15 · 4 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Machine Learning Engineer | Point72 | New York | Not specified | ❌ No | 30% | <a href="https://boards.greenhouse.io/point72/jobs/8170176002?gh_jid=8170176002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Deployment Strategist - MENA | Mistral AI | Abu Dhabi | Not specified | ❌ No | 22% | <a href="https://jobs.lever.co/mistral/c9e2dbb5-00ed-4096-ba88-ac0bdffb68fd"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, New Grad | Eventual | San Francisco | 1 | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/eventualcomputing/becb5675-3480-4d2b-b126-2acad40fd088"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| The Data School NY - Data Analyst Consultant | The Information Lab | New York City | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/theinformationlab/eaa64bb6-30b9-44bf-a490-3a2ea9754c13"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-09-12 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| AI Engineering Intern (Colombia) | Sezzle | Colombia, Remote | Not specified | ❌ No | 33% | <a href="https://job-boards.greenhouse.io/sezzle/jobs/6542539003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Machine Learning Engineer | Skild AI | San Mateo, Pittsburgh | Not specified | ❌ No | 33% | <a href="https://job-boards.greenhouse.io/skildai-careers/jobs/4919028008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-09-11 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| ML Software Engineer Intern - AI/CAD Integration | Falcomm | Atlanta, Georgia, United States | Not specified | ❌ No | 41% | <a href="https://apply.workable.com/j/B5EB495F31"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| ML Software Engineer Intern - AI/CAD Integration | Falcomm | Atlanta, Georgia, United States | Not specified | ❌ No | 19% | <a href="https://jobs.workable.com/view/d2SVcNt7aXcE1C1uJFNu9b/ml-software-engineer-intern---ai%2Fcad-integration-in-atlanta-at-falcomm"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-09-10 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer 3, Search Systems Replication & Routing | MongoDB | San Francisco | 2 | ❌ No | 15% | <a href="https://www.mongodb.com/careers/job/?gh_jid=7235322"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-09-08 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| AI Research Scientist/Engineer (f/m/d) | Sonar | Bochum | Not specified | ❌ No | 44% | <a href="https://jobs.lever.co/sonarsource/9984dd32-2082-4ca2-9ee5-d47cb6940da8"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Research Scientist/Engineer | Sonar | Geneva | 2 | ❌ No | 26% | <a href="https://jobs.lever.co/sonarsource/a0535931-bce3-4159-b43d-15ca3eb4d17f"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-09-05 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Front-End Software Engineer (Remote) | Bask Health | United States | Not specified | ❌ No | 11% | <a href="https://jobs.workable.com/view/vpKo7E1ongxEvHRNmZXcxH/front-end-software-engineer-(remote)-in-united-states-at-bask-health"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-09-04 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| RTK - Junior Software Engineer - Internship | Aechelon Technology | Farmer's Branch, Texas | 0-2 | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/aechelontechnology/jobs/4904960008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-09-03 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer, Infrastructure | Exa Labs | San Francisco, California | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/exa/2fbb5f73-528f-4ab5-b216-1d73bc0dd34a"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Security | Cursor | San Francisco | Not specified | ❌ No | 7% | <a href="https://jobs.ashbyhq.com/cursor/94cc6684-9dbf-43f9-8ffc-405614e64ddd"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-09-02 · 4 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Machine Learning Researcher | AXQ Capital | Beijing; New York; Shanghai | Not specified | ❌ No | 37% | <a href="https://job-boards.greenhouse.io/axq/jobs/5636445004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Machine Learning Engineer – HPC | Meshy | Shanghai | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/meshy/921df195-bd41-4dbf-952f-516682ef2b74"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer – Frontend / Backend / Fullstack | Padlet | San Francisco | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/padlet/92eeb42e-4648-4c39-9894-c3991beddeae"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer – Mobile | Padlet | San Francisco | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/padlet/0c6fba2d-f8b3-488c-8541-bd196a0277f5"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-08-29 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer - Training Infrastructure | Baseten | San Francisco | Not specified | ❌ No | 26% | <a href="https://jobs.ashbyhq.com/baseten/6f947409-2bc0-491a-81b3-507cdc95df85"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Power Systems Engineer I – Test & Launch | Relativity Space | Stennis Space Center, Mississippi | 1 | ❌ No | 4% | <a href="https://boards.greenhouse.io/relativity/jobs/8141065002?gh_jid=8141065002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-08-28 · 5 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| AI Engineer | Campfire | San Francisco | Not specified | ❌ No | 37% | <a href="https://jobs.ashbyhq.com/campfire/5b8a95d4-54ef-41f5-b399-17b99354797f"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer (Full Stack and Mobile) | EliseAI | New York City | 2 | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/EliseAI/a3f5a582-7613-498e-8705-2dcaeae2511e"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer | Pure Storage | Santa Clara, California | Not specified | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/purestorage/jobs/7206456"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Azure Data Engineer | Sapsol Technologies Inc | United States | Not specified | ❌ No | 11% | <a href="https://jobs.workable.com/view/hnbyE2YV7RPTmq4R2fHSH6/remote-azure-data-engineer-in-united-states-at-sapsol-technologies-inc"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Full Stack Engineer | Campfire | San Francisco | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/campfire/14daffc0-738c-40f4-ae9f-f3b9c7927a5b"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-08-27 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Systems Engineer (Firmware) | Matic | Menlo Park, CA | 2 | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/MaticRobots/b6623c4c-afd2-4f7e-b364-6ed7f6b0bbd3"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-08-26 · 3 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| AI/ML Scientist/Developer | Axle | Frederick, MD | Not specified | ❌ No | 44% | <a href="https://job-boards.greenhouse.io/axle/jobs/4840335007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Bioinformatics/Data Scientist | Axle | Frederick, MD | Not specified | ❌ No | 30% | <a href="https://job-boards.greenhouse.io/axle/jobs/4840670007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Quality Engineer | Neon Health | SF Office | Not specified | ❌ No | 7% | <a href="https://jobs.ashbyhq.com/neon-health/1bcf0a46-82a3-4b1d-9233-9c2f2a934c9b"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-08-25 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer (Agent Platform) | Browserbase | San Francisco | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/browserbase/7724fbe3-6a27-4418-9705-2dcc40751a16"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Applications Engineer | quadric, Inc | Burlingame, California, United States | Not specified | ❌ No | 11% | <a href="https://jobs.workable.com/view/gW5RoNYUb6JzCE1ZXgd49G/ai-applications-engineer-in-burlingame-at-quadric%2C-inc"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-08-22 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Eloquent AI Fellowship Program | Eloquent AI | San Francisco | Not specified | ❌ No | 41% | <a href="https://jobs.ashbyhq.com/eloquentai/6da20f29-5de4-4c58-9057-05d2937faca7"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Engineer, Platform | Eloquent AI | San Francisco | 2 | ❌ No | 33% | <a href="https://jobs.ashbyhq.com/eloquentai/5ebee283-cf69-40a6-af38-e7d703bbab0f"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-08-21 · 3 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Machine Learning Engineer Intern (Summer 2026) | Pulse | San Francisco | Not specified | ❌ No | 30% | <a href="https://jobs.ashbyhq.com/pulse/e9a43a34-1b7b-4ab8-b646-89f4db85d264"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Research Engineer - Datadog AI Research (DAIR) | Datadog | New York, New York, USA | Not specified | ❌ No | 22% | <a href="https://careers.datadoghq.com/detail/7183013/?gh_jid=7183013"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Strategy Consultant | Hightouch | Remote (North America) | Not specified | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/hightouch/jobs/5618829004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-08-20 · 4 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Machine Learning Engineer | Avride | Austin, TX | Not specified | ❌ No | 52% | <a href="https://job-boards.greenhouse.io/avride/jobs/4013230009"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Machine Learning Engineer – Motion Planning & Prediction | Avride | Austin, TX | Not specified | ❌ No | 37% | <a href="https://job-boards.greenhouse.io/avride/jobs/4013016009"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Scientist – AV Metrics & Evaluation Analytics | Avride | Austin, TX | 2 | ❌ No | 26% | <a href="https://job-boards.greenhouse.io/avride/jobs/4012771009"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| C++ Software Engineer – Motion Planning | Avride | Austin, TX | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/avride/jobs/4013017009"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-08-19 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Research Scientist (Research) | Applied Intuition | Sunnyvale | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/applied/39846b2a-1f0e-4f97-b463-75fd37f217ce"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Research Scientist - World-Action Foundation Model, Robotics | Applied Intuition | Sunnyvale | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/applied/a6c99f37-545a-46f2-8222-02ad43c1e2c3"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-08-18 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| AV Systems Engineer | Latitude | Havertown, PA | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/latitudeinc/f2c1c8df-3512-4041-ba2f-c903da3f5612"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-08-17 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Machine Learning Engineer | Verneek | New York, New York, United States | Not specified | ❌ No | 22% | <a href="https://jobs.workable.com/view/vycwfuQ72e6gwHympaRKek/machine-learning-engineer-in-new-york-at-verneek"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-08-15 · 3 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| High Performance Computing Software Engineer - Supercomputing | Institute of Foundation Models | Abu Dhabi | Not specified | ❌ No | 30% | <a href="https://jobs.lever.co/ifm-us/5c662f6d-0043-4bba-8b58-53dd4afd8e4e"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Backend Software Engineer, LiveOps | BRINC Drones | Seattle, WA | 1 | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/brinc/4cdc261c-24a6-4d69-bd09-8a2d1049d85d"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| FullStack Engineer, AI Observability & Evals Platform (LangSmith) | LangChain | San Francisco, CA | 2 | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/langchain/ddf92275-1cc3-49c0-9f25-e8ded43b07f6"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-08-14 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| AI / Machine Learning Engineer | 1Kosmos | Iselin, New Jersey, United States | Not specified | ❌ No | 19% | <a href="https://jobs.workable.com/view/pZ5UXSYYKrZo2YdgTcLVQ7/ai-%2F-machine-learning-engineer-in-iselin-at-1kosmos"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Product | Eventual | San Francisco | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/eventualcomputing/b358f161-6af7-4a6f-8ba2-2366efb342ba"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-08-12 · 4 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Machine Learning Engineer, Robot Learning | Path Robotics | Columbus, Ohio | Not specified | ❌ No | 19% | <a href="https://boards.greenhouse.io/pathrobotics/jobs/8116143002?gh_jid=8116143002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer I/II, Flight Software | Heart Aerospace | Los Angeles, CA | 2 | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/heartaerospace/jobs/4013531009"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Embedded Systems Engineer, Robotics Hardware | Field AI | Irvine, CA | Not specified | ❌ No | 7% | <a href="https://jobs.lever.co/field-ai/7a0d12c7-957b-42f6-a9c9-9605fab6d2a4"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Flight Systems Engineer | Heart Aerospace | Los Angeles, CA | 2 | ❌ No | 7% | <a href="https://job-boards.greenhouse.io/heartaerospace/jobs/4007362009"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-08-11 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| 2026 Early Career Software Engineer | Anduril | Atlanta, Georgia, United States; Costa Mesa, California, United States; Fort Collins, Colorado, United States; Seattle, Washington, United States | 2 | ❌ No | 22% | <a href="https://boards.greenhouse.io/andurilindustries/jobs/4802146007?gh_jid=4802146007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Planner Vehicle Dynamics | Waymo | Mountain View, California | Not specified | ❌ No | 22% | <a href="https://careers.withwaymo.com/jobs?gh_jid=7141380"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-08-07 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer Internship, Android | Ramp | New York, NY (HQ) | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/ramp/67fadb77-43d8-4449-954b-d4cf2c6d3b8b"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Founding Full-Stack Engineer | Dryft | San Francisco | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/dryft/352183c7-98bc-4626-bc80-b13cfaf005d4"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-08-06 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer | Secureframe | New York, NY | Not specified | ❌ No | 15% | <a href="https://jobs.lever.co/secureframe/a55bbed2-c0f0-40b6-89c0-70b7e90365d8"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-08-05 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Backend Engineer | Navier AI | San Francisco | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/navierai/jobs/4863071008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Data Specialist - Greek | RWS | Athens | Not specified | ❌ No | 7% | <a href="https://jobs.lever.co/rws/55c1a116-69c7-4487-b06f-b89b367f1053"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-08-01 · 6 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| AI/ML Engineer | Brain Co. | San Francisco Bay Area | Not specified | ❌ No | 33% | <a href="https://jobs.ashbyhq.com/brainco/58cff031-5b0b-4b92-a1ea-2ebf2495d89d"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Full Stack Engineer | Roboflow | NY, SF or Remote | Not specified | ❌ No | 33% | <a href="https://jobs.ashbyhq.com/roboflow/e1757849-8d06-45b8-b462-f08c8e761397"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Full Stack Engineer (Enterprise) | Roboflow | NY, SF or Remote | Not specified | ❌ No | 33% | <a href="https://jobs.ashbyhq.com/roboflow/e884aee4-ce5f-4046-919b-b72577937530"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Junior 3D Graphics Software Engineer | Aechelon Technology | Overland Park, Kansas | 0-2 | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/aechelontechnology/jobs/4831329008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Junior Software Engineer - Internship | Aechelon Technology | Overland Park, KS | 0-2 | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/aechelontechnology/jobs/4831334008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer (Java) | Adyen | Sao Jose dos Campos | Not specified | ❌ No | 7% | <a href="https://job-boards.greenhouse.io/adyen/jobs/7095304"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-07-31 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Junior Software Engineer with Accounting Experience | Sezzle | Türkiye, Remote | 0-2 | ❌ No | 33% | <a href="https://job-boards.greenhouse.io/sezzle/jobs/6668069003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Backend Engineer | Doss | San Francisco | Not specified | ❌ No | 7% | <a href="https://jobs.ashbyhq.com/doss/5e8c7108-bc96-41d8-9cde-008080782f98"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-07-30 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer | Pulse | San Francisco | 2 | ❌ No | 37% | <a href="https://jobs.ashbyhq.com/pulse/b952467f-30db-4941-afaf-ae2b6d729b2d"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Blockchain Security Expert - AI Track | Certik | US / Remote | 2 | ❌ No | 7% | <a href="https://jobs.lever.co/certik/2c4b70d2-43da-44fc-8018-060f1640041e"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-07-29 · 3 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer, Enterprise | Cursor | San Francisco | Not specified | ❌ No | 7% | <a href="https://jobs.ashbyhq.com/cursor/54a9cfcd-570a-4e9c-b52c-bd2336c60991"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Product | Cursor | San Francisco | Not specified | ❌ No | 7% | <a href="https://jobs.ashbyhq.com/cursor/3551cdaa-cf08-4c04-adbe-a968185bc769"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Generalist | Cursor | San Francisco | Not specified | ❌ No | 4% | <a href="https://jobs.ashbyhq.com/cursor/36e69353-0452-4bf6-9f35-b1e7307959a7"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-07-28 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer | TENEX.AI | San Jose, CA | Not specified | ❌ No | 37% | <a href="https://jobs.ashbyhq.com/tenex/3b828a98-6e81-4300-a966-eecd4da37a31"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-07-24 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| AI Research Internship - LLM | Institute of Foundation Models | Sunnyvale, CA | Not specified | ❌ No | 26% | <a href="https://jobs.lever.co/ifm-us/5342e333-61b9-406d-bfea-61a687a94d1f"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-07-23 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer, Next Gen | Neuralink | South San Francisco, California, United States | Not specified | ❌ No | 11% | <a href="https://boards.greenhouse.io/neuralink/jobs/6658884003?gh_jid=6658884003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Web Crawling | Exa Labs | San Francisco, California | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/exa/0298c908-e2ff-4dbb-a8cc-4899a9f6737a"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-07-22 · 3 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Engineering - Internal AI Transformation | ElevenLabs | United States | Not specified | ❌ No | 26% | <a href="https://jobs.ashbyhq.com/elevenlabs/a3097257-a07a-4a7e-b9fe-b8555c1a0fa7"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Applied AI | Artisan | San Francisco | 2 | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/artisan/e5805224-3fdc-4400-bfc0-8ab60440f157"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Privacy | OpenAI | San Francisco | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/openai/8a1b804f-b070-4c61-bd3d-cdf39ef9d935"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-07-21 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Java/Kotlin Software Engineer - Manchester | Zopa | Manchester | Not specified | ❌ No | 7% | <a href="https://jobs.lever.co/zopa/fd815001-859f-447f-96e1-6f38026636e5"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-07-19 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Junior Software Engineer | Mechanize | San Francisco | 0-2 | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/mechanize/b50c89dc-001c-4fb6-a4fc-a9f52f35b490"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-07-18 · 4 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Research Engineer/Research Scientist, Pre-training | Anthropic | Remote-Friendly (Travel-Required) \| San Francisco, CA \| Seattle, WA \| New York City, NY | Not specified | ❌ No | 37% | <a href="https://job-boards.greenhouse.io/anthropic/jobs/4616971008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer | State Affairs | Washington, DC | 1 | ❌ No | 30% | <a href="https://job-boards.greenhouse.io/stateaffairs/jobs/4009196009"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Forward Deployed Software Engineer | Northslope Technologies | New York | Not specified | ❌ No | 26% | <a href="https://jobs.ashbyhq.com/northslope-technologies/17e19439-5dda-4f90-af28-2df8b6583cbc"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Core Services | OpenAI | San Francisco | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/openai/21bfde35-ffec-42d2-a2c6-8a03dad789d5"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-07-17 · 3 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| 3D Machine Learning Engineer | Field AI | Irvine, CA | 2 | ❌ No | 37% | <a href="https://jobs.lever.co/field-ai/b600a2ab-cff1-4b8f-9940-4bd851c05e37"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Applied Scientist (ML) | Samaya | Mountain View, California, United States | 2 | ❌ No | 30% | <a href="https://job-boards.greenhouse.io/samayaai/jobs/4791004007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer - GPU Kernels | Baseten | San Francisco | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/baseten/ddb5bc98-6116-49a2-802e-1c05398663f1"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-07-16 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer | Aleph | Americas | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/aleph/95e768d4-05d2-482c-8bfc-83f4f2d84616"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-07-15 · 3 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer - Backend | Realm | Remote | 2 | ❌ No | 44% | <a href="https://jobs.ashbyhq.com/realmalliance/49a2da18-3088-43af-a4ba-4db2096abb37"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Fleet Hardware Health | OpenAI | San Francisco | Not specified | ❌ No | 30% | <a href="https://jobs.ashbyhq.com/openai/57551641-208c-48d9-bfb8-9a298d7e7510"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Engineering Intern - General / AI | Allium | New York | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/allium/5d697ce5-b820-45c0-a101-86a05e1fb15e"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-07-14 · 4 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer - L3 Support | Canonical | Home based - Worldwide | Not specified | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/canonical/jobs/6635671"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| ML Engineer (Internship and Full-time) | Tilde Research | San Francisco | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/tilderesearch/b2e145db-0111-47c1-9d9f-e856a057d8ef"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Quantum Benchmarking Initiative Systems Engineer | Technergetics | Remote | Not specified | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/technergetics/jobs/4584127006"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| ML Researcher (Internship and Full-time) | Tilde Research | San Francisco | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/tilderesearch/e850d5b0-a5d6-4b9c-9898-f7addb441508"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-07-11 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Research Scientist - World Modeling | Institute of Foundation Models | Abu Dhabi | Not specified | ❌ No | 30% | <a href="https://jobs.lever.co/ifm-us/2c2f5a7a-79f6-40ff-9274-638a047602c5"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-07-10 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| AI Analyst | Level AI | Noida | 2 | ❌ No | 33% | <a href="https://jobs.lever.co/levelai/c55479cf-bc3e-471b-9ed7-ac213b0ee8b5"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-07-09 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer - Kafka | Applied Intuition | Sunnyvale | 2 | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/applied/f4a70017-3f50-4eb9-9fae-922582fa226c"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-07-08 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer | Auctor | New York | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/auctor/45cd780b-30bd-4887-b1e8-0b4858aa8e63"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-07-07 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer | Jane Street | New York, New York, United States | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/janestreet/jobs/8046410002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-07-03 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| AI Assistant In-Car Tester | TSMG | Dallas, TX | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/tsmg/d8d89df5-3ab5-4ca6-a0d2-8ca33fcbc6e0"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-07-02 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Research Engineer - NLP | Institute of Foundation Models | Abu Dhabi | Not specified | ❌ No | 37% | <a href="https://jobs.lever.co/ifm-us/1b258c12-5942-4487-9c92-fd4d18e40c6a"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Research Scientist | Institute of Foundation Models | Abu Dhabi | Not specified | ❌ No | 33% | <a href="https://jobs.lever.co/ifm-us/4b367c0c-c1a5-4c3b-b637-5eb9e47a9bcb"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-07-01 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer: Backend & Infrastructure | Vooma | San Francisco Office | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/vooma/27eff832-988e-4d53-a6b4-b758085ae334"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-06-30 · 3 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer - Developer Infrastructure | Applied Intuition | Sunnyvale | 2 | ❌ No | 26% | <a href="https://jobs.ashbyhq.com/applied/ab036590-eae9-45ea-9edc-8d7528cdde9d"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Machine Learning Educator | Jane Street | New York, New York, United States | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/janestreet/jobs/8056588002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer (Frontend Design) | N1 | New York City | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/n1/c576b0dd-5737-4fcd-867b-b83c55f9cc11"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-06-27 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| AI/ML Engineer, Deployed | Brain Co. | Abu Dhabi | Not specified | ❌ No | 33% | <a href="https://jobs.ashbyhq.com/brainco/c5de5f45-ee53-48f0-86cf-2dfefa694ebb"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-06-26 · 4 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| AI Product Engineer | Brain Co. | San Francisco Bay Area | 2 | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/brainco/4866bc74-52fa-4819-a9d0-3a5e73c31951"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Research, ML | Exa Labs | San Francisco, California | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/exa/fcebd301-b473-40dc-b733-362883ac1f37"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Backend | Exa Labs | San Francisco, California | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/exa/41eb773d-9909-422c-b6b8-5bbdc407d318"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Backend Engineer, Generative AI Services | OPPO US Research Center | Palo Alto, California, United States | Not specified | ❌ No | 7% | <a href="https://jobs.workable.com/view/usRsworssi2j7BExpJBR66/backend-engineer%2C-generative-ai-services-in-palo-alto-at-oppo-us-research-center"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-06-24 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Forward Deployed Engineer, AI Agents | Inkeep | New York City | 2 | ❌ No | 7% | <a href="https://jobs.ashbyhq.com/inkeep/f277f68d-c397-4919-beeb-67ee1e19dc91"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-06-23 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer | Northstrat | Columbia, Maryland, United States | Not specified | ❌ No | 7% | <a href="https://jobs.workable.com/view/f5K91uFNXLeKG3Yyp78Z9H/hybrid-software-engineer-in-columbia-at-northstrat"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-06-20 · 4 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Junior Research Scientist | EliseAI | New York City | 0-2 | ❌ No | 26% | <a href="https://jobs.ashbyhq.com/EliseAI/54f71abf-9184-4b4a-8d41-43ebf1600eba"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Researcher | Hume AI | NYC, San Jose, or Remote | 2 | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/humeai/jobs/4775962008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Founding Software Engineer \| Healthcare | EliseAI | New York City | 1 | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/EliseAI/6b756f91-4355-49af-901b-77d3b62d656a"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Operations Specialist \| Housing (New Grads 2025-2026) | EliseAI | New York City | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/EliseAI/f8744c2a-ba16-47b8-894e-28406000681a"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-06-17 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Data Engineer | Institute of Foundation Models | Abu Dhabi | Not specified | ❌ No | 33% | <a href="https://jobs.lever.co/ifm-us/b6c7bc76-7a13-4a2c-84ce-d01c61d08d80"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Inference Software Engineer | Etched.ai | San Jose | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/Etched/0f9c0162-97c6-4be6-9cb7-d9afdcf0fa7c"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-06-16 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer (New grad) | Continue | San Francisco | 0-2 | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/continue/219fce3e-7af9-4b00-8fa7-87bf53db72f7"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-06-13 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Portfolio Data Analyst | Arcana | Bangalore | Not specified | ❌ No | 4% | <a href="https://job-boards.greenhouse.io/arcanaanalytics/jobs/4005204009"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-06-12 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| AI Software Engineer | Cottingham & Butler | Dubuque, Iowa, United States | Not specified | ❌ No | 30% | <a href="https://boards.greenhouse.io/cottinghambutlerinsuranceservicesinc/jobs/4757428008?gh_jid=4757428008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer - Platforms & Productivity | Cloudflare | In-Office | Not specified | ❌ No | 15% | <a href="https://boards.greenhouse.io/cloudflare/jobs/6972536?gh_jid=6972536"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-06-11 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| US - Financial Crime Data Analyst (SQL & Large Data Sets) | Capitex | United States | Not specified | ❌ No | 11% | <a href="https://jobs.workable.com/view/4bXm4UAQtdrQk54guunb6C/remote-us---financial-crime-data-analyst-(sql-%26-large-data-sets)-in-united-states-at-capitex"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-06-08 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Engineering Intern – Gen AI for FP&A Platform | Drivetrain | United States | Not specified | ❌ No | 15% | <a href="https://jobs.lever.co/drivetrain/7266784e-530b-4eb5-a61b-b09557f6e98d"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-06-05 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| New Grad Software Engineer (Backend Rust) | N1 | New York City | 0-2 | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/n1/a3e25c84-0846-454a-b2fc-a356c2a713bd"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-06-04 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Backend Software Engineer | Castle | Harvard Square | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/castle/d6d2a7db-ee6e-4f3c-8d05-662a910cc13b"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-06-03 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Applied NLP Engineer | Unwrap | Santa Barbara | 2 | ❌ No | 7% | <a href="https://jobs.ashbyhq.com/Unwrap/24bbc3aa-832e-4f64-99af-922faeeae802"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-06-02 · 4 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer Intern (Backend, Rust) | N1 | New York City | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/n1/afe7deb5-9cfd-4926-bcb4-058d418592a6"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer Intern (Fullstack) | N1 | New York City | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/n1/298585c3-96b1-4728-8d37-31482f85a064"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, BCI Applications | Neuralink | Austin - ATX1; South San Francisco, California, United States | Not specified | ❌ No | 11% | <a href="https://boards.greenhouse.io/neuralink/jobs/6596365003?gh_jid=6596365003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Backend Engineer | LayerZero Labs | Vancouver, BC | 2 | ❌ No | 7% | <a href="https://job-boards.greenhouse.io/layerzerolabs/jobs/5554606004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-05-30 · 3 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer, Agent Infrastructure | OpenAI | San Francisco | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/openai/c1316397-25bb-4add-9e9d-0e3ea8ba929a"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Machine Learning Engineer Intern | Neuralink | South San Francisco, California, United States | Not specified | ❌ No | 15% | <a href="https://boards.greenhouse.io/neuralink/jobs/6594261003?gh_jid=6594261003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer Intern, BCI Applications | Neuralink | South San Francisco, California, United States | Not specified | ❌ No | 11% | <a href="https://boards.greenhouse.io/neuralink/jobs/6594422003?gh_jid=6594422003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-05-28 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer, Applied AI | State Affairs | Washington, DC | Not specified | ❌ No | 44% | <a href="https://job-boards.greenhouse.io/stateaffairs/jobs/4001354009"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-05-27 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| RF Systems Engineer I - Operations | Rocket Lab USA | Auckland, NZ | Not specified | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/rocketlab/jobs/6589226003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-05-26 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| AI Research Engineer | Creatify Lab | Mountain View | Not specified | ❌ No | 30% | <a href="https://jobs.ashbyhq.com/creatify/2ebe3f70-171c-4b4e-b1aa-220133dcb202"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-05-25 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer, Product | Netic | San Francisco | 2 | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/netic/48bf32b5-827d-4d6b-934f-5f2c372baa38"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-05-23 · 1 role · 1 H-1B sponsor match

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Systems Engineer - Business Systems | Palantir | Denver, CO | 1 | ✅ Yes | 7% | <a href="https://jobs.lever.co/palantir/df20ad9f-3d7f-4267-8e37-8253f717534a"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-05-22 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Applied Research Scientist | AppLovin | Palo Alto, CA | 2 | ❌ No | 22% | <a href="https://boards.greenhouse.io/applovin/jobs/4570674006?gh_jid=4570674006"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-05-21 · 3 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer, Inference - Multi Modal | OpenAI | San Francisco | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/openai/4d14449e-5e7f-45d4-b103-8776a6c87086"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer | Middesk | San Francisco | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/middesk/e1c6af86-dce1-495f-a710-ad369fd1308c"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Technical Leader of Scientific AI Research | Kitware | Clifton Park, New York | Not specified | ❌ No | 15% | <a href="https://jobs.lever.co/kitware/b757f0c6-61c5-4918-b1c2-688d66567113"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-05-15 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Generative AI Analyst | Simulmedia | New York, New York | 2 | ❌ No | 26% | <a href="https://jobs.lever.co/simulmedia/52c56404-78f4-41be-a1a0-ef3ecd84993c"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer Intern | Haize Labs | NYC | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/haizelabs/jobs/4685944008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-05-14 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Research Engineer/Research Scientist, RL/Reasoning | OpenAI | San Francisco | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/openai/7e198d81-34e0-48b6-b64e-a501a75f9d53"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| R&D Systems Engineer | Silvus Technologies | Los Angeles | 2 | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/silvus/jobs/4685818008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-05-13 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Full Stack Engineer | Navier AI | San Francisco | Not specified | ❌ No | 30% | <a href="https://job-boards.greenhouse.io/navierai/jobs/4684292008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-05-08 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer Intern, Implant | Neuralink | Austin, Texas, United States; South San Francisco, California, United States | Not specified | ❌ No | 11% | <a href="https://boards.greenhouse.io/neuralink/jobs/6569018003?gh_jid=6569018003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-05-07 · 108 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer, Platform | Speechify | Remote | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5533936004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Alexandria, VA, USA | Speechify | Alexandria, VA, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974212004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Anaheim, CA, USA | Speechify | Anaheim, CA, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974137004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Anchorage, AK, USA | Speechify | Anchorage, AK, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974167004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Arlington, VA, USA | Speechify | Arlington, VA, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974210004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Atlanta, GA, USA | Speechify | Atlanta, GA, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974227004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Austin, TX, USA | Speechify | Austin, TX, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5976205004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Baltimore, MD, USA | Speechify | Baltimore, MD, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974222004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Baton Rouge, LA, USA | Speechify | Baton Rouge, LA, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974269004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Bellevue, WA, USA | Speechify | Bellevue, WA, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974150004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Berkeley, CA, USA | Speechify | Berkeley, CA, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974122004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Birmingham, AL, USA | Speechify | Birmingham, AL, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974263004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Bloomington, IN, USA | Speechify | Bloomington, IN, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974203004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Boise, ID, USA | Speechify | Boise, ID, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974166004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Boston, MA, USA | Speechify | Boston, MA, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974217004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Boston, MA, USA | Speechify | Boston, MA, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5976198004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Boulder, CO, USA | Speechify | Boulder, CO, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974174004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Buffalo, NY, USA | Speechify | Buffalo, NY, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974187004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Cambridge, MA, USA | Speechify | Cambridge, MA, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974219004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Cary, NC, USA | Speechify | Cary, NC, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974242004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Champaign, IL, USA | Speechify | Champaign, IL, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974175004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Chapel Hill, NC, USA | Speechify | Chapel Hill, NC, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974240004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Charleston, SC, USA | Speechify | Charleston, SC, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974248004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Chicago, IL, USA | Speechify | Chicago, IL, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974169004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Chicago, IL, USA | Speechify | Chicago, IL, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5976201004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Cincinnati, OH, USA | Speechify | Cincinnati, OH, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974195004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Cleveland, OH, USA | Speechify | Cleveland, OH, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974197004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - College Park, MD, USA | Speechify | College Park, MD, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974224004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Colorado Springs, CO, USA | Speechify | Colorado Springs, CO, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974178004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Columbia, SC, USA | Speechify | Columbia, SC, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974250004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Cupertino, CA, USA | Speechify | Cupertino, CA, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974126004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Dallas, TX, USA | Speechify | Dallas, TX, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974149004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Dayton, OH, USA | Speechify | Dayton, OH, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974199004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Denver, CO, USA | Speechify | Denver, CO, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5976200004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Des Moines, IA, USA | Speechify | Des Moines, IA, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974213004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Detroit, MI, USA | Speechify | Detroit, MI, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974186004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Durham, NC, USA | Speechify | Durham, NC, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974238004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - El Paso, TX, USA | Speechify | El Paso, TX, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974161004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Eugene, OR, USA | Speechify | Eugene, OR, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974162004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Evanston, IL, USA | Speechify | Evanston, IL, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974173004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Fort Lauderdale, FL, USA | Speechify | Fort Lauderdale, FL, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974276004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Fort Worth, TX, USA | Speechify | Fort Worth, TX, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974151004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Fremont, CA, USA | Speechify | Fremont, CA, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974130004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Fresno, CA, USA | Speechify | Fresno, CA, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974144004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Gainesville, FL, USA | Speechify | Gainesville, FL, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974239004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Grand Rapids, MI, USA | Speechify | Grand Rapids, MI, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974191004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Hartford, CT, USA | Speechify | Hartford, CT, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974198004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Honolulu, HI, USA | Speechify | Honolulu, HI, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974165004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Indianapolis, IN, USA | Speechify | Indianapolis, IN, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974201004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Iowa City, IA, USA | Speechify | Iowa City, IA, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974215004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Irvine, CA, USA | Speechify | Irvine, CA, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974138004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Jacksonville, FL, USA | Speechify | Jacksonville, FL, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974271004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Jersey City, NJ, USA | Speechify | Jersey City, NJ, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974223004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Kansas City, MO, USA | Speechify | Kansas City, MO, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974207004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Kirkland, WA, USA | Speechify | Kirkland, WA, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974154004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Lexington, KY, USA | Speechify | Lexington, KY, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974261004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Los Angeles, CA, USA | Speechify | Los Angeles, CA, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5976206004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Louisville, KY, USA | Speechify | Louisville, KY, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974259004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Memphis, TN, USA | Speechify | Memphis, TN, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974254004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Menlo Park, CA, USA | Speechify | Menlo Park, CA, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974125004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Miami, FL, USA | Speechify | Miami, FL, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974273004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Milwaukee, WI, USA | Speechify | Milwaukee, WI, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974183004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Minneapolis, MN, USA | Speechify | Minneapolis, MN, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974177004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Mountain View, CA, USA | Speechify | Mountain View, CA, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974124004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Nashville, TN, USA | Speechify | Nashville, TN, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974252004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - New York, NY, USA | Speechify | New York, NY, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974221004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Norfolk, VA, USA | Speechify | Norfolk, VA, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974220004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Oklahoma City, OK, USA | Speechify | Oklahoma City, OK, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974243004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Orlando, FL, USA | Speechify | Orlando, FL, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974229004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Palo Alto, CA, USA | Speechify | Palo Alto, CA, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5976207004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Palo Alto, CA, USA | Speechify | Palo Alto, CA, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974123004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Pasadena, CA, USA | Speechify | Pasadena, CA, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974139004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Philadelphia, PA, USA | Speechify | Philadelphia, PA, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974231004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Phoenix, AZ, USA | Speechify | Phoenix, AZ, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974188004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Plano, TX, USA | Speechify | Plano, TX, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974152004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Portland, OR, USA | Speechify | Portland, OR, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974160004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Princeton, NJ, USA | Speechify | Princeton, NJ, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974228004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Provo, UT, USA | Speechify | Provo, UT, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974170004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Raleigh, NC, USA | Speechify | Raleigh, NC, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974236004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Redmond, WA, USA | Speechify | Redmond, WA, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974153004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Reno, NV, USA | Speechify | Reno, NV, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974182004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Riverside, CA, USA | Speechify | Riverside, CA, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974142004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Rochester, NY, USA | Speechify | Rochester, NY, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974190004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Sacramento, CA, USA | Speechify | Sacramento, CA, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974132004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Saint Paul, MN, USA | Speechify | Saint Paul, MN, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974179004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Salt Lake City, UT, USA | Speechify | Salt Lake City, UT, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974168004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - San Antonio, TX, USA | Speechify | San Antonio, TX, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974158004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - San Diego, CA, USA | Speechify | San Diego, CA, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974140004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - San Francisco, CA, USA | Speechify | San Francisco, CA, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974119004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - San Mateo, CA, USA | Speechify | San Mateo, CA, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974129004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Santa Cruz, CA, USA | Speechify | Santa Cruz, CA, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974131004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Santa Monica, CA, USA | Speechify | Santa Monica, CA, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974134004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Seattle, WA, USA | Speechify | Seattle, WA, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974148004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Seattle, WA, USA | Speechify | Seattle, WA, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5976204004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Spokane, WA, USA | Speechify | Spokane, WA, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974159004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - St. Louis, MO, USA | Speechify | St. Louis, MO, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974209004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Stamford, CT, USA | Speechify | Stamford, CT, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974200004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - State College, PA, USA | Speechify | State College, PA, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974184004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Syracuse, NY, USA | Speechify | Syracuse, NY, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974192004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Tacoma, WA, USA | Speechify | Tacoma, WA, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974156004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Tallahassee, FL, USA | Speechify | Tallahassee, FL, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974241004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Tampa, FL, USA | Speechify | Tampa, FL, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974232004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Virginia Beach, VA, USA | Speechify | Virginia Beach, VA, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974218004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Washington, DC, USA | Speechify | Washington, DC, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5976199004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - West Lafayette, IN, USA | Speechify | West Lafayette, IN, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974205004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - West Palm Beach, FL, USA | Speechify | West Palm Beach, FL, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974237004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Winston-Salem, NC, USA | Speechify | Winston-Salem, NC, USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974246004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Implant | Neuralink | Austin, Texas, United States; South San Francisco, California, United States | Not specified | ❌ No | 11% | <a href="https://boards.greenhouse.io/neuralink/jobs/6569010003?gh_jid=6569010003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-05-06 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Generative AI - Graphics Engineer | Meshy | Bay Area Office | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/meshy/9527f581-8cfa-4761-8e28-368d0b5dae18"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-05-05 · 95 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Platform Engineer | Defense Unicorns | United States - Remote | Not specified | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/defenseunicorns/jobs/4725864007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product | Speechify | Remote | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5527897004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Anaheim, CA, USA | Speechify | Anaheim, CA, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981035004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Arlington, VA, USA | Speechify | Arlington, VA, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981128004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Atlanta, GA, USA | Speechify | Atlanta, GA, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981025004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Austin, TX, USA | Speechify | Austin, TX, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981019004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Bakersfield, CA, USA | Speechify | Bakersfield, CA, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981163004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Baltimore, MD, USA | Speechify | Baltimore, MD, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981140004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Baton Rouge, LA, USA | Speechify | Baton Rouge, LA, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981213004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Bellevue, WA, USA | Speechify | Bellevue, WA, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981018004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Bend, OR, USA | Speechify | Bend, OR, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981176004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Berkeley, CA, USA | Speechify | Berkeley, CA, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981070004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Birmingham, AL, USA | Speechify | Birmingham, AL, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981207004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Boise, ID, USA | Speechify | Boise, ID, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981178004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Cary, NC, USA | Speechify | Cary, NC, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981089004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Chapel Hill, NC, USA | Speechify | Chapel Hill, NC, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981086004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Charlotte, NC, USA | Speechify | Charlotte, NC, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981077004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Cincinnati, OH, USA | Speechify | Cincinnati, OH, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981091004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - College Park, MD, USA | Speechify | College Park, MD, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981069004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - College Station, TX, USA | Speechify | College Station, TX, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981193004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Colorado Springs, CO, USA | Speechify | Colorado Springs, CO, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981183004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Columbia, SC, USA | Speechify | Columbia, SC, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981255004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Dallas, TX, USA | Speechify | Dallas, TX, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981020004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Dayton, OH, USA | Speechify | Dayton, OH, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981205004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Denver, CO, USA | Speechify | Denver, CO, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981024004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Detroit, MI, USA | Speechify | Detroit, MI, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981085004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Durham, NC, USA | Speechify | Durham, NC, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981083004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - El Paso, TX, USA | Speechify | El Paso, TX, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981191004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Evanston, IL, USA | Speechify | Evanston, IL, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981104004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Fort Collins, CO, USA | Speechify | Fort Collins, CO, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981181004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Fort Lauderdale, FL, USA | Speechify | Fort Lauderdale, FL, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981103004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Fremont, CA, USA | Speechify | Fremont, CA, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981078004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Fresno, CA, USA | Speechify | Fresno, CA, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981162004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Frisco, TX, USA | Speechify | Frisco, TX, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981060004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Gainesville, FL, USA | Speechify | Gainesville, FL, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981222004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Grand Rapids, MI, USA | Speechify | Grand Rapids, MI, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981203004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Greensboro, NC, USA | Speechify | Greensboro, NC, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981248004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Honolulu, HI, USA | Speechify | Honolulu, HI, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981195004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Huntsville, AL, USA | Speechify | Huntsville, AL, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981095004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Indianapolis, IN, USA | Speechify | Indianapolis, IN, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981096004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Iowa City, IA, USA | Speechify | Iowa City, IA, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981220004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Irvine, CA, USA | Speechify | Irvine, CA, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981090004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Ithaca, NY, USA | Speechify | Ithaca, NY, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981235004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Jersey City, NJ, USA | Speechify | Jersey City, NJ, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981108004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Kansas City, MO, USA | Speechify | Kansas City, MO, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981098004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Kirkland, WA, USA | Speechify | Kirkland, WA, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981041004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Knoxville, TN, USA | Speechify | Knoxville, TN, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981261004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Las Vegas, NV, USA | Speechify | Las Vegas, NV, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981066004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Los Angeles, CA, USA | Speechify | Los Angeles, CA, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981021004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Louisville, KY, USA | Speechify | Louisville, KY, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981267004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Madison, WI, USA | Speechify | Madison, WI, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981079004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Menlo Park, CA, USA | Speechify | Menlo Park, CA, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981059004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Miami, FL, USA | Speechify | Miami, FL, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981097004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Milwaukee, WI, USA | Speechify | Milwaukee, WI, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981201004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Minneapolis, MN, USA | Speechify | Minneapolis, MN, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981071004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Mountain View, CA, USA | Speechify | Mountain View, CA, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981057004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Naperville, IL, USA | Speechify | Naperville, IL, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981102004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Nashville, TN, USA | Speechify | Nashville, TN, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981092004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - New Haven, CT, USA | Speechify | New Haven, CT, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981122004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Newark, NJ, USA | Speechify | Newark, NJ, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981110004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Norfolk, VA, USA | Speechify | Norfolk, VA, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981244004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Omaha, NE, USA | Speechify | Omaha, NE, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981214004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Palo Alto, CA, USA | Speechify | Palo Alto, CA, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981015004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Philadelphia, PA, USA | Speechify | Philadelphia, PA, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981115004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Phoenix, AZ, USA | Speechify | Phoenix, AZ, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981049004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Plano, TX, USA | Speechify | Plano, TX, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981058004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Princeton, NJ, USA | Speechify | Princeton, NJ, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981113004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Provo, UT, USA | Speechify | Provo, UT, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981047004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Raleigh, NC, USA | Speechify | Raleigh, NC, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981080004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Redmond, WA, USA | Speechify | Redmond, WA, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981039004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Reston, VA, USA | Speechify | Reston, VA, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981134004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Rochester, NY, USA | Speechify | Rochester, NY, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981229004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - San Antonio, TX, USA | Speechify | San Antonio, TX, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981063004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - San Diego, CA, USA | Speechify | San Diego, CA, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981037004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - San Francisco, CA, USA | Speechify | San Francisco, CA, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981014004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Santa Clara, CA, USA | Speechify | Santa Clara, CA, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981065004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Santa Cruz, CA, USA | Speechify | Santa Cruz, CA, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981231004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Santa Monica, CA, USA | Speechify | Santa Monica, CA, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981084004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Scottsdale, AZ, USA | Speechify | Scottsdale, AZ, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981051004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Silver Spring, MD, USA | Speechify | Silver Spring, MD, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981072004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - St. Petersburg, FL, USA | Speechify | St. Petersburg, FL, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981216004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Stamford, CT, USA | Speechify | Stamford, CT, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981121004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - State College, PA, USA | Speechify | State College, PA, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981223004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Stony Brook, NY, USA | Speechify | Stony Brook, NY, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981237004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Sunnyvale, CA, USA | Speechify | Sunnyvale, CA, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981064004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Syracuse, NY, USA | Speechify | Syracuse, NY, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981232004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Tacoma, WA, USA | Speechify | Tacoma, WA, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981166004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Tallahassee, FL, USA | Speechify | Tallahassee, FL, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981224004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Tampa, FL, USA | Speechify | Tampa, FL, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981101004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Tempe, AZ, USA | Speechify | Tempe, AZ, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981053004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Tucson, AZ, USA | Speechify | Tucson, AZ, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981189004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Tulsa, OK, USA | Speechify | Tulsa, OK, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981230004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Virginia Beach, VA, USA | Speechify | Virginia Beach, VA, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981242004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Washington, DC, USA | Speechify | Washington, DC, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981026004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - West Lafayette, IN, USA | Speechify | West Lafayette, IN, USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981211004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-05-04 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| AI Developer Advocate | Yotta Labs | United States | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/yotta/343ebde8-b8bc-4e98-a065-8fe8d1d5c30a"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Research Engineer - Decentralized AI Systems | Yotta Labs | United States | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/yotta/b5202314-91e1-4940-b8a1-9be0e02d1db5"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-05-02 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Research Scientist - World Modeling | Institute of Foundation Models | Sunnyvale, CA | Not specified | ❌ No | 30% | <a href="https://jobs.lever.co/ifm-us/adc38d88-64c7-4b26-9d45-ae287e178df6"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, ROS Developer | Field AI | Irvine, CA | Not specified | ❌ No | 15% | <a href="https://jobs.lever.co/field-ai/c3650d39-20eb-454e-97f8-4d38494e0fe6"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-05-01 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Research Scientist | Institute of Foundation Models | Sunnyvale, CA | Not specified | ❌ No | 33% | <a href="https://jobs.lever.co/ifm-us/057d2c3a-c17f-40f7-ac45-b1148f56c7f7"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-04-29 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| NLP / AI Engineer | Point72 | New York | Not specified | ❌ No | 33% | <a href="https://boards.greenhouse.io/point72/jobs/7661997002?gh_jid=7661997002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-04-28 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Machine Learning Engineer, Prediction & Planning | Waymo | Mountain View, CA, USA; San Francisco, CA, USA; New York City, NY, USA | 2 | ❌ No | 41% | <a href="https://careers.withwaymo.com/jobs?gh_jid=6506689"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Backend Engineer (Product, Infra) | SafetyKit | San Francisco | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/safetykit/27465006-cfb1-4420-8da2-17265150a2af"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-04-24 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer, Privacy Infrastructure | OpenAI | San Francisco | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/openai/07153f7c-7e8b-4283-a879-cb07a224e083"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-04-22 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| AI Engineer - Fury Team | Scout AI | Sunnyvale, CA | 2 | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/scoutai/jobs/4643324008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Researcher - Fury Team | Scout AI | Sunnyvale, CA | Not specified | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/scoutai/jobs/4643328008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-04-21 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Embedded Software Engineer, Implant Embedded Systems | Neuralink | Austin, Texas, United States; South San Francisco, California, United States | 1 | ❌ No | 7% | <a href="https://boards.greenhouse.io/neuralink/jobs/6550259003?gh_jid=6550259003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-04-17 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer I, Backend | Pinterest | Seattle, WA, US; San Francisco, CA, US | 1 | ❌ No | 19% | <a href="https://www.pinterestcareers.com/jobs/?gh_jid=6816337"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-04-16 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Machine Learning Engineer - 3D Sensor Simulation | Zoox | Seattle, WA | 2 | ❌ No | 26% | <a href="https://jobs.lever.co/zoox/a5b426d5-845c-4d26-bca2-7a32e00882a2"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-04-15 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Systems Engineer (Rust) | Matic | Menlo Park, CA | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/MaticRobots/56979df7-cb5e-45c3-baa9-3e1d9c8c2eb0"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-04-14 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Gen AI Data Engineer | Tiger Analytics Inc. | United States | Not specified | ❌ No | 26% | <a href="https://jobs.workable.com/view/tH2wopwwhphZEoPwV5LbC3/remote-gen-ai-data-engineer-in-united-states-at-tiger-analytics-inc."><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-04-10 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Full Stack Engineer | Unwrap | Santa Barbara | 2 | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/Unwrap/f5f0ecb5-c661-4e53-9700-da4f99cdde32"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-04-09 · 3 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Data Engineer | Institute of Foundation Models | Sunnyvale, CA | Not specified | ❌ No | 33% | <a href="https://jobs.lever.co/ifm-us/09018f47-2206-46bf-8b9c-07b24d4b5fa8"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Full Stack Software Engineer | Institute of Foundation Models | Sunnyvale, CA | Not specified | ❌ No | 30% | <a href="https://jobs.lever.co/ifm-us/1454349c-eb2b-480b-9a57-edfbb2aeeffe"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Scientific Software Engineer - Compiler | QuEra Computing | Boston, MA USA | Not specified | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/queracomputinginc/jobs/4584808008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-04-08 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Frontend Engineer | SafetyKit | San Francisco | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/safetykit/03d7e080-3e7a-4c6a-88a3-3d7418469082"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Applied AI Engineer | SafetyKit | San Francisco | Not specified | ❌ No | 7% | <a href="https://jobs.ashbyhq.com/safetykit/c619ef1d-7096-4bcc-9641-4ee49268c50b"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-04-05 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Research Scientist | OpenAI | San Francisco | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/openai/5f0c6579-0bfb-4a06-8a43-1dd371499e10"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-04-04 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer, Compute Platform | Replit | Foster City, CA | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/replit/659a8e1e-69ba-44c0-a632-96665051a3e8"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-04-03 · 1 role · 1 H-1B sponsor match

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Machine Learning Engineer (Defense) | Airspace Intelligence | Boston, US | Not specified | ✅ Yes | 48% | <a href="https://jobs.ashbyhq.com/airspace-intelligence.com/a035a6a4-0aee-4611-ae43-d0592995416a"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-04-01 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Research Engineer, Machine Learning (Reinforcement Learning) | Anthropic | San Francisco, CA \| New York City, NY | Not specified | ❌ No | 26% | <a href="https://job-boards.greenhouse.io/anthropic/jobs/4613568008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-03-31 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer - Core Database (Kernel) | Neo4j | Malmö | Not specified | ❌ No | 19% | <a href="https://boards.greenhouse.io/neo4j/jobs/4555260006?gh_jid=4555260006"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-03-26 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer - Internal Platform | Baseten | San Francisco | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/baseten/081cb52b-5e88-40a1-8def-1e82c8bc97de"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-03-25 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Research Scientist - Data | Institute of Foundation Models | Sunnyvale, CA | Not specified | ❌ No | 33% | <a href="https://jobs.lever.co/ifm-us/e71b87a7-e2ac-414e-b414-97fdc18658dc"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer (Core Infrastructure) | Browserbase | San Francisco | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/browserbase/bcbf0fb9-2405-497b-bbc9-e09d8f7a4963"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-03-24 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Front-End Software Engineer | Bask Health | New York, New York, United States | Not specified | ❌ No | 11% | <a href="https://jobs.workable.com/view/nmW9thjRF9zp7ptiH1Ryrd/hybrid-front-end-software-engineer-in-new-york-at-bask-health"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-03-17 · 3 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Research Scientist - NLP | Institute of Foundation Models | Sunnyvale, CA | Not specified | ❌ No | 37% | <a href="https://jobs.lever.co/ifm-us/6a4c7a41-983f-4c06-b785-c2deb5cd3f5d"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, AI Safety | OpenAI | San Francisco | Not specified | ❌ No | 26% | <a href="https://jobs.ashbyhq.com/openai/b9dee2a0-9bb3-447e-9bce-2b1bed784e5b"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Distributed Machine Learning Engineer | Institute of Foundation Models | Sunnyvale, CA | 2 | ❌ No | 22% | <a href="https://jobs.lever.co/ifm-us/965f914c-5be2-4670-b006-946d2274dc66"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-03-13 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Blockchain Security Expert Intern - AI Track | Certik | New York, New York / Remote | Not specified | ❌ No | 33% | <a href="https://jobs.lever.co/certik/1f446b66-1fae-4c31-9352-cde86e254754"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-03-11 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer, Machine Learning | Ema | San Francisco Bay Area | 2 | ❌ No | 37% | <a href="https://jobs.ashbyhq.com/ema/9728a171-9617-4533-9f03-10c14c3b6ca5"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Embedded Software Engineer, Vehicle Controls | Aurora Innovation | Pittsburgh, Pennsylvania | Not specified | ❌ No | 11% | <a href="https://aurora.tech/jobs/7822890002?gh_jid=7822890002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-03-10 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| ML Research Engineer, ML Systems | Scale AI | San Francisco, CA; Seattle, WA; New York, NY | Not specified | ❌ No | 30% | <a href="https://job-boards.greenhouse.io/scaleai/jobs/4534631005"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-03-09 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer - Infrastructure | Baseten | San Francisco | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/baseten/ae64d1d4-7b0a-4be4-8d77-7f5ce63849a7"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-03-06 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Linux Kernel Software Engineer - Systems Engineering | Pure Storage | Santa Clara, California | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/purestorage/jobs/6676814"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-03-04 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Backend Engineer, New Grad | AppLovin | Palo Alto, CA | 2 | ❌ No | 15% | <a href="https://boards.greenhouse.io/applovin/jobs/4451556006?gh_jid=4451556006"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Mobile Software Engineer - iOS | Drivemode | Mountain View, CA | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/drivemode/7610d1e6-74c4-4286-b78f-f0d4a1811834"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-02-26 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Machine Learning Engineer - 3D Sensor Simulation | Zoox | Foster City, CA | 2 | ❌ No | 26% | <a href="https://jobs.lever.co/zoox/55e51bf3-68ee-40d4-a1c5-5196e0e2d100"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-02-25 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer, C++ Middleware and Runtime Infrastructure | PlusAI | Santa Clara, CA | Not specified | ❌ No | 7% | <a href="https://jobs.lever.co/plus-2/1a1fc0e8-0741-4be1-adbb-52aa418eecf2"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-02-21 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Full-stack Engineer | Ekho | New York City HQ | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/Ekho/c8888199-a4aa-4b61-9744-67bd2c92f4d8"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-02-20 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| ML Research Intern | Samaya | Mountain View, California, United States | Not specified | ❌ No | 30% | <a href="https://job-boards.greenhouse.io/samayaai/jobs/4652765007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer (Full Stack) | N1 | New York City | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/n1/2213cef6-fbcd-42f7-8e0e-c6a23bfc1119"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-02-18 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer, Backend | Atomic Invest (AtomicVest) | Remote | 2 | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/atomic-invest/241de06e-858d-4e52-b3ac-43bc7c024176"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-02-17 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer | Column | San Francisco, CA | Not specified | ❌ No | 7% | <a href="https://jobs.ashbyhq.com/column/8ad3cf7b-7ea3-47f6-86c4-c83a9d78ff50"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-02-13 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer, Fleet Infrastructure | OpenAI | San Francisco | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/openai/a58add97-1968-4d5c-b504-ab62bea12df3"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Mid Level DevOps Engineer | Freedom Technology Solutions Group | Annapolis Junction, MD | Not specified | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/freedomconsulting/jobs/4646169007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-02-11 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| [Expression of Interest] Research Scientist / Engineer, Honesty | Anthropic | New York City, NY; San Francisco, CA | Not specified | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/anthropic/jobs/4532887008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-02-10 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Early Career Software Engineer – Applied AI | Wonderschool | San Francisco | 0-2 | ❌ No | 37% | <a href="https://job-boards.greenhouse.io/wonderschool/jobs/6359139003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Systems Engineer | WeRide | San Jose, CA | Not specified | ❌ No | 7% | <a href="https://jobs.lever.co/weride/b16618fa-d0be-451f-859d-b450e8e3dd82"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-02-07 · 2 roles · 1 H-1B sponsor match

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Forward Deployed Software Engineer - Warp Speed | Palantir | New York, NY | 1 | ✅ Yes | 19% | <a href="https://jobs.lever.co/palantir/13f99633-43b5-4459-8e84-25073f257c18"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Implant Manufacturing | Neuralink | Austin, Texas, United States | Not specified | ❌ No | 15% | <a href="https://boards.greenhouse.io/neuralink/jobs/6353417003?gh_jid=6353417003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-02-06 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Full Stack Engineer, Fleet Scheduling | OpenAI | San Francisco | Not specified | ❌ No | 26% | <a href="https://jobs.ashbyhq.com/openai/9d11e1d8-af1d-413b-873f-d8fac2bdee99"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-02-05 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Research Engineer, Machine Learning | Basis Research Institute | New York Office | Not specified | ❌ No | 33% | <a href="https://jobs.ashbyhq.com/basis-research/1e3dba92-ee3e-47c9-b321-695c3249479a"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-02-04 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Future Opportunities: Data Analytics and AI | 9th Way Insignia | United States - Remote | Not specified | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/9thwayinsignia/jobs/4521584008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-02-02 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer, Integrations | Topsort | Santiago, Santiago Metropolitan Region, Chile | 1 | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/topsort/jobs/4518094008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-01-30 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Associate Software Engineer in Test | Veeva | California - Pleasanton | Not specified | ❌ No | 15% | <a href="https://jobs.lever.co/veeva/452d7860-6d5f-45e0-bc00-6a2e8852698d"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Research Scientist, Compilers and Programming Languages | Basis Research Institute | New York Office | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/basis-research/96a52411-f147-41b5-86b5-e0fdfcd6b48d"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-01-29 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Research Scientist, Machine Learning / AI | Basis Research Institute | New York Office | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/basis-research/13c9e695-c800-46d5-b08c-5d57266ef578"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Firmware/ Embedded Systems Engineer | Skild AI | Pittsburgh, San Francisco, Bengaluru | Not specified | ❌ No | 7% | <a href="https://job-boards.greenhouse.io/skildai-careers/jobs/4511983008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-01-28 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer, Backend | Vercel | Remote - United States | Not specified | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/vercel/jobs/5430088004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-01-24 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| 1.5 Robotics AI Engineer – Field Foundation Models & Dynamics Foundation Models | Field AI | Irvine, CA | Not specified | ❌ No | 22% | <a href="https://jobs.lever.co/field-ai/ec9469b7-eebe-476d-8929-b72603be5a85"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Research Scientist - Datadog AI Research (DAIR) | Datadog | New York, New York, USA | Not specified | ❌ No | 22% | <a href="https://careers.datadoghq.com/detail/6572669/?gh_jid=6572669"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-01-23 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer - Embedded | Skydio | San Mateo, California, United States | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/skydio/ef9f7dd2-5a88-49b4-a507-d5fc9cad565a"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-01-22 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer, Simulator Evaluation | Waymo | Mountain View, California, United States; San Francisco, California, United States | 2 | ❌ No | 33% | <a href="https://careers.withwaymo.com/jobs?gh_jid=6562547"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Network Software Engineer, Real-Time Systems | Field AI | Irvine, CA | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/field-ai/f7995afe-f4e7-44d0-b206-53f8b1162949"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-01-21 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| ML Postdoc Researcher - LLMs & Generative AI | Truveta | Seattle, WA | Not specified | ❌ No | 44% | <a href="https://job-boards.greenhouse.io/truveta/jobs/5424558004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-01-15 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Research Scientist, Foundation Model | Prior Labs | Freiburg | Not specified | ❌ No | 30% | <a href="https://jobs.ashbyhq.com/prior-labs/b37463f2-775d-42e0-8c58-4ec26927534b"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-01-14 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer Intern, Robotics | Neuralink | Austin, Texas, United States; South San Francisco, California, United States | Not specified | ❌ No | 11% | <a href="https://boards.greenhouse.io/neuralink/jobs/5469305003?gh_jid=5469305003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-01-09 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software/Artificial Intelligence Engineer - Graduate Development Program | ION Group | Pisa | 0-2 | ❌ No | 19% | <a href="https://jobs.lever.co/ion/b4875cbe-2f8d-40cb-88b8-402a04c42993"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2025-01-07 · 9 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer, iOS Core Product | Speechify | Remote | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5411578004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Budapest, Hungary | Speechify | Budapest, Hungary | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981120004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Lima, Peru | Speechify | Lima, Peru | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981332004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Medellín, Colombia | Speechify | Medellín, Colombia | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981325004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Montevideo, Uruguay | Speechify | Montevideo, Uruguay | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981327004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Reykjavik, Iceland | Speechify | Reykjavik, Iceland | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981298004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Santiago, Chile | Speechify | Santiago, Chile | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981215004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Sarajevo, Bosnia and Herzegovina | Speechify | Sarajevo, Bosnia and Herzegovina | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981272004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, iOS Core Product - Yerevan, Armenia | Speechify | Yerevan, Armenia | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5981285004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-12-19 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Applied ML Engineer | Kognitos | Mountain View | Not specified | ❌ No | 26% | <a href="https://jobs.ashbyhq.com/Kognitos/bc1b3306-6d2b-41cc-b0ff-7ccb839778f5"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-12-17 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Full Stack Software Engineer | PerformYard | Arlington, Virginia, United States | Not specified | ❌ No | 15% | <a href="https://jobs.workable.com/view/dFfVnUKvydEYaiLjXNKw8b/remote-full-stack-software-engineer-in-arlington-at-performyard"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-12-13 · 4 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer - Orchestration | Neo4j | Malmö | Not specified | ❌ No | 22% | <a href="https://boards.greenhouse.io/neo4j/jobs/4426227006?gh_jid=4426227006"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| ML Research Resident | Elicit | Oakland, CA (or remote within US timezones) | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/elicit/e04136b7-57e5-44d5-9a7c-cced3e2cb0f8"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Back-End Software Engineer | Bask Health | United States | Not specified | ❌ No | 11% | <a href="https://jobs.workable.com/view/1ra61BLMatXettRMrdaMH9/remote-back-end-software-engineer-in-united-states-at-bask-health"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer Intern, Internal Apps | Neuralink | Austin, Texas, United States; South San Francisco, California, United States | Not specified | ❌ No | 11% | <a href="https://boards.greenhouse.io/neuralink/jobs/6083322003?gh_jid=6083322003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-12-12 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Generative AI - ML System Engineering | Meshy | Bay Area Office | Not specified | ❌ No | 26% | <a href="https://jobs.ashbyhq.com/meshy/90988ed5-f767-4c0d-9cbc-b69d792db1a9"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Drone Pilot for AI Training and Data Collection | TSMG | San Francisco, CA | Not specified | ❌ No | 15% | <a href="https://jobs.lever.co/tsmg/9ea7e756-d73e-4783-98a9-3a1dd63b292b"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-12-10 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer, Compute - Storage | OpenAI | San Francisco | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/openai/7649205e-20dc-4bb4-9358-69474a851132"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-12-03 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Embedded Software Engineer | Glydways | San Francisco-Bay Area, CA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/glydways/jobs/4594604007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-12-02 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Backend Engineer (BLR) | Revefi | Bangalore | 1 | ❌ No | 30% | <a href="https://jobs.lever.co/revefi/22239d2c-eb57-4a5e-a1d3-16d0f6bf196a"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-11-27 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Embedded Software Engineer Intern, Implant Embedded Systems | Neuralink | Austin, Texas, United States; South San Francisco, California, United States | 2 | ❌ No | 11% | <a href="https://boards.greenhouse.io/neuralink/jobs/6283663003?gh_jid=6283663003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-11-22 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer, Youth Well-Being | OpenAI | San Francisco | Not specified | ❌ No | 26% | <a href="https://jobs.ashbyhq.com/openai/f4e8a433-ae96-44ac-a7f9-97070335395f"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-11-19 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| ML Scientist | Layer Health | Boston or NYC | Not specified | ❌ No | 30% | <a href="https://job-boards.greenhouse.io/layerhealth/jobs/4408712008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-11-15 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Early Flight Software Engineer | Apex | Los Angeles | 1 | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/apex-technology-inc/a78c2ffd-bbaf-4884-b5a1-09631798f655"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-11-14 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Deep Learning Manipulation Engineer | Skild AI | Pittsburgh, San Mateo | Not specified | ❌ No | 26% | <a href="https://job-boards.greenhouse.io/skildai-careers/jobs/4408092008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-11-07 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer - Learned Trajectory Machine Learning Engineer | Zoox | Foster City, CA | Not specified | ❌ No | 26% | <a href="https://jobs.lever.co/zoox/9176aa65-14e3-4f9d-98f9-e755e9777d67"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Frontier Clusters Infrastructure | OpenAI | San Francisco | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/openai/770d5c3f-4e72-4b49-aec4-d444e8ad7a64"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-11-01 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer, Infrastructure - Autonomy & Robotics | DoorDash | San Francisco, CA | Not specified | ❌ No | 26% | <a href="https://job-boards.greenhouse.io/doordashusa/jobs/6367350"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-10-31 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer | Juicebox | San Francisco | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/juicebox/d6835260-53c4-467d-82f8-4cbedc154765"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-10-30 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Generative AI - 3D Foundation Model | Meshy | Bay Area Office | Not specified | ❌ No | 33% | <a href="https://jobs.ashbyhq.com/meshy/636fc439-83ad-4bf5-96a3-e25d8824d092"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-10-03 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Infrastructure Engineer | Tailscale | Remote (United States) | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/tailscale/jobs/4480736005"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Analyst with German language | Capco | Czech Republic - Brno | Not specified | ❌ No | 4% | <a href="https://job-boards.greenhouse.io/capco/jobs/6299628"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-10-02 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Embedded Software Engineer | Aquabyte | San Francisco Bay Area | Not specified | ❌ No | 22% | <a href="https://jobs.lever.co/aquabyte/ecff34ad-d659-4da1-af8d-0266103ba9bf"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-09-25 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Physical Design Intern - CPU/AI Hardware | Tenstorrent | Austin, Texas, United States; Santa Clara, California, United States | Not specified | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/tenstorrentuniversity/jobs/4526301007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-09-23 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Robotics Software Engineer | Skild AI | Pittsburgh, San Mateo, Bengaluru | Not specified | ❌ No | 26% | <a href="https://job-boards.greenhouse.io/skildai-careers/jobs/4136373008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-09-19 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Research Scientist | Skild AI | Pittsburgh, San Mateo | Not specified | ❌ No | 30% | <a href="https://job-boards.greenhouse.io/skildai-careers/jobs/4133795008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-09-18 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer (Full-Stack) | Replo | San Francisco | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/replo/1661d873-6c39-41f8-8390-a48d211728c4"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-09-17 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Research Scientist - Reinforcement Learning, Robotics | Applied Intuition | Sunnyvale | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/applied/52a070cf-4e1b-4fcc-bf73-727da8fb6d46"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Research Engineer - AI/RL Infrastructure | Applied Intuition | Sunnyvale | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/applied/091ed808-95c9-420b-8061-0ff2eb9342bc"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-09-13 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| AI Strategy Consultant, Frontier Tech | Scale AI | San Francisco, CA | Not specified | ❌ No | 30% | <a href="https://job-boards.greenhouse.io/scaleai/jobs/4472223005"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-09-12 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Full Stack Engineer | OffDeal | New York | 2 | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/offdeal/3f29a3f6-b336-459b-aee0-6975f7e2af24"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-09-11 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Machine Learning Engineer, Reinforcement Learning | Skild AI | Pittsburgh, San Mateo | Not specified | ❌ No | 33% | <a href="https://job-boards.greenhouse.io/skildai-careers/jobs/4125333008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-09-05 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer / Writer | Jane Street | New York, New York, United States | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/janestreet/jobs/7604415002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-08-30 · 3 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Intern - AI Compilers | Tenstorrent | Santa Clara, California, United States | Not specified | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/tenstorrentuniversity/jobs/4501189007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Machine Learning for Physical Design Intern - CPU/AI Hardware | Tenstorrent | Austin, Texas, United States | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/tenstorrentuniversity/jobs/4501164007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| CPU Core Performance Verification Intern - CPU/AI Hardware | Tenstorrent | Austin, Texas, United States | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/tenstorrentuniversity/jobs/4501134007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-08-29 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Daft - US - Software Engineer Interest Form | mthree | USA | Not specified | ❌ No | 4% | <a href="https://job-boards.greenhouse.io/mthreerecruitingportal/jobs/4398568006"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-08-27 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Machine Learning Engineer - LLM, AI & Robotics | XPENG Motors | Santa Clara, CA | Not specified | ❌ No | 33% | <a href="https://job-boards.greenhouse.io/xpengmotors/jobs/7613846002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Machine Learning Engineer, Robotics | XPENG Motors | Santa Clara, CA | Not specified | ❌ No | 33% | <a href="https://job-boards.greenhouse.io/xpengmotors/jobs/7614027002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-08-24 · 2 roles · 2 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| ML Infra Engineer | Physical Intelligence | San Francisco | Not specified | ✅ Yes | 22% | <a href="https://jobs.ashbyhq.com/physicalintelligence/70ebf855-16df-4879-a6a7-ee0161174acc"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Research Scientist | Physical Intelligence | San Francisco | Not specified | ✅ Yes | 7% | <a href="https://jobs.ashbyhq.com/physicalintelligence/f83ba447-2261-4832-95db-a2f88454e0ba"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-08-21 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer - Calibration | Applied Intuition | Sunnyvale | 2 | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/applied/eb8280ed-23af-4bff-9685-b09419ee750d"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-08-15 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Quantitative Researcher - Machine Learning | Point72 | New York | Not specified | ❌ No | 22% | <a href="https://boards.greenhouse.io/point72/jobs/7297513002?gh_jid=7297513002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Machine Learning Researcher - Intern | Point72 | New York | Not specified | ❌ No | 19% | <a href="https://boards.greenhouse.io/point72/jobs/7302611002?gh_jid=7302611002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-08-13 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer - Simulators | MatX | Mountain View, CA | Not specified | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/matx/jobs/4102858008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-08-07 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Data Engineer/Analyst - Graduate Development Program | ION Group | Trento | 0-2 | ❌ No | 11% | <a href="https://jobs.lever.co/ion/d7c926ae-367a-4349-93db-1eda963cc132"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-07-31 · 1 role · 1 H-1B sponsor match

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Golang Software Engineer (VISTA BIGHITTER), BS+7, Telework | Link | Annapolis Junction, MD | Not specified | ✅ Yes | 11% | <a href="https://jobs.lever.co/linkllc/2fdb638a-0bfe-4a60-96ba-c3cdabf0923a"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-07-24 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Machine Learning Engineer, Core Engineering | Pinterest | San Francisco, CA, US; Palo Alto, CA, US; Seattle, WA, US; Remote, US | 2 | ❌ No | 30% | <a href="https://www.pinterestcareers.com/jobs/?gh_jid=6121450"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-07-23 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Machine Learning Engineer, Monetization Engineering | Pinterest | San Francisco, CA, US; Palo Alto, CA, US; Seattle, WA, US | 2 | ❌ No | 30% | <a href="https://www.pinterestcareers.com/jobs/?gh_jid=6121543"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-07-19 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| AI Tester with French | TSMG | Lausanne | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/tsmg/937b4478-b148-494d-b188-389a285d2f1a"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-07-10 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer, Real Time | OpenAI | Seattle | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/openai/75420421-5a2a-4d99-8755-9eeff799de95"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-07-08 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Data Engineer | Figma | San Francisco, CA • New York, NY • United States | Not specified | ❌ No | 19% | <a href="https://boards.greenhouse.io/figma/jobs/5220003004?gh_jid=5220003004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Junior Software Engineer | mthree | USA | 0-2 | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/mthreerecruitingportal/jobs/4383912006"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-07-02 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Systems Engineer | InterWorks | Oklahoma City, Oklahoma, United States | Not specified | ❌ No | 7% | <a href="https://job-boards.greenhouse.io/interworks/jobs/4382931006"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-06-27 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Junior Business Scientist, Strategy & Data Science | Ekimetrics | Shanghai | 2 | ❌ No | 19% | <a href="https://jobs.lever.co/ekimetrics/358be550-80f6-4fb5-bc2a-aceceb8fd8a3"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-06-21 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Junior Software Engineer | mthree | USA | 0-2 | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/mthreerecruitingportal/jobs/4374589006"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-06-13 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer Intern, Infrastructure | Neuralink | South San Francisco, California, United States | Not specified | ❌ No | 26% | <a href="https://boards.greenhouse.io/neuralink/jobs/5469298003?gh_jid=5469298003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-06-11 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| AI Engineer | Elicit | Oakland, CA (or remote within US timezones) | Not specified | ❌ No | 30% | <a href="https://jobs.ashbyhq.com/elicit/d27d51d7-b318-4cb0-9b88-c37de18905f3"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Site Reliability Engineer / Production Support Analyst | mthree | USA | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/mthreerecruitingportal/jobs/4374788006"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-06-06 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Associate Software Engineer in Test | Veeva | Massachusetts - Boston | Not specified | ❌ No | 15% | <a href="https://jobs.lever.co/veeva/8683a486-a11b-44be-8824-d3afdaa37b2d"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-06-04 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer, Product Backend | Glean | Mountain View, CA | Not specified | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/gleanwork/jobs/4428090005"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Junior Software Engineer | mthree | USA | 0-2 | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/mthreerecruitingportal/jobs/4374540006"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-06-03 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Infrastructure Engineer | Railway | Remote (United States) | Not specified | ❌ No | 7% | <a href="https://jobs.ashbyhq.com/railway/b8072f95-043f-404d-a313-f0bdf8dd3c81"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-05-30 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer (Backend Rust) | N1 | New York City | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/n1/99a78724-a7eb-4801-9e75-cf4465950567"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-05-23 · 7 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| AI Scientist - Palo Alto | Mistral AI | Palo Alto | Not specified | ❌ No | 22% | <a href="https://jobs.lever.co/mistral/7b20d2c8-d5a7-4efd-a13e-05d920ec5985"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Evaluators for AI training (English language) | TSMG | Ivano-Frankivsk | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/tsmg/661d52f5-9ef9-4b97-935b-889f744c14d0"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Evaluators for AI training (English language) | TSMG | Ivano-Frankivsk | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/tsmg/df7b54e9-7a33-489c-94c4-b725cf58a3c5"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Evaluators for AI training (English language) | TSMG | Kyiv | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/tsmg/c8c840fb-1348-48bf-a924-b969236dba77"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Evaluators for AI training (English language) | TSMG | Kyiv | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/tsmg/35c11f80-aea0-42e2-b52c-75a0e89fbef5"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Evaluators for AI training (English language) | TSMG | Lviv | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/tsmg/a797cd3d-f990-4693-8ed7-b18ff19cc962"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Evaluators for AI training (English language) | TSMG | Lviv | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/tsmg/d7d0e689-ae9a-4b00-8ed7-68c0abe0d8c9"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-05-22 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Research Engineer, Applied AI Engineering | OpenAI | San Francisco | Not specified | ❌ No | 44% | <a href="https://jobs.ashbyhq.com/openai/d44c9f70-4aef-45a4-a36a-54fb65663ccb"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-05-20 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Machine Learning Performance Engineer | Jane Street | New York, New York, United States | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/janestreet/jobs/7449077002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Machine Learning Performance Engineer | Jane Street | New York, New York, United States | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/janestreet/jobs/7449190002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-05-16 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Quality Control Specialist (AI Training) | TSMG | Lviv | 1 | ❌ No | 4% | <a href="https://jobs.lever.co/tsmg/01509e78-b73d-482c-9bb7-ed3ef2744675"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Quality Control Specialist (AI Training) | TSMG | Kyiv | 1 | ❌ No | 4% | <a href="https://jobs.lever.co/tsmg/07975284-fb48-42ec-bf36-1836334047f4"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-05-14 · 11 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| AI tester with Arabic language | TSMG | Cairo | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/tsmg/656b4af1-e142-4eb1-98fd-da5e1bff0459"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI tester with French language | TSMG | Barcelona | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/tsmg/3d3faa0c-f63d-4eca-9de5-5457c2f613b0"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI tester with French language | TSMG | Rome | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/tsmg/74b46238-50c8-41fe-8b13-4c5deb5c53e6"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI tester with French language | TSMG | Chișinău | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/tsmg/1fbb9a0a-4d1e-4f18-a70d-d7400479a523"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI tester with French language | TSMG | Bucharest | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/tsmg/9ae5670f-41a2-4af9-b19f-4ef70dfb4276"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI tester with German language | TSMG | Bratislava | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/tsmg/12dba196-5ff2-46ba-a0ff-443dbffb37c3"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI tester with German language | TSMG | Bucharest | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/tsmg/7691e1bb-d251-4432-a78c-022d2ac623be"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI tester with German language | TSMG | Warsaw | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/tsmg/8a103fb1-5491-4ab5-9c13-2fcb6a194d03"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI tester with Italian language | TSMG | Rome | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/tsmg/6517b738-8c37-4799-9607-1f85312959b5"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI tester with Portuguese language | TSMG | Lisbon | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/tsmg/9752c307-600f-4604-b5ba-d0bf3e187277"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI tester with Spanish language | TSMG | Barcelona | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/tsmg/e4b32839-b580-4be3-a978-f80c4f5ce183"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-05-01 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Systems Engineer | InterWorks | Stillwater, Oklahoma, United States | Not specified | ❌ No | 7% | <a href="https://job-boards.greenhouse.io/interworks/jobs/4365316006"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-04-30 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| AI Engineer - Graduate Development Program | ION Group | Trento | 0-2 | ❌ No | 30% | <a href="https://jobs.lever.co/ion/f93f9d1a-9006-405e-ba38-9e79b98f4301"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-04-25 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Frontend Engineer | Doss | San Francisco | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/doss/be9a271a-75d0-4ab5-9fdb-0f64c641c692"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Fullstack Engineer | Doss | San Francisco | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/doss/c2b0e305-3138-48be-ac45-95e5fec10905"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-04-20 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer, Collective Communication | OpenAI | San Francisco | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/openai/340c0c22-8d8f-4232-b17e-f642b64c25c3"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-04-18 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Machine Learning Engineer, PhD Intern (Fall) | Instacart | United States - Remote | Not specified | ❌ No | 33% | <a href="https://instacart.careers/job/?gh_jid=5917202"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-04-16 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Flight Software Engineer | Astranis | San Francisco | Not specified | ❌ No | 7% | <a href="https://job-boards.greenhouse.io/astranis/jobs/4015622006"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-04-12 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Systems Engineer | InterWorks | Tulsa, Oklahoma, United States | Not specified | ❌ No | 7% | <a href="https://job-boards.greenhouse.io/interworks/jobs/4334271006"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-04-11 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Python and Kubernetes Software Engineer - Data, Workflows, AI/ML & Analytics | Canonical | Home based - Worldwide | Not specified | ❌ No | 30% | <a href="https://job-boards.greenhouse.io/canonical/jobs/5703396"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-03-29 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Data Scientist | Applied Physics | New York, New York, United States | Not specified | ❌ No | 11% | <a href="https://jobs.workable.com/view/cZq2UYfco6uEYGxzgG6rvb/hybrid-data-scientist-in-new-york-at-applied-physics"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Machine Learning Specialist | Applied Physics | New York, New York, United States | Not specified | ❌ No | 7% | <a href="https://jobs.workable.com/view/bAKWpfKsMCPQPn2jpXS19S/machine-learning-specialist-in-new-york-at-applied-physics"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-03-28 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer - Model Performance | Baseten | San Francisco | Not specified | ❌ No | 37% | <a href="https://jobs.ashbyhq.com/baseten/d29e748c-7209-460d-a024-8f77ae0a3d4d"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Applied AI Inference - Forward Deployed Engineer | Baseten | San Francisco | 2 | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/baseten/84c1801c-1a65-49fb-aaaa-beeafd530e7e"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-03-26 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer | Vooma | San Francisco Office | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/vooma/19e806f0-fca9-4e71-98aa-21d1b9751c37"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-03-22 · 2 roles · 1 H-1B sponsor match

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Forward Deployed AI Engineer | Palantir | New York, NY | Not specified | ✅ Yes | 26% | <a href="https://jobs.lever.co/palantir/636fc05c-d348-4a06-be51-597cb9e07488"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer | Castle | Harvard Square | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/castle/932f2d90-0233-4f8c-9ca6-5bf63b88d6cd"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-03-14 · 5 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer, Diagnostics & Tools | Harbinger Motors | Garden Grove, CA | Not specified | ❌ No | 26% | <a href="https://job-boards.greenhouse.io/harbingermotors/jobs/4297336007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer | Aviture | Omaha, Nebraska, United States | Not specified | ❌ No | 11% | <a href="https://jobs.workable.com/view/cCif3AzVQKiygnPyurfZ98/software-engineer-in-omaha-at-aviture"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer with Clearance | Aviture | Omaha, Nebraska, United States | Not specified | ❌ No | 11% | <a href="https://jobs.workable.com/view/1GsT9rVfEfFyHjZPEjghD2/software-engineer-with-clearance-in-omaha-at-aviture"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Web Developer | Steady Vision | Boston, Massachusetts, United States | Not specified | ❌ No | 4% | <a href="https://jobs.workable.com/view/2KefvjGba7zPxewZFgCcU5/remote-web-developer-in-boston-at-steady-vision"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Web Developer / Web Design - WordPress | Ebeacon | Overland Park, Kansas, United States | Not specified | ❌ No | 4% | <a href="https://jobs.workable.com/view/rzTwDYSJuNJpkKFuHYibom/web-developer-%2F-web-design---wordpress-in-overland-park-at-ebeacon"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-03-05 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Machine Learning Engineer, Voice | Speak | San Francisco | Not specified | ❌ No | 26% | <a href="https://jobs.ashbyhq.com/speak/e78edff4-5135-4c68-932d-e449ee460ea3"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-02-28 · 3 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer - Compiler | MatX | Mountain View, CA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/matx/jobs/4003260008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer - Kernels | MatX | Mountain View, CA | Not specified | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/matx/jobs/4003259008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Android Developer, New York | ION Group | New York | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/ion/b036470e-3c18-4301-95fe-5d53d4b1f457"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-02-23 · 1 role · 1 H-1B sponsor match

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer - Frontend Developer Productivity | Palantir | New York, NY | 2 | ✅ Yes | 19% | <a href="https://jobs.lever.co/palantir/71ed917e-850a-484b-9454-fa66bdf24540"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-02-07 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| AI Infrastructure Engineer | Spellbrush | San Francisco | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/spellbrush/55633abd-f242-4e43-b390-4508d7bb65ea"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Front-End Engineer (Anime) | Spellbrush | San Francisco | Not specified | ❌ No | 7% | <a href="https://jobs.ashbyhq.com/spellbrush/d490168e-2b28-479d-88a9-64d63e6fa8b3"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-02-05 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Deep Learning Compiler Engineer | Quadric | Burlingame, California, United States | Not specified | ❌ No | 26% | <a href="https://apply.workable.com/j/C8C03A3826"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-01-24 · 14 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer, Platform | Speechify | Remote | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5058944004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Almaty, Kazakhstan | Speechify | Almaty, Kazakhstan | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974405004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Bishkek, Kyrgyzstan | Speechify | Bishkek, Kyrgyzstan | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974407004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Bogotá, Colombia | Speechify | Bogotá, Colombia | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974429004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Budapest, Hungary | Speechify | Budapest, Hungary | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974351004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Casablanca, Morocco | Speechify | Casablanca, Morocco | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974426004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Lima, Peru | Speechify | Lima, Peru | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974437004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Medellín, Colombia | Speechify | Medellín, Colombia | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974431004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Reykjavik, Iceland | Speechify | Reykjavik, Iceland | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974336004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - San José, Costa Rica | Speechify | San José, Costa Rica | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974435004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Santiago, Chile | Speechify | Santiago, Chile | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974427004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Sarajevo, Bosnia and Herzegovina | Speechify | Sarajevo, Bosnia and Herzegovina | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974324004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Tbilisi, Georgia | Speechify | Tbilisi, Georgia | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974341004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Platform - Yerevan, Armenia | Speechify | Yerevan, Armenia | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/speechify/jobs/5974343004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2024-01-15 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Rust Backend Engineer | Svix | San Francisco (On-Site) | Not specified | ❌ No | 4% | <a href="https://jobs.ashbyhq.com/svix/84e99bc9-5cd6-4af0-af84-17d63a7494b5"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2023-12-15 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Cubist Data Scientist | Point72 | New York | Not specified | ❌ No | 19% | <a href="https://boards.greenhouse.io/point72/jobs/7045938002?gh_jid=7045938002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2023-11-14 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Research Scientist | Center for AI Safety | San Francisco, CA | Not specified | ❌ No | 19% | <a href="https://jobs.lever.co/aisafety/0e911ab2-89e0-4936-83e6-034f7e2f8977"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2023-11-10 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer - Computer Vision | Verkada | San Mateo, CA United States | 2 | ❌ No | 37% | <a href="https://job-boards.greenhouse.io/verkada/jobs/4128624007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2023-11-07 · 1 role · 1 H-1B sponsor match

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| PhD GenAI Research Scientist Intern | Databricks | San Francisco, California | Not specified | ✅ Yes | 26% | <a href="https://databricks.com/company/careers/open-positions/job?gh_jid=7011263002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2023-11-03 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Machine Learning Research Scientist, Behavior Planning and Prediction | Nuro | Mountain View, California (HQ) | Not specified | ❌ No | 19% | <a href="https://nuro.ai/careersitem?gh_jid=5434059"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2023-10-14 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Security Software Engineer | Canonical | Home based - Worldwide | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/canonical/jobs/5146620"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2023-10-11 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Web Frontend Engineer - JS, CSS, React, Flutter | Canonical | Home based - Worldwide | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/canonical/jobs/5150422"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2023-09-05 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Frontend Engineer | Elicit | Oakland, CA (or remote within US timezones) | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/elicit/b5e218b8-8730-4254-b026-1fe2fe02c3eb"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2023-09-01 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| DoW Skillbridge Fellowship- Software Engineer | PVM | Remote- US | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/pvminc/jobs/4073946007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2023-08-02 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Scientific Software Engineer | Proxima | New York | Not specified | ❌ No | 33% | <a href="https://jobs.ashbyhq.com/proxima/270191ee-a215-4b82-ba0c-301a4f356a3a"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer - Casablanca CDI - Theodo Maroc | Theodo | Casablanca | Not specified | ❌ No | 19% | <a href="https://jobs.lever.co/theodo/91f15a7a-c6be-4520-9b71-0e43f617b85e"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2023-07-19 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Distributed Systems Engineer | Canonical | Home based - Worldwide | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/canonical/jobs/4581200"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2023-07-07 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer, New Grad | Perpay | Philadelphia, Pennsylvania, United States | 0-2 | ❌ No | 33% | <a href="https://job-boards.greenhouse.io/perpay/jobs/4034578007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Mid-Level Software Engineer | Perpay | Philadelphia, Pennsylvania, United States | 2 | ❌ No | 26% | <a href="https://job-boards.greenhouse.io/perpay/jobs/4034545007"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2023-06-29 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Machine Learning Engineer | Neuralink | Austin, Texas, United States; South San Francisco, California, United States | Not specified | ❌ No | 30% | <a href="https://boards.greenhouse.io/neuralink/jobs/5663271003?gh_jid=5663271003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2023-06-10 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Scientific Data Engineer | Uncountable | San Francisco, New York | Not specified | ❌ No | 15% | <a href="https://jobs.ashbyhq.com/uncountable/48cbdfbc-c377-49bd-b39b-4c2d77357135"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2023-03-29 · 3 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Surveyor/Field Data Analyst | TSMG | Rouen | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/tsmg/3e964f0b-c3ee-410c-b6fa-cdc6435f6baf"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Surveyor/Field Data Analyst | TSMG | Bordeaux | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/tsmg/5d956f96-e518-4dba-adbe-0c424b4d8fcf"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Surveyor/Field Data Analyst | TSMG | Lille | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/tsmg/7879aaf4-e1bb-481f-83b1-6dafdc82a438"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2023-03-19 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer, Full-Stack | Loop | Chicago, IL | Not specified | ❌ No | 26% | <a href="https://job-boards.greenhouse.io/loop/jobs/4830548004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2023-03-09 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer, Frontend | Ramp | New York, NY (HQ) | 2 | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/ramp/4e64ab86-4e30-403b-b1b9-41dc052570ce"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2023-03-08 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer | Futurex | Bulverde, Texas, United States | Not specified | ❌ No | 7% | <a href="https://jobs.workable.com/view/4PKarXfoQPLUVe3MMMgazQ/software-engineer-in-bulverde-at-futurex"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2023-02-03 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer - Cloud Images | Canonical | Home Based - Americas | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/canonical/jobs/4398031"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2023-02-01 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer II, Backend | Pinterest | San Francisco, CA, US; Seattle, WA, US | 2 | ❌ No | 19% | <a href="https://www.pinterestcareers.com/jobs/?gh_jid=4813946"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2023-01-19 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer | Lever | Ann Arbor, MI \| Palo Alto, CA | Not specified | ❌ No | 7% | <a href="https://jobs.lever.co/leverdemo/e3df1c26-ae1e-4461-bb63-8e623f079734"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2023-01-09 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Data Engineer | Jane Street | New York, New York, United States | Not specified | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/janestreet/jobs/6558007002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2022-11-18 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Machine Learning Engineer | Jane Street | New York, New York, United States | Not specified | ❌ No | 30% | <a href="https://job-boards.greenhouse.io/janestreet/jobs/6485460002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2022-11-15 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Helix AI Engineer, Perception | Figure | San Jose, CA | Not specified | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/figureai/jobs/4007375006"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2022-08-10 · 2 roles · 2 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer - Apollo Platform | Palantir | New York, NY | Not specified | ✅ Yes | 15% | <a href="https://jobs.lever.co/palantir/8f308f3e-43d2-49c9-accd-cc7af0f1565c"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer - Apollo Platform | Palantir | Seattle, WA | Not specified | ✅ Yes | 15% | <a href="https://jobs.lever.co/palantir/afea07a8-2721-45e6-a9ca-6580f3f9783c"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2022-08-08 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Site Reliability Engineer | Canonical | Home based - Worldwide | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/canonical/jobs/4468036"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2022-08-01 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer | Allium | Remote | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/allium/d5c0f988-67ac-4388-bd54-1970c8cc17f5"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2022-07-29 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer - Maps Infrastructure | Applied Intuition | Sunnyvale | 2 | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/applied/4e756248-6edd-448e-8fbe-28d90b6deab2"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2022-07-19 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Cloud Engineer - Graduate Development Program | ION Group | Pisa | 0-2 | ❌ No | 7% | <a href="https://jobs.lever.co/ion/c01c2b2e-cd2f-43bc-8d69-71dd3c70a14c"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2022-06-30 · 1 role · 1 H-1B sponsor match

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Forward Deployed Software Engineer, Internship - US Government | Palantir | New York, NY | Not specified | ✅ Yes | 19% | <a href="https://jobs.lever.co/palantir/e0010393-c300-446f-bf67-fa2ef067f16f"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2022-06-24 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Front End Software Engineer | Jane Street | New York, New York, United States | Not specified | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/janestreet/jobs/6184529002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2022-06-08 · 3 roles · 3 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Systems Engineer - Business Systems | Palantir | New York, NY | 1 | ✅ Yes | 7% | <a href="https://jobs.lever.co/palantir/78dbb616-cf3c-489c-9eb2-e6fc9bd9993a"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Systems Engineer - Business Systems | Palantir | Washington, D.C. | 1 | ✅ Yes | 7% | <a href="https://jobs.lever.co/palantir/da426d8b-5963-42e5-9b19-84649cb519cc"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Systems Engineer - Business Systems | Palantir | Palo Alto, CA | 1 | ✅ Yes | 7% | <a href="https://jobs.lever.co/palantir/e1d6117e-2ee0-4cf6-8040-256c3009389f"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2022-05-29 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer (fullstack) | Waterfall | New York, NY | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/waterfall/e6a70c82-b41e-4a48-9e9f-f852d880cec2"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2022-05-25 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer - Ubuntu Server Certification | Canonical | Home Based - Americas | Not specified | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/canonical/jobs/4272811"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2022-04-21 · 4 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Machine Learning Engineer | Hive | Seattle | 2 | ❌ No | 37% | <a href="https://jobs.lever.co/hive/a06ede4e-46e3-40c8-b2e6-69af1658ab50"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Systems Engineer / DevOps | Hive | Seattle | 2 | ❌ No | 19% | <a href="https://jobs.lever.co/hive/efb68714-6896-4987-8d12-f06622323b2a"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer - Frontend | Hive | Seattle | 1 | ❌ No | 15% | <a href="https://jobs.lever.co/hive/00c84379-62f1-45c9-9ec6-f882a1a7549b"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer - Backend | Hive | Seattle | Not specified | ❌ No | 7% | <a href="https://jobs.lever.co/hive/432e24aa-953f-4031-9ea7-75a00b183b70"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2022-04-08 · 3 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Machine Learning Engineer, Search Quality | Glean | Mountain View, CA | 2 | ❌ No | 26% | <a href="https://job-boards.greenhouse.io/gleanwork/jobs/4006735005"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Fullstack | Glean | Mountain View, CA | Not specified | ❌ No | 26% | <a href="https://job-boards.greenhouse.io/gleanwork/jobs/4006734005"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Frontend | Glean | Mountain View, CA | Not specified | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/gleanwork/jobs/4006733005"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2022-03-26 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Embedded & Desktop Linux Systems Engineer - Optimisation | Canonical | Home based - Worldwide | Not specified | ❌ No | 7% | <a href="https://job-boards.greenhouse.io/canonical/jobs/3821346"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2022-02-23 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer - Python and K8s | Canonical | Home based - Worldwide | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/canonical/jobs/3752633"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2021-11-01 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| New Grad Software Engineer, Growth | Secureframe | New York, NY | 2 | ❌ No | 19% | <a href="https://jobs.lever.co/secureframe/29ff0477-faeb-44d6-abb3-8e894fc92a22"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2021-09-22 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Data Analyst - Evergreen | Lever | Bay Area, CA | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/leverdemo/a4f63c25-abbe-4c73-89a7-7b79d432f264"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2021-09-07 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer - App Stores | Canonical | Home based - Worldwide | Not specified | ❌ No | 15% | <a href="https://job-boards.greenhouse.io/canonical/jobs/3159992"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2021-09-02 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer, Full-Stack | Loop | San Francisco, CA | Not specified | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/loop/jobs/4102236004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2021-07-28 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| SAP Data Analyst (Contract) | Two95 International Inc. | Irving, Texas, United States | 1 | ❌ No | 4% | <a href="https://jobs.workable.com/view/3Lgayzt1Rwp6b2K2Bavy78/sap-data-analyst-(contract)-in-irving-at-two95-international-inc."><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2021-07-22 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer, Sustaining Engineering | Canonical | Home based - Worldwide | Not specified | ❌ No | 26% | <a href="https://job-boards.greenhouse.io/canonical/jobs/3326693"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2021-07-11 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer - Solutions Engineering | Canonical | Home based - Worldwide | Not specified | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/canonical/jobs/3290946"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2021-07-09 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer, Cloud - Sustaining Engineering | Canonical | Home based - Worldwide | Not specified | ❌ No | 26% | <a href="https://job-boards.greenhouse.io/canonical/jobs/3062022"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2021-07-01 · 1 role · 1 H-1B sponsor match

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Forward Deployed Software Engineer, Internship - US Government | Palantir | Washington, D.C. | Not specified | ✅ Yes | 19% | <a href="https://jobs.lever.co/palantir/e6ff8bf2-135e-474d-ad37-24f490ae1dd2"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2021-06-28 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer - Python - Cloud - graduate level | Canonical | Home Based - Americas | 0-2 | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/canonical/jobs/3257589"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2021-06-04 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| AI Engineer (in person) | SEP | Westfield, IN | Not specified | ❌ No | 22% | <a href="https://jobs.lever.co/sep/add5bcc4-329f-4c59-aafb-6581f16c7d81"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2021-04-15 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer | Smartcuts | Remote | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/smartcuts/972aa8d9-d2e9-4bdb-b410-6a15f460e9cf"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2021-03-18 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Distributed Systems Testing Software Engineer, Python / Go | Canonical | Home based - Worldwide | Not specified | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/canonical/jobs/2969042"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2021-02-25 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Financial Software Engineer | Galatea Associates | Somerville, MA | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/galatea-associates/ea475dfe-2e0b-4e6b-8dd7-88e4e85f9dcb"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2021-01-23 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Machine Learning Engineer | Elicit | Oakland, CA (or remote within US timezones) | Not specified | ❌ No | 26% | <a href="https://jobs.ashbyhq.com/elicit/913a03d5-bd26-4c64-8346-21a029f344f7"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2021-01-15 · 4 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Machine Learning Engineer | Hive | San Francisco | 2 | ❌ No | 37% | <a href="https://jobs.lever.co/hive/fb175ecc-b6ba-4242-a84a-8699f9b0e971"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Systems Engineer / DevOps | Hive | San Francisco | 2 | ❌ No | 19% | <a href="https://jobs.lever.co/hive/1da35c5a-313c-4f3b-a9c7-06e6f2fa20bd"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer - Frontend | Hive | San Francisco | 1 | ❌ No | 15% | <a href="https://jobs.lever.co/hive/e49f6b1d-1c84-4956-8b86-d6d36aead905"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer - Backend | Hive | San Francisco | Not specified | ❌ No | 7% | <a href="https://jobs.lever.co/hive/9461e715-9e58-4414-bc9b-13e449f92b08"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2020-11-16 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer (Python/Linux/Packaging) | Canonical | Home Based - Americas | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/canonical/jobs/2413329"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2020-11-03 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer, Robotics | Neuralink | Austin, Texas, United States; South San Francisco, California, United States | Not specified | ❌ No | 11% | <a href="https://boards.greenhouse.io/neuralink/jobs/4205469003?gh_jid=4205469003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2020-10-19 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Data Scientist | Lever |  | Not specified | ❌ No | 7% | <a href="https://jobs.lever.co/leverdemo/0219c58c-c62b-462e-b2d6-bc4f98714b79"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2020-10-07 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Data Science PhD Intern | Docugami | Kirkland, Washington, United States | Not specified | ❌ No | 26% | <a href="https://job-boards.greenhouse.io/docugami/jobs/4192122003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2020-05-02 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| General Software Engineer | WeRide | San Jose, CA | Not specified | ❌ No | 15% | <a href="https://jobs.lever.co/weride/2f22df18-e019-450e-bcfa-9b1c7b94334f"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Perception Engineer – ML/CV and Algorithms | WeRide | San Jose, CA | Not specified | ❌ No | 15% | <a href="https://jobs.lever.co/weride/628b7118-d946-47a2-a03b-ac034622d908"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2020-04-02 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Infrastructure Engineer | Lever | Boston, MA | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/leverdemo/c48774b7-1e36-4296-a870-ceab2ae6845a"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2020-02-11 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Machine Learning / Data Scientist | Docugami | Kirkland, Washington, United States | Not specified | ❌ No | 30% | <a href="https://job-boards.greenhouse.io/docugami/jobs/4016974003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2020-02-07 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer | Lever | Atlanta, Georgia | Not specified | ❌ No | 7% | <a href="https://jobs.lever.co/leverdemo/72eeb371-5ecb-4e54-a8b1-da57475b861f"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2019-10-20 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Full Stack Engineer | Lever | San Francisco, CA | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/leverdemo/4676ee31-6f91-4860-967e-7ccf87289307"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2019-09-25 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer | Lever | Atlanta, Georgia | Not specified | ❌ No | 7% | <a href="https://jobs.lever.co/leverdemo/34fc79c4-f981-43ff-8213-ab6837642ba0"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2019-09-05 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Data Engineer | Lever | San Francisco, CA | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/leverdemo/86651fe0-f324-480a-9244-1cc91b80d8a6"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2019-09-03 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Data Engineer | Lever | San Francisco, CA | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/leverdemo/45e016b1-e4b9-408d-9f4a-51f8c9877bfd"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2019-07-24 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer | Lever |  | Not specified | ❌ No | 15% | <a href="https://jobs.lever.co/leverdemo/b25088e2-66e9-44a4-abce-65fdbb4f1223"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2019-05-30 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer | Lever | Austin, TX | Not specified | ❌ No | 7% | <a href="https://jobs.lever.co/leverdemo/ebe2731d-5337-4569-892d-c2aaea4ad648"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2019-05-06 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer | Jane Street | New York, New York, United States | Not specified | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/janestreet/jobs/4274288002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2019-05-02 · 3 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Machine Learning Researcher | Jane Street | New York, New York, United States | Not specified | ❌ No | 22% | <a href="https://job-boards.greenhouse.io/janestreet/jobs/4276720002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer | Lever | Austin, TX | Not specified | ❌ No | 7% | <a href="https://jobs.lever.co/leverdemo/6bd49093-3083-4e71-a277-e5029056b838"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Full Stack Engineer | Lever | Atlanta, Georgia | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/leverdemo/b2fc5486-2621-4f7d-8c79-624839b879fe"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2019-04-26 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Full Stack Engineer | Lever |  | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/leverdemo/933ae4ee-b385-460d-a82b-01beaf3a7392"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2019-03-22 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer | Lever | Bay Area, CA | Not specified | ❌ No | 7% | <a href="https://jobs.lever.co/leverdemo/004f960b-c8be-4e98-8d37-b3be47f99ea0"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2019-02-26 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer | Lever |  | Not specified | ❌ No | 7% | <a href="https://jobs.lever.co/leverdemo/7179c076-125f-4de3-a7d2-7bb06e6bcfef"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2019-02-22 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer | Miracle Software Systems | Novi, MI, United States | Not specified | ❌ No | 4% | <a href="https://jobs.smartrecruiters.com/MiracleSoftwareSystem1/743999684206726"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2019-01-17 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| iOS Developer | Lever |  | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/leverdemo/3b41579d-b84d-4da5-b008-9b9683ad5ef3"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2018-12-27 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Front End Engineer | Lever | Atlanta, Georgia | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/leverdemo/5f5aa078-c5d8-4e3d-a8a4-b5bc132f7b4c"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2018-12-17 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Data Analyst | Lever | Denver, CO | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/leverdemo/e5253302-02bb-436c-a2e0-75c31551b7e0"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2018-10-29 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| 6 months Internship in Strategy & Data Science \| New York | Ekimetrics | New York | 2 | ❌ No | 15% | <a href="https://jobs.lever.co/ekimetrics/d8f0b664-ad5b-4111-a1dc-a8143934bf24"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2018-10-24 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Data Scientist | Lever |  | Not specified | ❌ No | 7% | <a href="https://jobs.lever.co/leverdemo/6f295a3a-0cc2-4357-ad61-34255ea48f1e"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2017-11-13 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Frontend Engineer | Hive | Delhi | 2 | ❌ No | 11% | <a href="https://jobs.lever.co/hive/49c64df4-209b-4334-8f98-7e1dc6440ed1"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2017-09-11 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Systems Coordinator, Radiology, Data Analytics | Randstad | Aurora, CO, United States | Not specified | ❌ No | 11% | <a href="https://jobs.smartrecruiters.com/Randstad4/743999659533473"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2017-09-05 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Systems Engineer | Randstad | Warren, NJ, United States | Not specified | ❌ No | 11% | <a href="https://jobs.smartrecruiters.com/Randstad4/743999659206928"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| ETL DataStage Consultant | Saxon Global | Oakland, CA, United States | 2 | ❌ No | 4% | <a href="https://jobs.smartrecruiters.com/SaxonGlobal/743999659183544"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2017-08-17 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Machine Learning Engineer | Lever |  | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/leverdemo/269227e5-6453-4421-a894-af9fc0e84793"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2017-08-09 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Data Scientist | Saxon Global | Fort Mill, SC, United States | Not specified | ❌ No | 4% | <a href="https://jobs.smartrecruiters.com/SaxonGlobal/743999657508817"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Scientist | Saxon Global | Chesterbrook, PA, United States | Not specified | ❌ No | 4% | <a href="https://jobs.smartrecruiters.com/SaxonGlobal/743999657496022"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2017-08-02 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer | Global Channel Management | Wilsonville, OR, United States | Not specified | ❌ No | 4% | <a href="https://jobs.smartrecruiters.com/GlobalChannelManagementInc/743999656941291"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2017-07-28 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Hybrid Mobile Developer | Randstad | Portland, OR, United States | Not specified | ❌ No | 22% | <a href="https://jobs.smartrecruiters.com/Randstad4/743999656650913"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2017-07-24 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Web Developer (with Game Design experience) | Collabera | The Woodlands, TX, United States | Not specified | ❌ No | 15% | <a href="https://jobs.smartrecruiters.com/Collabera2/743999656267171"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2017-07-19 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| IT Analyst IV / Software Engineer | Collabera | Johnston, IA, United States | Not specified | ❌ No | 4% | <a href="https://jobs.smartrecruiters.com/Collabera2/743999656020033"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2017-07-17 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Web Developer Level III | Collabera | The Woodlands, TX, United States | Not specified | ❌ No | 4% | <a href="https://jobs.smartrecruiters.com/Collabera2/743999655898377"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2017-07-14 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Web Developer III | Collabera | The Woodlands, TX, United States | Not specified | ❌ No | 4% | <a href="https://jobs.smartrecruiters.com/Collabera2/743999655760802"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2017-07-05 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| SOFTWARE ENGINEER | Collabera | Alpharetta, GA, United States | Not specified | ❌ No | 4% | <a href="https://jobs.smartrecruiters.com/Collabera2/743999654920777"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2017-06-30 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Local_ Data Scientist in Juno Beach FL | US IT Solutions | Juno Beach, FL, United States | Not specified | ❌ No | 4% | <a href="https://jobs.smartrecruiters.com/USITSolutionsInc/743999654610678"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2017-06-28 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer III | Collabera | Boca Raton, FL, United States | Not specified | ❌ No | 4% | <a href="https://jobs.smartrecruiters.com/Collabera2/743999654464475"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2017-06-26 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer III | Collabera | Alpharetta, GA, United States | Not specified | ❌ No | 4% | <a href="https://jobs.smartrecruiters.com/Collabera2/743999654240821"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2017-06-05 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Board Support Package Software Engineer | Idexcel | Cedar Rapids, IA, United States | Not specified | ❌ No | 11% | <a href="https://jobs.smartrecruiters.com/Idexcel3/743999652311582"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2017-05-15 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Web developer (html, Bootstrap, angular) for medical industry. | US IT Solutions | La Jolla Ranch, CA, United States | Not specified | ❌ No | 4% | <a href="https://jobs.smartrecruiters.com/USITSolutionsInc/116222497"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2017-04-28 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer (Web UI) | Lever |  | Not specified | ❌ No | 7% | <a href="https://jobs.lever.co/leverdemo/a51f4e09-a2c7-45a0-b8cf-ed9b479796b9"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2017-04-05 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Front End Engineer | Lever |  | Not specified | ❌ No | 7% | <a href="https://jobs.lever.co/leverdemo/37dd40ee-79e4-4cc8-8ea3-a95a9103d686"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2017-03-13 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Full Stack Engineer - II | Lever | Bay Area, CA | Not specified | ❌ No | 4% | <a href="https://jobs.lever.co/leverdemo/c80bf353-52e1-4b15-8018-aaf656a92b70"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2017-01-26 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Data Scientist | Saxon Global | Austin, TX, United States | Not specified | ❌ No | 4% | <a href="https://jobs.smartrecruiters.com/SaxonGlobal/106752283"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2017-01-20 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Web Developer | Lever | Perth | Not specified | ❌ No | 7% | <a href="https://jobs.lever.co/leverdemo/d7b41c8a-85fb-48df-96df-14d12c8d7a5c"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2016-12-15 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Embedded Software Engineer | Collabera | Wauwatosa, WI, United States | Not specified | ❌ No | 4% | <a href="https://jobs.smartrecruiters.com/Collabera2/104039207"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2016-10-18 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer | Collabera | Carrollton, TX, United States | Not specified | ❌ No | 4% | <a href="https://jobs.smartrecruiters.com/Collabera2/100590063"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2016-10-12 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer | Collabera | Eagan, MN, United States | Not specified | ❌ No | 4% | <a href="https://jobs.smartrecruiters.com/Collabera2/99896239"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2016-09-29 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Application Developer | EROS Technologies | San Ramon, CA, United States | Not specified | ❌ No | 15% | <a href="https://jobs.smartrecruiters.com/EROSTechnologiesInc/99230319"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2016-09-14 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Embedded Software Engineer | Collabera | Pompano Beach, FL, United States | Not specified | ❌ No | 4% | <a href="https://jobs.smartrecruiters.com/Collabera2/98473191"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2016-07-20 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer | Lever |  | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/leverdemo/fb388677-ac4d-45ac-bf78-99c3adc58009"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2016-07-11 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Snr. Developer Oracle(Pl/SQL + ETL) | EROS Technologies | Chicago, IL, United States | Not specified | ❌ No | 4% | <a href="https://jobs.smartrecruiters.com/EROSTechnologiesInc/94240523"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2016-06-27 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Network/Software Engineer | EROS Technologies | Fort Worth, TX, United States | Not specified | ❌ No | 4% | <a href="https://jobs.smartrecruiters.com/EROSTechnologiesInc/93791646"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2016-06-08 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Front-End Engineer | Lever |  | 2 | ❌ No | 15% | <a href="https://jobs.lever.co/leverdemo/776853fd-8d25-44fd-99f4-cc4e90909c69"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2016-05-12 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Data Analyst | Horizon Technologies | Minneapolis, MN, United States | Not specified | ❌ No | 7% | <a href="https://jobs.smartrecruiters.com/HorizonTechnologiesInc/92174649"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2016-02-15 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer | EROS Technologies | Chicago, IL, United States | Not specified | ❌ No | 4% | <a href="https://jobs.smartrecruiters.com/EROSTechnologiesInc/89472970"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2016-02-08 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer - Motion Planning | Zoox | Foster City, CA | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/zoox/7dd45151-9d8a-45a4-bb33-86fb88c1995d"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2015-12-11 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Big Data Analyst | Spruce InfoTech | King of Prussia, PA, United States | Not specified | ❌ No | 4% | <a href="https://jobs.smartrecruiters.com/SpruceInfotechInc/87838695"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2015-10-06 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Web Developer | Spruce InfoTech | Philadelphia, PA, United States | Not specified | ❌ No | 7% | <a href="https://jobs.smartrecruiters.com/SpruceInfotechInc/85784398"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Web Developer: | Spruce InfoTech | Philadelphia, PA, United States | Not specified | ❌ No | 7% | <a href="https://jobs.smartrecruiters.com/SpruceInfotechInc/85784745"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2015-10-02 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| C# .Net Web Developer | Spruce InfoTech | Dallas, TX, United States | 1 | ❌ No | 11% | <a href="https://jobs.smartrecruiters.com/SpruceInfotechInc/85712720"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2015-09-14 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Web Developer | Spruce InfoTech | Wilmington, DE, United States | Not specified | ❌ No | 4% | <a href="https://jobs.smartrecruiters.com/SpruceInfotechInc/85302237"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2015-08-08 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Full Stack Engineer - UI/UX | Lever |  | 2 | ❌ No | 7% | <a href="https://jobs.lever.co/leverdemo/e8682b1e-ef9d-4ba5-8164-927e842aec26"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2015-07-28 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer (C++, Java and/or Scala) | North Star Staffing Solutions | Boston, MA, United States | Not specified | ❌ No | 4% | <a href="https://jobs.smartrecruiters.com/NorthStarStaffingSolutions1/84325294"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2015-07-24 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer | North Star Staffing Solutions | Boston, MA, United States | Not specified | ❌ No | 4% | <a href="https://jobs.smartrecruiters.com/NorthStarStaffingSolutions1/84270465"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2015-07-10 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Data Scientist | North Star Staffing Solutions | New York, NY, United States | Not specified | ❌ No | 4% | <a href="https://jobs.smartrecruiters.com/NorthStarStaffingSolutions1/84012135"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2015-06-04 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Database ETL Developer | CoServe Global Solutions | Cranbury Township, NJ, United States | Not specified | ❌ No | 4% | <a href="https://jobs.smartrecruiters.com/CoServeGlobalSolutions/83338913"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2015-05-14 · 2 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Jr. DevOps Engineer | CoServe Global Solutions | Charleston, SC, United States | 0-2 | ❌ No | 15% | <a href="https://jobs.smartrecruiters.com/CoServeGlobalSolutions/82919330"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Jr. DevOps Engineer | CoServe Global Solutions | Cherry Hill, NJ, United States | 0-2 | ❌ No | 15% | <a href="https://jobs.smartrecruiters.com/CoServeGlobalSolutions/82919264"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2015-05-12 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Resident Software Engineer | North Star Staffing Solutions | Milford Mill, MD, United States | Not specified | ❌ No | 4% | <a href="https://jobs.smartrecruiters.com/NorthStarStaffingSolutions1/82861161"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2015-04-14 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Voice and Data Engineer | CoServe Global Solutions | Cumberland, MD, United States | Not specified | ❌ No | 4% | <a href="https://jobs.smartrecruiters.com/CoServeGlobalSolutions/82250741"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2015-04-06 · 8 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Voice and Data Engineer | CoServe Global Solutions | Merrillville, IN, United States | Not specified | ❌ No | 4% | <a href="https://jobs.smartrecruiters.com/CoServeGlobalSolutions/82114540"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Voice and Data Engineer | CoServe Global Solutions | Fort Wayne, IN, United States | Not specified | ❌ No | 4% | <a href="https://jobs.smartrecruiters.com/CoServeGlobalSolutions/82114482"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Voice and Data Engineer | CoServe Global Solutions | Mansfield, OH, United States | Not specified | ❌ No | 4% | <a href="https://jobs.smartrecruiters.com/CoServeGlobalSolutions/82114438"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Voice and Data Engineer | CoServe Global Solutions | St Clairsville, OH, United States | Not specified | ❌ No | 4% | <a href="https://jobs.smartrecruiters.com/CoServeGlobalSolutions/82114410"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Voice and Data Engineer | CoServe Global Solutions | St Albans, WV, United States | Not specified | ❌ No | 4% | <a href="https://jobs.smartrecruiters.com/CoServeGlobalSolutions/82114396"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Voice and Data Engineer | CoServe Global Solutions | Fredericksburg, VA, United States | Not specified | ❌ No | 4% | <a href="https://jobs.smartrecruiters.com/CoServeGlobalSolutions/82114325"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Voice and Data Engineer | CoServe Global Solutions | Springfield, MA, United States | Not specified | ❌ No | 4% | <a href="https://jobs.smartrecruiters.com/CoServeGlobalSolutions/82114282"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Voice and Data Engineer | CoServe Global Solutions | Pikeville, KY, United States | Not specified | ❌ No | 4% | <a href="https://jobs.smartrecruiters.com/CoServeGlobalSolutions/82114239"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2015-02-05 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer I | North Star Staffing Solutions | Cleveland, OH, United States | Not specified | ❌ No | 4% | <a href="https://jobs.smartrecruiters.com/NorthStarStaffingSolutions1/81064849"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2014-12-23 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Business Data Analyst | Miracle Software Systems | Cincinnati, OH, United States | Not specified | ❌ No | 4% | <a href="https://jobs.smartrecruiters.com/MiracleSoftwareSystem1/80581149"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2014-01-23 · 1 role · 1 H-1B sponsor match

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Forward Deployed Software Engineer | Palantir | New York, NY | 1 | ✅ Yes | 19% | <a href="https://jobs.lever.co/palantir/dab396d4-2f14-4796-aac0-0d82883dccf0"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2013-10-04 · 1 role · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| BackEnd Engineer | Lever |  | Not specified | ❌ No | 7% | <a href="https://jobs.lever.co/leverdemo/cd1ea494-1629-4cb1-a1c7-5dbcc9dea545"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### Unknown · 23 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer - RRT | Interact Software | n/a | 2 | ❌ No | 26% | <a href="https://careers.interactsoftware.com/en/postings/9db55870-d1c2-4f08-aada-b842848a745e"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Intern (Placement Year) | Interact Software | Manchester | Not specified | ❌ No | 15% | <a href="https://careers.interactsoftware.com/en/postings/77368e04-61bb-4327-9ce6-85501cea8b7a"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Embedded Software Engineer (Image Processing Algorithms) | Impulse Space | Redondo Beach | Not specified | ❌ No | 11% | <a href="https://impulsespace.pinpointhq.com/en/postings/1b070c7b-ba2d-45a7-ba66-00c79a4bcc8e"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AWS DevOps Engineer | NucleusTeq | Pune/Bangalore/Gurgaon/Hyderabad/Indore/Raipur, IN | Not specified | ❌ No | 7% | <a href="https://nucleusteq.breezy.hr/p/a7e6af98c745-aws-devops-engineer"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Business Intelligence Developer | Franklin Electric | Fort Wayne | Not specified | ❌ No | 7% | <a href="https://franklin-electric.pinpointhq.com/en/postings/36ef00a0-21d7-4834-b930-8b39a5030deb"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Embedded Software Engineer | Impulse Space | Redondo Beach | Not specified | ❌ No | 7% | <a href="https://impulsespace.pinpointhq.com/en/postings/395ef0f6-fe64-45a8-9403-d8c5698b0005"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Embedded Software Engineer (Camera Systems) | Impulse Space | Redondo Beach | Not specified | ❌ No | 7% | <a href="https://impulsespace.pinpointhq.com/en/postings/53615b51-6458-4464-894d-f48d8b91711b"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Flight Software Engineer | Impulse Space | Redondo Beach | Not specified | ❌ No | 7% | <a href="https://impulsespace.pinpointhq.com/en/postings/9b8a4ed3-27c5-4d88-84d9-6b420c85f786"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Optical Communications Systems Engineer | Impulse Space | Redondo Beach | Not specified | ❌ No | 7% | <a href="https://impulsespace.pinpointhq.com/en/postings/7f051451-9f17-4e5a-aced-60a780bffe60"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer- Entry Level (NIT/IIT) | NucleusTeq | Chennai, IN | 0-2 | ❌ No | 7% | <a href="https://nucleusteq.breezy.hr/p/7d9b260b4c7c-software-engineer-entry-level-nit-iit"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| [Mid Level] Data Analyst - Supply Chain Warehouse Reporting & Analytics (17536-1) | JND | Santa Ana, CA | Not specified | ❌ No | 4% | <a href="https://jnd-inc.breezy.hr/p/553de69e25ff-mid-level-data-analyst-supply-chain-warehouse-reporting-analytics-17536-1"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Agentic AI Developer | NucleusTeq | Indore/Gurgaon/Bangalore/Raipur/Hyderabad, IN | Not specified | ❌ No | 4% | <a href="https://nucleusteq.breezy.hr/p/3a1e8bb1a10f-agentic-ai-developer"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Analyst | Interact Software | Manchester | Not specified | ❌ No | 4% | <a href="https://careers.interactsoftware.com/en/postings/1bcd21af-042c-4b98-81fe-4e0345bf8c48"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Engineer | NucleusTeq | Indore/Raipur, IN | Not specified | ❌ No | 4% | <a href="https://nucleusteq.breezy.hr/p/4588b081a25c-data-engineer"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Engineer | NucleusTeq | Indore/Raipur, IN | Not specified | ❌ No | 4% | <a href="https://nucleusteq.breezy.hr/p/119ce433eee4-data-engineer"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Engineer + Gen AI (In-Person @ NYC) | NucleusTeq | NYC, NY | Not specified | ❌ No | 4% | <a href="https://nucleusteq.breezy.hr/p/3d46ba4ca7a1-data-engineer-gen-ai-in-person-nyc"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Engineer - AI | NucleusTeq | Indore, IN | Not specified | ❌ No | 4% | <a href="https://nucleusteq.breezy.hr/p/42564a984b07-data-engineer-ai"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Engineer- Pyspark | NucleusTeq | Indore/Raipur/Gurgaon/Bangalore, IN | Not specified | ❌ No | 4% | <a href="https://nucleusteq.breezy.hr/p/c608177104d5-data-engineer-pyspark"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Scientist | NucleusTeq | Indore, IN | Not specified | ❌ No | 4% | <a href="https://nucleusteq.breezy.hr/p/9fec78846f30-data-scientist"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Front End Engineer | NucleusTeq | Indore, Gurugram, Raipur, Bangalore, IN | Not specified | ❌ No | 4% | <a href="https://nucleusteq.breezy.hr/p/799811298c28-front-end-engineer"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Ground Software Engineer | Impulse Space | Redondo Beach | Not specified | ❌ No | 4% | <a href="https://impulsespace.pinpointhq.com/en/postings/3c736c5a-866e-4fa3-a96c-e2391d8d432f"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| IT Systems Engineer II | Impulse Space | Redondo Beach | Not specified | ❌ No | 4% | <a href="https://impulsespace.pinpointhq.com/en/postings/376ba6c6-041a-45fb-be2c-7f8f28506558"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Web Developer | Franklin Electric | Fort Wayne | Not specified | ❌ No | 4% | <a href="https://franklin-electric.pinpointhq.com/en/postings/4eb6be91-2d50-43cc-a838-7967c5060590"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
<!-- JOBS:END -->
