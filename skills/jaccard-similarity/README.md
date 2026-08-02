# jaccard-similarity

> Use this skill to measure word-set (Jaccard) similarity between two texts (0-1), with shared-word count and a near-duplicate flag (>=0.8). Deterministic, offline. For dedup and content-overlap detection.

`v0.1.0` `analyzer` `cost: free`

## Install

**Claude Code / any skills.sh-compatible agent:**
```bash
npx skills add <owner>/jaccard-similarity
```

**As an MCP tool:** point your MCP client at the bundled `mcp_tool.json`, or install via the MCP registry entry.

## Usage

```bash
python run.py --text_a <string> --text_b <string>
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `text_a` | string | yes | First text |
| `text_b` | string | yes | Second text |

## License

Proprietary — © SkillForge
