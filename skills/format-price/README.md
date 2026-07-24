# format-price

> Use this skill to format a numeric amount as a currency string with the correct symbol, thousands separators, and two decimals (USD, EUR, GBP, etc.). Handles ints, floats, and numeric strings. Deterministic, offline.

`v0.1.0` `tool` `cost: free`

## Install

**Claude Code / any skills.sh-compatible agent:**
```bash
npx skills add <owner>/format-price
```

**As an MCP tool:** point your MCP client at the bundled `mcp_tool.json`, or install via the MCP registry entry.

## Usage

```bash
python run.py --amount <number>
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `amount` | number | yes | The amount |
| `currency` | string | no | ISO code (USD/EUR/GBP/JPY), default USD |

## License

Proprietary — © SkillForge
