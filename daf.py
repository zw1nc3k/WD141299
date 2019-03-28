lista1 = [1, 2, 3, 4, 5, 6, 7]
lista2 = [7, 6, 5, 4, 3, 2, 1]

def czymalejaco(n):
    a=0
    x=0
    while a < len[n]:
        if n[a] > n[a+1]:
            x += 0
        elif n[a] < n[a+1]:
            x += 1
        a = a + 1
    if x > 0:
        return False
    elif x == 0:
         return True



print(czymalejaco(lista2))
