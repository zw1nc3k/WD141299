# Średni utarg dla poszczególnych kraji na wykresie słupkowym z pliku zamowienia_50.csv
# Wykres kołowy udziału wybranych kraji w sprzedaży z pliku zamowienia_50.csv
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('zamowienia_50.csv', delimiter=';')


sredni = data.groupby(['Kraj']).agg({'Utarg': 'mean'})
print(sredni)
sredni.plot.bar()
plt.title('Średni utarg dla poszczególnych kraji')
plt.ylabel('Średni utarg')
plt.legend()
plt.show()

kraje = data.groupby(['Kraj']).agg({'Utarg': 'sum'})
print(kraje)
kraje.plot.pie(subplots=True, autopct='%.2f%%')
plt.title('Udział wybranych kraji w sprzedaży')
plt.legend()
plt.show()
