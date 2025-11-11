def create_task(client, title="Test Task"):
    rv = client.post("/api/tasks", json={"title": title})
    assert rv.status_code == 201
    return rv.get_json()

def test_create_and_list_comments(client):
    t = create_task(client)
    task_id = t["id"]

    # create a comment
    r = client.post(f"/api/tasks/{task_id}/comments", json={"content": "hello", "author": "Zaid"})
    assert r.status_code == 201
    comment = r.get_json()
    assert comment["content"] == "hello"
    assert comment["author"] == "Zaid"

    # list comments
    lr = client.get(f"/api/tasks/{task_id}/comments")
    assert lr.status_code == 200
    arr = lr.get_json()
    assert isinstance(arr, list)
    assert len(arr) == 1
    assert arr[0]["content"] == "hello"

def test_update_and_delete_comment(client):
    t = create_task(client, "Task 2")
    task_id = t["id"]

    r = client.post(f"/api/tasks/{task_id}/comments", json={"content": "orig", "author": "A"})
    assert r.status_code == 201
    cid = r.get_json()["id"]

    # update (PUT)
    ur = client.put(f"/api/tasks/{task_id}/comments/{cid}", json={"content": "edited", "author": "B"})
    assert ur.status_code == 200
    assert ur.get_json()["content"] == "edited"
    assert ur.get_json()["author"] == "B"

    # delete
    dr = client.delete(f"/api/tasks/{task_id}/comments/{cid}")
    assert dr.status_code == 200
    assert dr.get_json()["message"] == "deleted"

    # ensure gone
    lr = client.get(f"/api/tasks/{task_id}/comments")
    assert all(c["id"] != cid for c in lr.get_json())
