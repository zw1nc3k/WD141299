a = (input("C-Celcjusz,K-Kelwin,F-Fahrenheit: "))
b = int(input("Podaj temperature: "))
if a == "C" and a != -273.15:
    print("Podales ", b, " stopni Celcjusza")
    print("Kelwin: ", b+273.15)
    print("Fahrenheit: ", 32+((9/5)*b))
elif a == "F" and a != -459.67:
    print("Podales", b, " stopni Fahrenheita")
    print("Celcjusza: ", (5/9)*(b-32))
    print("Kelwina: ", ((b-32)/(1.8))+273.15)
elif a == "K" and a != 0:
    print("Podales", b, " stopni Kelwina")
    print("Celcjusza: ", b-273.15)
    print("Fahrenheita: ", (b+459.67)*(5/9))
else:
    print("Podales zla wartosc")
