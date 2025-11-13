from flask import Blueprint, request, jsonify, abort
from backend.app import db
from backend.app.models import Task, Comment

tasks_bp = Blueprint('tasks', __name__)

def _task_to_dict(t):
    return {"id": t.id, "title": t.title, "created_at": getattr(t, "created_at", None)}

def _comment_to_dict(c):
    return {
        "id": c.id,
        "task_id": c.task_id,
        "content": c.content,
        "author": getattr(c, "author", None),
        "created_at": getattr(c, "created_at", None)
    }

@tasks_bp.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json() or {}
    title = data.get('title') or data.get('name') or ''
    if not title:
        return jsonify({"error": "title required"}), 400
    t = Task(title=title)
    db.session.add(t)
    db.session.commit()
    return jsonify(_task_to_dict(t)), 201

@tasks_bp.route('/tasks', methods=['GET'])
def list_tasks():
    tasks = Task.query.order_by(Task.id).all()
    return jsonify([_task_to_dict(t) for t in tasks]), 200

@tasks_bp.route('/tasks/<int:task_id>', methods=['PUT', 'PATCH'])
def update_task(task_id):
    t = Task.query.get_or_404(task_id)
    data = request.get_json() or {}
    if "title" in data:
        t.title = data.get("title")
    db.session.commit()
    return jsonify(_task_to_dict(t)), 200

@tasks_bp.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    t = Task.query.get_or_404(task_id)
    db.session.delete(t)
    db.session.commit()
    return jsonify({"message":"deleted"}), 200

@tasks_bp.route('/tasks/<int:task_id>/comments', methods=['POST'])
def create_comment(task_id):
    Task.query.get_or_404(task_id)
    data = request.get_json() or {}
    content = data.get('content')
    author = data.get('author')
    if not content:
        return jsonify({"error":"content required"}), 400
    c = Comment(task_id=task_id, content=content, author=author)
    db.session.add(c)
    db.session.commit()
    return jsonify(_comment_to_dict(c)), 201

@tasks_bp.route('/tasks/<int:task_id>/comments', methods=['GET'])
def list_comments(task_id):
    Task.query.get_or_404(task_id)
    comments = Comment.query.filter_by(task_id=task_id).order_by(Comment.id).all()
    return jsonify([_comment_to_dict(c) for c in comments]), 200

@tasks_bp.route('/tasks/<int:task_id>/comments/<int:cid>', methods=['PUT', 'PATCH'])
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

@tasks_bp.route('/tasks/<int:task_id>/comments/<int:cid>', methods=['DELETE'])
def delete_comment(task_id, cid):
    Task.query.get_or_404(task_id)
    c = Comment.query.filter_by(task_id=task_id, id=cid).first_or_404()
    db.session.delete(c)
    db.session.commit()
    return jsonify({"message":"deleted"}), 200
