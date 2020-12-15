luku1 = int(input("Anna ensimmäinen luku: "))
luku2 = int(input("Anna toinen luku: "))

while True:
    print("(1) +")
    print("(2) -")
    print("(3) *")
    print("(4) /")
    print("(5) Vaihda Luvut ")
    print("(6) Lopeta")
    print("Valitut luvut:" , luku1, luku2)
    valinta = input("Tee valinta (1-6): ")

    if (valinta == "1"):
        print("Tulos on:", luku1 + luku2)
    elif (valinta == "2"):
        print("Tulos on:", luku1 -luku2)
    elif (valinta == "3"):
        print("Tulos on:", luku1 * luku2)
    elif (valinta == "4"):
        print("Tulos on:", luku1 / luku2)
    elif (valinta == "5"):
        luku1 = int(input("Anna uusi ensimmäinen luku: "))
        luku2 = int(input("Anna uusi toinen luku: "))
    elif (valinta == "6"):
        break
    else:
        print("Valintaa ei tunnistettu.")
