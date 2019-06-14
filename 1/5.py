# 5 najmniejszych otwarć w trzecim kwartale roku 2016 w pliku wig_od_2015.csv
import pandas as pd

data = pd.read_csv('wig_od_2015.csv')

otwarcie = data[(data['Data'] >= '2016-07-01') & (data['Data'] <= '2016-09-30')].sort_values(by='Otwarcie')[0:5]
print(otwarcie)
