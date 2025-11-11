from datetime import datetime
from .extensions import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    comments = db.relationship("Comment", backref="task", cascade="all, delete-orphan")

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey("task.id"), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
