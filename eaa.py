class Car:
    def __init__(self, m, r):
        self.marka = m
        self.rocznik = r
 
    def wyswietl(self):
        print("Marka: ", self.marka, " Rocznik: ", self.rocznik)
 
 
car1 = Car("Mazda", 1990)
car2 = Car("Opel", 2018)
car1.wyswietl()
car2.wyswietl()
car1 = car2
car1.wyswietl()
