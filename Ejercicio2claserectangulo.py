class Rectangulo:
    def __init__(self, largo, ancho):
        if largo > 0 and ancho > 0:
            self.__largo = largo
            self.__ancho = ancho
        else:
            raise ValueError("Las dimensiones deben ser mayores que cero.")
    
    def cambiar_dimensiones(self, nuevo_largo, nuevo_ancho):
        if nuevo_largo > 0 and nuevo_ancho > 0:
            self.__largo = nuevo_largo
            self.__ancho = nuevo_ancho
        else:
            raise ValueError("Las dimensiones deben ser mayores que cero.")
    
    def calcular_area(self):
        return self.__largo * self.__ancho
    
    def calcular_perimetro(self):
        return 2 * (self.__largo + self.__ancho)
    
    def consultar_dimensiones(self):
        return self.__largo, self.__ancho

try:
    rectangulo = Rectangulo(5, 3)
    print(f"Dimensiones iniciales: {rectangulo.consultar_dimensiones()}")
    print(f"Área: {rectangulo.calcular_area()}")
    print(f"Perímetro: {rectangulo.calcular_perimetro()}")

    rectangulo.cambiar_dimensiones(7, 4)
    print(f"Dimensiones modificadas: {rectangulo.consultar_dimensiones()}")
    print(f"Área: {rectangulo.calcular_area()}")
    print(f"Perímetro: {rectangulo.calcular_perimetro()}")

except ValueError as e:
    print(e)
