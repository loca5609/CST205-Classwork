from flask import Flask, render_template
import requests, json
from flask_bootstrap import Bootstrap
from pprint import pprint

app = Flask(__name__)
bootstrap = Bootstrap(app)


# apikey = open("ApiKey.txt","r")
# key = apikey.readline()
# HTTPS requires a paid plan...
# endpoint = 'http://data.fixer.io/api/latest?access_key='+key
data = {
    "date": "2018-10-16",
    "rates": {
        "CAD": 1.85,
        "GBP": 2.85,
        "JPY": 118.26
    }
}
keys = list(data['rates'].keys())


    
@app.route("/")
@app.route("/home")
def main():   
    return render_template("index.html",data=data,keys=keys)
