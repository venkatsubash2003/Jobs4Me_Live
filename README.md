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
| Posting date | Keeps jobs posted on or after June 19, 2026. Jobs with unknown or unparseable posting dates are ignored. |
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
_Last updated: 2026-06-25 18:29 UTC_

**Showing 133 roles across 7 posting dates.** H-1B sponsor matches: **3**.

### 2026-06-25 · 18 roles · 2 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Software Engineer - Moveworks | ServiceNow | Mountain View, CALIFORNIA, United States | 2 | ✅ Yes | 22% | <a href="https://jobs.smartrecruiters.com/ServiceNow/744000134304689"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI/ML Flex Solution Engineer | Snowflake | US-CA-Remote | 2 | ✅ Yes | 11% | <a href="https://jobs.ashbyhq.com/snowflake/7c0fa868-20c5-4727-9f22-a5ab4bfbc08b"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer II, Machine Learning (Feature Platform) | Affirm | Remote US | 1.5 | ❌ No | 26% | <a href="https://job-boards.greenhouse.io/affirm/jobs/7785600003"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Product Engineer | PostHog | Remote | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/posthog/bd597451-e465-46f6-857f-befe28366f20"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Research Engineer / Research Scientist -Personal AGI, Proactivity | OpenAI | San Francisco | Not specified | ❌ No | 22% | <a href="https://jobs.ashbyhq.com/openai/e57d196b-4fa0-4463-bd33-d8189f0d3541"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Co-Op, ML Scientist for Biology | Lila Sciences | San Francisco, CA USA | Not specified | ❌ No | 19% | <a href="https://job-boards.greenhouse.io/lilasciences/jobs/4294212009"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Research Engineer/Research Scientist - Personal AGI, North Stars | OpenAI | San Francisco | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/openai/171ebca6-de53-4d6e-a312-30332f353957"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Research Scientist - Computational Neuroscience | Astera | Hybrid | Not specified | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/astera/0a1a566e-c48d-4605-b78f-458c234df670"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Insights | Benchling | San Francisco, CA | 2 | ❌ No | 19% | <a href="https://jobs.ashbyhq.com/benchling/259613a6-686a-4756-82fd-e653d53e9904"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Associate Software Engineer – C++ (Computer Aided Manufacturing) | Protolabs | Brooklyn Park, MN | Not specified | ❌ No | 15% | <a href="https://jobs.lever.co/protolabs/9da2126b-76e7-4d10-aee7-ec97cbff5bec"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Infrastructure Engineer | Gauntlet | New York | 1 | ❌ No | 15% | <a href="https://jobs.lever.co/gauntlet/56230d07-8402-4ed8-99d2-cc76391108fa"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Engineer I | Frontier Medicines | South San Francisco, California, United States | Not specified | ❌ No | 11% | <a href="https://jobs.workable.com/view/t4nn6yTEUyur9CmKuJBZT1/ai-engineer-i-in-south-san-francisco-at-frontier-medicines"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Infrastructure Engineer | SpaceX | Redmond, WA | 1 | ❌ No | 11% | <a href="https://boards.greenhouse.io/spacex/jobs/8604308002?gh_jid=8604308002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, Growth - Rime Ai | Unusual | San Francisco, California | Not specified | ❌ No | 11% | <a href="https://jobs.lever.co/unusual/0d58768b-9ca2-4af6-9b46-56534da5b3f1"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Analytics Intern | Massachusetts Life Sciences Center | Waltham, Massachusetts, United States | Not specified | ❌ No | 7% | <a href="https://jobs.workable.com/view/mvWpDiUcZdFNPjmH6VdSxA/hybrid-data-analytics-intern-in-waltham-at-massachusetts-life-sciences-center"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Embedded Software Engineer | Icarus | El Segundo | 1 | ❌ No | 7% | <a href="https://job-boards.greenhouse.io/icarus/jobs/5279638008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Paid Research Participant – AI Training Study (Columbus, OH) | HumanSignal | Columbus, OH | Not specified | ❌ No | 7% | <a href="https://job-boards.greenhouse.io/humansignal/jobs/6101368004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Business Intelligence & Data Analytics Intern (Undergraduate) | Phamily | New York, NY | Not specified | ❌ No | 4% | <a href="https://job-boards.greenhouse.io/jobsatphamily/jobs/5281446008"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-06-24 · 36 roles · 1 H-1B sponsor match

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
| AI Engineer, Agentic Ad Creative (Multimodal) | NewsBreak | Mountain View, California, United States | Not specified | ❌ No | 11% | <a href="https://job-boards.greenhouse.io/newsbreak/jobs/4691989006"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Engineer, Product | Brex | San Francisco, California, United States | Not specified | ❌ No | 11% | <a href="https://www.brex.com/careers/8606845002?gh_jid=8606845002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Associate Software Engineer | OptiTrack | Corvallis, Oregon, United States | Not specified | ❌ No | 11% | <a href="https://jobs.workable.com/view/v9bPjPpxbu6w7ZW8rWPW6D/associate-software-engineer-in-corvallis-at-optitrack"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Backend Engineer (EST timezone) | PostHog | Remote | Not specified | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/posthog/af00b414-fdb3-41b5-8843-828b4a0e373a"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Development Engineer in Test [Geospatial] | One Brief | United States \| Remote | 2 | ❌ No | 11% | <a href="https://jobs.ashbyhq.com/onebrief/8ee26b8a-97dd-4035-95e2-6ebe657fa59b"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| 1675 - Software Engineer | Sigma Defense | Washington, District of Columbia, United States | Not specified | ❌ No | 7% | <a href="https://jobs.workable.com/view/9BDAEdPgw1jHZ9qHNcs3CU/1675---software-engineer-in-washington-at-sigma-defense"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| 1698 - Data Scientist | Sigma Defense | San Diego, California, United States | Not specified | ❌ No | 7% | <a href="https://jobs.workable.com/view/5TG657X6U2RNTsjjbehotc/1698---data-scientist-in-san-diego-at-sigma-defense"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Engineer, Ecosystem | Brex | San Francisco, California, United States | Not specified | ❌ No | 7% | <a href="https://www.brex.com/careers/8606890002?gh_jid=8606890002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Engineer, Ecosystem | Brex | Seattle, Washington, United States | Not specified | ❌ No | 7% | <a href="https://www.brex.com/careers/8606885002?gh_jid=8606885002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Network Engineer (with Programming) - Data & AI Systems | Weekday AI | United States | Not specified | ❌ No | 7% | <a href="https://jobs.workable.com/view/97B6bSoKgbRH74Pm2KWH75/remote-network-engineer-(with-programming)---data-%26-ai-systems-in-united-states-at-weekday-ai"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| 1504 - Software Systems Engineer | Sigma Defense | United States | Not specified | ❌ No | 4% | <a href="https://jobs.workable.com/view/6KRa9XjyrAfMYRMrMN979U/remote-1504---software-systems-engineer-in-united-states-at-sigma-defense"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

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

### 2026-06-22 · 37 roles · 0 H-1B sponsor matches

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
| Deployment Associate, AI Solutions | Brellium | New York City | 2 | ❌ No | 7% | <a href="https://jobs.ashbyhq.com/brellium/65f55c9f-4614-4b41-a64b-0cdb6a55792e"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Development Engineer in Test II (SDET Contractor) | Sony Interactive Entertainment | United States, San Mateo, CA | Not specified | ❌ No | 7% | <a href="https://job-boards.greenhouse.io/sonyinteractiveentertainmentglobal/jobs/6099174004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Development Engineer in Test II (SDET Contractor) | Sony Interactive Entertainment | United States, Los Angeles, CA | Not specified | ❌ No | 7% | <a href="https://job-boards.greenhouse.io/sonyinteractiveentertainmentglobal/jobs/6020548004"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Software Engineer, C++ (Simulations) | SpaceX | Hawthorne, CA | 2 | ❌ No | 7% | <a href="https://boards.greenhouse.io/spacex/jobs/8603609002?gh_jid=8603609002"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| AI Systems Engineer - Forward-Deployed Builder | AI Acquisition | United States | Not specified | ❌ No | 4% | <a href="https://jobs.workable.com/view/bYBM1XUdBbeG1c8KLjvPbh/remote-ai-systems-engineer---forward-deployed-builder-in-united-states-at-ai-acquisition"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Backend Engineer (NYC) | MLabs | New York, New York, United States | Not specified | ❌ No | 4% | <a href="https://jobs.workable.com/view/6AQjUPZGuvia6buDc3N3AZ/hybrid-backend-engineer-(nyc)-in-new-york-at-mlabs"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Analyst, ACO Operations - Part time, Contract | Pearl Health | Seattle, New York City, Boston, or Remote | Not specified | ❌ No | 4% | <a href="https://jobs.ashbyhq.com/pearlhealth/77c51f6c-ba07-4566-a247-f4f06ae16d6f"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Infrastructure/Backend Engineer | MLabs | New York, New York, United States | Not specified | ❌ No | 4% | <a href="https://jobs.workable.com/view/srcxQ1aRFQm8rftXK4Qoe5/hybrid-infrastructure%2Fbackend-engineer-in-new-york-at-mlabs"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Recruitment Intern - AI & Automation | Eulerity | New York, NY | Not specified | ❌ No | 4% | <a href="https://job-boards.greenhouse.io/eulerity/jobs/4691149006"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |

### 2026-06-21 · 3 roles · 0 H-1B sponsor matches

| Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | ---: | --- | ---: | --- |
| Applied AI Engineer, Silicon Engineering | Etched.ai | San Jose | Not specified | ❌ No | 30% | <a href="https://jobs.ashbyhq.com/Etched/831bfa22-d883-450b-9b10-2a16421525a0"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
| Data Analyst Internship | ConnectPrep | Boston, Massachusetts, United States | Not specified | ❌ No | 22% | <a href="https://apply.workable.com/j/E4655645B8"><img alt="Apply" src="https://img.shields.io/badge/Apply-Open-2563eb?style=flat-square"></a> |
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
<!-- JOBS:END -->
