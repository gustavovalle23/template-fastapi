from fastapi.testclient import TestClient
import pytest

from app.main import app
from tests.seeds import UserSeed

client = TestClient(app)


@pytest.fixture(autouse=True)
def run_around_tests():
    UserSeed.insert_all()
    yield
    UserSeed.remove_all()


def test_should_check_list_users_endpoint():
    response = client.get("/user/all")
    assert response.status_code == 200
    assert response.json() == [{'email': 'admin@gmail.com'}, {'email': 'admin2@gmail.com'}]
