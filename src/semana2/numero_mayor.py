import random
def numero_mayor(lista):
    n_mayor=lista[0]
    for n in lista:
        if n > n_mayor:
            n_mayor = n    
    return n_mayor
    
numeros=[random.randint(-50,50)for _ in range(15)]
numero_lista = numero_mayor(numeros)
print(numeros)
print(numero_mayor(numeros))