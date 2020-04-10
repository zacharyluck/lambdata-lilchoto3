from my_lambdata.lambdata import DataFrameTransmogrifier
import pandas as pd
from pandas.testing import assert_frame_equal
import unittest


# Docstring
'''
DOCSTRING
Tests the functionality of DataFrameTransmogrifier and its
various capabilities
'''

base_df = pd.DataFrame({
    'name': ['Anders', 'Charles', 'Bryce'],
    'score': [87, 32, 58],
    'date': ['09-03-2020', '02-29-2020', '01-15-2019']
})


class LambdataTest(unittest.TestCase):
    '''
    Tests functionality for DataFrameTransmogrifier
    '''
    def test_lambdata_init(self):
        # test initialization of DataFrameTransmogrifier
        df = base_df.copy()
        df_t = DataFrameTransmogrifier(df)
        assert_frame_equal(df_t.df, df)

    def test_lambdata_date_split(self):
        # test splitting datetimes
        df = base_df.copy()
        df['date'] = pd.to_datetime(base_df['date'],
                                    infer_datetime_format=True)
        df_t = DataFrameTransmogrifier(df)

        # run the function itself
        df_t.split_datetime()

        # run what I think should happen
        df['date_month'] = df['date'].dt.month
        df['date_day'] = df['date'].dt.day
        df['date_year'] = df['date'].dt.year

        # check if i've done this right
        assert_frame_equal(df_t.df, df)

    def test_lambdata_add_column(self):
        # test adding a column of data
        df = base_df.copy()

        # create some data to test with
        data_to_add = [1, 0, 1]
        df_t = DataFrameTransmogrifier(df)

        # run what I think should happen
        df['ones_and_zeroes'] = pd.Series(data_to_add, index=df.index)

        # run the function itself
        df_t.add_column(data_to_add, 'ones_and_zeroes')

        # check if i've done this right
        assert_frame_equal(df_t.df, df)


def run_tests():
    unittest.main()

if __name__ == "__main__":
    unittest.main()
