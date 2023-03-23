from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "<h1>Hello, World!</h1>"


@app.route("/recipe", methods=["GET"])
def recipe():
    return {"title": "Pizza", "description": "A delicious pizza!", "author": "John Doe"}
