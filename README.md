This repository contains my full-stack implementation for the Associate Software Engineer (Python + React) assessment.

## Tech
- Backend: Flask + SQLAlchemy
- Frontend: React + Axios
- DB: SQLite (local)
- Tests: pytest
- CI: GitHub Actions (runs pytest on push/PR)

## Backend
cd backend
source ../.venv/bin/activate
python -m backend.manage
# then: curl http://127.0.0.1:5000/health

## Frontend
cd frontend
npm install
npm start
# opens http://localhost:3000

## Tests
pytest -q

