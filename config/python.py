""" python deps for this project """

import config.shared

install_requires: list[str] = [
    "pygooglehelper",
    "google-api-python-client",
    "pytconf",
    "pylogconf",
]
build_requires: list[str] = [
    "hatch",
    "pydmt",
    "pymakehelper",
    "pycmdtools",
]
test_requires: list[str] = [
    "pylint",
    "pytest",
    "mypy",
    "ruff",
]
requires = install_requires + build_requires + test_requires

scripts: dict[str,str] = {
    "pygpeople": "pygpeople.main:main",
}

