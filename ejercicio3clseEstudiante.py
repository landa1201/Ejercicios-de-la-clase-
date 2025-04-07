class Estudiante:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
        self.__notas = []
    
    def agregar_nota(self, nota):
        if 0 <= nota <= 100:
            self.__notas.append(nota)
        else:
            raise ValueError("La nota debe estar entre 0 y 100.")
    
    def calcular_promedio(self):
        if len(self.__notas) > 0:
            return sum(self.__notas) / len(self.__notas)
        else:
            return 0 
    
    def consultar_nombre(self):
        return self.__nombre
    
    def consultar_edad(self):
        return self.__edad

    def consultar_notas(self):
        return self.__notas

try:
    estudiante = Estudiante("Juan Pérez", 20)
    print(f"Nombre: {estudiante.consultar_nombre()}")
    print(f"Edad: {estudiante.consultar_edad()}")

    estudiante.agregar_nota(85)
    estudiante.agregar_nota(92)
    estudiante.agregar_nota(78)

    print(f"Notas: {estudiante.consultar_notas()}")
    print(f"Promedio de notas: {estudiante.calcular_promedio()}")

    estudiante.agregar_nota(110)  
except ValueError as e:
    print(e)
