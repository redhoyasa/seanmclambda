import unittest
from unittest import mock

import vcr

from functions.goldbroker import *


class GoldbrokerTest(unittest.TestCase):

    @mock.patch("requests.get")
    def test_get_latest_gold_prices(self, response):
        response.return_value.ok = True
        response.return_value.json.return_value = {
            "weight_unit": "g",
            "_embedded": {
                "spot_prices": [
                    {
                        "date": "2020-03-26T03:35:02+00:00",
                        "value": 842911.17
                    },
                    {
                        "date": "2020-03-26T03:40:03+00:00",
                        "value": 844629.61
                    }
                ]
            }
        }
        result = get_latest_gold_prices()
        time_format = "%Y-%m-%dT%H:%M:%S%z"
        expected_result = {
            datetime.strptime("2020-03-26T03:35:02+00:00", time_format): 842911.17,
            datetime.strptime("2020-03-26T03:40:03+00:00", time_format): 844629.61
        }
        pd.testing.assert_frame_equal(pd.DataFrame(expected_result.items(), columns=['timestamp', 'value']), result)

    @mock.patch("requests.get")
    def test_get_gold_prices_failed(self, response):
        response.return_value.ok = False
        self.assertRaises(Exception, get_latest_gold_prices)

    @vcr.use_cassette('fixtures/vcr_cassettes/historical_spot_prices.yaml')
    def test_historical_gold_prices(self):
        result = get_historical_gold_prices()
        date_format = "%Y-%m-%d"
        expected_result = {
            datetime.strptime("2020-08-19", date_format): 923703.81,
        }
        pd.testing.assert_series_equal(pd.DataFrame(expected_result.items(), columns=['timestamp', 'value']).iloc[0], result.iloc[0])

if __name__ == '__main__':
    unittest.main()
