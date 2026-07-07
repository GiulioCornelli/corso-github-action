# Corso GitHub Action

Repository di esempio per imparare GitHub Actions.

## Contenuto

- **`app/`** — mini applicazione Flask con API REST per gestire task
  - Endpoint: `/`, `/health`, `/ping`, `/tasks` (GET/POST), `/tasks/<id>` (GET)
  - Test con pytest in `main_test.py`
- **`.github/workflows/`** — workflow CI che esegue i test su PR verso `main`

## Come avviare

```bash
cd app
uv sync
uv run python main.py
```

Il server parte su `http://0.0.0.0:9090`.

## Come testare

```bash
cd app
uv run pytest main_test.py -v
```
