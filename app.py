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
    
    if not company:
        return "Missing company name"
    
    stocks = api.get_stocks(company)
    if len(stocks) == 0:
        return 'Returned 0 elements, are you sure you are using correct stock code?'
    #Golden line
    stocks_str = json.dumps(stocks, default=lambda x: x.__dict__, indent=4)

    return Response(stocks_str, mimetype='application/json')
