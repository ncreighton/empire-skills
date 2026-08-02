# csv-column

> Use this skill to extract a single column's values from CSV text by header name or index. Deterministic, offline. For pulling one field out of a spreadsheet export.

`v0.1.0` `tool` `cost: free`

## Install

**Claude Code / any skills.sh-compatible agent:**
```bash
npx skills add <owner>/csv-column
```

**As an MCP tool:** point your MCP client at the bundled `mcp_tool.json`, or install via the MCP registry entry.

## Usage

```bash
python run.py --csv <string> --column <string>
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `csv` | string | yes | CSV text |
| `column` | string | yes | Header name or 0-based index |

## License

Proprietary — © SkillForge
