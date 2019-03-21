lista= []
lista.append(input("Podaj Nazwisko 1: "))
lista.append(input("Podaj Nazwisko 2: "))
lista.append(input("Podaj Nazwisko 3: "))
lista.append(input("Podaj Nazwisko 4: "))
lista.append(input("Podaj Nazwisko 5: "))
lista2 = [item for item in lista if
          (item[0] == "Q") or (item[0] == "R") or (item[0] == "R") or (item[0] == "R") or (item[0] == "S") or (
                  item[0] == "T") or (item[0] == "U") or (item[0] == "V") or (item[0] == "W") or (
                  item[0] == "X") or (item[0] == "Y") or (item[0] == "Z")]
print(lista2)
for item in lista2[:]:
    if len(item) > 5:
        print(item)
