def toinenpotenssi(lukuarvo):
    """Lasketaan parametrin lukuarvo toinen potenssi ja tulostetaan se ruudulle."""
    print("Toinen potenssi on", lukuarvo**2)

def main():
    luku = int(input("Anna lukuarvo: "))
    toinenpotenssi(luku)

if __name__ == "__main__":
    main()