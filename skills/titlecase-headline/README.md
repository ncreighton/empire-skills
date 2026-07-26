# titlecase-headline

> Use this skill to convert a string to AP-style headline title case: capitalizes the first and last word and all major words, but lowercases short articles/conjunctions/prepositions (a, an, the, and, of, to, etc.) when they fall mid-headline. Deterministic, offline. For post titles and headings.

`v0.1.0` `tool` `cost: free`

## Install

**Claude Code / any skills.sh-compatible agent:**
```bash
npx skills add <owner>/titlecase-headline
```

**As an MCP tool:** point your MCP client at the bundled `mcp_tool.json`, or install via the MCP registry entry.

## Usage

```bash
python run.py --text <string>
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `text` | string | yes | Headline text to title-case |

## License

Proprietary — © SkillForge
