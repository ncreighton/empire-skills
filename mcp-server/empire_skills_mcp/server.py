"""empire-skills MCP server — exposes every bundled executable skill as an MCP tool.

Each skill is a skills/<name>/skill.py with `def skill(ctx, **kwargs) -> dict`.
We load them dynamically, build an MCP tool per skill from its manifest.json input
schema, and dispatch calls over stdio. Deterministic skills need no ctx services,
so we pass a minimal shim.
"""
from __future__ import annotations

import importlib.util
import json
import os
from pathlib import Path

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

_HERE = Path(__file__).resolve().parent
_SKILLS = _HERE / "skills"

app = Server("empire-skills")


class _Ctx:
    niche = "general"
    agent_id = "mcp"

    def llm(self, prompt, model=None, max_tokens=1000):
        return ""  # deterministic skills don't call the LLM


def _load(name: str):
    spec = importlib.util.spec_from_file_location(
        f"skill_{name.replace('-', '_')}", _SKILLS / name / "skill.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return getattr(mod, "skill")


def _manifest(name: str) -> dict:
    p = _SKILLS / name / "manifest.json"
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _input_schema(man: dict) -> dict:
    props, required = {}, []
    for p in man.get("params", []):
        t = {"number": "number", "boolean": "boolean", "array": "array",
             "object": "object"}.get(p.get("type"), "string")
        props[p["name"]] = {"type": t, "description": p.get("description", "")}
        if p.get("required"):
            required.append(p["name"])
    return {"type": "object", "properties": props, "required": required}


_SKILL_NAMES = sorted(d.name for d in _SKILLS.iterdir() if (d / "skill.py").exists())


@app.list_tools()
async def list_tools() -> list[Tool]:
    tools = []
    for name in _SKILL_NAMES:
        man = _manifest(name)
        tools.append(Tool(
            name=name.replace("-", "_"),
            description=man.get("description", f"Empire skill: {name}"),
            inputSchema=_input_schema(man)))
    return tools


@app.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    skill_name = name.replace("_", "-")
    if skill_name not in _SKILL_NAMES:
        # tolerate underscore/hyphen mismatch
        skill_name = next((s for s in _SKILL_NAMES
                           if s.replace("-", "_") == name), skill_name)
    fn = _load(skill_name)
    result = fn(_Ctx(), **(arguments or {}))
    return [TextContent(type="text",
                        text=json.dumps(result, ensure_ascii=False, default=str))]


def main():
    import asyncio

    async def _run():
        async with stdio_server() as (r, w):
            await app.run(r, w, app.create_initialization_options())

    asyncio.run(_run())


if __name__ == "__main__":
    main()
