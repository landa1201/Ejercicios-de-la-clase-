class Producto:
    def __init__(self, nombre, precio):
        self.__nombre = nombre
        self.__precio = precio

    def cambiar_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            raise ValueError("El precio debe ser mayor que cero.")

    def obtener_precio(self):
        return self.__precio

    def obtener_nombre(self):
        return self.__nombre

    def aplicar_descuento(self, porcentaje_descuento):
        if 0 <= porcentaje_descuento <= 100:
            descuento = (self.__precio * porcentaje_descuento) / 100
            self.__precio -= descuento
        else:
            raise ValueError("El porcentaje de descuento debe estar entre 0 y 100.")

try:
    producto = Producto("Laptop", 1000)
    print(f"Producto: {producto.obtener_nombre()}, Precio inicial: {producto.obtener_precio()}")

    producto.cambiar_precio(1200)
    print(f"Nuevo precio: {producto.obtener_precio()}")

    producto.aplicar_descuento(10)
    print(f"Precio con descuento: {producto.obtener_precio()}")
except ValueError as e:
    print(e)
