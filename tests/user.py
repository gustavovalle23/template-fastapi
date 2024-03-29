import json
import pytest
from fastapi.testclient import TestClient
from requests.models import Response

from app.main import app
from tests.seeds import UserSeed

client = TestClient(app)


@pytest.fixture(autouse=True)
def run_around_tests():
    UserSeed.insert_all()
    yield
    UserSeed.remove_all()


def test_should_list_users():
    response: Response = client.get("/users")
    assert response.status_code == 200
    assert response.json() == [
        {'id': 1, 'email': 'admin@gmail.com', 'active': True},
        {'id': 2, 'email': 'admin2@gmail.com', 'active': True}
    ]


def test_should_get_an_user():
    response: Response = client.get("/user/1")
    assert response.status_code == 200
    assert response.json() == {
        'id': 1, 'email': 'admin@gmail.com', 'active': True
    }


def test_should_update_an_user():
    user = json.dumps({'email': 'admin_updated@gmail.com', 'active': True})
    update_user: Response = client.post("/user/1", data=user)
    assert update_user.status_code == 200
    user_updated: Response = client.get("/user/1")
    assert user_updated.json().get('email') == 'admin_updated@gmail.com'


def test_should_create_an_user():
    user = json.dumps({'email': 'new_user@gmail.com',
                      'password': '123', 'active': True})
    response: Response = client.post("/user/register", data=user)
    assert response.status_code == 201
    assert response.json().get('user').get('id') != None


def test_should_delete_an_user():
    response: Response = client.delete("/user/1")
    assert response.status_code == 200
    response: Response = client.get("/user/1")
    print(response.json())
