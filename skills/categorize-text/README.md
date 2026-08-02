# categorize-text

> Use this skill to assign the single best category to a text from a provided list of candidate categories, with a confidence note. Uses an LLM. For routing, tagging, and triage.

`v0.1.0` `analyzer` `cost: near_free`

## Install

**Claude Code / any skills.sh-compatible agent:**
```bash
npx skills add <owner>/categorize-text
```

**As an MCP tool:** point your MCP client at the bundled `mcp_tool.json`, or install via the MCP registry entry.

## Usage

```bash
python run.py --text <string> --categories <array>
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `text` | string | yes | Input text |
| `categories` | array | yes | Candidate categories (list or comma string) |

## License

Proprietary — © SkillForge
