from flask import request, jsonify, abort
from .extensions import db
from .models import Task, Comment

def _comment_to_dict(c):
    return {
        "id": c.id,
        "task_id": c.task_id,
        "content": c.content,
        "author": c.author,
        "created_at": c.created_at.isoformat() if c.created_at else None,
    }

def register_routes(app):
    @app.route("/api/tasks", methods=["POST"])
    def create_task():
        data = request.get_json() or {}
        title = data.get("title")
        if not title:
            return jsonify({"error": "title required"}), 400
        t = Task(title=title, description=data.get("description"))
        db.session.add(t)
        db.session.commit()
        return jsonify({"id": t.id, "title": t.title, "description": t.description}), 201

    @app.route("/api/tasks", methods=["GET"])
    def list_tasks():
        tasks = Task.query.all()
        return jsonify([{"id": t.id, "title": t.title, "description": t.description} for t in tasks])

    @app.route("/api/tasks/<int:task_id>/comments", methods=["POST"])
    def add_comment(task_id):
        # Ensure task exists
        task = Task.query.get_or_404(task_id)
        data = request.get_json() or {}
        content = data.get("content")
        if not content:
            return jsonify({"error": "content required"}), 400
        c = Comment(task_id=task.id, content=content, author=data.get("author"))
        db.session.add(c)
        db.session.commit()
        return jsonify(_comment_to_dict(c)), 201

    @app.route("/api/tasks/<int:task_id>/comments", methods=["GET"])
    def list_comments(task_id):
        Task.query.get_or_404(task_id)
        comments = Comment.query.filter_by(task_id=task_id).order_by(Comment.created_at.desc()).all()
        return jsonify([_comment_to_dict(c) for c in comments])

    @app.route("/api/tasks/<int:task_id>/comments/<int:cid>", methods=["PUT", "PATCH"])
    def update_comment(task_id, cid):
        Task.query.get_or_404(task_id)
        c = Comment.query.filter_by(task_id=task_id, id=cid).first_or_404()
        data = request.get_json() or {}
        if "content" in data:
            c.content = data.get("content")
        if "author" in data:
            c.author = data.get("author")
        db.session.commit()
        return jsonify(_comment_to_dict(c)), 200

    @app.route("/api/tasks/<int:task_id>/comments/<int:cid>", methods=["DELETE"])
    def delete_comment(task_id, cid):
        Task.query.get_or_404(task_id)
        c = Comment.query.filter_by(task_id=task_id, id=cid).first_or_404()
        db.session.delete(c)
        db.session.commit()
        return jsonify({"message": "deleted"}), 200
