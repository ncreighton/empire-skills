# slugify

> Use this skill whenever you need to convert an arbitrary string into a clean URL slug: lowercase, non-alphanumerics to single hyphens, collapse repeats, trim, optional max length on a word boundary. Deterministic, offline, no dependencies.

`v0.1.0` `tool` `cost: free`

## Install

**Claude Code / any skills.sh-compatible agent:**
```bash
npx skills add <owner>/slugify
```

**As an MCP tool:** point your MCP client at the bundled `mcp_tool.json`, or install via the MCP registry entry.

## Usage

```bash
python run.py --text <string>
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `text` | string | yes | Text to slugify |
| `max_length` | number | no | Max slug length (word-boundary trim) |

## License

Proprietary — © SkillForge
