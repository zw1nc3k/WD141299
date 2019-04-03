klucz = {"a": "y", "e": "i", "i": "o", "o": "a", "y": "e"}
litery = input("Podaj slowo ktore ma zostac zaszyfrowane \n")
ciag = []
zaszyfr = []
for litera in litery:
    ciag.append(litera)
szyfr = tuple(ciag)
a = 0
while a < len(szyfr):
    try:
        zaszyfr.append(klucz[litery[a]])
        a += 1
    except Exception:
        zaszyfr.append(litery[a])
        a += 1
        continue
print(*zaszyfr, sep='')