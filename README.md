# HeyRepli Examples

Integration examples for [HeyRepli](https://heyrepli.com) social media API. Each example folder is self-contained and shows how to call the API from a specific tool.

## Examples

| Folder | Tool | Description |
|---|---|---|
| [n8n-workflow/](n8n-workflow/) | n8n | Workflow that auto-fetches YouTube transcripts and rewrites them for Twitter |
| [make-scenario/](make-scenario/) | Make | Scenario that schedules posts across 6 platforms from a single Google Sheet |
| [python-script/](python-script/) | Python | Standalone script that aggregates TikTok/IG/Twitter metrics into a daily report |
| [openclaw-skill/](openclaw-skill/) | OpenClaw | Skill that exposes HeyRepli tools to AI agents via MCP |

## Setup

1. Get an API key at https://app.heyrepli.com/dashboard/settings/account
2. Set  in your environment
3. Pick an example, follow its README

## Security

- **Never commit API keys** - all examples read from  env var
- **No real keys in any file** - this repo is scanned before each push
- For local testing only - dont deploy examples to public servers with embedded keys

## Related

- [qiaohu23/heyrepli-js](https://github.com/qiaohu23/heyrepli-js) - Official TypeScript SDK
