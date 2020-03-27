import unittest
from datetime import datetime

import pandas as pd
from functions.dataframe.utils import add_hour


class Utils(unittest.TestCase):

    def test_add_hour(self):
        time_arr = [
            datetime(2020, 3, 27, 15, 0, 0),
            datetime(2020, 3, 27, 16, 0, 0)
        ]
        df = pd.DataFrame({"timestamp": time_arr})

        df = add_hour(df, column="timestamp", hour=2)

        expected_time_arr = [
            datetime(2020, 3, 27, 17, 0, 0),
            datetime(2020, 3, 27, 18, 0, 0)
        ]
        expected_df = pd.DataFrame({"timestamp": expected_time_arr})
        pd.testing.assert_frame_equal(expected_df, df)
        self.assertEqual(len(expected_df.index), len(df.index))


if __name__ == '__main__':
    unittest.main()
