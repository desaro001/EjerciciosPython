dolorDeCabeza = int(input("Te duele la cabeza? [0-No, 1-Si]:"))
fiebre = int(input("Tienes fiebre? [0-No, 1-Si]:"))
origen = int(input("Vienes de China? [0-No, 1-Si]:"))
if dolorDeCabeza==1:
    if fiebre==1:
        if origen==1:
            print("Coronavirus")
        else:
            print("Gripe")
    else:
        print("No tienes nada")
else:
    print("Estas a tope")

