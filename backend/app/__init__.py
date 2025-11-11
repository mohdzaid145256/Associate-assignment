from flask import Flask
from .extensions import db
from .models import Task, Comment
from .routes import register_routes

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    register_routes(app)

    # Flask 3.x compatible: create tables inside app context immediately
    with app.app_context():
        db.create_all()

    @app.route("/health")
    def health():
        return {"status": "ok"}

    return app
