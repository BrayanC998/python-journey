# definicioon de varialbe temperatura.
def clasificar_temperatura(
    temperatura,
):  # aqui la variable temperatura es la que se ingresar y se guarda
    if temperatura <= 0:
        return "¡Cuidado, punto de congelación! ❄️"
    elif temperatura < 10:
        return "Hace frío 🥶"
    elif temperatura < 25:
        return "El clima está templado 😌"
    elif temperatura >= 40:
        return "Temperatura extrema 🥵🥵🥵"
    else:
        return "Hace calor 🥵"


# Codigo principal para imprimir la logica de la temperatura.
print("Bienvenido al clasificador de temperatura 🌡️")
while True:
    try:
        grados_temperatura = float(input("Ingresar la temperatura del dia de hoy:🌡️  "))
        resultado_definicion_ = clasificar_temperatura(grados_temperatura)
        # secambia variable temperatura por grados_temperatura para leerla variable de ingreso tambien.
        print(resultado_definicion_)
        break
    except ValueError:
        print("Ingresar el valor correcto")
