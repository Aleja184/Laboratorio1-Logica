from nodo_cajas import Nodo_Cajas

class Cajas_Disponibles:
    def __init__(self):
        self.cabecera = None
        self.cola = None

    def insertar(self,codigo_seguridad):
        nuevo_nodo = Nodo_Cajas(codigo_seguridad)
        if self.cabecera == None:
            self.cabecera = nuevo_nodo
            self.cola = nuevo_nodo
            return
        nodo_actual = self.cabecera
        while nodo_actual.siguiente != None:
            nodo_actual = nodo_actual.siguiente
        nodo_actual.siguiente = nuevo_nodo
        self.cola = nuevo_nodo

    def eliminar(self):
        if self.cabecera is None:
            return

        if self.cabecera is self.cola:
            self.cabecera = None
            self.cola = None
            return

        nodo_actual = self.cabecera
        while nodo_actual.siguiente is not self.cola:
            nodo_actual = nodo_actual.siguiente

        nodo_actual.siguiente = None
        self.cola = nodo_actual