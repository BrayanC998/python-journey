import random

def analizar_lista(lista):
    cant_positivos = 0
    cant_negativos = 0
    cant_ceros = 0

    num_mayor = lista[0]
    num_menor = lista[0]

    suma_promedio = 0
    cont_promedio = 0

    for n in lista:
        suma_promedio += n
        cont_promedio += 1
        prom_numeros = suma_promedio / cont_promedio

        if n > 0:
            cant_positivos += 1
        if n < 0:
            cant_negativos += 1
        if n == 0:
            cant_ceros += 1

        if n > num_mayor:
            num_mayor = n
        if n < num_menor:
            num_menor = n

    return cant_positivos, cant_negativos, cant_ceros, num_mayor, num_menor, prom_numeros

numeros=[random.randint(-20,20) for _ in range(15)]
v_analizar = analizar_lista(numeros)
print(numeros)
print(v_analizar)