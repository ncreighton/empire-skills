# temperature-convert

> Use this skill to convert a temperature between Celsius, Fahrenheit, and Kelvin (from_unit/to_unit = C/F/K). Deterministic, offline.

`v0.1.0` `tool` `cost: free`

## Install

**Claude Code / any skills.sh-compatible agent:**
```bash
npx skills add <owner>/temperature-convert
```

**As an MCP tool:** point your MCP client at the bundled `mcp_tool.json`, or install via the MCP registry entry.

## Usage

```bash
python run.py --value <number>
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `value` | number | yes | Temperature value |
| `from_unit` | string | no | C/F/K (default C) |
| `to_unit` | string | no | C/F/K (default F) |

## License

Proprietary — © SkillForge
