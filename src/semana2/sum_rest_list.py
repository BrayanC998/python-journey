import random
def sumar_positivo(lista1):
    suma_positivos = 0
    for n  in lista1:
        if n > 0:
            suma_positivos += n
    return suma_positivos
def resta_negativos(lista2):
    resta_negativos = 0
    for n in lista2:
        if n < 0:
            resta_negativos += n
    return resta_negativos
def sumar_ceros(lista3):
    cuntos_ceros = 0
    for n in lista3:
        if n == 0:
            cuntos_ceros += 1
    return cuntos_ceros
numeros=[random.randint(-20,20)for _ in range(20)]
numeros_lista1 = sumar_positivo(numeros)
numeros_lista2 = resta_negativos(numeros)
numeros_lista3 = sumar_ceros(numeros)
print(numeros)
print(numeros_lista1)
print(numeros_lista2)
print(numeros_lista3)