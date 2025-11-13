from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Instantiate extensions without an app; they'll be initialized in create_app()
db = SQLAlchemy()
migrate = Migrate()
