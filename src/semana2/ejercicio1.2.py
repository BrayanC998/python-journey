def determinar_numero():
    while True:
        try:
            entrada = input("Pedir un número: ").strip()
            a = float(entrada)

            if a > 0:
                print("Es positivo")
            elif a < 0:
                print("Es negativo")
            else:
                print("Es cero")

            return a

        except ValueError:
            print("❌ Error: escribe un número válido.")
x = determinar_numero()
print(x)
