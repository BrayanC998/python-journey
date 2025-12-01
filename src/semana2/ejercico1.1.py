def comparar_tres_numeros():
    while True:
        try:
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))
            c = float(input("Tercer número: "))
            
            # 1. Identificar el mayor
            mayor = max(a, b, c)

            if a == b == c:
                print("Los tres números son iguales.")
            else:
                if a == mayor:
                    print("El primer número es el mayor.")
                if b == mayor:
                    print("El segundo número es el mayor.")
                if c == mayor:
                    print("El tercer número es el mayor.")
            
            # 2. Comprobar empates
            if a == b and a != c:
                print("El primero y el segundo son iguales.")
            if a == c and a != b:
                print("El primero y el tercero son iguales.")
            if b == c and b != a:
                print("El segundo y el tercero son iguales.")
            
            return a, b, c
        
        except ValueError:
            print("❌ Error: escribe un número válido.")
        

x, y, z = comparar_tres_numeros()
print("Ingresaste:", x, y, z)
