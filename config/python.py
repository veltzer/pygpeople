""" python deps for this project """

scripts: dict[str,str] = {
    "pygpeople": "pygpeople.main:main",
}

config_requires: list[str] = [
    "pyclassifiers",
]
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
requires = config_requires + install_requires + build_requires + test_requires
