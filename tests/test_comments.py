from app.models import db, Task, Comment

def test_create_comment(client, app):
    with app.app_context():
        t = Task(title="Sample")
        db.session.add(t)
        db.session.commit()
        tid = t.id

    r = client.post(f"/api/tasks/{tid}/comments", json={"body": "Hello", "author": "Zaid"})
    assert r.status_code == 201
    data = r.get_json()
    assert data["body"] == "Hello"
    assert data["author"] == "Zaid"

def test_list_comments(client, app):
    with app.app_context():
        t = Task(title="Test")
        db.session.add(t)
        db.session.commit()
        tid = t.id
        db.session.add(Comment(task_id=tid, body="A"))
        db.session.commit()

    r = client.get(f"/api/tasks/{tid}/comments")
    assert r.status_code == 200
    arr = r.get_json()
    assert len(arr) == 1
    assert arr[0]["body"] == "A"
