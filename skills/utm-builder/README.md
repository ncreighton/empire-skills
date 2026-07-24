# utm-builder

> Use this skill to append correctly-encoded UTM tracking parameters to a URL for campaign attribution (source, medium, campaign, term, content). Handles existing query strings and fragments. Deterministic, offline. Returns the tagged URL.

`v0.1.0` `tool` `cost: free`

## Install

**Claude Code / any skills.sh-compatible agent:**
```bash
npx skills add <owner>/utm-builder
```

**As an MCP tool:** point your MCP client at the bundled `mcp_tool.json`, or install via the MCP registry entry.

## Usage

```bash
python run.py --url <string> --source <string> --medium <string> --campaign <string>
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `url` | string | yes | Base URL |
| `source` | string | yes | utm_source |
| `medium` | string | yes | utm_medium |
| `campaign` | string | yes | utm_campaign |
| `term` | string | no | utm_term |
| `content` | string | no | utm_content |

## License

Proprietary — © SkillForge
