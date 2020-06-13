import pandas as pd

mf_DataFrame = pd.read_csv('D:\Deepak\python\Project\Practice\Sample Programs\DataAnalysis\MF.csv')
print(mf_DataFrame.index)
print(mf_DataFrame.sort_values(by='Quantity', ascending=True, inplace=True))
mf_dataFrame_sorted = mf_DataFrame.sort_values(by='Quantity', ascending=True)
print(mf_dataFrame_sorted.dtypes)
print(mf_dataFrame_sorted.tail(4))
print(type(mf_DataFrame))


