import pandas as pd
import glob

def initialize1():
    df = pd.read_csv('Pandas_100_knocks-master/input/titanic3.csv')
    return df

def initialize2():
    df = pd.read_csv('Pandas_100_knocks-master/input/data1.csv')
    return df

df = initialize1()
df2 = initialize2()
df3 = pd.read_csv('Pandas_100_knocks-master/input/data1_2.csv')
df4 = pd.read_csv('Pandas_100_knocks-master/input/data1_3.csv')
df5 = pd.read_csv('Pandas_100_knocks-master/input/data2.csv', encoding='cp932')

#1
print(df.head(5))

#2
print(df.tail(5))

#3
print(df.shape)

#4
print(df2.head(5))

#5
print(df.sort_values('fare'))

#6
df_copy = df.copy()
print(df_copy.head(5))