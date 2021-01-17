import os
import click
import dotenv

import api

dotenv.load_dotenv(verbose=True)

API_KEY = os.getenv("AV_API_KEY")
if not API_KEY:
    print("error: API_KEY is null")
    exit(1)

MAIN_URL = "https://www.alphavantage.co"
QUERY_URL = MAIN_URL + "/query"


@click.command()
@click.option("--company", type=str, help="company to scrape data")
def main(company: str):
    if not company:
        print("error: company is null")
        exit(1)

    stocks = api.get_stocks(company)

    for stock in stocks:
        print(f"{stock.date}: open: {stock.open}")


if __name__ == "__main__":
    main()
