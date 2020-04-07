import pandas as pd

def split_datetime(df, columns=None):
    """
    Split datetime columns in a Dataframe by month, day, and year.

    Specify which columns specifically to split or leave blank
    to split all datetime dtype columns.

    Parameters
    ----------
    df : DataFrame
        Dataframe to split datetime columns in.

    columns : single label or list-like
        Column labels to drop.

    Returns
    -------
    DataFrame
        DataFrame with the specified dtype datetime columns split
    """

    # Check if it's a DataFrame at all
    if not isinstance(df, pd.DataFrame):
        raise TypeError('Inputted object is not a DataFrame')
    
    # Grab a copy of the dataframe to avoid warnings
    temp = df.copy()

    # turn the columns from a string into a list for easier code
    if isinstance(columns, str):
        columns = [columns]

    # function if given columns
    if isinstance(columns, list):
        # this should throw a keyerror if the user gave bad columns
        temp = temp[[columns]]
        for col in columns:
            # check if the column is actually datetime
            if temp[col].dtype.char == 'M':
                # split it up
                temp[col+'_month'] = temp[col].dt.month
                temp[col+'_day'] = temp[col].dt.day
                temp[col+'_year'] = temp[col].dt.year

                # Drop old columns
                temp = temp.drop(columns=col)
    else:
        # else do all columns
        for col in df.columns:
            # check column for datetime dtype
            if temp[col].dtype.char == 'M':
                # split it up
                temp[col+'_month'] = temp[col].dt.month
                temp[col+'_day'] = temp[col].dt.day
                temp[col+'_year'] = temp[col].dt.year

            # Drop column regardless of whether or not it was split,
            # temp needs to be only split columns by the end of it.
            temp = temp.drop(columns=col)

    # Once all is said and done, recombine temp with the inputted df
    # and return it.
    return pd.concat([df, temp], axis=1)

def add_column(df, series, name):
    """
    Appends a list as a new column onto a given DataFrame.

    Parameters
    ----------
    df : DataFrame
        DataFrame to append list onto.

    series : list
        List to append onto DataFrame.
    
    name : str
        Name of the column to be added.

    Returns
    -------
    DataFrame
        DataFrame with the list added onto it as a new
        Series with column header.
    """

    # Check if it's a DataFrame at all
    if not isinstance(df, pd.DataFrame):
        raise TypeError('Inputted object is not a DataFrame')

    # Make sure the column isn't in df already
    if name in df.columns or not isinstance(name, str):
        raise KeyError('Name is already in DataFrame or not a string')

    temp = df.copy()
    if isinstance(series, list):
        if (df.shape[0] == len(series)):
            series = pd.Series(series)
            temp[name] = series
        else:
            raise ValueError('Length of Series is not the same as DataFrame')
    else:
        raise ValueError('Series is not a list')

    return temp

if __name__ == "__main__":
    # Testing code functionality
    df = pd.DataFrame({
        'name': ['Anders','Charles','Bryce'],
        'score': [87,32,58],
        'date': ['09-03-2020','02-29-2020','01-15-2019']
    })

    df['date'] = pd.to_datetime(df['date'], infer_datetime_format=True)

    df = split_datetime(df)

    df = add_column(df, [99, 92, 93], 'score_retake')

    print(f'Resulting Dataframe:\n{df}')