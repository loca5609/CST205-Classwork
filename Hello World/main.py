from flask import Flask, render_template
import requests, json
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)
data = {
    "name":"Jeremy",
    "age": 23,
    "class": "Druid"
}

@app.route("/")
@app.route("/home")
def main():
    return render_template("home.html",data=data)