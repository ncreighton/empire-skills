# strip-markdown

> Use this skill to strip markdown formatting from text and return clean plain text: removes headings, bold/italic, links (keeps link text), code fences, list markers, and blockquotes. Deterministic, offline. Great for generating previews or plain-text excerpts.

`v0.1.0` `tool` `cost: free`

## Install

**Claude Code / any skills.sh-compatible agent:**
```bash
npx skills add <owner>/strip-markdown
```

**As an MCP tool:** point your MCP client at the bundled `mcp_tool.json`, or install via the MCP registry entry.

## Usage

```bash
python run.py --markdown <string>
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `markdown` | string | yes | Markdown text |

## License

Proprietary — © SkillForge
