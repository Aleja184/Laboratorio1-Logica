from nodo import Nodo

class Vecindad2:
    def __init__(self):
        self.cabecera = None
        self.ultimo_nodo = None
        self.nombre = None
        self.id = None
        self.pareja_id = None
        self.imc = None
    
    def insertar(self,nombre,id,imc,pareja_id):
        nodo_nuevo = Nodo(nombre,id,imc,pareja_id)
        self.nombre = nombre
        self.id = id
        self.pareja_id = pareja_id
        self.imc = imc
        if self.cabecera == None:
            self.cabecera = nodo_nuevo
            self.cabecera.siguiente = self.cabecera
        else:
            nodo_actual = self.cabecera
            while nodo_actual.siguiente != self.cabecera:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nodo_nuevo
            nodo_nuevo.siguiente = self.cabecera
            self.ultimo_nodo = nodo_nuevo
    
    def imprimir(self):
        if self.cabecera == None:
            print("Nodo vacío")
        else:
            nodo_actual = self.cabecera
            while nodo_actual.siguiente != self.cabecera:
                print(f"{nodo_actual.nombre}->")
                nodo_actual = nodo_actual.siguiente
            print(nodo_actual.nombre)
            print(nodo_actual.siguiente.nombre)
    
    def eliminar(self,id):
        if self.cabecera == None:
            print("Nodo vacío")
        elif self.cabecera.id is id:
            self.cabecera = self.cabecera.siguiente
            self.ultimo_nodo.siguiente = self.cabecera
        else:
            nodo_anterior = self.cabecera
            nodo_actual = self.cabecera
            while nodo_actual.id != id:
                nodo_anterior = nodo_actual
                nodo_actual = nodo_actual.siguiente
            nodo_anterior.siguiente = nodo_actual.siguiente