# Zaimportuj dane z pliku ,,airports.csv'' i wykonaj na nich poniższe polecenia:
#
# wybierz nazwy państw ostatnich 12 lotnisk w tabeli,
# wybierz wiersz o indeksie 1 korzystając z indeksera .loc oraz .iloc (porównaj otrzymane wyniki),
# wybierz wszystkie lotniska w Polsce,
# wybierz wszystkie lotniska, których nazwa różni się od nazwy miasta, w którym się znajdują.
# przelicz wartości wysokości na metry i zapisz zmodyfikowaną kolumnę w miejsce starej
# (w naszej tabeli wysokość jest podana w * stopach nad poziomem morza; jedna stopa angielska równa się 30,48 cm),
# znajdź wszystkie państwa, w których znajduje się wyłącznie 1 lotnisko (zobacz procedurę .unique()).

from pandas import Series, DataFrame
import pandas as pd

df = pd.read_csv('Data/airports.csv', names=['col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7', 'col8', 'col9', 'col10', 'col11', 'col12'])

print(df)

# panstwa ostatnich 12 lotnisk
# print(df['col4'].tail(12).unique())

# print(df.loc[1])
# print()
# print(df.iloc[1])

# lotniska w polsce
# print(df[df.col4 == 'Poland'])

# lotniska o nazwie innej niz miasto
# print(df[df.col2 != df.col3])

# stopy na metry
# df['col9'] = (df['col9'] * 30.48) / 100
# print(df['col9'])

# Państwa z 1 lotniskiem
print(pd.unique(df['col4']))
