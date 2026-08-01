# alt-text-check

> Use this skill to audit image alt text in markdown: counts images, missing alt, and alt over 125 chars. Deterministic, offline. For accessibility + SEO image compliance.

`v0.1.0` `analyzer` `cost: free`

## Install

**Claude Code / any skills.sh-compatible agent:**
```bash
npx skills add <owner>/alt-text-check
```

**As an MCP tool:** point your MCP client at the bundled `mcp_tool.json`, or install via the MCP registry entry.

## Usage

```bash
python run.py --markdown <string>
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `markdown` | string | yes | Markdown/HTML content |

## License

Proprietary — © SkillForge
