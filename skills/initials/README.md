# initials

> Use this skill to get the initials of a name/phrase (first letter of each word, uppercased, capped at max). Deterministic, offline. For avatars/monograms.

`v0.1.0` `tool` `cost: free`

## Install

**Claude Code / any skills.sh-compatible agent:**
```bash
npx skills add <owner>/initials
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
| `max` | number | no | Max initials (default 3) |

## License

Proprietary — © SkillForge
