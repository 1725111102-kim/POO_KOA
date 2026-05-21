class LibroBiblioteca:
    def __init__(self, titulo, autor, editorial, ano_publicacion, num_paginas, genero, isbn, idioma, estado, codigo_biblioteca):
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.ano_publicacion = ano_publicacion
        self.num_paginas = num_paginas
        self.genero = genero
        self.isbn = isbn
        self.idioma = idioma
        self.estado = estado  # Ej. "Disponible", "Dañado"
        self.codigo_biblioteca = codigo_biblioteca
        self.esta_abierto = False

    def prestarse(self):
        self.estado = "Prestado"
        return f"El libro '{self.titulo}' ha sido prestado."

    def devolverse(self):
        self.estado = "Disponible"
        return f"El libro '{self.titulo}' ha sido devuelto a la biblioteca."

    def abrirse(self):
        self.esta_abierto = True
        return f"Has abierto el libro '{self.titulo}'."

    def leerse(self):
        return f"Estás leyendo las páginas de este libro de género {self.genero}."

    def registrarse(self):
        return f"El libro con código {self.codigo_biblioteca} ha sido registrado en el sistema."


# Creando el objeto pasando únicamente los valores en el orden correcto
mi_libro = LibroBiblioteca("Cien años de soledad", "Gabriel García Márquez", "Editorial Sudamericana", 1967, 496, "Novela", "978-0307474728", "Español", "Disponible", "BIB-00123")

# Probando los métodos
print(mi_libro.registrarse())
print(mi_libro.prestarse())
print(mi_libro.devolverse())
print(mi_libro.abrirse())
print(mi_libro.leerse()class LibroBiblioteca:
  
