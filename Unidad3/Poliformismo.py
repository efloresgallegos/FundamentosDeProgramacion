# Clase base
class Vehiculo:
    def acelerar(self):
        print("El vehículo está acelerando...")

# Subclase 1
class Auto(Vehiculo):
    def acelerar(self):
        print("El auto acelera aumentando la gasolina ")

# Subclase 2
class Bicicleta(Vehiculo):
    def acelerar(self):
        print("La bicicleta acelera pedaleando más rápido ")

# Subclase 3
class Avion(Vehiculo):
    def acelerar(self):
        print("El avión acelera encendiendo los motores a reacción ")


auto1 = Auto()
bici1 = Bicicleta()
avion1 = Avion()

# Mismo método, diferente comportamiento
auto1.acelerar()
bici1.acelerar()
avion1.acelerar()