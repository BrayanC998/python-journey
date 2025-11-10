
print("Hola a todos")


while True:
    try:
        temperatura = float(input("La temperatura de hoy es de: "))
        if temperatura < 10 :
            print("Hace frío 🥶")
            
        elif temperatura < 25:
            print("El clima está templado 😌")
            
        else :
            print("Hace calor 🥵")
        
        break
    except ValueError:
        print("Añade un valor correcto")