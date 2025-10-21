def consultar_libros():
    try:
        with open("libros.txt", "r", encoding="utf-8") as f:
            libros = f.readlines()

        if not libros:
            print("\n Lista de libros:")
            for linea in libros:
                titulo, autor = libros.strip().split(",", 1)
                print(f" {titulo} — {autor}")
        else:
            print("No hay libros registrados.")
            
    except FileNotFoundError:
        print(" Aún no existe el archivo de libros.")

if __name__ == "__main__":
    consultar_libros()