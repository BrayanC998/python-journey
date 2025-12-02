def multiplo_3_7():
    while True:
        try:
            ingresar = input("Ingresar un numero: ").strip()
            a = int(ingresar)
            if a % 21 == 0:
                print("Es multiplo de 3 y 7")
            elif a % 3 == 0:
                print("Es multiplo de 3")
            elif a % 7 == 0:
                print("Es  multiplo de 7")
            
            else:
                print("No es multiplo de 3 ni 7")
            return a
        except ValueError:
            print("Ingresar un numero")
x= multiplo_3_7()
print("Ingresaste: ", x)