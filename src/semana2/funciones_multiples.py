def calcular_rectangulo(base, altura):
    area = base * altura
    perimetro = 2 * (base + altura)
    return area, perimetro


print("calcular el are de un rectangulo")
base = float(input("Ingrese la base: "))
altura = float(input("Ingresar la Altura: "))

area_resultado, perimetro_resultado = calcular_rectangulo(base, altura)

print(f"Este es el area del rectangulo: {area_resultado}")
print(f"Este es el perimetro del rectangulo: {perimetro_resultado}")
