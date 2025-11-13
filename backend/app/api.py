from flask import Blueprint, request, jsonify
from .extensions import db
from .models import Task, Comment

def _iso(dt):
    try:
        return dt.isoformat()
    except:
        return None

def to_dict_task(t):
    return {"id": t.id, "title": t.title, "created_at": _iso(getattr(t, "created_at", None))}

def to_dict_comment(c):
    return {"id": c.id, "task_id": c.task_id, "body": c.body, "author": c.author, "created_at": _iso(getattr(c, "created_at", None))}

bp = Blueprint("api", __name__, url_prefix="/api")

@bp.route("/tasks", methods=["GET","POST"])
def tasks():
    if request.method == "POST":
        data = request.get_json() or {}
        title = data.get("title") or "Untitled"
        t = Task(title=title)
        db.session.add(t)
        db.session.commit()
        return jsonify(to_dict_task(t)), 201
    ts = Task.query.order_by(Task.id).all()
    return jsonify([to_dict_task(t) for t in ts]), 200

@bp.route("/tasks/<int:task_id>", methods=["PUT","DELETE"])
def task_modify(task_id):
    t = Task.query.get_or_404(task_id)
    if request.method == "PUT":
        data = request.get_json() or {}
        t.title = data.get("title", t.title)
        db.session.commit()
        return jsonify(to_dict_task(t)), 200
    if request.method == "DELETE":
        db.session.delete(t)
        db.session.commit()
        return jsonify({"message":"deleted"}), 200

@bp.route("/tasks/<int:task_id>/comments", methods=["GET","POST"])
def comments_for_task(task_id):
    Task.query.get_or_404(task_id)
    if request.method == "POST":
        data = request.get_json() or {}
        body = data.get("body")
        if not body:
            return jsonify({"error":"body required"}), 400
        c = Comment(task_id=task_id, body=body, author=data.get("author"))
        db.session.add(c)
        db.session.commit()
        return jsonify(to_dict_comment(c)), 201
    cs = Comment.query.filter_by(task_id=task_id).order_by(Comment.created_at.desc()).all()
    return jsonify([to_dict_comment(c) for c in cs]), 200

@bp.route("/comments/<int:comment_id>", methods=["PUT","DELETE"])
def comment_modify(comment_id):
    c = Comment.query.get_or_404(comment_id)
    if request.method == "PUT":
        data = request.get_json() or {}
        c.body = data.get("body", c.body)
        c.author = data.get("author", c.author)
        db.session.commit()
        return jsonify(to_dict_comment(c)), 200
    if request.method == "DELETE":
        db.session.delete(c)
        db.session.commit()
        return jsonify({"message":"deleted"}), 200
