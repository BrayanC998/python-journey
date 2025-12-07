import random
def sumar_positivo(lista):
    suma_positivos = 0
    for n  in lista:
        if n > 0:
            suma_positivos += n
    return suma_positivos

numeros=[random.randint(-20,20)for _ in range(10)]
numero_lista = sumar_positivo(numeros)
print(numeros)
print(numero_lista)