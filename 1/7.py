# Wykres słupkowy ilości poszczególnych departamentów w pliku username-password-recovery-code.csv
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('username-password-recovery-code.csv', delimiter=';')
print(data)

department = data.groupby(['Department']).agg({'Department': 'count'})
print(department)

department.plot.bar()
plt.title('Ilość poszczególnych departamentów')
plt.ylabel('Ilość departamentów')
plt.legend()
plt.show()
