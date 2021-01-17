import json

import requests
from flask import Flask, request, Response
import api

app = Flask(__name__)

TOKEN = "6GLcBmAQJkTAo4u6H3cYbg"


@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/upload_via_presigned_url")
def upload_file_via_presigned_url():
    # First, we need to get pre-signed url
    r = requests.post("https://api2.dropbase.io/v1/pipeline/generate_presigned_url", data={"token": TOKEN})
    if r.status_code != 200:  # Something failed
        return f"error, status: {r.status_code}, msg: {r.json}"

    presigned_url = r.json()["upload_url"]  # Link to upload a file
    job_id = r.json()["job_id"]  # Job_id to see the status of the pipeline once the file is uploaded

    # Now we upload the file
    r = requests.put(presigned_url,
                     data=open("data.json", "rb"))  # replace NHkJR6qjRu8kkRSk8zHiGt.csv with your file

    if r.status_code != 200:  # Failed to upload and run pipeline
        return f"error, status: {r.status_code}, msg: {r.json}"

    # The pipeline will now run
    return f"pipeline is running, id: {job_id}"

@app.route("/upload_via_presigned_url")
def upload_file_via_presigned_url():
    # First, we need to get pre-signed url
    r = requests.post("https://api2.dropbase.io/v1/pipeline/generate_presigned_url", data={"token": TOKEN})
    if r.status_code != 200:  # Something failed
        return f"error, status: {r.status_code}, msg: {r.json}"

    presigned_url = r.json()["upload_url"]  # Link to upload a file
    job_id = r.json()["job_id"]  # Job_id to see the status of the pipeline once the file is uploaded

    # Now we upload the file
    r = requests.put(presigned_url,
                     data=open("data.json", "rb"))  # replace NHkJR6qjRu8kkRSk8zHiGt.csv with your file

    if r.status_code != 200:  # Failed to upload and run pipeline
        return f"error, status: {r.status_code}, msg: {r.json}"

    # The pipeline will now run
    return f"pipeline is running, id: {job_id}"


@app.route("/data", methods=["GET"])
def get_data():
    company = request.args.get("company")
    
    if not company:
        return "Missing company name"
    
    stocks = api.get_stocks(company)
    if len(stocks) == 0:
        return 'Returned 0 elements, are you sure you are using correct stock code?'
    #Golden line
    stocks_str = json.dumps(stocks, default=lambda x: x.__dict__, indent=4)

    return Response(stocks_str, mimetype="application/json")
