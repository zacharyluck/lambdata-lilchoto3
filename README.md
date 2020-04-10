# lambdata-lilchoto3 - Automated data science tools for use on pandas DataFrames

## What is it?

lambdata-lilchoto3 adds a variety of data science tools to easily clean and manage data, make new features, and find new information about the data you're working with. It does this via it's own custom pipeline which uses pandas' powerful DataFrames and functions to easily and quickly perform any number of commonplace transformations that any data scientist would find useful.

## Main Features

### What's implemented so far:

- One-step datetime column splitting into month/day/year columns, with option to remove the original column
- One-step addition of a new column onto a DataFrames

## Installation from sources:

To install lambdata-lilchoto3, you can do so from test.pypi:
`pip install -i https://test.pypi.org/simple/ lambdata-zacharyluck`

## How to use it:

First, start by importing `DataFrameTransmogrifier`.

After that, instantiate a variable using the constructor with the DataFrame as the only parameter:

`df_t = DataFrameTransmogrifier(df)`

From there, use any of `DataFrameTransmogrifier`'s many functions to modify your DataFrame; `DataFrameTransmogrifier` creates a copy of your original DataFrame, so don't worry about accidental modification.

### Examples:

`df_t.split_datetime()` will find any `datetime` type columns in the DataFrame and create three new columns containing the month, day, and year.