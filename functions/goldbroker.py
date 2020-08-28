from datetime import datetime

import pandas as pd
import requests

SPOT_PRICE_URL = "https://www.goldbroker.com/api/spot-prices?metal=XAU&currency={currency}&weight_unit=g"
HISTORICAL_PRICE_URL = "https://www.goldbroker.com/api/historical-spot-prices?metal=XAU&currency={currency}&weight_unit=g"
TIME_FORMAT = "%Y-%m-%dT%H:%M:%S%z"
DATE_FORMAT = "%Y-%m-%d"
NUMBER_OF_ENTRIES = 7


def get_latest_gold_prices(currency="IDR"):
    result = {}

    response = requests.get(SPOT_PRICE_URL.format(currency=currency))
    if not response.ok:
        raise Exception("failed to get gold prices")
    data = response.json()
    for price in data["_embedded"]["spot_prices"]:
        result[datetime.strptime(price["date"], TIME_FORMAT)] = price["value"]

    return pd.DataFrame(result.items(), columns=['timestamp', 'value'])


def get_historical_gold_prices(currency="IDR"):
    result = {}

    response = requests.get(HISTORICAL_PRICE_URL.format(currency=currency))
    if not response.ok:
        raise Exception("failed to get gold prices")
    data = response.json()
    for price in data["_embedded"]["historical_spot_prices"]:
        result[datetime.strptime(price["date"], DATE_FORMAT)] = price["close"]

    return pd.DataFrame(result.items(), columns=['timestamp', 'value'])\
        .tail(n=NUMBER_OF_ENTRIES)\
        .reset_index(drop=True)
