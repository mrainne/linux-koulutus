def pituusmitta(syote):
    """Palauttaa syötteenä saadun merkkijonon pituuden"""
    pituus = len(syote)
    return pituus

def main():
    while True:
        sana = input("Anna syöte (Lopeta lopettaa): ")

        if sana == "Lopeta": #lopetetaan ohjelma suoritus
            break
        elif sana == "": #tyhjä merkkijono
            print("Et antanut syötettä")
            continue
        else:
            print("Antamasi syöte oli", pituusmitta(sana), "merkkiä pitkä.")

if __name__ == "__main__":
    main()