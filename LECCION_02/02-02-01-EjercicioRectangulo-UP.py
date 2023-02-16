"""
Instrucciones de la tarea:
- En el siguiente ejercicio se solicita calcular el área y el perímetro de un Rectángulo,
para ello deberemos crear las siguientes variables:

alto (int)
ancho (int)

- El usuario debe proporcionar los valores de alto y ancho,
y después se debe imprimir el resultado en el siguiente formato
(no usar acentos y respetar los espacios, mayúsculas, minúsculas y saltos de línea):

Proporciona el alto:
Proporciona el ancho:
Area: <area>
Perimetro: <perimetro>

Las formulas para calcular el area y el perimetro de un Rectangulo son:
Area: alto * ancho
Perimetro: (alto + ancho) * 2
"""
Alto = int(input("Proporciona el alto: "))
Ancho = int(input("Proporciona el ancho: "))
Area = Alto * Ancho
Perimetro = (Alto + Ancho) * 2
print(f"Area: {Area}")
print(f"Perimetro: {Perimetro}")
print("Fin del programa.")
