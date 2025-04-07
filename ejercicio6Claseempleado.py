class Empleado:
    contador_empleados = 0
    
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
        
        Empleado.contador_empleados += 1
    
    @classmethod
    def cantidad_empleados(cls):
        return cls.contador_empleados

empleado1 = Empleado("Juan Pérez", 3500)
empleado2 = Empleado("Ana Gómez", 4200)
empleado3 = Empleado("Carlos Rodríguez", 3800)

print(f"Total de empleados: {Empleado.cantidad_empleados()}") 