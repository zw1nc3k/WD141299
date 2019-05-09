class Lucznik:
    def __init__(self, imie, hp, agi, pt):
        if hp > 1.0:
            hp = 1.0
        if hp < 0 :
            hp = 0
        self.imie = imie
        self.hp = hp
        self.agi = agi
        self.pt = pt
 
    def zmianahp(self, ile):
        if self.hp > 1.0:
            self.hp = 1.0
        print("Zabrano Ci ", ile * 100, "% życia")
        self.hp -= ile
        if self.hp < 0:
            self.hp = 0
        print("Pozostało Ci ", self.hp * 100, "% życia")
 
    def mocataku(self):
        mocataku = self.agi * self.pt *self.hp
        print("Twoja moc ataku wynosi: ", mocataku, "jakis jednostek")
 
 
class Wojownik:
    def __init__(self, imie, hp, str, pt):
        self.imie = imie
        self.hp = hp
        self.str = str
        self.pt = pt
 
    def zmianahp(self, ile):
        if self.hp > 1.0:
            self.hp = 1.0
        print("Zabrano Ci ", ile*100, "% życia")
        self.hp -= ile
        if self.hp < 0:
            self.hp = 0
        print("Pozostało Ci ", self.hp*100, "% życia")
 
    def mocataku(self):
        if self.hp > 0.2:
            mocataku = self.str * self.pt *self.hp
            print("Twoja moc ataku wynosi: ", mocataku, "jakis jednostek")
        if self.hp < 0.2:
            mocataku = self.str * self.pt * self.hp * 1.5
            print("Twoja moc ataku wynosi: ", mocataku, "jakis jednostek")
 
 
legolas = Lucznik("Legolas", float(1.0), 100, 250)
bk = Wojownik("Blade Knight", float(1.0), 250, 100)
woj = Wojownik("Wojownik", float(1.0), 250, 100)
legolas.zmianahp(0.21)
legolas.mocataku()
bk.zmianahp(0.81)
bk.mocataku()
woj.zmianahp(0.79)
woj.mocataku()
