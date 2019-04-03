class Osoba:
    def __init__(self, i, n, r):
        self.imie = i
        self.nazwisko = n
        self.rokurodzenia = r

    def wyswietl(self):
        print("| ", self.imie, " | ", self.nazwisko, " | ", self.rokurodzenia, " | ", 2019-self.rokurodzenia, " |")


Janek = Osoba("Jan", "Kowalski", 1990)
Agata = Osoba("Agata", "Jakastam", 1960)
Janek.wyswietl()
Agata.wyswietl()
