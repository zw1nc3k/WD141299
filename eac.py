class Konto:
    def __init__(self, saldo, wlasciciel, nrkonta):
        self.saldo = saldo
        self.wlasciciel = wlasciciel
        self.nrkonta = nrkonta
 
    def przelewmiedzykontami(self, kwota, nakonto):
        if self.saldo < 0:
            print("Brak srodkow na koncie")
        if self.saldo - kwota > 0:
            print("Saldo konta przed przelewem: ", self.nrkonta, "Ktorego wlascicielem jest: "
                  , self.wlasciciel, " Wynosi: ", self.saldo)
            self.saldo -= kwota
            print("Saldo konta przed przelewem: ", nakonto.nrkonta, "Ktorego wlascicielem jest: "
                  , nakonto.wlasciciel, " Wynosi: ", nakonto.saldo)
            nakonto.saldo += kwota
            print("Saldo konta przed przelewem: ", self.nrkonta, "Ktorego wlascicielem jest: "
                  , self.wlasciciel, " Wynosi: ", self.saldo)
            print("Saldo konta przed przelewem: ", nakonto.nrkonta, "Ktorego wlascicielem jest: "
                  , nakonto.wlasciciel, " Wynosi: ", nakonto.saldo)
        if self.saldo-kwota < 0:
            print("Nie wystarczajaca liczba srodkow na koncie, saldo wynosi: ", self.saldo)
 
    def przelewzewnetrzny(self, kwota):
        if self.saldo < 0:
            print("Brak srodkow na koncie")
        if self.saldo-kwota > 0:
            print("Saldo konta przed przelewem wynosi: ", self.saldo)
            self.saldo -= kwota
            print("Saldo konta po przelewie wynosi: ", self.saldo)
        if self.saldo-kwota < 0:
            print("Nie wystarczajaca liczba srodkow na koncie, saldo wynosi: ", self.saldo)
 
    def wplata(self, kwota):
        self.saldo += kwota
        print("Saldo po wpłacie wynosi: ", self.saldo)
 
    def wyplata(self, kwota):
        if self.saldo-kwota < 0:
            print("Nie wystarczajaca liczba srodkow na koncie, saldo wynosi: ", self.saldo)
        if self.saldo-kwota > 0:
            self.saldo -= kwota
            print("Saldo po wypłacie wynosi: ", self.saldo)
 
konto1 = Konto(2500, "Kowalski", 1111)
konto2 = Konto(1500, "Dyro", 1112)
konto3 = Konto(3250, "Wieckowski", 1113)
konto1.przelewmiedzykontami(2000, konto2)
konto1.przelewzewnetrzny(2000)
konto3.wplata(10000)
konto3.wyplata(5123)
konto2.wyplata(4000)
 