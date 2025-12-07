def sumar_positivo(lista):
    lista=[]
    while True:
        print("Opcion 1, ingresar numeros a la lista")
        print("Opcion 2, hacer calculo de sumas de numeros positivos")
        print("Opcion 3, hacer calculo de numeros negativos")
        print("Opcion 4, sumar todo los numeros")
        
        opciones=int(input("Ingresar numeros de la lista:"))
        
        if opciones == 1:
            entrada_numeros = int(input("ingresar numero para la lista"))
            if entrada_numeros:
                lista.append(entrada_numeros)
                print(f"Ingresaste nuevo numero a la lista: {entrada_numeros}")
            else:
                print("No ingresaste ningun numero")