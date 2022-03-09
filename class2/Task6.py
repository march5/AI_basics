from pandas import Series, DataFrame
import pandas as pd

df = pd.read_csv('Data/titanic.csv')
print(df.shape)
print(df.head())

print(df.columns)

df.drop(['PassengerId', 'Name', 'Ticket'], axis=1, inplace=True)

print("\nPo usunięciu kolumn: \n")
print(df.head())

df = df.loc[df.Cabin.isnull()]

df['HasCabin'] = 1
df.loc[df.Cabin.isnull(), 'HasCabin'] = 0
df.drop('Cabin', axis=1, inplace=True)

print("\nDodanie HasCabin i usuniecie Cabin: \n")
print(df)
