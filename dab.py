def silnia(n):
    a = 1
    for i in range(2, n+1):
        a = a * i
    return a


print(silnia(10))
