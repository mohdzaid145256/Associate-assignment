# backend/manage.py — package-safe entrypoint
# This file uses package-qualified imports so `python -m backend.manage`
# works from the project root and `python manage.py` works from backend/.
from backend.app import create_app
from backend.app.extensions import db
# Import models so SQLAlchemy sees them (migrations/tests)
from backend.app import models  # noqa: F401

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
