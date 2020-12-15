# tiedostonimi voitaisiin kysyä käyttäjältä
tiedostonimi = "sanoja.txt"

# luodaan tyhjä lista
sanalista = []

# avataan tiedosto with lauseessa
# tiedosto suljetaan automaattisesti, kun lause on suoritettu
with open(tiedostonimi, "r") as tiedosto:
    # lisätään sanat sanalistaan
    for line in tiedosto:
        sanalista.append(line.strip())  # leikataan rivinvaihto sanan lopusta

# tulostus
print("Sanat laitettuna aakkosjärjestykseen:")
# tulostetaan sanat sorted -funktiolla järjestetystä listasta
for sana in sorted(sanalista):
    print(sana)



