# n8n Workflow: YouTube transcript to Twitter drafts

Daily workflow:
1. Pull 5 video IDs from a list
2. Get transcript for each via HeyRepli (no YouTube API key needed)
3. AI rewrite each for Twitter
4. Save drafts to a Google Sheet for review

## Files

- workflow.json - importable n8n workflow definition
- HEYREPLI_SETUP.md - one-time setup notes

## Setup

1. Set HEYREPLI_API_KEY credential in n8n (Settings > Credentials > Header Auth)
2. Import workflow.json
3. Set your video ID list (replace sample IDs)
4. Connect a Google Sheet for draft storage
