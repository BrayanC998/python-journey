def registrar_personas():
    
    nombre = input("Registrar Nombre: ")
    edad = int(input("Registrar la edad: "))
    ciudad = input("Registrar la ciudad: ")
    
    diccionario = {
        "nombre" : nombre,
        "edad" : edad,
        "ciudad": ciudad
    }
    return diccionario
personas = []
while True:
    registro = registrar_personas()
    personas.append(registro)
    opcion=input("Quieres registrar otra persona: s/n: ")
    if opcion == "s":
        print("Registro Nuevo")
    elif opcion == "n":
        print("Salir")
        break

print(personas)

buscar_nombre=input("Pedir nombre que se va a buscar: ")
encontrar= False

for n in personas:
    if n["nombre"]== buscar_nombre:
        encontrar = True
        print("Persona Encontrada")
        print(buscar_nombre)
if encontrar== False:
    print("No encontrada")
    
