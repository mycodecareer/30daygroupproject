from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'

@app.route("/recipe")
def get_recipe():
    return [{"title":"Pizza Recipe", "author":"John Doe","description":"A simple pizza recipe!!"}]
