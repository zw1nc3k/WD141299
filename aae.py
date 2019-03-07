import math
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

delta = pow(b, 2)-4*a*c
print(delta)
if delta < 0:
    print("Rownanie nie ma rozwiazan w zbiorze liczb rzeczywistych")
elif delta > 0:
    print(math.sqrt(delta))
    xb = (-b-math.sqrt(delta))/(2*a)
    xa = (-b+math.sqrt(delta))/(2*a)
    print(xb)
    print(xa)
else:
    xa = (-b)/(2*a)
    print(xa)
