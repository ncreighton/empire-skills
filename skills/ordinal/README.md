# ordinal

> Use this skill to convert an integer to its ordinal string (1->1st, 22->22nd, 113->113th). Deterministic, offline. For ranks and dates.

`v0.1.0` `tool` `cost: free`

## Install

**Claude Code / any skills.sh-compatible agent:**
```bash
npx skills add <owner>/ordinal
```

**As an MCP tool:** point your MCP client at the bundled `mcp_tool.json`, or install via the MCP registry entry.

## Usage

```bash
python run.py --number <number>
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `number` | number | yes | Integer to convert |

## License

Proprietary — © SkillForge
