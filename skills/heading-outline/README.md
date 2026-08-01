# heading-outline

> Use this skill to extract the heading outline (H1-H6) from markdown and check hierarchy health: flags multiple H1s and level jumps (H2->H4). Deterministic, offline. For SEO structure audits.

`v0.1.0` `analyzer` `cost: free`

## Install

**Claude Code / any skills.sh-compatible agent:**
```bash
npx skills add <owner>/heading-outline
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
