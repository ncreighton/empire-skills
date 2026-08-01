# extract-numbers

> Use this skill to pull all numbers (ints, decimals, thousands-separated) from text, with their sum. Deterministic, offline. For parsing prices, stats, and quantities out of copy.

`v0.1.0` `analyzer` `cost: free`

## Install

**Claude Code / any skills.sh-compatible agent:**
```bash
npx skills add <owner>/extract-numbers
```

**As an MCP tool:** point your MCP client at the bundled `mcp_tool.json`, or install via the MCP registry entry.

## Usage

```bash
python run.py --text <string>
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `text` | string | yes | Input text |

## License

Proprietary — © SkillForge
