import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("wc.csv", index_col="Team", sep=';')
golegrupowe = data.groupby(['Group']).agg({'Goals' : ['sum']})
wykres = golegrupowe.plot.pie(subplots=True)
plt.show()