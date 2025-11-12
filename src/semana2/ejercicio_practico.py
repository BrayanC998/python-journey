def doblar_numero(numero):
    print(f"📥 Entrando a la función con el número: {numero}")
    resultado = numero * 2
    print(f"📤 Saliendo de la función con el resultado: {resultado}")
    return resultado


valor = int(input("Un numero: "))
doble_numero = doblar_numero(valor)
print(f"Resultado final recibido: {doble_numero}")
