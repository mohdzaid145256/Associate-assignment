# Task & Comments Manager  
*A full-stack application: Flask API + React UI*

## Table of Contents  
- [Description](#description)  
- [Features](#features)  
- [Tech Stack](#tech-stack)  
- [Backend Setup](#backend-setup)  
- [Frontend Setup](#frontend-setup)  
- [API Endpoints](#api-endpoints)  
- [Usage & Demo](#usage--demo)  
- [Screenshots](#screenshots)  
- [Testing](#testing)  
- [Roadmap](#roadmap)  
- [Contributing](#contributing)  
- [License](#license)  
- [Author](#author)  

---

## Description  
This project is a professional full-stack web application built using **Flask** for the backend and **React** for the frontend. It allows users to create and manage tasks, add comments to tasks, edit and delete both tasks and comments, while offering a modern, polished UI with dark/light mode and timestamp functionality.

---

## Features  
- Create, list, edit, and delete **Tasks**  
- For each task: view, add, edit, and delete **Comments**  
- Dark/Light mode toggle, with smooth UI transitions  
- Relative timestamps (e.g., “6 h ago”) and full timestamp on hover  
- Responsive, professional UI with animations  
- RESTful API backend with database migrations and CORS support  
- React frontend uses Axios for API calls and modern UI tooling  

---

## Tech Stack  
**Backend:**  
- Python 3.12  
- Flask  
- SQLAlchemy ORM  
- Flask-Migrate / Alembic (for database migrations)  
- SQLite (for development)  
- Flask-CORS  

**Frontend:**  
- React  
- Axios  
- Tailwind CSS  
- Framer Motion (for animations)  
- React Icons  

---

## Backend Setup  
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export FLASK_APP=run.py
# If first time:
flask db init
flask db migrate -m "initial schema"
flask db upgrade
flask run --port=5001


Installation

Clone the repo:

git clone https://github.com/<your-username>/<repo-name>.git

cd <repo-name>

Backend Setup

Create & activate venv (recommended):

python -m venv venv

# macOS / Linux

source venv/bin/activate

Install backend requirements:

cd backend

pip install -r requirements.txt

Set env var and run migrations (first time only):

# macOS / Linux

export FLASK_APP=run.py

export FLASK_ENV=development

flask db init            # only first time

flask db migrate -m "initial schema"

flask db upgrade

Start backend:

flask run --port=5001

# Backend runs at http://127.0.0.1:5001 (default port used by the frontend connection)


Frontend Setup

From project root:

cd frontend

npm install

npm start

Frontend runs at: http://localhost:3000 and connects to backend on port 5001 by default.

Manual API check example:

curl -i http://127.0.0.1:5001/api/tasks

Testing

Backend unit tests are located in backend/tests/. Run them with:

cd backend

pytest -q

Author & Contact

Mohd Zaid – Python & React Developer


