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
7. Calculates a resume-alignment percentage from 0-100.
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

- `MAX_JOBS`: maximum rows to write, default `60`.
- `H1B_SPONSORS_CSV_URL`: optional CSV URL or local path with employer names from historical H-1B records.

ATS board configuration lives in `data/ats_boards.yml`. The app supports Greenhouse, Lever, Ashby, Workday, SmartRecruiters, Workable, Pinpoint, and Breezy. It also searches Workable's global jobs API for relevant U.S. roles.

To use the PDF resume parser, place your resume at `resume/resume.pdf`. The workflow installs `pypdf`, so PDF parsing is available in GitHub Actions.

## H-1B Sponsor Field

`✅ Yes` means the normalized company name matched prior sponsor records in the loaded sponsor data. `❌ No` means no prior record was found in the configured data sources; it is not legal advice or a guarantee about future sponsorship.

## Automation

The GitHub Actions workflow in `.github/workflows/update-jobs.yml` runs every 6 hours (`0 */6 * * *`, UTC) and commits README updates when the generated table changes. GitHub Pages/README display is updated from those commits.

<!-- JOBS:START -->
_Last updated: 2026-06-25 08:57 UTC_

| Date | Role | Company | Location | YOE | H1b Sponsorship | Percentage of alignment | Apply link |
| --- | --- | --- | --- | ---: | --- | ---: | --- |
| 2025-09-26 | Artificial Intelligence (AI) Engineers | Substance \| Level Up by Substance | United States | Not specified | ❌ No | 52% | [Apply](https://jobs.workable.com/view/1YHyxu9kpbCGv17oSnBUt6/remote-artificial-intelligence-(ai)-engineers-in-united-states-at-substance-%7C-level-up-by-substance) |
| 2026-04-20 | PhD Fall Machine Learning Intern (ATG — Visual, Multimodal, and Recommender Systems) | Pinterest | San Francisco, CA, US; Palo Alto, CA, US; Seattle, WA, US; New York, NY, US | Not specified | ❌ No | 48% | [Apply](https://www.pinterestcareers.com/jobs/?gh_jid=7255640) |
| 2025-09-18 | Data Scientist, Applied AI - Remote | Azumo | United States | Not specified | ❌ No | 48% | [Apply](https://jobs.workable.com/view/czghxrEWSvvujrShXZDcng/data-scientist%2C-applied-ai---remote-in-united-states-at-azumo) |
| 2026-06-22 | Machine Learning Engineer | Reddit | New York City, NY | Not specified | ❌ No | 41% | [Apply](https://job-boards.greenhouse.io/reddit/jobs/8014401) |
| 2026-06-22 | Machine Learning Engineer | Reddit | San Francisco, CA | Not specified | ❌ No | 41% | [Apply](https://job-boards.greenhouse.io/reddit/jobs/8014436) |
| 2026-05-29 | Open-Source Machine Learning Engineer - US Remote | Hugging Face | New York, New York, United States | Not specified | ❌ No | 41% | [Apply](https://jobs.workable.com/view/8UbCFFqNjvdNUKZBYdFAMR/open-source-machine-learning-engineer---us-remote-in-new-york-at-hugging-face) |
| 2026-06-24 | Machine Learning Engineer, Agentic AI Systems - Moveworks | ServiceNow | Mountain View, CALIFORNIA, United States | Not specified | ✅ Yes | 37% | [Apply](https://jobs.smartrecruiters.com/ServiceNow/744000134027173) |
| 2026-06-02 | Machine Learning Engineer | Robinhood | Bellevue, WA | Not specified | ❌ No | 37% | [Apply](https://boards.greenhouse.io/robinhood/jobs/7960680?t=gh_src=&gh_jid=7960680) |
| 2025-10-14 | [2026] Applied Scientist - PhD Intern | Roblox | San Mateo, CA, United States | Not specified | ❌ No | 37% | [Apply](https://careers.roblox.com/jobs/7142298?gh_jid=7142298) |
| 2024-03-28 | Software Engineer - Model Performance | Baseten | San Francisco | Not specified | ❌ No | 37% | [Apply](https://jobs.ashbyhq.com/baseten/d29e748c-7209-460d-a024-8f77ae0a3d4d) |
| 2023-11-10 | Software Engineer - Computer Vision | Verkada | San Mateo, CA United States | 2 | ❌ No | 37% | [Apply](https://job-boards.greenhouse.io/verkada/jobs/4128624007) |
| 2026-06-17 | AI Engineers | Accellor | Mountain View, California, United States | Not specified | ❌ No | 33% | [Apply](https://jobs.workable.com/view/9kiDdviPjNupVTu6Yq4rQo/ai-engineers-in-mountain-view-at-accellor) |
| 2026-06-17 | AI Engineers | Accellor | San Francisco, California, United States | Not specified | ❌ No | 33% | [Apply](https://jobs.workable.com/view/1jCARuH9ADsR1oFDmF4iqF/ai-engineers-in-san-francisco-at-accellor) |
| 2026-06-16 | Full Stack AI Developer | Enterprise Knowledge | Arlington, Virginia, United States | Not specified | ❌ No | 33% | [Apply](https://jobs.workable.com/view/uxNr5H3YKc8gay9EbCykcq/hybrid-full-stack-ai-developer-in-arlington-at-enterprise-knowledge) |
| 2026-06-02 | Software Engineer, Agentic AI | Robinhood | Bellevue, WA | Not specified | ❌ No | 33% | [Apply](https://boards.greenhouse.io/robinhood/jobs/7975477?t=gh_src=&gh_jid=7975477) |
| 2026-06-02 | Data Scientist (Looker / AI / BI) | Northramp LLC | Washington, District of Columbia, United States | Not specified | ❌ No | 33% | [Apply](https://jobs.workable.com/view/8m9Ro5UhgNCuSQuUvgABnV/hybrid-data-scientist-(looker-%2F-ai-%2F-bi)-in-washington-at-northramp-llc) |
| 2026-06-01 | Machine Learning Engineer | Multi Media LLC | United States | Not specified | ❌ No | 33% | [Apply](https://jobs.workable.com/view/bqkqSAJN2W35yHL1WmQ5C9/remote-machine-learning-engineer-in-united-states-at-multi-media-llc) |
| 2026-05-12 | Machine Learning Engineer, LLM Evals & Observability | Glean | Mountain View, CA | 2 | ❌ No | 33% | [Apply](https://job-boards.greenhouse.io/gleanwork/jobs/4694716005) |
| 2026-03-11 | Software Engineer, Data Platform | Ramp | New York, NY (HQ) | Not specified | ❌ No | 33% | [Apply](https://jobs.ashbyhq.com/ramp/bca0346c-b843-4795-96df-6091f51e421b) |
| 2026-03-10 | AI Engineer | DataVisor | Mountain View, California, United States | Not specified | ❌ No | 33% | [Apply](https://jobs.workable.com/view/ooAokaoHEf3mZchbKcsk2G/hybrid-ai-engineer-in-mountain-view-at-datavisor) |
| 2026-03-05 | Machine Learning Engineer, LLM Evals & Observability | Glean | San Francisco, CA | 2 | ❌ No | 33% | [Apply](https://job-boards.greenhouse.io/gleanwork/jobs/4669417005) |
| 2026-01-13 | Machine Learning PhD Intern, Economics (Fall) | Instacart | United States - Remote | Not specified | ❌ No | 33% | [Apply](https://instacart.careers/job/?gh_jid=7532267) |
| 2024-04-18 | Machine Learning Engineer, PhD Intern (Fall) | Instacart | United States - Remote | Not specified | ❌ No | 33% | [Apply](https://instacart.careers/job/?gh_jid=5917202) |
| 2026-04-27 | Applied Machine Learning Engineer, Circuit Design - New College Grad 2026 | NVIDIA | US, CA, Santa Clara; US, CA, Remote | Not specified | ✅ Yes | 30% | [Apply](https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/job/US-CA-Santa-Clara/Applied-Machine-Learning-Engineer--Circuit-Design---New-College-Grad-2026_JR2011517) |
| 2026-06-01 | Software Engineer | RouteSmart Technologies Inc | Melville, New York, United States | Not specified | ❌ No | 30% | [Apply](https://jobs.workable.com/view/q9H6VWXEQif7tkicj2h4Gh/hybrid-software-engineer-in-melville-at-routesmart-technologies-inc) |
| 2026-06-01 | Software Engineer | RouteSmart Technologies Inc | Columbia, Maryland, United States | Not specified | ❌ No | 30% | [Apply](https://jobs.workable.com/view/5CWgUuVTAtTTWQsYiJf2Lc/hybrid-software-engineer-in-columbia-at-routesmart-technologies-inc) |
| 2026-05-20 | Instructor - Generative AI in Data Analytics | Fullstack Academy | United States | Not specified | ❌ No | 30% | [Apply](https://jobs.workable.com/view/dWLbaPJorv3rKjUynFMek9/remote-instructor---generative-ai-in-data-analytics-in-united-states-at-fullstack-academy) |
| 2026-04-27 | Software Engineer, New Grad (AI) | Notion | San Francisco, California | 0-2 | ❌ No | 30% | [Apply](https://jobs.ashbyhq.com/notion/7e6dc7fe-7ddd-42c1-8928-13f7bddb9ec9) |
| 2026-04-23 | Software Engineer - Voice AI (Inference Runtime) | Baseten | San Francisco | Not specified | ❌ No | 30% | [Apply](https://jobs.ashbyhq.com/baseten/6e396eb7-acb3-436a-89ec-05e755c477f2) |
| 2026-04-23 | Data Scientist, Core Data - PhD (2026) | Figma | San Francisco, CA • New York, NY | Not specified | ❌ No | 30% | [Apply](https://boards.greenhouse.io/figma/jobs/5976930004?gh_jid=5976930004) |
| 2026-04-05 | Data Scientist | KDA Consulting Inc | McLean, Virginia, United States | Not specified | ❌ No | 30% | [Apply](https://jobs.workable.com/view/mKFf6YvVZGEUKLaiw1y4PG/data-scientist-in-mclean-at-kda-consulting-inc) |
| 2026-04-05 | Data Scientist | KDA Consulting Inc | Herndon, Virginia, United States | Not specified | ❌ No | 30% | [Apply](https://jobs.workable.com/view/knFZBmcV8JLHTWmUK6PtGz/data-scientist-in-herndon-at-kda-consulting-inc) |
| 2026-04-05 | Data Scientist | KDA Consulting Inc | Chantilly, Virginia, United States | Not specified | ❌ No | 30% | [Apply](https://jobs.workable.com/view/upgcpGZRswdMLoeyHNawNb/data-scientist-in-chantilly-at-kda-consulting-inc) |
| 2026-04-02 | AI Engineer | InterImage | Annapolis Junction, Maryland, United States | Not specified | ❌ No | 30% | [Apply](https://jobs.workable.com/view/2e6kCgKWXUs6uEiDJEQAZW/ai-engineer-in-annapolis-junction-at-interimage) |
| 2026-03-12 | AI Solutions Engineer | Pinterest | San Francisco, CA, US; Remote, US | Not specified | ❌ No | 30% | [Apply](https://www.pinterestcareers.com/jobs/?gh_jid=7714127) |
| 2026-03-10 | Machine Learning Engineer II, Computer Vision Applied Science | Pinterest | San Francisco, CA, US; Remote, US | 2 | ❌ No | 30% | [Apply](https://www.pinterestcareers.com/jobs/?gh_jid=7697137) |
| 2026-01-07 | Software Engineer, Model Performance Systems | Baseten | San Francisco | Not specified | ❌ No | 30% | [Apply](https://jobs.ashbyhq.com/baseten/75d7beac-0298-40fa-b206-2e0c0c08a64f) |
| 2025-12-23 | Full-stack Software Engineer | Nick AI | United States | Not specified | ❌ No | 30% | [Apply](https://jobs.workable.com/view/37quUoKsDu7UNMqPD8ZEYH/remote-full-stack-software-engineer-in-united-states-at-nick-ai) |
| 2025-12-16 | [2026] Data Scientist, Social | Roblox | San Mateo, CA, United States | 2 | ❌ No | 30% | [Apply](https://careers.roblox.com/jobs/7463634?gh_jid=7463634) |
| 2025-09-18 | AI Software Engineer - Remote | Azumo | United States | Not specified | ❌ No | 30% | [Apply](https://jobs.workable.com/view/7xRPgnRuDPJxP1jtoyCpz9/ai-software-engineer---remote-in-united-states-at-azumo) |
| 2024-07-24 | Machine Learning Engineer, Core Engineering | Pinterest | San Francisco, CA, US; Palo Alto, CA, US; Seattle, WA, US; Remote, US | 2 | ❌ No | 30% | [Apply](https://www.pinterestcareers.com/jobs/?gh_jid=6121450) |
| 2024-07-23 | Machine Learning Engineer, Monetization Engineering | Pinterest | San Francisco, CA, US; Palo Alto, CA, US; Seattle, WA, US | 2 | ❌ No | 30% | [Apply](https://www.pinterestcareers.com/jobs/?gh_jid=6121543) |
| 2026-05-05 | Data Scientist, Algorithms, Optimization - Fulfillment | Lyft | San Francisco, CA | 2 | ✅ Yes | 26% | [Apply](https://app.careerpuck.com/job-board/lyft/job/8536085002?gh_jid=8536085002) |
| 2025-12-12 | Data Scientist, Algorithms, Optimization - Fulfillment | Lyft | New York, NY | 2 | ✅ Yes | 26% | [Apply](https://app.careerpuck.com/job-board/lyft/job/8335733002?gh_jid=8335733002) |
| 2025-12-12 | Data Scientist, Algorithms, Optimization - Fulfillment | Lyft | Seattle, WA | 2 | ✅ Yes | 26% | [Apply](https://app.careerpuck.com/job-board/lyft/job/8335715002?gh_jid=8335715002) |
| 2023-11-07 | PhD GenAI Research Scientist Intern | Databricks | San Francisco, California | Not specified | ✅ Yes | 26% | [Apply](https://databricks.com/company/careers/open-positions/job?gh_jid=7011263002) |
| 2026-06-16 | Full-Stack AI Engineer (evergreen) | Komodo Health | San Francisco, CA | Not specified | ❌ No | 26% | [Apply](https://job-boards.greenhouse.io/komodohealth/jobs/8584991002) |
| 2026-06-15 | Junior AI/ML Engineer | Node.Digital | Herndon, Virginia, United States | 0-2 | ❌ No | 26% | [Apply](https://jobs.workable.com/view/tnF3oMi9HKzzNrZnKqZ6et/hybrid-junior-ai%2Fml-engineer-in-herndon-at-node.digital) |
| 2026-06-11 | Software Engineer II, Backend (ML Training & Serving) | Affirm | Remote US | 1.5 | ❌ No | 26% | [Apply](https://job-boards.greenhouse.io/affirm/jobs/7762568003) |
| 2026-06-08 | AI/ML Engineer | Chime Financial | San Francisco, CA, USA | 2 | ❌ No | 26% | [Apply](https://boards.greenhouse.io/chime/jobs/8569368002?gh_jid=8569368002) |
| 2026-06-02 | Software Engineer | Robinhood | Menlo Park, CA | 1 | ❌ No | 26% | [Apply](https://boards.greenhouse.io/robinhood/jobs/7975558?t=gh_src=&gh_jid=7975558) |
| 2026-06-02 | Software Engineer | Robinhood | Menlo Park, CA | Not specified | ❌ No | 26% | [Apply](https://boards.greenhouse.io/robinhood/jobs/7975531?t=gh_src=&gh_jid=7975531) |
| 2026-06-02 | Software Engineer | Robinhood | Menlo Park, CA | Not specified | ❌ No | 26% | [Apply](https://boards.greenhouse.io/robinhood/jobs/7975530?t=gh_src=&gh_jid=7975530) |
| 2026-05-15 | Software Engineer (L2) Segment Team | Twilio | Remote - US | 2 | ❌ No | 26% | [Apply](https://job-boards.greenhouse.io/twilio/jobs/7767263) |
| 2026-03-19 | Machine Learning Engineer | Spotify | New York, NY | Not specified | ❌ No | 26% | [Apply](https://jobs.lever.co/spotify/e68ad741-4c4e-4b06-ae11-9cf1e36dd40f) |
| 2026-03-13 | Software Engineer | Twilio | Remote - Estonia | 2 | ❌ No | 26% | [Apply](https://job-boards.greenhouse.io/twilio/jobs/7647708) |
| 2026-02-25 | Software Engineer II, Simulation, tvScientific | Pinterest | San Francisco, CA, US; Remote, US | Not specified | ❌ No | 26% | [Apply](https://www.pinterestcareers.com/jobs/?gh_jid=7642265) |
| 2026-02-19 | Software Engineer, (L2) CDP | Twilio | Remote - US | Not specified | ❌ No | 26% | [Apply](https://job-boards.greenhouse.io/twilio/jobs/7602727) |
| 2026-02-17 | Data Science Analyst | Tatari | San Francisco, California, United States | 2 | ❌ No | 26% | [Apply](https://job-boards.greenhouse.io/tatari/jobs/8350484002) |
| 2026-02-17 | Data Science Analyst | Tatari | Los Angeles, California, United States | 2 | ❌ No | 26% | [Apply](https://job-boards.greenhouse.io/tatari/jobs/8350482002) |
<!-- JOBS:END -->
