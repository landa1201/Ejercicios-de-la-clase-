class Libro:
    def _init_(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def mostrar_info(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Número de páginas: {self.paginas}")

    def actualizar_paginas(self, nuevas_paginas):
        if nuevas_paginas > 0:
            self.paginas = nuevas_paginas
            print(f"El número de páginas de '{self.titulo}' ha sido actualizado a {self.paginas}.")
        else:
            print("El número de páginas debe ser un valor positivo.")

libro1 = Libro("El Quijote", "Miguel de Cervantes", 500)
libro1.mostrar_info()

libro1.actualizar_paginas(550)
libro1.mostrar_info()
