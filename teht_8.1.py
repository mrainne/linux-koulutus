tiedosto_nimi = input("Minkäniminen tiedosto luodaan?: ")
sisalto = input("Mitä kirjoitetaan tiedostoon?: ")

tiedosto = open(tiedosto_nimi, "w")
tiedosto.write(sisalto)

print("Luotiin tiedosto", tiedosto_nimi, "ja siihen tallennettiin teksti:", sisalto
      )
tiedosto.close()
