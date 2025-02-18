import pandas as pd
import numpy as np


def clean_and_proccess_data(df):
    df.head(10)

    df.shape

    df.dtypes

    df.columns

    df = df.drop(['url', 'address', 'phone', 'menu_item', 'dish_liked', 'reviews_list'], axis=1)
    df.head()

    df.info()

    df.isnull().sum()

    # % of missing values
    df.isnull().sum() / len(df) * 100

    unique_rate = df['rate'].unique()
    print(unique_rate)

    # Removing "NEW" , "-" and "/5" from Rate Column

    def handlerate(value):
        if (value == 'NEW' or value == '-'):
            return np.nan
        else:
            value = str(value).split('/')
            value = value[0]
            return float(value)

    df['rate'] = df['rate'].apply(handlerate)
    df['rate'].head()

    # Filling Null Values in Rate Column with Mean

    df['rate'].fillna(df['rate'].mean(), inplace=True)
    df['rate'].isnull().sum()

    df.info()

    # Dropping Null Values
    df.dropna(inplace=True)
    df.head()

    df.rename(
        columns={'approx_cost(for two people)': 'Cost2plates', 'listed_in(type)': 'Type', 'listed_in(city)': 'city'},
        inplace=True)
    df.head()

    df['location'].unique()

    df['city'].unique()

    # City and location, both are there, lets keep only one.
    df = df.drop(['city'], axis=1)
    df.head()

    df['Cost2plates'].unique()

    # Removing "," from Cost2Plates Column

    def handlecomma(value):
        value = str(value)
        if ',' in value:
            value = value.replace(',', '')
            return float(value)
        else:
            return float(value)

    df['Cost2plates'] = df['Cost2plates'].apply(handlecomma)
    df['Cost2plates'].unique()
    df.head()

    return df
