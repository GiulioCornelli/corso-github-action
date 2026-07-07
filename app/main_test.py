import os
from dotenv import load_dotenv
import pytest
from main import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_index(client):
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.get_json() == {"message": "Ciao dal Flask app!"}


def test_health(client):
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.get_json() == {"status": "ok"}


def test_get_tasks(client):
    resp = client.get("/tasks")
    assert resp.status_code == 200
    data = resp.get_json()
    assert len(data) == 2


def test_get_task_found(client):
    resp = client.get("/tasks/1")
    assert resp.status_code == 200
    assert resp.get_json()["id"] == 1


def test_get_task_not_found(client):
    resp = client.get("/tasks/999")
    assert resp.status_code == 404


def test_create_task(client):
    resp = client.post("/tasks", json={"title": "Test task"})
    assert resp.status_code == 201
    data = resp.get_json()
    assert data["title"] == "Test task"
    assert data["done"] is False


def test_create_task_missing_title(client):
    resp = client.post("/tasks", json={})
    assert resp.status_code == 400
