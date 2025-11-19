# Lista inicial
frutas = ["manzana", "pera", "kiwi"]

print(f"Las frutas son: {frutas}")

# Cambiar una fruta
posicion = int(input("Que posicion quieres cambiar 0, 1 , 2: "))
nueva_fruta = input("Cual es la fruta nueva ")

frutas[posicion] = nueva_fruta

print("Frutas actualizadas", frutas)

# Eliminar una fruta
while True:
    try:

        eliminar = input("Que fruta deseas eliminar: ")
        if eliminar in frutas:
            frutas.remove(eliminar)
            print("Lista despues de eliminar ", frutas)
            break
        else:
            print("No se a eliminado ninguna fruta.")
    except ValueError:
        break
