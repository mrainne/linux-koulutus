class Kilpailija:
    """Kilpailija: sisältää pisteet ja värin"""
    pisteet = 0
    vari = ""

    def __init__(self):
        self.vari = input("Anna minulle väri: ")

    def tilanne(self):
        print("Olen", self.vari, "ja minulla on", self.pisteet, "pistettä!")

    def maali(self):
        self.pisteet += 1

eka = Kilpailija()
toka = Kilpailija()
eka.tilanne()
toka.tilanne()
print(Kilpailija.__doc__)
