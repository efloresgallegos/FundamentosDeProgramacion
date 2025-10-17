class Libro:
    def __init__(self, titulo, autor):
    self.titulo = titulo          # atributo de instancia
        self.autor = autor            # atributo de instancia
        self.disponible = True        # atributo de estado

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f'«{self.titulo}» ha sido prestado.')
        else:
            print(f'Lo siento, «{self.titulo}» ya está prestado.');

    def devolver(self):
        if not self.disponible:
            self.disponible = True
            print(f'«{self.titulo}» ha sido devuelto.')
        else:
            print(f'«{self.titulo}» ya estaba en la estantería.')

    def __str__(self):
        estado = 'Disponible' if self.disponible else 'Prestado'
        return f'"{self.titulo}" de {self.autor} [{estado}]'


class Biblioteca:
    def __init__(self):
        self.catalogo = []   

    def agregar_libro(self, libro):
        self.catalogo.append(libro)

    def buscar_por_titulo(self, titulo):
        resultados = [l for l in self.catalogo if titulo.lower() in l.titulo.lower()]
        return resultados

    def mostrar_catalogo(self):
        print("\nCatálogo de la biblioteca:")
        for libro in self.catalogo:
            print("  -", libro)


if __name__ == "__main__":
    #Creamos la biblioteca y algunos libros
    bib = Biblioteca1()
    bib.agregar_libro(Libro("Cien años de soledad", "Gabriel García Márquez"))
    bib.agregar_libro(Libro("Don Quijote de la Mancha", "Miguel de Cervantes"))
    bib.agregar_libro(Libro("El Principito", "Antoine de Saint‑Exupéry"))

    #Mostramos el catálogo completo
    bib.mostrar_catalogo()