import math

# pyydetään käyttäjältä kaksi lukua
luku1 = int(input("Anna ensimmäinen luku: "))
luku2 = int(input("Anna toinen luku: "))

while True:
    # tulostetaan laskimen eri vaihtoehdot käyttäjälle
    print("(1) +")
    print("(2) -")
    print("(3) *")
    print("(4) /")
    print("(5) sin(luku1/luku2)")
    print("(6) cos(luku1/luku2)")
    print("(7) Vaihda luvut")
    print("(8) Lopeta")
    print("Valitut luvut:", luku1, luku2)
    # pyydetään käyttäjää valitsemaan joku arvoista
    valinta = input("Tee valinta (1-8): ")

    # käydään läpi eri valinnat ja tulostetaan valinnan mukainan tulos
    if valinta == "1":  # yhteenlasku
        print("Tulos on:", luku1 + luku2)
    elif valinta == "2":  # vähennyslasku
        print("Tulos on:", luku1 - luku2)
    elif valinta == "3":  # kertolasku
        print("Tulos on:", luku1 * luku2)
    elif valinta == "4":  # jakolasku
        print("Tulos on:", luku1 / luku2)
    elif valinta == "5":  # sin(luku1/luku2)
        print("Tulos on:", math.sin(luku1 / luku2))
    elif valinta == "6":  # cos(luku1/luku2)
        print("Tulos on:", math.cos(luku1 / luku2))
    elif valinta == "7":  # vaihdetaan luvut
        luku1 = int(input("Anna uusi ensimmäinen luku: "))
        luku2 = int(input("Anna uusi toinen luku: "))
        continue
    elif valinta == "8":  # lopetetaan suoritus
        break