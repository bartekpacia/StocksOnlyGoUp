import json

from flask import Flask, request
import api

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"


@app.route('/data', methods=["GET"])
def get_data():
    company = request.args.get("company")
    print(f"{company=}")
    stocks = api.get_stocks(company)

    json_string = json.dumps([repr(obj) for obj in stocks])

    return json.dumps(json_string)
