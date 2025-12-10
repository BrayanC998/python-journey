import random
def numero_menor(lista):
    n_menor = lista[0]
    for n in lista:
        if n < n_menor:
            n_menor = n
            
    return n_menor
numeros=[random.randint(-50,50)for _ in range(15)]
numero_lista = numero_menor(numeros)
print(numeros)
print(numero_menor(numeros))