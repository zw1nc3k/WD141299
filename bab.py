str = "asdfghjklzxcvbnmqwer"
x = 0
while x < len(str):
    a = x % 2
    if a == 0:
        print(str[x] + " ", x)
    x += 1
print(str[len(str)-3:])
print(str[12])
b = str + str
print(b)
c = str * 5
print(c)
d = str[5] * 3
print(d)

