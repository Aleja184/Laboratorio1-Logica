from nodo_pedidos import Nodo_Pedidos

class Pedidos:
    def __init__(self,cajas_disponibles):
        self.cabecera = None
        self.cola = None
        self.id_pedidos = 0
        self.cajas_disponibles = cajas_disponibles

    def insertar(self):
        if self.cajas_disponibles.cola is None:
            raise Exception("No hay cajas disponibles para asignar al pedido")
        codigo = self.cajas_disponibles.cola.codigo_seguridad
        self.cajas_disponibles.eliminar()
        nuevo_nodo = Nodo_Pedidos(self.id_pedidos, codigo)
        if self.cabecera == None:
            self.cabecera = nuevo_nodo
            self.cola = nuevo_nodo
            self.id_pedidos+=1
            return
        nodo_actual = self.cabecera
        while nodo_actual.siguiente!=None:
            nodo_actual = nodo_actual.siguiente
        nodo_actual.siguiente = nuevo_nodo
        nuevo_nodo.anterior = nodo_actual
        self.id_pedidos+=1
    
    def eliminar(self):
        nodo_actual = self.cabecera
        while nodo_actual.siguiente !=self.cola:
            nodo_actual = nodo_actual.siguiente
        nodo_actual.siguiente = None

    def imprimir(self):
        nodo_actual = self.cabecera
        while nodo_actual.siguiente !=None:
            print(f'El número del pedido es:{nodo_actual.id_pedido} y la caja asignada es: {nodo_actual.caja_asignada}->')
            nodo_actual = nodo_actual.siguiente
        print(f'El número del pedido es:{nodo_actual.id_pedido} y la caja asignada es: {nodo_actual.caja_asignada}')