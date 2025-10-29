class Consultar:
    def consultar_libros(self):
        try:
            with open("libros.txt", "r") as f:
                return f.readlines()
        except FileNotFoundError:
            return []