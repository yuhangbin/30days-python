import pandas as pd
import numpy as np

nums = [1, 2, 3, 4,5]
s = pd.Series(nums)
print(s)

nums = [1, 2, 3, 4, 5]
s = pd.Series(nums, index=[0, 2, 3, 4, 5])
print(s)


s = pd.Series(np.linspace(5, 20, 10)) # linspace(starting, end, items)
print(s)

data = [
    ['Asabeneh', 'Finland', 'Helsink'], 
    ['David', 'UK', 'London'],
    ['John', 'Sweden', 'Stockholm']
]
df = pd.DataFrame(data, columns=['Names','Country','City'])
print(df)

data = {'Name': ['Asabeneh', 'David', 'John'], 'Country':[
    'Finland', 'UK', 'Sweden'], 'City': ['Helsiki', 'London', 'Stockholm']}
df = pd.DataFrame(data)
print(df)

data = [
    {'Name': 'Asabeneh', 'Country': 'Finland', 'City': 'Helsinki'},
    {'Name': 'David', 'Country': 'UK', 'City': 'London'},
    {'Name': 'John', 'Country': 'Sweden', 'City': 'Stockholm'}]
df = pd.DataFrame(data)
print(df)

df = pd.read_csv('../data/hacker_news.csv')