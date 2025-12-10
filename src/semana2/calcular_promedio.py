#Usando las funciones de len() y sum() realizo la operaciones utomatico sin yo usar contadores.
"""import random

def calcular_promedio(lista):
    suma = sum(lista)
    cantidad = len(lista)
    promedio = suma / cantidad
    return promedio     

numeros = [random.randint(-50,50) for _ in range(15)]

promedio_lista = calcular_promedio(numeros)

print("Lista de números:", numeros)
print("Promedio:", promedio_lista)"""


"""import random

def calcular_promedio_manual(lista):
    suma = 0          # Acumulador: aquí vamos sumando cada número
    contador = 0      # Contador: aquí contamos cuántos números hay

    for n in lista:   # n toma cada número de la lista uno por uno
        suma += n     # sumamos cada número
        contador += 1 # contamos cada elemento

    promedio = suma / contador
    return promedio

# Generar lista aleatoria
numeros = [random.randint(-50,50) for _ in range(15)]

promedio = calcular_promedio_manual(numeros)

print("Lista:", numeros)
print("Promedio calculado a mano:", promedio)"""

import random

def calcular_promedio_detallado(lista):
    suma = 0
    contador = 0

    print("Iniciando cálculo del promedio...\n")

    for n in lista:
        print(f"Valor actual (n): {n}")
        
        suma += n
        print(f"Suma acumulada: {suma}")
        
        contador += 1
        print(f"Cantidad de elementos contados hasta ahora: {contador}")
        
        print("----------------------------------------")

    promedio = suma / contador

    print("\nCálculo final:")
    print(f"Suma total: {suma}")
    print(f"Cantidad total de elementos: {contador}")
    print(f"Promedio = {suma} / {contador} = {promedio}")

    return promedio


# Generar lista aleatoria
numeros = [random.randint(-50,50) for _ in range(10)]

print("Lista generada:")
print(numeros)
print("\n")

promedio = calcular_promedio_detallado(numeros)

