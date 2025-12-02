def par_impar():
    while True:
        try:
            entrada = input("Ingresar un número: ").strip()
            a = int(entrada)  # Convertir a entero
            
            if a % 2 == 0:
                print("Es par")
            else:
                print("Es impar")
            return a
        except ValueError:
            print("❌ Error: escribe un número entero válido.")

x = par_impar()
print("Ingresaste", x)
