import random

print("Heitetään kolikkoa viidesti:")

for i in range(5):
    luku = random.randint(0, 1) # arpoo luvun 0 tai 1
    if luku == 0:
        print("Klaava!")
    else:
        print("Kruuna!")

