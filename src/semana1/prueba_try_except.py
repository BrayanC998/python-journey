while True:
    try:
        numero = int(input("Escrbie un numero: "))
        print("el doble de numero es :", numero * 2)
        break
    except:
        print("Ese no es un numero, porfavor escribe un numero: ")
