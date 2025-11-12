# practicando definiendo funciones..

# definir funcion
def saludar_usuario(nombre):
    return f"¡Hola {nombre}! 😊 Espero que te encuentres bien para practicar funciones hoy."


# codigo principal

nombre_usuario = input("Dime tu nombre: ")
saludo_personal = saludar_usuario(nombre_usuario)
print(saludo_personal)
