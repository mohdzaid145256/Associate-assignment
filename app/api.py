from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models import Task, Comment

bp = Blueprint("api", __name__, url_prefix="/api")

def to_dict(comment):
    return {
        "id": comment.id,
        "task_id": comment.task_id,
        "body": comment.body,
        "author": comment.author,
        "created_at": comment.created_at.isoformat() if comment.created_at else None
    }

@bp.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json() or {}
    title = data.get("title") or "Untitled"
    t = Task(title=title)
    db.session.add(t)
    db.session.commit()
    return jsonify({"id": t.id, "title": t.title}), 201

@bp.route("/tasks/<int:task_id>/comments", methods=["POST"])
def create_comment(task_id):
    Task.query.get_or_404(task_id)
    data = request.get_json() or {}
    body = data.get("body")
    if not body:
        return jsonify({"error": "body is required"}), 400
    c = Comment(task_id=task_id, body=body, author=data.get("author"))
    db.session.add(c)
    db.session.commit()
    return jsonify(to_dict(c)), 201

@bp.route("/tasks/<int:task_id>/comments", methods=["GET"])
def list_comments(task_id):
    Task.query.get_or_404(task_id)
    comments = Comment.query.filter_by(task_id=task_id).order_by(Comment.created_at.desc()).all()
    return jsonify([to_dict(c) for c in comments]), 200

@bp.route("/comments/<int:comment_id>", methods=["PUT"])
def update_comment(comment_id):
    c = Comment.query.get_or_404(comment_id)
    data = request.get_json() or {}
    c.body = data.get("body", c.body)
    c.author = data.get("author", c.author)
    db.session.commit()
    return jsonify(to_dict(c)), 200

@bp.route("/comments/<int:comment_id>", methods=["DELETE"])
def delete_comment(comment_id):
    c = Comment.query.get_or_404(comment_id)
    db.session.delete(c)
    db.session.commit()
    return jsonify({"message": "deleted"}), 200
