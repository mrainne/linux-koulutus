luku1 = int(input("Anna ensimmäinen luku: "))
luku2 = int(input("Anna toinen luku: "))
print("(1) +")
print("(2) -")
print("(3) *")
print("(4) /")
valinta = input("Tee valinta (1-4): ")

if (valinta == "1"):
    print("Tulos on:", luku1 + luku2)
elif (valinta == "2"):
    print("Tulos on:", luku1 -luku2)
elif (valinta == "3"):
    print("Tulos on:", luku1 * luku2)
elif (valinta == "4"):
    print("Tulos on:", luku1 / luku2)
else:
    print("Valintaa ei tunnistettu.")
