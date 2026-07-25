# utm-report

> Use this skill to audit a batch of URLs for campaign attribution: parses UTM parameters from every URL, flags untagged links, and aggregates counts by source and by campaign. Deterministic, offline. Feed it your link list and get an attribution-readiness report.

`v0.1.0` `analyzer` `cost: free` `$5.00`

## Install

**Claude Code / any skills.sh-compatible agent:**
```bash
npx skills add <owner>/utm-report
```

**As an MCP tool:** point your MCP client at the bundled `mcp_tool.json`, or install via the MCP registry entry.

## Usage

```bash
python run.py --urls <array>
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `urls` | array | yes | List of URLs (or a newline-separated string) |

## License

Proprietary — © SkillForge
