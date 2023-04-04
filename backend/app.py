from flask import Flask, request
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.route("/")
def hello():
    return "<h1>Hello, World!</h1>"


@app.route("/recipe", methods=["GET", "POST"])
def recipe():
    if request.method == "POST":
        # Lets store data recieved from form in a dictionary
        record = {}
        # Append information only if it's present
        if not request.form.get("title"):
            return "Title is missing"
        else:
            record["title"] = request.form.get("title")

        if not request.form.get("description"):
            return "Description is missing"
        else:
            record["description"] = request.form.get("description")

        if not request.form.get("author"):
            return "Who is author by the way?"
        else:
            record["author"] = request.form.get("author")

        return record
    else:
        return {
            "title": "Pizza",
            "description": "A delicious pizza!",
            "author": "John Doe",
        }
