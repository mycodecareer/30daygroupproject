# Code in this file is inspired by
# https://flask.palletsprojects.com/en/1.1.x/testing/

import pytest

from app import app
from dotenv import load_dotenv, dotenv_values


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
        b'{\n  "author": "John Doe",\n  "description": "A delicious pizza!",\n  "title": "Pizza"\n}\n'
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
        b'{\n  "author": "babushka",\n  "description": "Meatballs in dough",\n  "title": "Pelmeny"\n}\n'
        in resp.data
    )


def test_enviroment_variables(client):
    load_dotenv()
    assert "FLASK_APP" in dotenv_values(".env")
    assert "FLASK_DEBUG" in dotenv_values(".env")
