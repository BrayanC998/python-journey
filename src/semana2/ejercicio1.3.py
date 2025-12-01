def par_impar():
    while True:
        try:
            entrada = input("Ingresar un numero: ").strip()
            a= float(entrada)
            
            if a % 2 == 0:
                print("ES par")
            else:
                print("Es impar")
            return a
        except ValueError:
            print("❌")
x = par_impar()
print("Ingresaste", x)