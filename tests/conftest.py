import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

import pytest
from backend.app import create_app
from backend.app.extensions import db as _db

@pytest.fixture
def app():
    app = create_app()
    app.config.update({"TESTING": True, "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"})
    with app.app_context():
        _db.create_all()
        yield app
        _db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()
