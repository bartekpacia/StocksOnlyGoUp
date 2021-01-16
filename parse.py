import json

with open("query.json", "r") as file:
    query = json.load(file)

series = query["Time Series (Daily)"]

for k, date in enumerate(series):
    key_open = "1. open"
    value_open = series[date][key_open]

    print(f"{date}: {key_open}: {value_open}")
