def summ(x):
    if x == 0:
        return 0
    elif x > 0:
        return x % 10 + summ(x/10)
    else:
        x *= -1
        return x % 10 + summ(x / 10)


x = int(input("Podaj liczby"))
print(int(summ(x)))
