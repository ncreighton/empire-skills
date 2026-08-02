# generate-cta

> Use this skill to generate N compelling call-to-action lines for a given product or offer description. Uses an LLM. Returns a list of CTA options.

`v0.1.0` `tool` `cost: near_free`

## Install

**Claude Code / any skills.sh-compatible agent:**
```bash
npx skills add <owner>/generate-cta
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
| `count` | number | no | How many CTAs (default 5) |

## License

Proprietary — © SkillForge
