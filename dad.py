import math


def cg(a1, q, n):
    n -= 1
    return a1 * math.pow(q, n)


print(cg(1, 2, 5))
print(cg(4, 2, 12))
