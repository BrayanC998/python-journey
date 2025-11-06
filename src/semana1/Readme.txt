# 🔐 Generador de Contraseñas Seguras

Proyecto realizado como parte del **Módulo 1** del curso de Python: *Fundamentos y primeros pasos*.

Este programa genera contraseñas seguras de manera aleatoria, combinando letras, números y símbolos.  
También valida la longitud de la contraseña ingresada por el usuario y guarda cada una con su fecha y hora de creación.

---

## 🧠 Conceptos aplicados

- Uso de variables y tipos de datos.
- Bucles `while` y control de flujo con `if`, `elif`, `else`.
- Manejo de errores con `try` y `except`.
- Funciones (`def`) y retorno de valores.
- Manejo de rutas con el módulo `os`.
- Manejo de archivos (`with open`).
- Registro de fecha y hora con `datetime`.

---

## ⚙️ Requisitos

- Tener **Python 3.8 o superior** instalado.  
- No requiere librerías externas (solo módulos estándar de Python).

---

## ▶️ Cómo ejecutar el programa

1. Abre una terminal o consola.  
2. Navega hasta la carpeta donde está el archivo:

   ```bash
   cd src/semana1
3. Ejecuta el programa:
   python generador_contrasena.py
4. Ingresa la longitud deseada para la contraseña (entre 4 y 64 caracteres).
5. El programa mostrará la contraseña generada y la guardará en el archivo passwords.txt

## 💾 Ejemplo de salida
	Bienvenido al generador de Contraseñas
	Cuál es la Longitud de tu contraseña?: 12
	La contraseña segura es: N&9hK@t!2sR#
	Contraseña Guardada en passwords.txt
## El archivo passwords.txt contendrá:
 2025-11-06 22:51:04 - N&9hK@t!2sR#

## 🧩 Estructura del proyecto
semana1/
│
├── generador_contrasena.py   # Código principal del proyecto
├── passwords.txt              # Archivo generado automáticamente
└── README.md                  # Descripción del proyecto

## 🧠 Lecciones aprendidas

Durante el desarrollo de este proyecto aprendí a:
Usar funciones y bucles correctamente.
Controlar errores y validar entradas del usuario.
Trabajar con rutas y archivos de manera segura.
Escribir código más limpio y legible.

## 🏗️ Próximos pasos

Agregar opciones para incluir o excluir símbolos.
Permitir generar múltiples contraseñas a la vez.
Crear una pequeña interfaz en consola o web para el usuario.