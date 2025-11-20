def celcius_fahrenheit(c):
    resultado = (c * 9 / 5) + 32
    return resultado


# Programa principal
print("Bienvenido al convertidor de Celcius a Fahrenheit🌡️:")
while True:
    try:
        ingresar_grados = float(input("Ingresa la temperatura en Celsius🌡️: "))
        grados = celcius_fahrenheit(ingresar_grados)
        print(f"{ingresar_grados}°C equivalen a {grados}°F")
        break
    except ValueError:
        print("Escribe un número valido ")
