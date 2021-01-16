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

    ret = ""
    for c in stocks:
        ret += str(c)

    print(f"{ret=}")
    return ret
