def silnia(n):
    if n > 1:
        return n*silnia(n-1)
    elif n in (0, 1):
        return 1


print(silnia(3))
