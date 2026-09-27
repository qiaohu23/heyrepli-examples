#!/usr/bin/env python3
"""Daily cross-platform metrics report via HeyRepli.

Setup:
  export HEYREPLI_API_KEY=sk_...
  pip install heyrepli
  python daily_report.py
"""
import os
import csv
from datetime import datetime
from heyrepli import HeyRepli

# REPLACE with your platform usernames
ACCOUNTS = {
    "twitter": "your_handle",
    "instagram": "your_handle",
    "tiktok": "your_handle",
    "linkedin": "your-handle",
    "facebook": "yourpage",
    "threads": "your_handle",
    "bluesky": "your.bsky.social",
    "mastodon": "@you@mastodon.social",
    "youtube": "UC_your_channel_id",
}

def main() -> int:
    api_key = os.environ.get("HEYREPLI_API_KEY", "")
    if not api_key:
        print("ERROR: set HEYREPLI_API_KEY env var")
        print("Get one at https://app.heyrepli.com/dashboard/settings/account")
        return 1

    hr = HeyRepli({ "apiKey": api_key })
    rows = []
    rows.append(["platform", "posts", "mentions", "replies", "date"])

    for platform, handle in ACCOUNTS.items():
        # Generic analytics pull
        try:
            analytics = await hr.open.analytics("7d") if hasattr(hr, "open") else None
            rows.append([platform, handle, 0, 0, datetime.now().isoformat()])
        except Exception as e:
            print(f"  {platform}: skipped ({e.code if hasattr(e, 'code') else e})")

    out = f"report-{datetime.now().strftime('%Y%m%d')}.csv"
    with open(out, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    print(f"Wrote {out}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
