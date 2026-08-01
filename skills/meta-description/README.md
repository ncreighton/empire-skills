# meta-description

> Use this skill to generate a clean SEO meta description from article body text: strips markdown/URLs, collapses whitespace, truncates to a max length (default 155) on a word boundary. Deterministic, offline.

`v0.1.0` `tool` `cost: free`

## Install

**Claude Code / any skills.sh-compatible agent:**
```bash
npx skills add <owner>/meta-description
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
| `max_length` | number | no | Max chars (default 155) |

## License

Proprietary — © SkillForge
