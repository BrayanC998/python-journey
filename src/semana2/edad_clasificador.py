print("Hola un gussto conocerte")
name = input("Cuál es tu nombre: ")

while True:
    try:
        age = int(input(f"{name} , Cuál es tu edad: "))
        if age < 0:
            print("Numero invalido tiene que ser mayor a 0---")

        elif age > 120:
            print("Numero invalido tiene que ser menor a 120---")

        elif age < 18:
            print("Menor de edad")
            break
        elif age < 64:
            print("Eres un adulto")
            break
        else:
            print("Eres mayor")
            break
    except ValueError:
        print("Error---")
