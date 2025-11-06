import random
import string
import os


def contrasena_segura(longitud):

    letras = string.ascii_letters
    numeros = string.digits
    simbolos = string.punctuation
    combinado = letras + numeros + simbolos
    contrasena = ""

    for i in range(longitud):
        aleatorio = random.choice(combinado)
        contrasena += aleatorio
    return contrasena


print("Bienvenido al generador de Contraseñas")
while True:
    try:

        longitud_usuario = int(input("Cual es la Longitud de tu contraseña?: "))
        contrasena_generada = contrasena_segura(longitud_usuario)
        print(f"La contraseña segura es: {contrasena_generada}")
        break

    except:
        print("Error de usuario correrir longitud de contraseña")


# Ruta absoluta a la carpeta 'semana1'
ruta_carpeta = r"C:\Users\SrK2xD\Desktop\python-journey\src\semana1"
ruta_archivo = os.path.join(ruta_carpeta, "passwords.txt")

with open(ruta_archivo, "a") as file:
    file.write(contrasena_generada + "\n")

print("Contraseña Guardada en passwords.txt")
