import sys
import pandas as pd
import numpy as np

print(sys.version)
first_series = pd.Series()
second_series = pd.Series(np.arange(3, 13, 2))
print(second_series)

third_series = pd.Series(['orange', 'apple', 'mango', 'grapes'])
print(third_series)
third_series.index = ['A', 'B', 'C', 'D']
print(third_series)
print(third_series.index)
first_series = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [11, 12, 13, 14], 'C': [21, 22, 23, 24]})
print(first_series)

csv_series = pd.read_csv('D:\Deepak\python\Project\Practice\Sample Programs\DataAnalysis\Data.csv')
print(csv_series)
print(csv_series.head())
print(csv_series.tail(2))
print(csv_series.describe())
print(csv_series.columns)
print(csv_series.iloc[2:4, 0:5])
print(csv_series.loc[2:4, 'A': 'Salary'])
print(csv_series[['A', 'Salary']].tail(3))
csv_series_1 = csv_series.loc[2:6, 'A': 'Salary']
csv_series.sort_values(by='Salary', ascending=False, inplace=True)
print(csv_series.head(4))
print(csv_series.sort_values(by='Salary', ascending=True, inplace=True))
print(csv_series.head(4))
#print(csv_series_sub.describe())