# Ostoslistaohjelma
# luodaan tyhjä ostoslista
ostoslista = []

while True:
    # kysytään käyttäjältä mitä halutaan tehdä
    print("Haluatko")
    print("(1)Lisätä listaan")
    print("(2)Poistaa listalta vai")
    valinta = input("(3)Lopettaa?:")

    try:
        if valinta == "1": # lisätään ostoslistaan tavaroita
            tavara = input("Mitä lisätään?:")
            ostoslista.append(tavara)
        elif valinta == "2": # poistetaan ostoslistalta haluttu alkio
            print("Listalla on", len(ostoslista), "alkiota.")
            poistettava = int(input("Monesko niistä poistetaan?:"))
            ostoslista.pop(poistettava)
        elif valinta == "3": # tulostetaan lista ja päätetään ohjelma
            print("Listalla oli tuotteet:")
            for alkio in ostoslista:
                print(alkio)
            break
        else:
            # käyttäjän antama valinta ei täsmää, nostetaan poikkeus
            raise Exception
    except Exception:
        # käsitellään käyttäjän antamat virheelliset syötteet
        print("Virheellinen valinta.")

