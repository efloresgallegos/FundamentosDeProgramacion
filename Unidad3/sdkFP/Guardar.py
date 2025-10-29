class Guardar:
    def guardar_libro(self, titulo, autor):
        with open("libros.txt", "a") as f:
            f.write(f"{titulo} - {autor}\n")
        return f"Libro '{titulo}' guardado correctamente."