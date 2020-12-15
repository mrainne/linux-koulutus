luku1 = int(input("Anna luku: "))
luku2 = int(input("Anna toinen luku: "))

if (luku1 % 2 == 0) and (luku2 % 2 == 0):
    print("Molemmat luvut ovat parillisia.")
elif (luku1 % 2 == 0) or (luku2 % 2 == 0):
    print("Toinen luku on parillinen.")
else:
    print("Molemmat luvut ovat parittomia.")