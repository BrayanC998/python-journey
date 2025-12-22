def registrar_persona():
    nombre = input("Registrar Nombre: ")
    edad = int(input("Registrar la edad: "))
    ciudad = input("Registrar la ciudad: ")
    
    diccionario = {
        "nombre" : nombre,
        "edad" : edad,
        "ciudad" : ciudad
        }
    return diccionario

personas = []
while True:
    print("Registro de Personas")
    print("1 Opcion de Registro")
    print("2 Opcion de Mostar registro")
    print("3 Opcion de buscar registro")
    print("4 Salir")
    
    opciones = (input("Escojer la opcion que necesites 1-4: "))
    print("")
    
    if opciones == "1":
        nueva_persona = registrar_persona()
        if nueva_persona:
            personas.append(nueva_persona)
            print("")
            print("Registro nuevo. ")
            print("---------------------------------")
        else:
            print("No se realizo ningun registro. ")
            print("---------------------------------")

    elif opciones == "2":
        if not personas:
            print("No hay personas registradas")
            print("")
            
        else:
            print("--- Personas Registradas ---")
            print("")
            for n in personas:
                print("Nombre: ", n["nombre"])
                print("Edad: ", n["edad"])
                print("Ciudad: ", n["ciudad"])
                print("---------------------------------")
                

    elif opciones == "3":
        if not personas:
            print("No hay personas registradas para buscar.")
            print("---------------------------------")
        else:
            buscar_persona = input("Nombre de la persona a buscar: ")
            print("---------------------------------")
            encontrada = False

            for n in personas:
                if n["nombre"] == buscar_persona:
                    print("Persona encontrada:")
                    print("Nombre:", n["nombre"])
                    print("Edad:", n["edad"])
                    print("Ciudad:", n["ciudad"])
                    print("---------------------------------")
                    encontrada = True
                    break  # detenemos la búsqueda

            if not encontrada:
                print("Persona no encontrada.")
                print("---------------------------------")
        
    elif opciones == "4":
        print("Salir")
        break
    else:
        print("❌ Opción no válida. Intenta de nuevo.")
        
        

