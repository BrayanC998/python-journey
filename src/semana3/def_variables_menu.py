def registrar_persona(personas):
    nombre = input("Registrar Nombre: ").lower().strip()
    edad = int(input("Registrar la edad: "))
    ciudad = input("Registrar la ciudad: ")

    persona = {
        "nombre": nombre,
        "edad": edad,
        "ciudad": ciudad
    }

    personas.append(persona)


def mostrar_personas(personas):
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


def buscar_personas(personas):
    if not personas:
            print("No hay personas registradas para buscar.")
            print("---------------------------------")
    else:
        buscar_persona = input("Nombre de la persona a buscar: ").lower().strip()
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


lista_personas = []

while True:
    print("Registro de Personas")
    print("1 Opcion de Registro")
    print("2 Opcion de Mostar registro")
    print("3 Opcion de buscar registro")
    print("4 Salir")

    opciones = input("Escojer la opcion que necesites 1-4: ")
    print("")

    if opciones == "1":
        registrar_persona(lista_personas)
        print("Registro nuevo.")
        print("---------------------------------")

    elif opciones == "2":
        mostrar_personas(lista_personas)

    elif opciones == "3":
        buscar_personas(lista_personas)

    elif opciones == "4":
        print("Salir")
        break
    else:
        print("❌ Opción no válida. Intenta de nuevo.")
