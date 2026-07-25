# csv-to-json

> Use this skill to convert CSV text into a list of JSON records, auto-detecting the delimiter (comma, semicolon, tab, or pipe) and using the first row as headers. Handles ragged rows. Deterministic, offline. The reliable first step before processing spreadsheet exports.

`v0.1.0` `tool` `cost: free` `$5.00`

## Install

**Claude Code / any skills.sh-compatible agent:**
```bash
npx skills add <owner>/csv-to-json
```

**As an MCP tool:** point your MCP client at the bundled `mcp_tool.json`, or install via the MCP registry entry.

## Usage

```bash
python run.py --csv <string>
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `csv` | string | yes | CSV text to parse |
| `delimiter` | string | no | Force a delimiter (default: auto-detect) |

## License

Proprietary — © SkillForge
