import math
from abc import ABC, abstractmethod

# Clase abstracta base
class Forma(ABC):
    @abstractmethod
    def calcular_area(self):
        pass
    
    @abstractmethod
    def mostrar_info(self):
        pass

class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        return math.pi * self.radio ** 2
    
    def mostrar_info(self):
        return f"Círculo - Radio: {self.radio}, Área: {self.calcular_area():.2f}"

class Cuadrado(Forma):
    def __init__(self, lado):
        self.lado = lado
    
    def calcular_area(self):
        return self.lado ** 2
    
    def mostrar_info(self):
        return f"Cuadrado - Lado: {self.lado}, Área: {self.calcular_area():.2f}"

class Triangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return (self.base * self.altura) / 2
    
    def mostrar_info(self):
        return f"Triángulo - Base: {self.base}, Altura: {self.altura}, Área: {self.calcular_area():.2f}"

class FabricaFormas:
    @staticmethod
    def crear_forma(tipo_forma, *args):
        if tipo_forma.lower() == "circulo":
            return Circulo(args[0])
        elif tipo_forma.lower() == "cuadrado":
            return Cuadrado(args[0])
        elif tipo_forma.lower() == "triangulo":
            return Triangulo(args[0], args[1])
        else:
            raise ValueError(f"Tipo de forma '{tipo_forma}' no soportado")
    
    @staticmethod
    def tipos_disponibles():
        return ["circulo", "cuadrado", "triangulo"]


def main():
    print("=== Demostración Patrón Factory Method ===")
    
    fabrica = FabricaFormas()
    
    print(f"Tipos de formas disponibles: {fabrica.tipos_disponibles()}")
    print()
    
    formas = []
    
    circulo = fabrica.crear_forma("circulo", 5)
    formas.append(circulo)
    
    cuadrado = fabrica.crear_forma("cuadrado", 4)
    formas.append(cuadrado)
    
    triangulo = fabrica.crear_forma("triangulo", 6, 8)
    formas.append(triangulo)
    
    print("Formas creadas:")
    for i, forma in enumerate(formas, 1):
        print(f"{i}. {forma.mostrar_info()}")
    
    print()
    
    area_total = sum(forma.calcular_area() for forma in formas)
    print(f"Área total de todas las formas: {area_total:.2f}")
    
    try:
        forma_invalida = fabrica.crear_forma("hexagono", 5)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()