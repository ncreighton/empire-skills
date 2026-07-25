# parse-any-date

> Use this skill to parse a date/time from almost any format (ISO 8601, GMT/RFC, epoch seconds or millis, common US/EU formats), normalize it to UTC, and get a humanized 'time ago' string plus age in hours. Deterministic, offline. Handles the messy timestamps agents get from APIs and scraped pages.

`v0.1.0` `tool` `cost: free`

## Install

**Claude Code / any skills.sh-compatible agent:**
```bash
npx skills add <owner>/parse-any-date
```

**As an MCP tool:** point your MCP client at the bundled `mcp_tool.json`, or install via the MCP registry entry.

## Usage

```bash
python run.py --value <string>
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `value` | string | yes | A date/time in any common format (or epoch number) |

## License

Proprietary — © SkillForge
