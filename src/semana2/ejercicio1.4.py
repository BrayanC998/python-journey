def multiplo_cinco():
    while True:
        try:
            numero = input("Ingresa un numero: ").strip()
            a = int(numero)

            if a % 5 == 0:
                print("Es múltiplo de 5")
            else:
                print("No es múltiplo de 5")

            return a

        except ValueError:
            print("❌ Error: Debes escribir un número entero.")

x = multiplo_cinco()
print("Ingresaste:", x)
