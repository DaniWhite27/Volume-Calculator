import math
import unittest

def area_circulo(radio):
    """Calcula el área de un círculo."""
    if radio <= 0:
        raise ValueError("El radio debe ser un valor positivo.")
    return math.pi * radio**2

def area_triangulo(base, altura):
    """Calcula el área de un triángulo."""
    if base <= 0 or altura <= 0:
        raise ValueError("La base y la altura deben ser valores positivos.")
    return 0.5 * base * altura

def area_cuadrado(lado_cuadrado):
    """Calcula el área de un cuadrado."""
    if lado_cuadrado <= 0:
        raise ValueError("El lado debe ser un valor positivo.")
    return lado_cuadrado**2

def volumen_cubo(lado_cubo):
    """Calcula el volumen de un cubo."""
    if lado_cubo <= 0:
        raise ValueError("El lado debe ser un valor positivo.")
    return lado_cubo**3

try:   
    radio = int(input("Ingrese el radio del círculo en cm: "))
    base = int(input("Ingrese la base del triángulo en cm: "))
    altura = int(input("Ingrese la altura del triángulo en cm: "))
    lado_cuadrado = int(input("Ingrese el lado del cuadrado en cm: "))
    lado_cubo = int(input("Ingrese el lado del cubo en cm: "))

    print("Área del círculo con radio", radio, ":", area_circulo(radio), "cm2")
    print("Área del triángulo con base", base, "y altura", altura, ":", area_triangulo(base, altura), "cm2")
    print("Área del cuadrado con lado", lado_cuadrado, ":", area_cuadrado(lado_cuadrado), "cm2")
    print("Volumen del cubo con lado", lado_cubo, ":", volumen_cubo(lado_cubo), "cm3")
except ValueError as error:
    print("Error:", error)

class TestCalculadora(unittest.TestCase):
    
    def test_area_circulo(self):
        self.assertAlmostEqual(area_circulo(2), 12.566370, places=5)
        with self.assertRaises(ValueError):
            area_circulo(-2)

    def test_area_triangulo(self):
        self.assertAlmostEqual(area_triangulo(3, 4), 6)
        with self.assertRaises(ValueError):
            area_triangulo(-3, 4)

    def test_area_cuadrado(self):
        self.assertAlmostEqual(area_cuadrado(5), 25)
        with self.assertRaises(ValueError):
            area_cuadrado(-5)

    def test_volumen_cubo(self):
        self.assertAlmostEqual(volumen_cubo(3), 27)
        with self.assertRaises(ValueError):
            volumen_cubo(-3)

if __name__ == '__main__':
    unittest.main()


