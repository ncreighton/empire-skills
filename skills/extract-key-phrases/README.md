# extract-key-phrases

> Use this skill to extract the most important key phrases / topics from a text as a short list. Uses an LLM. For tagging and SEO keyword discovery.

`v0.1.0` `analyzer` `cost: near_free`

## Install

**Claude Code / any skills.sh-compatible agent:**
```bash
npx skills add <owner>/extract-key-phrases
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
