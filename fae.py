def rekurencja(n):
    if n < 0:
        return "wartosc nieprawidlowa"
    elif n <= 1:
        return 1
    else:
        return 4 * rekurencja(n - 1) + 5


print(rekurencja(2))
print(rekurencja(3))
