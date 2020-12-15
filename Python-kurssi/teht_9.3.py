def tulosta(syote = "Oletustulostus"):
    """Tulostaa ruudulle parametrinä saatavan tekstin tai oletusparametrin
    mukaisen tekstin."""
    print(syote)

def main():
    while True:
        syote = input("Anna syöte (Lopeta lopettaa): ")
        if syote == "Lopeta":
            break
        else:
            # mikäli syötteessä on 5 tai useampia merkkejä funktiota tulosta()
            # kutsutaan parametrilla syote, muuten funktiota kutsutaan ilman
            # parametrejä.
            if len(syote) >= 5:
                tulosta(syote)
            else:
                tulosta()

if __name__ == "__main__":
    main()
