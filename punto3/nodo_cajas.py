#Nodo para cada caja que recibe como parametro el código de seguridad de cada una
class Nodo_Cajas:
    def __init__(self,codigo_seguridad):
        self.codigo_seguridad = codigo_seguridad
        self.siguiente = None