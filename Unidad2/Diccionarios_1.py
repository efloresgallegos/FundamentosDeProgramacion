edades = {
    "Brayan": 25,"Pabellón de Arteaga",
    "Luis": 30,
    "José": 22
}
print("Edad de Luis:", edades["Luis"])    
edades["Pedro"] = 28
print("\nDespués de añadir a Pedro:")
print(edades)                               

edades["Luis"] = 26
print("\nDespués de actualizar la edad de Luis:")
print(edades)                              

del edades["María"]
print("\nDespués de eliminar a José:")
print(edades)                               

print("\nRecorriendo el diccionario:")
for nombre, edad in edades.items():         
     print(f"{nombre} tiene {edad} años")