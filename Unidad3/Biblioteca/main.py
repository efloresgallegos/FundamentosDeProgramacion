from guardar_libro import guardar_libro
from eliminar_libro import eliminar_libro
from consultar_libros import consultar_libros

def menu():
    while True:
        print("\n=== BIBLIOTECA ===")
        print("1. Guardar libro")
        print("2. Eliminar libro")
        print("3. Consultar libros")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            guardar_libro(titulo, autor)
        elif opcion == "2":
            titulo = input("Título del libro a eliminar: ")
            eliminar_libro(titulo)
        elif opcion == "3":
            consultar_libros()
        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    menu()