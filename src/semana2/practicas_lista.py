# programa para practicar lista.

# crear una lista vacia.
frutas = []

# 2. Pedir al usuario cuántas frutas quiere ingresar
cantidad = int(input("Cuantas frutas quieres ingresar: "))

# 3 repetir segun la cantidad indicada.

for i in range(cantidad):
    fruta = input(f"Ingresa las frutas: {i+1} ")
    frutas.append(fruta)

# 4. Mostrar todas las frutas ingresadas
print(f"las frutas son {frutas}")
