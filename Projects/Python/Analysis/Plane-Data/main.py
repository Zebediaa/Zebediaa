import pandas as pd
import datetime as dt
import seaborn
import matplotlib.pyplot as plt
from seaborn import barplot

number_of_travelers_df = pd.read_csv('data')
number_of_travelers_df['month'] = pd.to_datetime(number_of_travelers_df['month'], format='%Y-%m-%d')
number_of_travelers_df['trimester'] = number_of_travelers_df['month'].dt.quarter
number_of_travelers_df['year'] = number_of_travelers_df['month'].dt.year
travelers = number_of_travelers_df[['passengers','year','trimester']].groupby(by=['year','trimester']).sum().values
travelers_by_trimester = pd.DataFrame(travelers.reshape(20, 4), index = list(range(2000, 2020)), columns=['Q1', 'Q2', 'Q3', 'Q4'])

# print(number_of_travelers_df['trimester'])

fig, ax = plt.subplots(figsize=(15, 6))
travelers_by_trimester.plot()
plt.show()
