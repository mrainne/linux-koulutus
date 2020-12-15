import time
import pickle

def tulosta_merkintojen_lkm():
    """Tulostaa muistikirjan merkintöjen lukuäärän."""
    print("Listalla on {} merkintää.".format(len(muistilista)))

tiedostonimi = "muistio.dat"

# muistikirjan toiminnot tallennetaan sanakirjaan, jotta tulostus saadaan
# toistorakenteeseen
vaihtoehdot = {"1" : "Lue muistikirjaa", "2" : "Lisää merkintä",
               "3" : "Muokkaa merkintää", "4" : "Poista merkintä",
               "5" : "Tallenna ja lopeta"}

muistilista = []
aikaleima = time.strftime("%X %x")

# yritetään avata tiedosto ja ladata sisältö muuttujaan muistilista
# tulostetaan virheilmoitus ellei tiedostoa ole (tiedosto luodaan vasta
# ohjelman suoritusta lopettaessa.
try:
    with open(tiedostonimi, "br") as tiedosto:
        muistilista = pickle.load(tiedosto)
except FileNotFoundError:
    print("Virhe tiedostossa, luodaan uusi", tiedostonimi + ".")

while True:
    # tulostetaan valikko
    for numero, toiminto in vaihtoehdot.items():
        print("({}) {}".format(numero, toiminto))

    valinta = input("\nMitä haluat tehdä?:")

    if valinta == "1": # tulostetaan muistikirjan sisältö
        for alkio in muistilista:
            print(alkio)
    elif valinta == "2": # lisätään merkintä
        merkinta = input("Kirjoita uusi merkintä: ")
        muistilista.append("{}:::{}".format(merkinta, aikaleima))
    elif valinta == "3": # muokataan olemassaolevaa merkintää
        tulosta_merkintojen_lkm()
        muutettava_merkinta = int(input("Mitä niistä muutetaan?: "))
        print(muistilista[muutettava_merkinta-1])
        uusi_merkinta = input("Anna uusi teksti: ")
        muistilista[muutettava_merkinta-1] = "{}:::{}".format(uusi_merkinta, aikaleima)
    elif valinta == "4": # merkinnän poistaminen
        tulosta_merkintojen_lkm()
        poistettava_merkinta = int(input("Mitä niistä poistetaan?: "))
        print("Poistettiin merkintä", muistilista.pop(poistettava_merkinta-1))
    elif valinta == "5":
        print("Lopetetaan.")
        # tallennetaan muistilista tiedostoon
        with open(tiedostonimi, "wb") as tiedosto:
            pickle.dump(muistilista, tiedosto)
        break
    else: # jatketaan kunnes käyttäjä valitsee sallitun arvon
        continue
