#Clase nodo con el nombre del cajero y el tiempo que tarda en atender
class Nodo:
    def __init__(self,nombre_cajero,tiempo):
        self.nombre_cajero = nombre_cajero
        self.tiempo = tiempo
        self.siguiente = None