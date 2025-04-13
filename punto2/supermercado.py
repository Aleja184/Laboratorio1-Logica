from nodo import Nodo

class Supermercado:
    def __init__(self):
        self.cabecera = None
        self.cola = None

    def insertar(self,nombre_cajero,tiempo):
        nuevo_nodo = Nodo(nombre_cajero,tiempo)
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
        nodo_actual = self.cabecera
        while nodo_actual.siguiente != self.cola:
            nodo_actual = nodo_actual.siguiente
        nodo_actual.siguiente = None

    def imprimir(self):
        nodo_actual = self.cabecera
        while nodo_actual.siguiente != None:
            print(f'{nodo_actual.nombre_cajero}->')
            nodo_actual = nodo_actual.siguiente
        print(f'{nodo_actual.nombre_cajero}')

    def cajero_mas_rapido(self):
        nodo_actual = self.cabecera
        tiempos = 100
        nombre_cajero = None
        while nodo_actual.siguiente != None:
            if nodo_actual.tiempo < tiempos:
                tiempos = nodo_actual.tiempo
                nombre_cajero = nodo_actual.nombre_cajero
            nodo_actual = nodo_actual.siguiente
        print(f'El cajero más rápido es: {nombre_cajero}')
    

            