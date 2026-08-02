# bytes-human

> Use this skill to format a byte count as a human-readable size (B/KB/MB/GB/TB/PB). Deterministic, offline. For file sizes and quotas.

`v0.1.0` `tool` `cost: free`

## Install

**Claude Code / any skills.sh-compatible agent:**
```bash
npx skills add <owner>/bytes-human
```

**As an MCP tool:** point your MCP client at the bundled `mcp_tool.json`, or install via the MCP registry entry.

## Usage

```bash
python run.py --bytes <number>
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `bytes` | number | yes | Number of bytes |

## License

Proprietary — © SkillForge
