import time

muistio = open("muistio.txt", "w")
muistio.close()

while True:
    print("(1)", "Lue muistikirjaa")
    print("(2)", "Lisää merkintä")
    print("(3)", "Tyhjennä muistikirja")
    print("(4)", "Lopeta\n")


    valinta = input("Mitä haluat tehdä?: ")

    if (valinta == "1"):
        muistikirja = open("muistio.txt", "r")
        sisalto = muistikirja.read()
        print(sisalto)
        muistikirja.close()
    elif valinta == "2":
        merkinta = input("Kirjoita uusi merkintä: ")
        muistikirja = open("muistio.txt", "a")
        muistikirja.write(merkinta + ":::" + time.strftime("%X %x"))
        muistikirja.close()
    elif valinta == "3":
        muistikirja = open("muistio.txt", "w")
        muistikirja.close()
        print("Muistio tyhjennetty.")
    else:
        print("Lopetetaan.")
        break