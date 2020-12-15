class Kilpailija:
    pisteet = 0
    vari = ""

    def tilanne(self):
        print("Olen", self.vari, "ja minulla on", self.pisteet, "pistettä!")

    def maali(self):
        self.pisteet += 1

eka = Kilpailija()
eka.vari = "sininen"
eka.maali()
eka.tilanne()
