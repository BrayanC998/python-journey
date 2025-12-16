def registrar_persona():
    nombre = input("Ingresar nombre para Diccionario: ")
    edad = int(input("Ingresar edad para Diccionario: "))
    ciudad = input("Ingresar ciudad para Diccionario: ")
    
    diccionario = {
        "nombres" : nombre,
        "edad" : edad,
        "ciudad" : ciudad
    }
    return diccionario

personas = registrar_persona()
print(personas)