# Importing Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('dark_background')


def analyse_visualize_data(df):
    # Top 20 resturants in Bengaluru.

    plt.figure(figsize=(10, 7))
    chains = df['name'].value_counts()[0:20]
    sns.barplot(x=chains, y=chains.index, palette='deep')
    plt.title("Most famous restaurants chains in Bengaluru")
    plt.xlabel("Number of outlets")

![Image](https://github.com/user-attachments/assets/bef08adf-ef31-476e-9196-62ed9bb022fc)

    # Top 10 Restaurant types in Bengaluru

    plt.figure(figsize=(10, 7))
    rtype = df['rest_type'].value_counts()[0:15]
    sns.barplot(x=rtype, y=rtype.index, palette='deep')
    plt.title("Restaurant types in Bengaluru")
    plt.xlabel("Count")

    # Top 10 Cuisine types in Bengaluru

    plt.figure(figsize=(10, 7))
    cus = df['cuisines'].value_counts()[0:10]
    sns.barplot(x=cus, y=cus.index, palette='deep')
    plt.title("Cuisines types in Bengaluru")
    plt.xlabel("Count")

    # Top 10 resturant locations in Bengaluru

    plt.figure(figsize=(10, 7))
    locc = df['location'].value_counts()[0:10]
    sns.barplot(x=locc, y=locc.index, palette='deep')
    plt.title("Resturant locations in Bengaluru")
    plt.xlabel("Count")

    # To determine the order type (online/offline) and ascertain whether the restaurants offer a table booking facility.

    df_online_booking = df.groupby(["online_order", "book_table"]).size().reset_index(name="Count")
    plt.figure(figsize=(10, 7))
    sns.barplot(x="online_order", y="Count", hue="book_table", data=df_online_booking, palette='inferno')
    plt.title("Online Order - Book Table", fontsize=16, fontweight='bold')
    plt.show()

    label1 = ["Accepted", "Not Accepted"]
    label2 = ["Not Accepted", "Accepted"]

    df_online = df['online_order'].value_counts().values
    df_table = df['book_table'].value_counts().values

    plt.figure(figsize=(10, 7))
    plt.subplot(1, 2, 1)
    plt.pie(df_online, labels=label1, autopct='%1.1f%%', colors=['purple', 'orange'])
    plt.title('Online Orders')

    plt.subplot(1, 2, 2)
    plt.pie(df_table, labels=label2, autopct='%1.1f%%', colors=['purple', 'orange'])
    plt.title('Book Tables')
    plt.show()

    # Is cost affected by online order and table bookings ??

    plt.figure(figsize=(10, 8))
    sns.barplot(data=df, x='online_order', y='Cost2plates', hue='book_table', palette='rainbow')
    plt.show()

    # Visualizing Online Order vs Rate

    plt.figure(figsize=(6, 6))
    sns.boxplot(x='online_order', y='rate', data=df)

    # Visualizing Book Table vs Rate

    plt.figure(figsize=(6, 6))
    sns.boxplot(x='book_table', y='rate', data=df)

    # Visualizing Online Order Facility, Location Wise

    df1 = df.groupby(['location', 'online_order'])['name'].count()
    df1.to_csv('location_online.csv')
    df1 = pd.read_csv('location_online.csv')
    df1 = pd.pivot_table(df1, values=None, index=['location'], columns=['online_order'], fill_value=0, aggfunc=np.sum)
    df1

    df1.plot(kind='bar', figsize=(15, 8))

    # Visualizing Book Table Facility, Location Wise

    df2 = df.groupby(['location', 'book_table'])['name'].count()
    df2.to_csv('location_booktable.csv')
    df2 = pd.read_csv('location_booktable.csv')
    df2 = pd.pivot_table(df2, values=None, index=['location'], columns=['book_table'], fill_value=0, aggfunc=np.sum)
    df2

    df2.plot(kind='bar', figsize=(15, 8))

    # Average cost of restaurants at each loaction

    a = df.groupby('location').agg({'Cost2plates': 'mean'})
    plt.figure(figsize=(15, 10))
    plt.title("Distribution of mean avg cost at different location")
    sns.distplot(a["Cost2plates"]);

    # Observation: Most of the restaurants have cost between Rs. 400 and Rs. Depending on our budget one can select the location.

    plt.rcParams["figure.figsize"] = (20, 10)
    a.plot(kind='bar', color='#FF616D')
    plt.title('Average cost2plates of restaurants at each Location', fontsize=16, fontweight='bold')
    plt.xticks(rotation=90)
    plt.legend()
    plt.show()

    # Visualizing Types of Restaurents vs Rate

    plt.figure(figsize=(14, 8))
    sns.boxplot(x='Type', y='rate', data=df, palette='inferno')

    # Relation of rate and votes

    plt.figure(figsize=(15, 8))
    sns.lineplot(x='rate', y='votes', data=df)
    plt.title('Rate and Votes', fontsize=20, fontweight='bold')
    plt.show()
   
    # Grouping Types of Restaurents, location wise

    df3 = df.groupby(['location', 'Type'])['name'].count()
    df3.to_csv('location_Type.csv')
    df3 = pd.read_csv('location_Type.csv')
    df3 = pd.pivot_table(df3, values=None, index=['location'], columns=['Type'], fill_value=0, aggfunc=np.sum)
    df3

    df3.plot(kind='bar', figsize=(36, 8))

    # Top 5 locations on the basis of Votes

    df4 = df[['location', 'votes']]
    df4.drop_duplicates()
    df5 = df4.groupby(['location'])['votes'].sum()
    df5 = df5.to_frame()
    df5 = df5.sort_values('votes', ascending=False)
    df5.head()

    # Top 5 Cuisines

    df6 = df[['cuisines', 'votes']]
    df6.drop_duplicates()
    df7 = df6.groupby(['cuisines'])['votes'].sum()
    df7 = df7.to_frame()
    df7 = df7.sort_values('votes', ascending=False)
    df7.head()
