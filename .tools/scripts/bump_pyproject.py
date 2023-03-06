"""Bump `pyproject.toml` with changes in `requirements.txt`."""

from pathlib import Path

import toml

PYPROJECT = Path("pyproject.toml")
REQUIREMENTS = Path("requirements.txt")
PYPROJECT_TOOLS = Path(".tools") / PYPROJECT

requirements = REQUIREMENTS.read_text(encoding="utf-8").splitlines()
dependencies = [
    line.rstrip().replace("==", ">=")
    for line in requirements
    if line != "\n" and not line.startswith("#")
]

content = toml.loads(PYPROJECT.read_text(encoding="utf-8"))
content["project"]["dependencies"] = dependencies

PYPROJECT.write_text(
    encoding="utf-8",
    data=(
        "\n".join(
            (
                toml.dumps(content),
                PYPROJECT_TOOLS.read_text(encoding="utf-8"),
            )
        )
    ),
)
