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


def test_post_recipe(client):
    resp = client.post("/recipe")
    assert b"Title is missing" in resp.data

    resp = client.post("/recipe", data={"title": "Pelmeny", "author": "babushka"})
    assert b"Description is missing" in resp.data

    resp = client.post(
        "/recipe", data={"title": "Pelmeny", "description": "Meatballs in dough"}
    )
    assert b"Who is author by the way?" in resp.data

    resp = client.post(
        "/recipe",
        data={
            "title": "Pelmeny",
            "description": "Meatballs in dough",
            "author": "babushka",
        },
    )
    assert (
        b'{"author":"babushka","description":"Meatballs in dough","title":"Pelmeny"}\n'
        in resp.data
    )
