import pandas as pd


class DataFrameTransmogrifier():
    def __init__(self, df):
        """
        Class constructor for DataFrameTransmogrifier.

        The transmogrifier is designed to take a given DataFrame
        and alter it for data science purposes.

        Parameters
        ----------
        df : DataFrame
            The DataFrame that will be modified.

            SEE: DataFrameTransmogrifier.return_dataframe()
                on getting the modified DataFrame out of the
                transmogrifier.
        """
        self.df = df

    def return_dataframe(self):
        """
        Get the DataFrame from the transmogrifier.

        Returns
        -------
        DataFrame
            DataFrame as stored in the transmogrifier.
        """
        return self.df

    def split_datetime(self, columns=None, dropcols=False):
        """
        Split datetime columns in a Dataframe by month, day, and year.

        Specify which columns specifically to split or leave blank
        to split all datetime dtype columns.

        Parameters
        ----------
        columns : single label or list-like
            Column labels to drop.
        """

        # Check if it's a DataFrame at all
        if not isinstance(self.df, pd.DataFrame):
            raise TypeError('Dataframe object is not a DataFrame')

        # check if the user didn't modify the columns parameter
        # aka: wants to do it for all columns
        if columns is None:
            columns = list(self.df.columns)

        # Check if given columns are reasonable
        if not isinstance(columns, str) and not isinstance(columns, list):
            raise TypeError(
                'Columns variable is not a string, list, or the default value.'
                )

        # print(columns)

        # this should throw a keyerror if the user gave bad columns.
        # also, regardless of whether the user gave a list or string
        # for columns, this should work
        temp = self.df.copy()
        mod_cols = temp[columns]
        for col in mod_cols:
            # check if the column is actually datetime
            # print (mod_cols[col].dtype.char)
            if mod_cols[col].dtype.char == 'M':
                # print('This column is a datetime')
                # split it up
                mod_cols[col+'_month'] = mod_cols[col].dt.month
                mod_cols[col+'_day'] = mod_cols[col].dt.day
                mod_cols[col+'_year'] = mod_cols[col].dt.year

                # Drop original column after splitting, if specified
                if dropcols:
                    temp = temp.drop(columns=col)

            # drop the split column from mod_cols to avoid duplicate
            # columns being added
            mod_cols = mod_cols.drop(columns=col)

        # Once all is said and done, recombine temp with the inputted df
        # and save the changes
        self.df = pd.concat([temp, mod_cols], axis=1).copy()

    def add_column(self, series, name):
        """
        Appends a list as a new column onto a given DataFrame.

        Parameters
        ----------
        series : list
            List to append onto DataFrame.

        name : str
            Name of the column to be added.
        """

        # print(self.df)

        # Check if it's a DataFrame at all
        if not isinstance(self.df, pd.DataFrame):
            raise TypeError('Inputted object is not a DataFrame')

        # Make sure the column isn't in df already
        if name in self.df.columns or not isinstance(name, str):
            raise KeyError('Name is already in DataFrame or not a string.')

        temp = self.df.copy()
        if isinstance(series, list):
            if (self.df.shape[0] == len(series)):
                series = pd.Series(series)
                temp[name] = series
            else:
                raise ValueError(
                    'Length of series variable is not the same as DataFrame.'
                )
        else:
            raise ValueError('Series variable is not a list.')

        # Save the changes
        self.df = temp

if __name__ == "__main__":
    # Testing code functionality
    df = pd.DataFrame({
        'name': ['Anders', 'Charles', 'Bryce'],
        'score': [87, 32, 58],
        'date': ['09-03-2020', '02-29-2020', '01-15-2019']
    })

    df['date'] = pd.to_datetime(df['date'], infer_datetime_format=True)

    print(f'Starting Dataframe:\n{df}\n')

    # initialize the class
    df_t = DataFrameTransmogrifier(df)

    # Test the functions
    df_t.split_datetime()
    df_t.add_column([92, 98, 99], 'new_score')
    df = df_t.return_dataframe()

    print(f'Resulting Dataframe:\n{df}')
