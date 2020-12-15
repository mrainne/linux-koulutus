import time

def avaa_muistio(tiedostonimi):
    """Avaa tiedoston, jonka nimi on parametrina annettu tiedostonnimi. Ellei
    tiedostoa ole olemassa, luodaan tiedosto."""
    try:
        muistio = open(tiedostonimi, "r")
        muistio.close()
    except FileNotFoundError:
        print("Tiedostoa ei löydy, luodaan tiedosto.")
        muistio = open(tiedostonimi, "w")
        muistio.close()

def main():
    # oletuksena käytetään tiedostoa muistio.txt
    muistionnimi = "muistio.txt"

    # luodaan oletustiedosto ellei sitä ole
    # avaa_tiedosto -funktio ei käy, koska poikkeustapauksessa tulostetaan
    # eri teksti
    try:
        muistio = open(muistionnimi, "r")
        muistio.close()
    except FileNotFoundError:
        print("Oletusmuistioa ei löydy, luodaan tiedosto.")
        muistio = open(muistionnimi, "w")
        muistio.close()

    while True:
        #tulostetaan käytettävän muistion nimi
        print("Käytetään muistiota:", muistionnimi)
        # tulostetaan käytettävissä olevat valinnat
        print("(1)", "Lue muistikirjaa")
        print("(2)", "Lisää merkintä")
        print("(3)", "Tyhjennä muistikirja")
        print("(4)", "Vaihda muistiota")
        print("(5)", "Lopeta\n")

        # pyydetään käyttäjää valitsemaan jokin ylläolevista vaihtoehdoista
        valinta = input("Mitä haluat tehdä?: ")

        if (valinta == "1"): # tulostetaan muistikirjan sisältö
            muistikirja = open(muistionnimi, "r")
            sisalto = muistikirja.read()
            print(sisalto)
            muistikirja.close()
        elif valinta == "2": # lisätään muisikirjaan merkintä
            merkinta = input("Kirjoita uusi merkintä: ")
            muistikirja = open(muistionnimi, "a")
            muistikirja.write(merkinta + ":::" + time.strftime("%X %x"))
            muistikirja.close()
        elif valinta == "3": # tyhjennetään muistio
            muistikirja = open(muistionnimi, "w")
            muistikirja.close()
            print("Muistio tyhjennetty.")
        elif valinta == "4": # vaihdetaan muistikirjaa
            muistionnimi = input("Anna tiedostonnimi: ")
            avaa_muistio(muistionnimi)
        else: # lopetetaan
            print("Lopetetaan.")
            break

if __name__ == "__main__":
    main()