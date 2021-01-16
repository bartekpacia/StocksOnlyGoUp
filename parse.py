import json
import os
import requests

import click
import dotenv

dotenv.load_dotenv(verbose=True)

API_KEY = None
MAIN_URL = "https://www.alphavantage.co"
QUERY_URL = MAIN_URL + "/query"


@click.command()
@click.option("--company", type=str, help="company to scrape data")
def main(company: str):
    API_KEY = os.getenv("AV_API_KEY")

    if not API_KEY:
        print("error: API_KEY is null")
        exit(1)

    if not company:
        print("error: company is null")
        exit(1)

    query_params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": company,
        "apikey": API_KEY,
    }

    response = requests.get(QUERY_URL, params=query_params)

    print(f"status: {response.status_code}, url: {response.url}")
    response_data = response.json()

    series = response_data["Time Series (Daily)"]

    for k, date in enumerate(series):
        key_open = "1. open"
        value_open = series[date][key_open]

        print(f"{date}: {key_open}: {value_open}")


if __name__ == "__main__":
    main()
