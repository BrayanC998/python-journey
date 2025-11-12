import random
import string
import os
from datetime import datetime


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
        longitud_usuario = int(input("Cuál es la Longitud de tu contraseña?: "))

        if longitud_usuario < 4:
            print("La contraseña es menor a 4 caracteres es insegura: ")
        elif longitud_usuario > 64:
            print("La contraseña supera el rango de 64 caracteres: ")
        else:
            # Si pasa las validaciones, genera la contraseña
            contrasena_generada = contrasena_segura(longitud_usuario)
            print(f"La contraseña segura es: {contrasena_generada}")
            break  # sale del while porque todo salió bien

    except ValueError:
        print("Error: debes escribir un número válido: ")


# Ruta absoluta a la carpeta 'semana1'
ruta_carpeta = os.path.dirname(__file__)  # abre carpeta donde esta el archivo
ruta_archivo = os.path.join(
    ruta_carpeta, "passwords.txt"
)  # revisa si existe el nombre del archivo o crea si no existe y escribe el resultado ahi

fecha_hora = datetime.now().strftime(
    "%Y-%m-%d %H:%M:%S"
)  # Guarda la fecha y la hora del comento de guardar la contraseña
with open(ruta_archivo, "a") as file:
    file.write(f"{fecha_hora} - {contrasena_generada}  \n")

print("Contraseña Guardada en passwords.txt")
