# percent-change

> Use this skill to compute the percentage change from an old value to a new value, plus absolute change and direction. Handles old=0. Deterministic, offline. For metrics/analytics.

`v0.1.0` `analyzer` `cost: free`

## Install

**Claude Code / any skills.sh-compatible agent:**
```bash
npx skills add <owner>/percent-change
```

**As an MCP tool:** point your MCP client at the bundled `mcp_tool.json`, or install via the MCP registry entry.

## Usage

```bash
python run.py --old <number> --new <number>
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `old` | number | yes | Original value |
| `new` | number | yes | New value |

## License

Proprietary — © SkillForge
