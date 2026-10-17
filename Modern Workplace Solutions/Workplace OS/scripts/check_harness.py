"""Check the local development foundation without network access or tenant calls."""

import ast
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

PROJECT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "AGENTS.md", ".agents/skills/project-tutor/SKILL.md", "README.md", "LAB.md",
    "CONTRIBUTIONS.md", "EVALUATION.md", "CHANGELOG.md", "DEMO SCRIPT.md",
    "docs/development-state.md", "docs/task-brief-template.md",
    "docs/harness-evaluation.md", "docs/adr/ADR-001-control-plane-and-adapters.md",
)
SKIP = {".git", ".venv", "venv", "node_modules", "__pycache__", ".pytest_cache",
        "dist", "build", "coverage", "private", "personal", "secrets", "logs"}


def source_files(folder):
    """Walk public project sources, avoiding dependencies and private directories."""
    for path in sorted(folder.iterdir()):
        if path.is_symlink() or path.name in SKIP:
            continue
        if path.is_dir():
            yield from source_files(path)
        elif path.suffix in {".md", ".py"}:
            yield path


def exact_path_exists(path):
    """Detect casing mistakes even on a case-insensitive filesystem."""
    if not path.exists():
        return False
    current = Path(path.anchor)
    for part in path.parts[1:]:
        if part not in {entry.name for entry in current.iterdir()}:
            return False
        current = current / part
    return True


def check(project=PROJECT):
    project = project.resolve()
    errors = []
    for name in REQUIRED:
        path = project / name
        if not path.is_file() or not path.read_text(encoding="utf-8").strip():
            errors.append(f"Missing or empty foundation file: {name}")
    counts = {"markdown_files": 0, "python_files": 0, "local_links": 0}
    for path in source_files(project):
        name = str(path.relative_to(project))
        try:
            content = path.read_text(encoding="utf-8-sig")
        except (OSError, UnicodeError) as exc:
            errors.append(f"{name}: cannot read source: {exc}")
            continue
        if path.suffix == ".py":
            counts["python_files"] += 1
            try:
                ast.parse(content, filename=name)
            except SyntaxError as exc:
                errors.append(f"{name}: Python syntax error at line {exc.lineno}")
            continue
        counts["markdown_files"] += 1
        content = re.sub(r"```.*?```", "", content, flags=re.S)
        content = re.sub(r"`[^`\n]*`", "", content)
        for target in re.findall(r"\]\(([^)]+)\)", content):
            target = target.split(' "')[0].strip().strip("<>")
            if not target or target.startswith("#") or urlsplit(target).scheme:
                continue
            counts["local_links"] += 1
            raw_path = path.parent / unquote(target.split("#")[0])
            resolved = raw_path.resolve()
            if not resolved.is_relative_to(project):
                errors.append(f"{name}: local link outside project: {target}")
            elif not exact_path_exists(resolved):
                errors.append(f"{name}: missing or wrong-case local link: {target}")
    return {"scope": "Workplace OS foundation files, local links and Python syntax",
            **counts, "errors": errors,
            "limits": "No application, agent-behaviour, secret-scan or live tenant verification."}


if __name__ == "__main__":
    result = check()
    print(json.dumps(result, indent=2))
    raise SystemExit(bool(result["errors"]))
