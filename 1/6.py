# Udział największych typów płatności w pliku SalesJan2009.csv
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('SalesJan2009.csv')
print(data)

platnosci = data.groupby('Payment_Type').agg({'Payment_Type': 'count'})
print(platnosci)

platnosci.plot.pie(subplots=True, autopct='%.2f%%')
plt.title('Udział największych typów płatności')
plt.legend()
plt.show()
