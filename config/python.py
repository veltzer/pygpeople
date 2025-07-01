""" python deps for this project """

import config.shared

install_requires: list[str] = [
    "pygooglehelper",
    "google-api-python-client",
    "pytconf",
    "pylogconf",
]
build_requires: list[str] = config.shared.PBUILD
test_requires: list[str] = config.shared.PTEST
requires = install_requires + build_requires + test_requires

scripts: dict[str,str] = {
    "pygpeople": "pygpeople.main:main",
}
