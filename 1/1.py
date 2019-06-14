import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("wc.csv", index_col="Name", sep=';')
data2 = data.drop(columns="Position")
data2 = data2.drop(columns="Group")
data2 = data2.drop(columns="Type")
data2 = data2.drop(columns="Team")
data2 = data2.drop(columns="Country and Club")
golegrupowe = data.groupby(['Group']).agg({'Goals' : ['sum']})
wykres = golegrupowe.plot.pie(subplots=True)
plt.show()
zawodnicy10=data2[data2["Goals"] > 10]
zawodnicy10.groupby(["Name"])
print(zawodnicy10)
