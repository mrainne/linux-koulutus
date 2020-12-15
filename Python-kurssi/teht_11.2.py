# pyydetään käyttäjältä tiedostonimi
tiedostonimi = input("Anna tiedoston nimi: ")

# yritetään avata tiedosto ja tulostaa tiedoston sisältämän lukuarvon ja luvun
# 313 summa
try:
    tiedosto = open(tiedostonimi, "r")
    sisalto = tiedosto.read()
    tulos = int(sisalto) + 313
    print("Saatiin tulos", tulos)

    tiedosto.close()
except IOError:
    print("Virheellinen tiedostonnimi")
except ValueError:
    print("Tiedoston sisältö virheellinen!")