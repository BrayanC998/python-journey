# 🥝 PROGRAMA: MENÚ DE FRUTAS 🥝

frutas = []

while True:
    print("\n🍎 MENÚ DE OPCIONES 🍎")
    print("1️⃣ Agregar una fruta")
    print("2️⃣ Mostrar frutas")
    print("3️⃣ Cambiar una fruta")
    print("4️⃣ Eliminar una fruta")
    print("5️⃣ Salir")

    opciones = input("Seleccionar una opcion de 1-5: ")

    # ---------------------
    # 1️⃣ AGREGAR FRUTA
    # ---------------------
    if opciones == "1":
        nueva_fruta = input("Ingresa una fruta: ").strip().lower()
        if nueva_fruta:
            frutas.append(nueva_fruta)
            print(f"✅ {nueva_fruta} fue agregada a la lista.")
        else:
            print("⚠️ No escribiste ninguna fruta.")

    # ---------------------
    # 2️⃣ MOSTRAR FRUTAS
    # ---------------------
    elif opciones == "2":
        if len(frutas) == 0:
            print("❗ Aún no hay frutas en la lista.")
        else:
            print("🍉 Lista de frutas:")
            for indice, fruta in enumerate(frutas):
                print(f"{indice} - {fruta}")

    # ---------------------
    # 3️⃣ CAMBIAR FRUTA
    # ---------------------
    elif opciones == "3":
        if len(frutas) == 0:
            print("No hay frutas para cambiar.")
        else:
            for indice, fruta in enumerate(frutas):
                print(f"{indice} - {fruta}")

            try:
                pos = int(input("¿Qué posición quieres cambiar?: "))
                if pos < 0 or pos >= len(frutas):
                    print("Índice inválido.")
                else:
                    nueva = input("Ingresa la nueva fruta: ").strip().lower()
                    frutas[pos] = nueva
                    print("Fruta actualizada correctamente.")
            except ValueError:
                print("❌ Debes ingresar un número válido.")

    # ---------------------
    # 4️⃣ ELIMINAR FRUTA
    # ---------------------
    elif opciones == "4":
        if len(frutas) == 0:
            print("No hay frutas para eliminar.")
        else:
            for indice, fruta in enumerate(frutas):
                print(f"{indice} - {fruta}")

            try:
                pos = int(input("¿Qué posición quieres eliminar?: "))
                if pos < 0 or pos >= len(frutas):
                    print("Índice inválido.")
                else:
                    fruta_eliminada = frutas.pop(pos)
                    print(f"🗑️ Se eliminó: {fruta_eliminada}")
            except ValueError:
                print("❌ Debes ingresar un número válido.")

    # ---------------------
    # 5️⃣ SALIR
    # ---------------------
    elif opciones == "5":
        print("👋 Saliendo del programa... ¡Hasta pronto!")
        break

    else:
        print("❌ Opción no válida. Intenta de nuevo.")
