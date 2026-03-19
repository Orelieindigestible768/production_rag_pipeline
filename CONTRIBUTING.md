# Contributing

Thanks for contributing to `production_rag_pipeline`.

## Development Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e '.[full]'
```

## Verification

Run these checks before opening a pull request:

```bash
python -m unittest discover -s tests -v
python -m compileall src
```

## Pull Requests

- Keep changes scoped and explain the motivation clearly.
- Update `README.md` when behavior, API, or setup changes.
- Add or update tests for non-trivial changes.
- Include concrete reproduction steps for bug fixes.

## Issues

- Use the bug report template for regressions or incorrect behavior.
- Use the feature request template for product or API ideas.
- Include examples, logs, or failing inputs when possible.

## Style

- Prefer clear, direct code over clever abstractions.
- Keep public API changes intentional and documented.
- Avoid introducing optional dependencies into the base install unless necessary.
