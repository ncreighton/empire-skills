# word-frequency

> Use this skill to get the most frequent words in a text: tokenizes, lowercases, drops common stopwords (optional), and returns the top-N words with counts plus total/unique word counts. Deterministic, offline. For content analysis, keyword discovery, and tag suggestions.

`v0.1.0` `analyzer` `cost: free`

## Install

**Claude Code / any skills.sh-compatible agent:**
```bash
npx skills add <owner>/word-frequency
```

**As an MCP tool:** point your MCP client at the bundled `mcp_tool.json`, or install via the MCP registry entry.

## Usage

```bash
python run.py --text <string>
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `text` | string | yes | Text to analyze |
| `top` | number | no | How many top words (default 10) |
| `include_stopwords` | boolean | no | Include common stopwords (default false) |

## License

Proprietary — © SkillForge
