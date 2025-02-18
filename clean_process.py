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

    rest_types = df['rest_type'].value_counts(ascending=False)
    rest_types

    rest_types_lessthan1000 = rest_types[rest_types < 1000]
    rest_types_lessthan1000

    # Making Rest Types less than 1000 in frequency as others

    '''def handle_rest_type(value):
        if(value in rest_types_lessthan1000):
            return 'others'
        else:
            return value

    df['rest_type'] = df['rest_type'].apply(handle_rest_type)
    df['rest_type'].value_counts()'''

    # Cleaning location column by making location less than 300 in frequency as others

    '''location = df['location'].value_counts(ascending  = False)

    location_lessthan300 = location[location<300]



    def handle_location(value):
        if(value in location_lessthan300):
            return 'others'
        else:
            return value

    df['location'] = df['location'].apply(handle_location)
    df['location'].value_counts()'''

    # Cleaning cuisines column by making cuisines less than 100 in frequency as others

    '''cuisines = df['cuisines'].value_counts(ascending  = False)


    cuisines_lessthan100 = cuisines[cuisines<100]



    def handle_cuisines(value):
        if(value in cuisines_lessthan100):
            return 'others'
        else:
            return value

    df['cuisines'] = df['cuisines'].apply(handle_cuisines)
    df['cuisines'].value_counts()'''

    df.head()

    rest_types = df['rest_type'].value_counts(ascending=False)
    rest_types

    Type = df['Type'].value_counts(ascending=False)
    Type

    return df