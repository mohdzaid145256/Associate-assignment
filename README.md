# Task & Comments Manager  
## Full-Stack Application (Flask + React)

### Description  
This project is a professional full-stack web application built with a Python/Flask backend and a React frontend. It allows users to create and manage tasks, add comments to tasks, edit and delete both, with a modern UI featuring dark/light mode, smooth animations and timestamp management.  
It demonstrates end-to-end CRUD operations, REST API design, database migrations, and UI/UX polish.

---

### Table of Contents  
- [Features](#features)  
- [Tech Stack](#tech-stack)  
- [Backend Setup](#backend-setup)  
- [Frontend Setup](#frontend-setup)  
- [API Endpoints](#api-endpoints)  
- [Usage & Demo](#usage--demo)  
- [Screenshots](#screenshots)  
- [Testing](#testing)  
- [Project Status & Roadmap](#project-status--roadmap)  
- [Contributing](#contributing)  
- [License](#license)  

---

### Features  
- Create, list, edit and delete **Tasks**  
- For each task: view, add, edit and delete **Comments**  
- Dark/Light mode toggle with smooth UI transitions  
- Relative timestamps (e.g., “6 h”) plus full timestamp on hover  
- Responsive, professional UI built with animations  
- Backend: RESTful API endpoints, database migrations (Alembic), CORS support  
- Frontend: React + Axios for API calls, Tailwind CSS + Framer Motion for animations  

---

### Tech Stack  
**Backend:**  
- Python 3.12  
- Flask  
- SQLAlchemy ORM  
- Alembic / Flask-Migrate (database migrations)  
- SQLite (development)  
- Flask-CORS  

**Frontend:**  
- React  
- Axios  
- Tailwind CSS  
- Framer Motion  
- React Icons  

---

### Backend Setup  
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
By default, backend runs at: http://127.0.0.1:5001

Frontend Setup

cd frontend

npm install

npm start

API Endpoints
Tasks
Method	URL	Description
POST	/api/tasks	Create a new task
GET	/api/tasks	List all tasks
PUT	/api/tasks/<id>	Edit a task title
DELETE	/api/tasks/<id>	Delete a task
Comments
Method	URL	Description
POST	/api/tasks/<task_id>/comments	Create a comment under task
GET	/api/tasks/<task_id>/comments	List comments for a task
PUT	/api/comments/<comment_id>	Edit a comment
DELETE	/api/comments/<comment_id>	Delete a comment


