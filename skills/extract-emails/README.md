# extract-emails

> Use this skill to extract all valid email addresses from arbitrary text, de-duplicated and lowercased. Uses RFC-ish validation. Deterministic, offline. Useful for parsing scraped pages, contact forms, or documents for leads.

`v0.1.0` `analyzer` `cost: free`

## Install

**Claude Code / any skills.sh-compatible agent:**
```bash
npx skills add <owner>/extract-emails
```

**As an MCP tool:** point your MCP client at the bundled `mcp_tool.json`, or install via the MCP registry entry.

## Usage

```bash
python run.py --text <string>
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `text` | string | yes | Text to scan for emails |

## License

Proprietary — © SkillForge
