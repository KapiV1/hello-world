class Przeciwnik:
    def __init__(self, nazwa, życie, atak):
            self.nazwa = nazwa
            self.życie = życie
            self.atak = atak

zombi = Przeciwnik('Zombie', 20, 5)
szkielet = Przeciwnik('szkielet', 15, 12)

moby = [zombi, szkielet]

class Kłoda:
    def __init__ (self,nazwa, odporność):
        self.nazwa = nazwa
        self.odporność = odporność

sosna = Kłoda('sosna', 20)
dąb = Kłoda('dąb', 100)

kłody = [sosna, dąb]