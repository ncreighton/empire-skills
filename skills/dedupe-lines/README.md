# dedupe-lines

> Use this skill to remove duplicate lines from text, preserving first-seen order by default (optionally sorted or case-insensitive). Deterministic, offline. Returns the deduped text plus kept/removed counts.

`v0.1.0` `tool` `cost: free`

## Install

**Claude Code / any skills.sh-compatible agent:**
```bash
npx skills add <owner>/dedupe-lines
```

**As an MCP tool:** point your MCP client at the bundled `mcp_tool.json`, or install via the MCP registry entry.

## Usage

```bash
python run.py --text <string>
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `text` | string | yes | Text with lines |
| `case_insensitive` | boolean | no | Treat lines differing only in case as duplicates |
| `keep_order` | boolean | no | Preserve first-seen order (else sorted) |

## License

Proprietary — © SkillForge
