# Backend — FastAPI

Modular monolith: `API → Service → Repository → Database`. See [../docs/architecture.md](../docs/architecture.md).

## Run locally (without Docker)

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

cp ../.env.example ../.env   # edit values as needed

uvicorn app.main:app --reload
```

- API: http://localhost:8000
- Docs: http://localhost:8000/docs
- Health check: http://localhost:8000/health

## Run tests

```bash
pytest
```

## Layout

```text
app/
├── api/v1/          Versioned route definitions (thin — delegate to services)
├── core/            Config, security, shared settings
├── models/          SQLAlchemy ORM models
├── schemas/         Pydantic request/response schemas
├── services/        Business logic (ai/, storage/, resume/, matching/)
├── repositories/    Database access, one per aggregate
├── db/              Session/engine setup, Alembic migrations
└── main.py          App factory
```
