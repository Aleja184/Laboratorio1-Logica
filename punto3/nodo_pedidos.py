class Nodo_Pedidos:
    def __init__(self,id_pedido,caja_asignada):
        self.id_pedido = id_pedido
        self.caja_asignada = caja_asignada
        self.siguiente = None
        self.anterior = None