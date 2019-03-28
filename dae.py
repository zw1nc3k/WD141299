def palindrom(n):
    n = n.lower()
    return str(n) == str(n)[::-1]


print(palindrom("AsdDsa"))
