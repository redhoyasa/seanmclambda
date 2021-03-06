import logging
import os

from functions.altair import generate_time_series_chart_meta
from functions.goldbroker import get_historical_gold_prices
from functions.kroki import get_graph
from functions.seanmcapp import broadcast_photo


def broadcast_seanmcgold(event, context):
    logging.info('getting gold price')
    df_gold = get_historical_gold_prices()

    logging.info('generating chart meta')
    chart_meta = generate_time_series_chart_meta(df_gold, x="timestamp", y="value")

    logging.info('generating graph')
    graph_file = get_graph(chart_meta)

    logging.info('publish graph')
    secret_key = os.environ['SEANMCAPP_KEY']
    subscriber = int(os.environ['SEANMCGOLD_SUBSCRIBER'])
    broadcast_photo(secret_key=secret_key,
                    chat_id=subscriber,
                    photo_file=graph_file,
                    caption="Seanmcgold melaporkan harga emas saat ini")

    return {
        "message": "Seanmcgold executed successfully!",
        "event": event
    }
