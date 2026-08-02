# levenshtein-distance

> Use this skill to compute the Levenshtein edit distance between two strings plus a 0-1 similarity ratio. Deterministic, offline. For fuzzy matching and typo detection.

`v0.1.0` `analyzer` `cost: free`

## Install

**Claude Code / any skills.sh-compatible agent:**
```bash
npx skills add <owner>/levenshtein-distance
```

**As an MCP tool:** point your MCP client at the bundled `mcp_tool.json`, or install via the MCP registry entry.

## Usage

```bash
python run.py --a <string> --b <string>
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `a` | string | yes | First string |
| `b` | string | yes | Second string |

## License

Proprietary — © SkillForge
