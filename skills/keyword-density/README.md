# keyword-density

> Use this skill to compute how often a target keyword (or phrase) appears in a text, as a raw count and as a percentage of total words (0-100). Case-insensitive, whole-word matching, supports multi-word phrases. Deterministic, offline. Flags over-optimization above 3%.

`v0.1.0` `analyzer` `cost: free`

## Install

**Claude Code / any skills.sh-compatible agent:**
```bash
npx skills add <owner>/keyword-density
```

**As an MCP tool:** point your MCP client at the bundled `mcp_tool.json`, or install via the MCP registry entry.

## Usage

```bash
python run.py --text <string> --keyword <string>
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `text` | string | yes | The body text |
| `keyword` | string | yes | Keyword or phrase to measure |

## License

Proprietary — © SkillForge
