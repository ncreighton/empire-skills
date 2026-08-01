# chunk-list

> Use this skill to split a list (or comma string) into fixed-size chunks. Deterministic, offline. For batching, pagination, grid layouts.

`v0.1.0` `tool` `cost: free`

## Install

**Claude Code / any skills.sh-compatible agent:**
```bash
npx skills add <owner>/chunk-list
```

**As an MCP tool:** point your MCP client at the bundled `mcp_tool.json`, or install via the MCP registry entry.

## Usage

```bash
python run.py --items <array>
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `items` | array | yes | List or comma-separated string |
| `size` | number | no | Chunk size (default 3) |

## License

Proprietary — © SkillForge
