import json
from typing import List
import requests

import main


class Stock:
    def __init__(self, date: str, open: float, high: float, low: float, close: float, volume: int):
        self.date = date
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume

    def __str__(self):
        return f"Stock(date: {self.date}, open: {self.open}, high: {self.high}, low: {self.low}, close: {self.close}, volume: {self.volume})"


def get_stocks(company: str) -> List[Stock]:
    query_params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": company,
        "apikey": main.API_KEY,
    }

    response = requests.get(main.QUERY_URL, params=query_params)
    
    print(f"status: {response.status_code}, url: {response.url}")
    response_data = response.json()
    stocks: List[Stock] = []
    print("begin")
    print(response_data)
    print("end")
    if response_data.get("Error Message"):
        print("Wrong stock code")
        return stocks

    stocks_by_date = response_data["Time Series (Daily)"]
    

    for date, stock_value in stocks_by_date.items():
        key_open = "1. open"
        value_open = stock_value[key_open]

        key_high = "2. high"
        value_high = stock_value[key_high]

        key_low = "3. low"
        value_low = stock_value[key_low]

        key_close = "4. close"
        value_close = stock_value[key_close]

        key_volume = "5. volume"
        value_volume = stock_value[key_volume]

        stock = Stock(date, open=float(value_open), high=float(value_high), low=float(value_low),
                      close=float(value_close), volume=int(value_volume)
                      )

        stocks.append(stock)

    return stocks
