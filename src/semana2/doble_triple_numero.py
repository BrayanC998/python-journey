def calcular_potencias(numero):
    """Funciones"""
    doble = numero * 2

    triple = numero * 3

    return doble, triple


# programa principal

valor = int(input("Inserta un numero: "))
res_doble, res_triple = calcular_potencias(valor)
print(f"El doble de {valor} es: {res_doble}")
print(f"El triple de {valor} es: {res_triple}")
