# extract-action-items

> Use this skill to extract a clean list of concrete action items / to-dos from meeting notes or a message thread. Uses an LLM. Returns a list of short imperative tasks.

`v0.1.0` `analyzer` `cost: near_free`

## Install

**Claude Code / any skills.sh-compatible agent:**
```bash
npx skills add <owner>/extract-action-items
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
