from datetime import datetime

import pandas as pd
import requests

BASE_URL = "https://www.goldbroker.com/api/spot-prices?metal=XAU&currency={currency}&weight_unit=g"
TIME_FORMAT = "%Y-%m-%dT%H:%M:%S%z"


def get_latest_gold_prices(currency="IDR"):
    result = {}

    response = requests.get(BASE_URL.format(currency=currency))
    if not response.ok:
        raise Exception("failed to get gold prices")
    data = response.json()
    for price in data["_embedded"]["spot_prices"]:
        result[datetime.strptime(price["date"], TIME_FORMAT)] = price["value"]

    return pd.DataFrame(result.items(), columns=['timestamp', 'value'])
