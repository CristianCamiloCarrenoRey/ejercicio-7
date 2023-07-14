import time

class Vehiculo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.velocidad = 0

    def acelerar(self, velocidad):
        self.velocidad = velocidad

    def frenar(self):
        self.velocidad = 0

    def mover(self):
        print(f"{self.nombre} se está moviendo a {self.velocidad} km/h.")

class Semaforo:
    def __init__(self,numero):

        self.numero=numero
        self.estado = "verde"

    def cambiar_estado(self):
        if self.estado == "verde":
            self.estado = "rojo"
        else:
            self.estado = "verde"

    def mostrar_estado(self):
        print(f"El semáforo  {self.numero} está en  {self.estado}.")

class Cruce:
    def __init__(self, semaforo):
        self.semaforo = semaforo

    def cruzar(self, vehiculo):
        if self.semaforo.estado == "verde":
            print(f"{vehiculo.nombre} cruza el cruce.")
        else:
            print(f"{vehiculo.nombre} espera en el cruce.")

# Crear objetos
vehiculo1 = Vehiculo("Coche 1")
vehiculo2 = Vehiculo("coche 2")
semaforo1 = Semaforo("1")
semaforo2 = Semaforo("2")
cruce1 = Cruce(semaforo1)
cruce2= Cruce(semaforo2)

# Simulación
vehiculo1.acelerar(50)
vehiculo1.mover()

vehiculo2.acelerar(30)
vehiculo2.mover()

semaforo1.mostrar_estado()
cruce1.cruzar(vehiculo1)

vehiculo2.frenar()

semaforo1.cambiar_estado()
cruce1.cruzar(vehiculo2)


semaforo2.mostrar_estado()

cruce2.cruzar(vehiculo2)





