from flask import Flask
from .extensions import db, migrate

def create_app(config=None):
    app = Flask(__name__)

    # default config
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///dev.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # override with provided config (used by tests)
    if config:
        for k, v in config.items():
            app.config[k] = v

    # initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # import models so they are registered with SQLAlchemy
    # (importing here avoids circular imports)
    from app import models  # noqa: F401

    # register blueprints
    from app.api import bp as api_bp
    app.register_blueprint(api_bp)

    return app
