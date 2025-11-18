## CI workflow overview

- GitHub Actions workflow lives at `.github/workflows/ci.yml`.
- It runs on every push and pull request across branches.
- Steps: checkout, set up Python 3.12, install dependencies, run migrations, then run Django tests.

## Run checks locally

From the project root:

```bash
python -m venv .venv && source .venv/bin/activate  # optional
pip install -r requirements.txt
python manage.py migrate --noinput
python manage.py test
```

If you want to mimic CI logs via Docker:

```bash
docker compose run --rm web python manage.py test
```

