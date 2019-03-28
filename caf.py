A = set(["Warszawa", "Ciechanow", "Gdansk", "Olsztyn", "Lodz"])
B = set(["Lodz", "Rzeszow", "Krakow"])
C = set(["Szczecin", "Poznan", "Plonsk", "Lodz", "Ciechanow"])
#miasta, które są w przynajmniej jednym ze zbiorów (odpowiednik sumy zbiorów)
print(A.union(B, C))
#miasta, które są jednoczeście we wszystkich zbiorach (odpowidnik części wspólnej zbiorów)
print(A.intersection(B, C))
#miasta, które są w pierwszym zbiorze, ale nie ma ich w drugim zbiorze (odpowiednik różnicy zbiorów).
print(A.difference(B))
