import unittest
from datetime import datetime

import pandas as pd

from functions.altair import generate_time_series_chart_meta


class AltairTest(unittest.TestCase):

    def test_generate_time_series_chart_meta(self):
        time_arr = [
            datetime(2020, 3, 27, 15, 0, 0),
            datetime(2020, 3, 27, 16, 0, 0),
            datetime(2020, 3, 27, 17, 0, 0)
        ]
        df = pd.DataFrame({
            "timestamp": time_arr,
            "value": [1.22, 4.33, 3.22]})
        result = generate_time_series_chart_meta(df=df, x="timestamp", y="value")

        expected_result = {
          'config': {
            'view': {
              'continuousWidth': 400,
              'continuousHeight': 300
            }
          },
          'data': {
            'name': 'data-b9495870e7cafae3f5bd2d0a5f9893fb'
          },
          'mark': 'line',
          'encoding': {
            'x': {
              'type': 'temporal',
              'field': 'timestamp'
            },
            'y': {
              'type': 'quantitative',
              'field': 'value',
              'scale': {
                'zero': False
              }
            }
          },
          '$schema': 'https://vega.github.io/schema/vega-lite/v4.0.2.json',
          'datasets': {
            'data-b9495870e7cafae3f5bd2d0a5f9893fb': [{
              'timestamp': '2020-03-27T15:00:00',
              'value': 1.22
            }, {
              'timestamp': '2020-03-27T16:00:00',
              'value': 4.33
            }, {
              'timestamp': '2020-03-27T17:00:00',
              'value': 3.22
            }]
          }
        }
        self.assertDictEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
