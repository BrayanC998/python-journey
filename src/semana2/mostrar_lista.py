def mostrar_lista(lista):
    # 1. Comprobar si la lista está vacía
    if not lista:
        print("La lista está vacía")
    else:
        print("La lista tiene elementos, procediendo a sumar...")

    # 2. Inicializar variable para acumular la suma
    suma_total = 0

    # 3. Recorrer la lista y sumar
    for n in lista:
        suma_total += n

    # 4. Devolver la suma
    return suma_total


# 👉 CREAR UNA LISTA ANTES DE USAR LA FUNCIÓN
lista = [10, 20, 30, 40]

m_lista = mostrar_lista(lista)
print("La suma total es:", m_lista)
