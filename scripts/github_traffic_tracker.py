#!/usr/bin/env python3
"""
GitHub Repository Traffic Tracker

Fetches traffic data (clones, views, referrers, popular paths) from the GitHub API
and maintains both raw snapshots and an aggregated summary file. GitHub only retains
14 days of traffic data, so this script should be run at least every 14 days.

Usage:
    export GITHUB_TOKEN=<your_token>
    python github_traffic_tracker.py
"""

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

import requests

REPO_OWNER = "aws-samples"
REPO_NAME = "sample-ai-invoice-processing-with-amazon-bedrock"
SCRIPT_DIR = Path(__file__).parent
DATA_FILE = SCRIPT_DIR / "traffic_history.json"
AGGREGATED_FILE = SCRIPT_DIR / "aggregated_traffic.json"
API_BASE = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}"


def load_json(path):
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return None


def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, default=str)


def github_get(endpoint, token):
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    resp = requests.get(f"{API_BASE}{endpoint}", headers=headers, timeout=30)
    resp.raise_for_status()
    return resp.json()


def fetch_traffic(token):
    clones = github_get("/traffic/clones", token)
    views = github_get("/traffic/views", token)
    referrers = github_get("/traffic/popular/referrers", token)
    paths = github_get("/traffic/popular/paths", token)

    return {
        "collected_at": datetime.now(timezone.utc).isoformat(),
        "period": {
            "start": clones["clones"][0]["timestamp"] if clones["clones"] else None,
            "end": clones["clones"][-1]["timestamp"] if clones["clones"] else None,
        },
        "clones": {
            "total": clones["count"],
            "unique": clones["uniques"],
            "daily": [
                {"date": c["timestamp"][:10], "total": c["count"], "unique": c["uniques"]}
                for c in clones["clones"]
            ],
        },
        "views": {
            "total": views["count"],
            "unique": views["uniques"],
            "daily": [
                {"date": v["timestamp"][:10], "total": v["count"], "unique": v["uniques"]}
                for v in views["views"]
            ],
        },
        "referrers": [
            {"source": r["referrer"], "total": r["count"], "unique": r["uniques"]}
            for r in referrers
        ],
        "popular_paths": [
            {"path": p["path"], "title": p["title"], "total": p["count"], "unique": p["uniques"]}
            for p in paths
        ],
    }


def seed_initial_data():
    """Seed the first 14-day snapshot (March 9-23, 2026) from manually recorded data."""
    return {
        "collected_at": "2026-03-23T23:59:59Z",
        "period": {"start": "2026-03-09", "end": "2026-03-23"},
        "clones": {"total": 52, "unique": 39, "peak_single_day": 22, "daily": []},
        "views": {"total": 113, "unique": 37, "peak_single_day": 35, "daily": []},
        "referrers": [
            {"source": "github.com", "total": 12, "unique": 7},
            {"source": "google.com", "total": 9, "unique": 6},
            {"source": "statics.teams.cdn.office.net", "total": 4, "unique": 3},
            {"source": "yahoo.com", "total": 2, "unique": 1},
        ],
        "popular_paths": [
            {"path": f"/{REPO_OWNER}/{REPO_NAME}", "title": "Main repository page", "total": 60, "unique": 27},
            {"path": f"/{REPO_OWNER}/{REPO_NAME}/issues", "title": "Issues", "total": 7, "unique": 4},
            {"path": f"/{REPO_OWNER}/{REPO_NAME}/pulls", "title": "Pull requests", "total": 6, "unique": 4},
            {"path": f"/{REPO_OWNER}/{REPO_NAME}/pulse", "title": "Pulse", "total": 7, "unique": 4},
            {"path": f"/{REPO_OWNER}/{REPO_NAME}/graphs/contributors", "title": "Contributors", "total": 5, "unique": 3},
        ],
    }


def aggregate_all(history):
    """Merge all snapshots into a single aggregated summary, deduplicating daily data."""
    # Merge daily clones/views by date (latest value wins for overlapping days)
    clone_days = {}
    view_days = {}
    referrer_totals = {}  # source -> {total, unique}
    path_totals = {}  # path -> {title, total, unique}

    for snap in history["snapshots"]:
        # Daily data: deduplicate by date
        for d in snap["clones"].get("daily", []):
            clone_days[d["date"]] = {"total": d["total"], "unique": d["unique"]}
        for d in snap["views"].get("daily", []):
            view_days[d["date"]] = {"total": d["total"], "unique": d["unique"]}

        # Referrers & paths: sum across non-overlapping snapshots.
        # For overlapping periods, the latest snapshot overwrites, so we
        # accumulate per-snapshot and the dedup happens via the daily data.
        for r in snap.get("referrers", []):
            src = r["source"].lower()
            if src not in referrer_totals:
                referrer_totals[src] = {"source": r["source"], "total": 0, "unique": 0}
            referrer_totals[src]["total"] += r["total"]
            referrer_totals[src]["unique"] += r["unique"]

        for p in snap.get("popular_paths", []):
            key = p["path"]
            if key not in path_totals:
                path_totals[key] = {"path": p["path"], "title": p["title"], "total": 0, "unique": 0}
            path_totals[key]["total"] += p["total"]
            path_totals[key]["unique"] += p["unique"]

    sorted_clone_days = sorted(clone_days.items())
    sorted_view_days = sorted(view_days.items())

    # For snapshots without daily data (like the seed), use the snapshot-level totals
    # for days not covered by daily entries
    seed_clone_total = sum(
        s["clones"]["total"] for s in history["snapshots"] if not s["clones"].get("daily")
    )
    seed_clone_unique = sum(
        s["clones"]["unique"] for s in history["snapshots"] if not s["clones"].get("daily")
    )
    seed_view_total = sum(
        s["views"]["total"] for s in history["snapshots"] if not s["views"].get("daily")
    )
    seed_view_unique = sum(
        s["views"]["unique"] for s in history["snapshots"] if not s["views"].get("daily")
    )

    daily_clone_total = sum(v["total"] for v in clone_days.values())
    daily_clone_unique = sum(v["unique"] for v in clone_days.values())
    daily_view_total = sum(v["total"] for v in view_days.values())
    daily_view_unique = sum(v["unique"] for v in view_days.values())

    all_dates = sorted(set(list(clone_days.keys()) + list(view_days.keys())))
    date_range_start = all_dates[0] if all_dates else None
    date_range_end = all_dates[-1] if all_dates else None

    # Use seed period start if it's earlier
    for s in history["snapshots"]:
        p_start = s["period"].get("start", "")[:10]
        if p_start and (date_range_start is None or p_start < date_range_start):
            date_range_start = p_start

    aggregated = {
        "repo": history["repo"],
        "last_updated": datetime.now(timezone.utc).isoformat(),
        "date_range": {"start": date_range_start, "end": date_range_end},
        "total_snapshots": len(history["snapshots"]),
        "clones": {
            "all_time_total": seed_clone_total + daily_clone_total,
            "all_time_unique": seed_clone_unique + daily_clone_unique,
            "daily": [{"date": d, **v} for d, v in sorted_clone_days],
        },
        "views": {
            "all_time_total": seed_view_total + daily_view_total,
            "all_time_unique": seed_view_unique + daily_view_unique,
            "daily": [{"date": d, **v} for d, v in sorted_view_days],
        },
        "referrers": sorted(referrer_totals.values(), key=lambda x: x["total"], reverse=True),
        "popular_paths": sorted(path_totals.values(), key=lambda x: x["total"], reverse=True),
    }
    return aggregated


def generate_dashboard(aggregated):
    """Generate a self-contained HTML dashboard with embedded data."""
    data_json = json.dumps(aggregated, indent=None, default=str)
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>GitHub Traffic Dashboard</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4"></script>
<style>
  *{{margin:0;padding:0;box-sizing:border-box}}
  body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;background:#0d1117;color:#e6edf3;padding:24px}}
  h1{{font-size:1.4em;margin-bottom:4px}}
  .subtitle{{color:#8b949e;font-size:0.85em;margin-bottom:24px}}
  .cards{{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-bottom:24px}}
  .card{{background:#161b22;border:1px solid #30363d;border-radius:8px;padding:16px}}
  .card .label{{color:#8b949e;font-size:0.75em;text-transform:uppercase;letter-spacing:0.5px}}
  .card .value{{font-size:1.8em;font-weight:600;margin-top:4px}}
  .card .sub{{color:#8b949e;font-size:0.8em;margin-top:2px}}
  .charts{{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:24px}}
  .chart-box{{background:#161b22;border:1px solid #30363d;border-radius:8px;padding:16px}}
  .chart-box h3{{font-size:0.9em;margin-bottom:12px;color:#8b949e}}
  .full-width{{grid-column:1/-1}}
  table{{width:100%;border-collapse:collapse;font-size:0.85em}}
  th{{text-align:left;color:#8b949e;padding:8px;border-bottom:1px solid #30363d;font-weight:500}}
  td{{padding:8px;border-bottom:1px solid #21262d}}
  .bar{{background:#238636;height:6px;border-radius:3px;display:inline-block;vertical-align:middle;margin-right:8px}}
</style>
</head>
<body>
<h1>&#128202; InvoiceFlow AI — GitHub Traffic Dashboard</h1>
<div class="subtitle" id="subtitle"></div>
<div class="cards" id="cards"></div>
<div class="charts">
  <div class="chart-box full-width"><h3>Daily Views &amp; Clones</h3><canvas id="dailyChart"></canvas></div>
  <div class="chart-box"><h3>Top Referrers</h3><canvas id="refChart"></canvas></div>
  <div class="chart-box"><h3>Top Pages</h3><canvas id="pathChart"></canvas></div>
</div>
<div class="chart-box full-width" style="margin-bottom:24px">
  <h3>All Pages Visited</h3>
  <table id="pathTable"><thead><tr><th>Page</th><th>Views</th><th>Unique</th><th></th></tr></thead><tbody></tbody></table>
</div>
<script>
const d = {data_json};
const repo = '/aws-samples/sample-ai-invoice-processing-with-amazon-bedrock';
const updated = new Date(d.last_updated).toLocaleDateString('en-US',{{year:'numeric',month:'short',day:'numeric',hour:'2-digit',minute:'2-digit'}});
document.getElementById('subtitle').textContent = d.date_range.start+' → '+d.date_range.end+'  •  Updated '+updated+'  •  '+d.total_snapshots+' snapshots';
const cards=[
  {{label:'Total Views',value:d.views.all_time_total,sub:d.views.all_time_unique+' unique'}},
  {{label:'Total Clones',value:d.clones.all_time_total,sub:d.clones.all_time_unique+' unique'}},
  {{label:'Top Referrer',value:d.referrers[0]?d.referrers[0].source:'—',sub:(d.referrers[0]?d.referrers[0].total:0)+' views'}},
  {{label:'Days Tracked',value:d.clones.daily.length,sub:'with daily data'}},
];
document.getElementById('cards').innerHTML=cards.map(c=>'<div class="card"><div class="label">'+c.label+'</div><div class="value">'+c.value+'</div><div class="sub">'+c.sub+'</div></div>').join('');
const labels=d.views.daily.map(v=>v.date.slice(5));
const cloneMap=Object.fromEntries(d.clones.daily.map(c=>[c.date.slice(5),c.total]));
new Chart(document.getElementById('dailyChart'),{{type:'bar',data:{{labels,datasets:[{{label:'Views',data:d.views.daily.map(v=>v.total),backgroundColor:'#388bfd'}},{{label:'Clones',data:labels.map(l=>cloneMap[l]||0),backgroundColor:'#238636'}}]}},options:{{responsive:true,scales:{{x:{{ticks:{{color:'#8b949e'}}}},y:{{ticks:{{color:'#8b949e'}},beginAtZero:true}}}},plugins:{{legend:{{labels:{{color:'#e6edf3'}}}}}}}}}});
const refs=d.referrers.slice(0,6);
new Chart(document.getElementById('refChart'),{{type:'doughnut',data:{{labels:refs.map(r=>r.source),datasets:[{{data:refs.map(r=>r.total),backgroundColor:['#388bfd','#238636','#f78166','#d2a8ff','#8b949e','#56d364']}}]}},options:{{responsive:true,plugins:{{legend:{{position:'bottom',labels:{{color:'#e6edf3',boxWidth:12}}}}}}}}}});
const topPaths=d.popular_paths.slice(0,8);
const shortNames=topPaths.map(p=>p.path.replace(repo,'')||'/');
new Chart(document.getElementById('pathChart'),{{type:'bar',data:{{labels:shortNames,datasets:[{{label:'Views',data:topPaths.map(p=>p.total),backgroundColor:'#d2a8ff'}}]}},options:{{indexAxis:'y',responsive:true,scales:{{x:{{ticks:{{color:'#8b949e'}},beginAtZero:true}},y:{{ticks:{{color:'#e6edf3',font:{{size:11}}}}}}}},plugins:{{legend:{{display:false}}}}}}}});
const maxP=d.popular_paths[0]?d.popular_paths[0].total:1;
document.querySelector('#pathTable tbody').innerHTML=d.popular_paths.map(p=>{{const s=p.path.replace(repo,'')||'/';const pct=Math.round(p.total/maxP*100);return '<tr><td>'+s+'</td><td>'+p.total+'</td><td>'+p.unique+'</td><td><span class="bar" style="width:'+pct+'px"></span></td></tr>'}}).join('');
</script>
</body>
</html>"""
    dashboard_path = SCRIPT_DIR / "traffic_dashboard.html"
    with open(dashboard_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Dashboard written to {dashboard_path}")


def print_summary(aggregated):
    print(f"\n{'='*60}")
    print(f"Aggregated Traffic: {aggregated['date_range']['start']} to {aggregated['date_range']['end']}")
    print(f"{'='*60}")
    print(f"Clones:  {aggregated['clones']['all_time_total']} total, {aggregated['clones']['all_time_unique']} unique")
    print(f"Views:   {aggregated['views']['all_time_total']} total, {aggregated['views']['all_time_unique']} unique")
    print(f"\nTop Referrers:")
    for r in aggregated["referrers"][:10]:
        print(f"  {r['source']}: {r['total']} views ({r['unique']} unique)")
    print(f"\nTop Paths:")
    for p in aggregated["popular_paths"][:10]:
        print(f"  {p['path']}: {p['total']} views ({p['unique']} unique)")
    print(f"\nSnapshots: {aggregated['total_snapshots']}")
    print(f"Written to: {AGGREGATED_FILE}\n")


def main():
    history = load_json(DATA_FILE) or {"repo": f"{REPO_OWNER}/{REPO_NAME}", "snapshots": []}

    # Seed initial data if history is empty
    if not history["snapshots"]:
        print("Seeding initial traffic data (March 9-23, 2026)...")
        history["snapshots"].append(seed_initial_data())
        save_json(DATA_FILE, history)

    # Fetch live data if token is available
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        print("GITHUB_TOKEN not set. Skipping live API fetch.")
        if history["snapshots"]:
            print(f"History contains {len(history['snapshots'])} snapshot(s).")
    else:
        print(f"Fetching traffic data for {REPO_OWNER}/{REPO_NAME}...")
        try:
            snapshot = fetch_traffic(token)
        except requests.exceptions.HTTPError as e:
            print(f"API error: {e}")
            sys.exit(1)

        # Deduplicate: replace snapshot with same period
        period_key = (snapshot["period"]["start"], snapshot["period"]["end"])
        history["snapshots"] = [
            s for s in history["snapshots"]
            if (s["period"]["start"], s["period"]["end"]) != period_key
        ]
        history["snapshots"].append(snapshot)
        save_json(DATA_FILE, history)
        print(f"Saved raw snapshot to {DATA_FILE}")

    # Always rebuild and write the aggregated file + dashboard
    aggregated = aggregate_all(history)
    save_json(AGGREGATED_FILE, aggregated)
    generate_dashboard(aggregated)
    print_summary(aggregated)


if __name__ == "__main__":
    main()
