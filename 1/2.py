# 5 najwyższych wartości zamówień z pliku zamowienia.csv
# usunięcie kolumny idZamowienia z pliku zamowienia.csv
import pandas as pd

data = pd.read_csv('zamowienia.csv', delimiter=';')
# print(data)
# print(data.dtypes)

NajwyzszeZamowienia = data.sort_values(by='Utarg', ascending=False)[0:5]

del NajwyzszeZamowienia['idZamowienia']
print(NajwyzszeZamowienia)
