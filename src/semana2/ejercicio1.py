def pedir_numero():
    while True:
        try:
            a = float(input("Escribe el primer numero: "))
            b = float(input("Escribe el segundo numero: "))
            if a > b :
                print("El primer numero es mayor")
            else:
                print("El segundo numero es mayor")
            if a ==b :
                print("Son iguales")
            return a, b
        except ValueError:
            print("Error escribe un numero: ")
            
x,y =pedir_numero()
print(f"Ingresaste {x} y {y}")