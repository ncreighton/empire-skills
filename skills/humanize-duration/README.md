# humanize-duration

> Use this skill to convert a number of seconds into a human duration like '2h 5m 30s'. Deterministic, offline. For run-times, ETAs, video lengths.

`v0.1.0` `tool` `cost: free`

## Install

**Claude Code / any skills.sh-compatible agent:**
```bash
npx skills add <owner>/humanize-duration
```

**As an MCP tool:** point your MCP client at the bundled `mcp_tool.json`, or install via the MCP registry entry.

## Usage

```bash
python run.py --seconds <number>
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `seconds` | number | yes | Duration in seconds |

## License

Proprietary — © SkillForge
