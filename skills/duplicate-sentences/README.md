# duplicate-sentences

> Use this skill to detect repeated sentences in text (case/whitespace-insensitive) with their counts. Deterministic, offline. For catching LLM repetition and thin/padded content.

`v0.1.0` `analyzer` `cost: free`

## Install

**Claude Code / any skills.sh-compatible agent:**
```bash
npx skills add <owner>/duplicate-sentences
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
