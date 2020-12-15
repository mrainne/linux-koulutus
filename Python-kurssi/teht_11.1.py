# pyydetään käyttäjää syöttämään luku
luku = input("Anna luku: ")

# yritetään muuttaa käyttäjän antama syöte kokonaisluvuksi
try:
    luku = int(luku)
    print("Syöte oli kelvollinen.")
except Exception:
    print("Virheellinen syöte!")