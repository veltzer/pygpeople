# TOFIX

Findings from a code scan on 2026-10-04.

## Medium

- `src/pygpeople/constants.py:6` - `SCOPES` requests full read/write `auth/calendar` (plus the redundant `calendar.readonly` at line 7) although the tool only reads profile and contacts through the People API (`main.py:33`, `main.py:54`); drop both calendar scopes so the OAuth grant is least-privilege (existing tokens are keyed by the scope hash, so users will simply re-consent once).
- `doc/TODO.txt:1` - the first two items ("move to the people api", "move to the new python API from the gdata- API") are already done - `main.py:7` uses `googleapiclient` with the People API v1; remove them and re-check the rest (the "update method" item at line 12 refers to code that no longer exists).
- `src/pygpeople/configs.py:8` - `ConfigEmpty` with a `doit` "Really fix the source?" flag is a copy-paste leftover; nothing imports it (both endpoints use `configs=[]`) - delete the module and its entry in `sphinx/pygpeople.rst:7`.

## Low

- `src/pygpeople/main.py:48` - `page_counter` is incremented (line 73) but never read; remove it or use it for progress logging.
- `src/pygpeople/__init__.py:5` - `LOGGER_NAME` duplicates the generated `static.py:5` value; drop the hand-written copy and import it from `pygpeople.static` where needed.
- `pyproject.toml:97` - `mypy_path = "src:python:scripts"` names `python/` and `scripts/` directories that do not exist; reduce it to `src`.
- `rsconstruct.toml:28` - `[processor.ruff]` and `[processor.mypy]` (line 32) list `config` in `src_dirs`, but `config/` holds only `.lua` files; drop it (and add `hatch_build.py` via `src_files` so the build hook is linted).
