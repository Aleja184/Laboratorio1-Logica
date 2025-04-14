#Nodo creado para la nueva población, donde solo se recibe como parametro a la persona
class NodoP:
    def __init__(self,persona):
        self.persona = persona
        self.siguiente = None
        self.anterior = None