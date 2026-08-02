# roman-numeral

> Use this skill to convert an integer (1-3999) to a Roman numeral, or a Roman numeral back to an integer (to=roman|int). Deterministic, offline.

`v0.1.0` `tool` `cost: free`

## Install

**Claude Code / any skills.sh-compatible agent:**
```bash
npx skills add <owner>/roman-numeral
```

**As an MCP tool:** point your MCP client at the bundled `mcp_tool.json`, or install via the MCP registry entry.

## Usage

```bash
python run.py --value <string>
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `value` | string | yes | Integer or roman numeral |
| `to` | string | no | roman (default) or int |

## License

Proprietary — © SkillForge
