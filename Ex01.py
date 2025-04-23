import math

# Classe base
class FiguraGeometrica:
    def area(self):
        pass

    def perimetro(self):
        pass

# Subclasses
class Circulo(FiguraGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return math.pi * self.raio ** 2

    def perimetro(self):
        return 2 * math.pi * self.raio

    def __str__(self):
        return "Círculo"

class Quadrado(FiguraGeometrica):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

    def perimetro(self):
        return 4 * self.lado

    def __str__(self):
        return "Quadrado"

class TrianguloEquilatero(FiguraGeometrica):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return (math.sqrt(3) / 4) * self.lado ** 2

    def perimetro(self):
        return 3 * self.lado

    def __str__(self):
        return "Triângulo Equilátero"

# Programa principal
figuras = [
    Circulo(3),
    Quadrado(4),
    TrianguloEquilatero(5)
]

for figura in figuras:
    print(f"{figura}")
    print(f"Área: {figura.area():.2f}")
    print(f"Perímetro: {figura.perimetro():.2f}\n")
