# AI Job Application Copilot

A full-stack AI-assisted job application tracker: upload resumes, add job postings, get a deterministic resume/job match score, and track applications end to end.

This repository is currently a **backbone** — the initial milestone focuses on structure, authentication, and the core Register → Login → Upload Resume → Add Job → Analyze → Match → Track Application flow. See [docs/architecture.md](docs/architecture.md) for the full design and [infrastructure/azure/README.md](infrastructure/azure/README.md) for the target Azure deployment.

## Stack

- **Frontend:** React, TypeScript, Vite, Tailwind CSS, React Router, TanStack Query
- **Backend:** Python 3.12+, FastAPI, Pydantic, SQLAlchemy, Alembic
- **Database:** PostgreSQL + pgvector
- **AI:** OpenAI API, behind an internal `AIService` abstraction
- **Target cloud:** Azure (Static Web Apps, Container Apps, PostgreSQL Flexible Server, Blob Storage, Key Vault, Monitor)

## Repository layout

```text
job-copilot/
├── frontend/       React + TypeScript app
├── backend/        FastAPI app (modular monolith)
├── infrastructure/ Azure deployment notes
├── docs/           Architecture documentation
└── docker-compose.yml
```

## Running locally

Local development runs entirely without Azure.

```bash
cp .env.example .env
docker compose up --build
```

- Frontend: http://localhost:5173
- Backend API: http://localhost:8000
- API docs: http://localhost:8000/docs

Frontend and backend can also be run independently — see `frontend/README.md` and `backend/README.md` (added as those pieces are built).

## Status

This project is being built incrementally, milestone by milestone. See [docs/architecture.md](docs/architecture.md) for the milestone plan and current progress.
