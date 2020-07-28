import unittest
from unittest import mock

from functions.kroki import get_graph


class KrokiTest(unittest.TestCase):

    @mock.patch("requests.get")
    def test_get_graph(self, response):
        response.return_value.ok = True

        diagram_source = {
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
        f = get_graph(diagram_source=diagram_source)
        self.assertIsNotNone(f)

    @mock.patch("requests.get")
    def test_get_graph_failed(self, response):
        response.return_value.ok = False
        self.assertRaises(Exception, get_graph)


if __name__ == '__main__':
    unittest.main()
