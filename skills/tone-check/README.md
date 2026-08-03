# tone-check

> Use this skill to assess the tone of a text (e.g. professional, casual, aggressive, warm) and flag any tone that clashes with a stated target tone. Uses an LLM. For brand-voice QA.

`v0.1.0` `analyzer` `cost: near_free`

## Install

**Claude Code / any skills.sh-compatible agent:**
```bash
npx skills add <owner>/tone-check
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
| `target_tone` | string | no | Desired tone to check against |

## License

Proprietary — © SkillForge
