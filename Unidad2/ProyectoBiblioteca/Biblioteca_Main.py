import json

biblioteca = {
    "978-84-376-0494-7": {
        "título": "Cien años de soledad",
        "autor": ["Gabriel García Márquez"],
        "géneros": ["Realismo mágico", "Novela histórica"]
    },
    "978-84-204-1625-5": {
        "título": "Don Quijote de la Mancha",
        "autor": ["Miguel de Cervantes Saavedra"],
        "géneros": ["Novela de caballería", "Satira"]
    }
}

isbn = "978-84-376-0494-7"
info_libro = biblioteca.get(isbn)          
print("\nInformación del libro:", info_libro)

nuevo_isbn = "978-84-376-0500-0"
biblioteca.setdefault(
    nuevo_isbn,
    {
        "título": "La sombra del viento",
        "autor": ["Carlos Ruiz Zafón"],
        "géneros": ["Misterio", "Novela urbana"]
    }
)
print("\nBiblioteca después de setdefault():")
print(json.dumps(biblioteca, indent=4, ensure_ascii=False))

biblioteca[isbn]["géneros"].append("Ficción")
print("\nGéneros actualizados de Cien años de soledad:")
print(biblioteca[isbn]["géneros"])
print(biblioteca)

with open("biblioteca.json", "w", encoding="utf-8") as f:
    json.dump(biblioteca, f, ensure_ascii=False, indent=4)
print("\n✅ Biblioteca guardada en 'biblioteca.json'")
