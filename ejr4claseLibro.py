class Libro:
    def __init__(self, titulo, autor, num_paginas):
        self.__titulo = titulo
        self.__autor = autor
        self.__num_paginas = num_paginas
        self.__pagina_actual = 1  
    
    def avanzar_paginas(self, paginas):
        if self.__pagina_actual + paginas > self.__num_paginas:
            raise ValueError("No puedes avanzar más allá del número total de páginas.")
        else:
            self.__pagina_actual += paginas
    
    def retroceder_paginas(self, paginas):
        
        if self.__pagina_actual - paginas < 1:
            raise ValueError("No puedes retroceder más allá de la página 1.")
        else:
            self.__pagina_actual -= paginas
    
    def consultar_pagina_actual(self):
        return self.__pagina_actual
    
    def obtener_info_libro(self):
        return f"Título: {self.__titulo}\nAutor: {self.__autor}\nNúmero de páginas: {self.__num_paginas}\nPágina actual: {self.__pagina_actual}"

try:
    libro = Libro("Cien Años de Soledad", "Gabriel García Márquez", 400)
    
    print(libro.obtener_info_libro())
    
    libro.avanzar_paginas(50)
    print(f"Página actual después de avanzar 50 páginas: {libro.consultar_pagina_actual()}")
    
    libro.retroceder_paginas(20)
    print(f"Página actual después de retroceder 20 páginas: {libro.consultar_pagina_actual()}")
    
    libro.avanzar_paginas(400) 
except ValueError as e:
    print(e)

