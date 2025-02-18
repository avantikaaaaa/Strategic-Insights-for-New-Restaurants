import pandas as pd

from Visualize import analyse_visualize_data
from clean_process import clean_and_proccess_data

df = pd.read_csv('zomato.csv')
cleaned_df = clean_and_proccess_data(df)
analyse_visualize_data(cleaned_df)

