# readability-grade

> Use this skill to score text readability with the correct Flesch Reading Ease (0-100) and Flesch-Kincaid grade-level formulas, plus a plain-language difficulty band. Deterministic, offline, no dependencies. Grade a draft before publishing to check it matches your audience.

`v0.1.0` `analyzer` `cost: free` `$7.00`

## Install

**Claude Code / any skills.sh-compatible agent:**
```bash
npx skills add <owner>/readability-grade
```

**As an MCP tool:** point your MCP client at the bundled `mcp_tool.json`, or install via the MCP registry entry.

## Usage

```bash
python run.py --text <string>
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `text` | string | yes | Text to grade |

## License

Proprietary — © SkillForge
