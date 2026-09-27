# Python: Daily cross-platform metrics report

Standalone script that aggregates TikTok/IG/Twitter post metrics into a CSV report.

## Setup

```bash
export HEYREPLI_API_KEY=sk_...  # get from https://app.heyrepli.com/dashboard/settings/account
pip install heyrepli
python daily_report.py
```

## What it does

1. Calls HeyRepli API to fetch your last 7 days of posts across platforms
2. Aggregates views, likes, comments per platform
3. Writes report.csv with daily breakdown

Set your platform usernames in the  dict before running.
