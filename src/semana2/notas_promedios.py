# --- Calcular promedio de notas ---


# 1️⃣ Definimos una función que recibe una lista de notas
def calcular_promedio(lista_notas):
    suma = sum(lista_notas)  # suma() agrega todas las notas
    cantidad = len(lista_notas)  # len() cuenta cuántas notas hay
    promedio = suma / cantidad  # división para obtener el promedio
    return promedio  # devuelve el resultado


# 2️⃣ Código principal
notas = []

cuantas_notas = int(input("Cantidad de notas del estudiante: "))

for i in range(cuantas_notas):
    nota = float(input(f"Ingrese las notas {i+1}: "))
    notas.append(nota)


# 3️⃣ Llamamos a la función y mostramos el resultado

promedio_final = calcular_promedio(notas)
print(f"\nLas notas ingresadas son: {notas}")
print(f"El premodio es: {promedio_final:.2f}")
