# Zapis danych z kghm_od_2000.csv z roku 2000 do pliku o nazwie 2000.csv, a danych z 2001 do pliku 2001.csv
import pandas as pd

data = pd.read_csv('kghm_od_2000.csv')
# print(df)

DwaTysZero = data[(data['Data'] >= '2000-01-01') & (data['Data'] <= '2000-12-31')]
print(DwaTysZero)

DwaTysJeden = data[(data['Data'] >= '2001-01-01') & (data['Data'] <= '2001-12-31')]
print(DwaTysJeden)

DwaTysZero.to_csv('2000.csv')
DwaTysJeden.to_csv('2001.csv')
