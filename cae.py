lista = []
wynik = []
ciag = input("Podaj liczby: \n")
for liczba in ciag:
   lista.append(liczba)
lista2 = [item for item in lista if
          (item[0]) >= "0" and item[0] <="9"]
lista2 = [int(x) for x in lista2]
krotka = tuple(lista2)
liczbadoslowa = {0: 'zero', 4: 'cztery', 1: 'jeden', 3: 'trzy', 2: 'dwa', 5: 'piec', 6: 'szesc', 7: 'siedem', 8: 'osiem', 9: 'dziewiec',10: 'dziesiec'}
a = 0
while a < len(krotka):
   wynik.append(liczbadoslowa[krotka[a]])
   a += 1
print(*wynik)