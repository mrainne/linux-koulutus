tiedosto_nimi = "merkkijonoja.txt"

tiedosto = open(tiedosto_nimi, "r")

for merkkijono in tiedosto:
    if merkkijono[:-1].isalnum():
        print(merkkijono[:-1], "kelpaa salasanaksi.")
    else:
        print(merkkijono[:-1], "sisältää virheellisiä merkkejä.")

tiedosto.close()
