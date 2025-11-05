#consolidar tipos básicos (int, float, str, bool, list, dict) y operaciones básicas.

#Creacion de variable de usuario
name: str ="Brayan"
age: int = 27
height: float = 1.77
student: bool = True
hobbies: list = ["read", "travel", "music" ,"game"]
info_contact: dict= {"brayancamach5@gmail.com","+57301345671", "Calle 12334 #45-67"}

#Impresion de variables
#-----print("Mi nombre es,", name, ", mi edad es de,", age ,", mi altura es,", height)

#Agregar un nuevo hobbie a la lista
hobbies.append("sports")
#Imprimir lista y contarlas con len()
#-----print("Mis hobbies son",hobbies, "y son en total", len(hobbies))


#Crear varialbe año de nacimiento
#from sirve para obtener el año actual y import sirve para importar librerias
#datatime es la libreria y sirve para manejar fechas y date es la clase que maneja fechas
from datetime import date
#Obtener el año actual
current_year = date.today().year
#Calcular año de nacimiento
ano_nacimiento:int=current_year-age
#-----print("Año de nacimiento es:", ano_nacimiento , " y tengo ",age, "años.")

#definir una variable de tipo diccionario con información de contacto

def resumen_usuario(name, age, height,ano_nacimiento, hobbies):
    resume = f"Mi nombre es {name}, tengo {age} años, altura de {height} metros, naci en el año {ano_nacimiento} y mis hobbies son {hobbies}."
    return resume
resume=resumen_usuario(name, age, height,ano_nacimiento, hobbies)
#----print("Mi resumen es:", resume)

if __name__ == "__main__":
    print(resume)

