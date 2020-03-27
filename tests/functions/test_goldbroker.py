import unittest
from unittest import mock

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
        expected_result = {
            "2020-03-26T03:35:02+00:00": 842911.17,
            "2020-03-26T03:40:03+00:00": 844629.61
        }
        pd.testing.assert_frame_equal(pd.DataFrame(expected_result.items(), columns=['timestamp', 'value']), result)

    @mock.patch("requests.get")
    def test_get_gold_prices_failed(self, response):
        response.return_value.ok = False
        self.assertRaises(Exception, get_latest_gold_prices)