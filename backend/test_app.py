# Code in this file is inspired by
# https://flask.palletsprojects.com/en/1.1.x/testing/

import pytest

from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_get_home(client):
    resp = client.get("/")
    assert b"<h1>Hello, World!</h1>" in resp.data


def test_get_recipe(client):
    resp = client.get("/recipe")
    assert (
        b'{"author":"John Doe","description":"A delicious pizza!","title":"Pizza"}\n'
        in resp.data
    )
