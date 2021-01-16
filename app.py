import json

from flask import Flask, request, Response
import api

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"


@app.route('/data', methods=["GET"])
def get_data():
    company = request.args.get("company")
    stocks = api.get_stocks(company)

    stocks_str = json.dumps(stocks, default=lambda x: x.__dict__, indent=4)

    return Response(stocks_str, mimetype='application/json')
