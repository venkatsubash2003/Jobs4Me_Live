from __future__ import annotations

import json
from datetime import datetime, timezone
from html import escape
from pathlib import Path

from .config import SITE_DATA_PATH, SITE_DIR, SITE_INDEX_PATH
from .jobs import MatchedJob, parse_job_datetime
from .readme import next_fetch_label

DOMAINS_LABEL = "Data Science, AI/ML, Data Analytics, Software Engineering, ML Engineer"
REGION_LABEL = "USA"
EXPERIENCE_LABEL = "0-2 years"


def _utc_label(now: datetime | None = None) -> str:
    current = now or datetime.now(timezone.utc)
    if current.tzinfo is None:
        current = current.replace(tzinfo=timezone.utc)
    return current.astimezone(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


def _job_date(value: str) -> str:
    parsed = parse_job_datetime(value)
    if parsed.year <= 1:
        return "Unknown"
    return parsed.strftime("%Y-%m-%d")


def job_to_dict(item: MatchedJob) -> dict[str, object]:
    job = item.job
    return {
        "date": _job_date(job.published_at),
        "role": job.title,
        "company": job.company,
        "location": job.location,
        "yoe": item.years_required,
        "h1b_sponsor": item.h1b_sponsor,
        "alignment": item.score,
        "apply_url": job.url,
        "category": item.role,
        "source": job.source,
        "published_at": job.published_at,
    }


def build_site_payload(jobs: list[MatchedJob], now: datetime | None = None) -> dict[str, object]:
    sponsor_count = sum(1 for item in jobs if item.h1b_sponsor)
    dates = sorted({_job_date(item.job.published_at) for item in jobs}, reverse=True)
    return {
        "generated_at": _utc_label(now),
        "next_fetch_in": next_fetch_label(now),
        "domains": DOMAINS_LABEL,
        "region": REGION_LABEL,
        "experience": EXPERIENCE_LABEL,
        "stats": {
            "total_jobs": len(jobs),
            "h1b_sponsors": sponsor_count,
            "posting_dates": len(dates),
            "latest_date": dates[0] if dates else "None",
        },
        "jobs": [job_to_dict(item) for item in jobs],
    }


def _json_for_html(payload: dict[str, object]) -> str:
    return json.dumps(payload, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")


def render_site_html(payload: dict[str, object]) -> str:
    data = _json_for_html(payload)
    title = "Jobs4Me Live"
    description = "Resume-aware job dashboard for early-career AI, ML, data, analytics, and software roles."
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{escape(description, quote=True)}">
  <title>{escape(title)}</title>
  <style>
    :root {{
      color-scheme: light;
      --bg: #f7f8fb;
      --panel: #ffffff;
      --ink: #1f2937;
      --muted: #667085;
      --line: #d8dee8;
      --blue: #2563eb;
      --green: #15803d;
      --orange: #c2410c;
      --red: #b42318;
      --shadow: 0 12px 30px rgba(15, 23, 42, 0.08);
    }}

    * {{ box-sizing: border-box; }}

    body {{
      margin: 0;
      background: var(--bg);
      color: var(--ink);
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      line-height: 1.5;
    }}

    a {{ color: inherit; }}

    .shell {{
      width: min(1440px, calc(100% - 32px));
      margin: 0 auto;
      padding: 24px 0 40px;
    }}

    header {{
      display: grid;
      grid-template-columns: minmax(0, 1fr) auto;
      gap: 20px;
      align-items: end;
      margin-bottom: 18px;
    }}

    h1 {{
      margin: 0;
      font-size: clamp(1.75rem, 3vw, 2.6rem);
      line-height: 1.05;
      letter-spacing: 0;
    }}

    .subtitle {{
      margin: 8px 0 0;
      color: var(--muted);
      max-width: 760px;
    }}

    .updated {{
      justify-self: end;
      color: var(--muted);
      font-size: 0.94rem;
      text-align: right;
      white-space: nowrap;
    }}

    .metrics {{
      display: grid;
      grid-template-columns: repeat(4, minmax(0, 1fr));
      gap: 12px;
      margin-bottom: 18px;
    }}

    .metric {{
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 14px 16px;
      box-shadow: var(--shadow);
      min-height: 92px;
    }}

    .metric span {{
      display: block;
      color: var(--muted);
      font-size: 0.78rem;
      font-weight: 700;
      text-transform: uppercase;
    }}

    .metric strong {{
      display: block;
      margin-top: 7px;
      font-size: 1.05rem;
      line-height: 1.28;
    }}

    .toolbar {{
      display: grid;
      grid-template-columns: minmax(220px, 1fr) 190px 160px 170px;
      gap: 10px;
      align-items: center;
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 12px;
      box-shadow: var(--shadow);
      margin-bottom: 14px;
    }}

    input,
    select {{
      width: 100%;
      min-height: 42px;
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 0 12px;
      color: var(--ink);
      background: #fff;
      font: inherit;
    }}

    input:focus,
    select:focus {{
      outline: 2px solid rgba(37, 99, 235, 0.2);
      border-color: var(--blue);
    }}

    .summary {{
      display: flex;
      justify-content: space-between;
      gap: 12px;
      align-items: center;
      margin: 0 0 10px;
      color: var(--muted);
      font-size: 0.95rem;
    }}

    .table-wrap {{
      overflow: auto;
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 8px;
      box-shadow: var(--shadow);
    }}

    table {{
      width: 100%;
      min-width: 1060px;
      border-collapse: collapse;
    }}

    th,
    td {{
      padding: 11px 12px;
      border-bottom: 1px solid #edf0f5;
      text-align: left;
      vertical-align: middle;
      font-size: 0.93rem;
    }}

    th {{
      position: sticky;
      top: 0;
      z-index: 1;
      background: #f4f6fa;
      color: #475467;
      font-size: 0.76rem;
      text-transform: uppercase;
      letter-spacing: 0;
    }}

    tbody tr:hover {{ background: #f8fbff; }}

    .role {{
      font-weight: 700;
      color: #111827;
    }}

    .subtle {{
      color: var(--muted);
      font-size: 0.82rem;
    }}

    .pill {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      min-width: 58px;
      min-height: 28px;
      border-radius: 999px;
      padding: 2px 10px;
      font-weight: 700;
      font-size: 0.82rem;
    }}

    .yes {{
      color: var(--green);
      background: #ecfdf3;
      border: 1px solid #bbf7d0;
    }}

    .no {{
      color: var(--red);
      background: #fff1f3;
      border: 1px solid #fecdd3;
    }}

    .match {{
      color: var(--blue);
      font-weight: 800;
      white-space: nowrap;
    }}

    .apply {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      min-height: 34px;
      border-radius: 8px;
      background: var(--blue);
      color: #fff;
      padding: 0 13px;
      font-weight: 800;
      text-decoration: none;
      white-space: nowrap;
    }}

    .empty {{
      padding: 32px 16px;
      text-align: center;
      color: var(--muted);
    }}

    @media (max-width: 920px) {{
      .shell {{ width: min(100% - 20px, 760px); padding-top: 16px; }}
      header {{ grid-template-columns: 1fr; }}
      .updated {{ justify-self: start; text-align: left; white-space: normal; }}
      .metrics {{ grid-template-columns: repeat(2, minmax(0, 1fr)); }}
      .toolbar {{ grid-template-columns: 1fr 1fr; }}
    }}

    @media (max-width: 560px) {{
      .metrics,
      .toolbar {{ grid-template-columns: 1fr; }}
      th,
      td {{ padding: 10px; }}
    }}
  </style>
</head>
<body>
  <main class="shell">
    <header>
      <div>
        <h1>Jobs4Me Live</h1>
        <p class="subtitle">{escape(description)}</p>
      </div>
      <div class="updated">Updated <strong id="generatedAt"></strong><br>Next fetch in <strong id="nextFetch"></strong></div>
    </header>

    <section class="metrics" aria-label="Job board metrics">
      <div class="metric"><span>Domains</span><strong id="domains"></strong></div>
      <div class="metric"><span>Region</span><strong>🇺🇸 <span id="region"></span></strong></div>
      <div class="metric"><span>Total Jobs</span><strong id="totalJobs"></strong></div>
      <div class="metric"><span>Experience</span><strong id="experience"></strong></div>
    </section>

    <section class="toolbar" aria-label="Job filters">
      <input id="search" type="search" placeholder="Search role, company, location, keyword">
      <select id="dateFilter" aria-label="Date"></select>
      <select id="sponsorFilter" aria-label="H-1B sponsorship">
        <option value="all">All H-1B signals</option>
        <option value="yes">Sponsors only</option>
        <option value="no">Non-sponsors</option>
      </select>
      <select id="roleFilter" aria-label="Domain"></select>
    </section>

    <div class="summary">
      <span id="resultCount"></span>
      <span id="sponsorCount"></span>
    </div>

    <section class="table-wrap" aria-label="Matching jobs">
      <table>
        <thead>
          <tr>
            <th>Date</th>
            <th>Role</th>
            <th>Company</th>
            <th>Location</th>
            <th>YOE</th>
            <th>H-1B</th>
            <th>Match</th>
            <th>Apply</th>
          </tr>
        </thead>
        <tbody id="jobsBody"></tbody>
      </table>
      <div class="empty" id="emptyState" hidden>No jobs match the current filters.</div>
    </section>
  </main>

  <script id="jobs-data" type="application/json">{data}</script>
  <script>
    const payload = JSON.parse(document.getElementById("jobs-data").textContent);
    const state = {{
      query: "",
      date: "all",
      sponsor: "all",
      role: "all"
    }};

    const jobs = payload.jobs || [];
    const body = document.getElementById("jobsBody");
    const emptyState = document.getElementById("emptyState");
    const resultCount = document.getElementById("resultCount");
    const sponsorCount = document.getElementById("sponsorCount");
    const dateFilter = document.getElementById("dateFilter");
    const roleFilter = document.getElementById("roleFilter");

    document.getElementById("generatedAt").textContent = payload.generated_at;
    document.getElementById("nextFetch").textContent = payload.next_fetch_in;
    document.getElementById("domains").textContent = payload.domains;
    document.getElementById("region").textContent = payload.region;
    document.getElementById("experience").textContent = payload.experience;
    document.getElementById("totalJobs").textContent = (payload.stats?.total_jobs || jobs.length).toLocaleString();

    function option(value, label) {{
      const item = document.createElement("option");
      item.value = value;
      item.textContent = label;
      return item;
    }}

    function populateFilters() {{
      const dates = [...new Set(jobs.map((job) => job.date))].filter(Boolean);
      const roles = [...new Set(jobs.map((job) => job.category))].filter(Boolean).sort();
      dateFilter.appendChild(option("all", "All dates"));
      dates.forEach((date) => dateFilter.appendChild(option(date, date)));
      roleFilter.appendChild(option("all", "All domains"));
      roles.forEach((role) => roleFilter.appendChild(option(role, role)));
    }}

    function matches(job) {{
      const text = [job.role, job.company, job.location, job.category, job.source].join(" ").toLowerCase();
      const queryOk = !state.query || text.includes(state.query);
      const dateOk = state.date === "all" || job.date === state.date;
      const roleOk = state.role === "all" || job.category === state.role;
      const sponsorOk =
        state.sponsor === "all" ||
        (state.sponsor === "yes" && job.h1b_sponsor) ||
        (state.sponsor === "no" && !job.h1b_sponsor);
      return queryOk && dateOk && roleOk && sponsorOk;
    }}

    function render() {{
      const rows = jobs.filter(matches);
      body.textContent = "";
      const fragment = document.createDocumentFragment();
      rows.forEach((job) => {{
        const row = document.createElement("tr");
        const sponsorClass = job.h1b_sponsor ? "yes" : "no";
        const sponsorLabel = job.h1b_sponsor ? "✓ Yes" : "× No";
        row.innerHTML = `
          <td>${{escapeHtml(job.date)}}</td>
          <td><div class="role">${{escapeHtml(job.role)}}</div><div class="subtle">${{escapeHtml(job.category || "")}}</div></td>
          <td>${{escapeHtml(job.company)}}</td>
          <td>${{escapeHtml(job.location)}}</td>
          <td>${{escapeHtml(job.yoe)}}</td>
          <td><span class="pill ${{sponsorClass}}">${{sponsorLabel}}</span></td>
          <td><span class="match">${{Number(job.alignment || 0)}}%</span></td>
          <td><a class="apply" href="${{escapeHtml(job.apply_url || "#")}}" target="_blank" rel="noopener">Apply</a></td>
        `;
        fragment.appendChild(row);
      }});
      body.appendChild(fragment);
      emptyState.hidden = rows.length > 0;
      resultCount.textContent = `${{rows.length.toLocaleString()}} of ${{jobs.length.toLocaleString()}} jobs shown`;
      sponsorCount.textContent = `${{rows.filter((job) => job.h1b_sponsor).length.toLocaleString()}} H-1B sponsor matches`;
    }}

    function escapeHtml(value) {{
      return String(value ?? "")
        .replaceAll("&", "&amp;")
        .replaceAll("<", "&lt;")
        .replaceAll(">", "&gt;")
        .replaceAll('"', "&quot;")
        .replaceAll("'", "&#039;");
    }}

    document.getElementById("search").addEventListener("input", (event) => {{
      state.query = event.target.value.trim().toLowerCase();
      render();
    }});
    dateFilter.addEventListener("change", (event) => {{
      state.date = event.target.value;
      render();
    }});
    document.getElementById("sponsorFilter").addEventListener("change", (event) => {{
      state.sponsor = event.target.value;
      render();
    }});
    roleFilter.addEventListener("change", (event) => {{
      state.role = event.target.value;
      render();
    }});

    populateFilters();
    render();
  </script>
</body>
</html>
"""


def update_site(
    jobs: list[MatchedJob],
    site_dir: Path = SITE_DIR,
    index_path: Path = SITE_INDEX_PATH,
    data_path: Path = SITE_DATA_PATH,
    now: datetime | None = None,
) -> None:
    payload = build_site_payload(jobs, now)
    site_dir.mkdir(parents=True, exist_ok=True)
    data_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    index_path.write_text(render_site_html(payload), encoding="utf-8")
