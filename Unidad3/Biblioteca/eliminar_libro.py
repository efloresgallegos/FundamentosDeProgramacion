def eliminar_libro(titulo):
    try:
        with open("libros.txt", "r", encoding="utf-8") as f:
            lineas = f.readlines()

        nuevo_contenido = [l for l in lineas if not l.lower().startswith(titulo.lower() + ",")]

        if len(lineas) == len(nuevo_contenido):
            print(f"El libro '{titulo}' no fue encontrado.")
            return

        with open("libros.txt", "w", encoding="utf-8") as f:
            f.writelines(nuevo_contenido)
        print(f"Libro '{titulo}' eliminado correctamente.")
    except FileNotFoundError:
        print("No hay libros guardados aún.")

if __name__ == "__main__":
    t = input("Título del libro a eliminar: ")
    eliminar_libro(t)