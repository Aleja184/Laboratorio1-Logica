from nodo import Nodo
#Cola usando lista simplemente ligada.
class Supermercado:
    def __init__(self):
        self.cabecera = None
        self.cola = None
    #Se inserta un nuevo cajero al supermercado con su nombre y el tiempo que tarda en atender
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
    #Al ser una cola solo se puede eliminar el último miembro del supermercado
    def eliminar(self):
        nodo_actual = self.cabecera
        while nodo_actual.siguiente != self.cola:
            nodo_actual = nodo_actual.siguiente
        nodo_actual.siguiente = None
    #Se imprime cada miembro del supermercado
    def imprimir(self):
        nodo_actual = self.cabecera
        while nodo_actual.siguiente != None:
            print(f'{nodo_actual.nombre_cajero}->')
            nodo_actual = nodo_actual.siguiente
        print(f'{nodo_actual.nombre_cajero}')

    #Se busca entre los tiempos de cada cajero cuál es el que menor tiempo tarda en atender
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
    

            