x = int(input("Podaj skok: \n"))


def ciag():
    lista = [n + 4 for n in range(78)]
    return [a for a in lista if a % x == 0 and a < 78]


print(ciag())
