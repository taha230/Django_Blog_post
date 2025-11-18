## CI workflow overview

- GitHub Actions workflow lives at `.github/workflows/ci.yml`.
- It runs on every push and pull request across branches.
- Steps: checkout, set up Python 3.12, install dependencies, run `flake8` (currently targeting core project modules and `tests`), run migrations, then execute `pytest`.

## Run checks locally

From the project root:

```bash
python -m venv .venv && source .venv/bin/activate  # optional
pip install -r requirements.txt
flake8
python manage.py migrate --noinput
pytest
```

If you want to mimic CI logs via Docker:

```bash
docker compose run --rm web flake8
docker compose run --rm web pytest
```

