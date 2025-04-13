from nodo_poblacion import NodoP
from vecindad1 import Vecindad1
from vecindad2 import Vecindad2

class Poblacion: 
    def __init__(self):
        self.cabecera = None

    def insertar(self,persona1,persona2):
        nodo_nuevo = None
        nodo_nuevo2 = None
        if ((isinstance(persona1,Vecindad1) and isinstance(persona2,Vecindad2)) or (isinstance(persona2,Vecindad1) and isinstance(persona1,Vecindad2))) and ((persona1.imc>=19 and persona1.imc<25)and(persona2.imc>=19 and persona2.imc<25)):
                nodo_nuevo = NodoP(persona1)
                nodo_nuevo2 = NodoP(persona2)
        else:
            print("La pareja debe estar conformada por una persona de la vecindad 1 y una persona de la vecindad 2, y de cada uno su imc debe ser >=19 y <25")
            return
        if self.cabecera == None:
            self.cabecera = nodo_nuevo
            self.cabecera.siguiente = nodo_nuevo2
            nodo_nuevo2.anterior = self.cabecera
        else:
            nodo_actual = self.cabecera
            while nodo_actual.siguiente != None:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nodo_nuevo
            nodo_nuevo.anterior = nodo_actual
            nodo_nuevo.siguiente = nodo_nuevo2
            nodo_nuevo2.anterior = nodo_nuevo


    def eliminar(self,id):
        if self.cabecera.persona.id == id:
            nodo_siguiente_pareja = self.cabecera.siguiente.siguiente 
            self.cabecera = nodo_siguiente_pareja
            return 
        nodo_actual = self.cabecera
        pareja_id = None
        while nodo_actual.persona.id != id:
            nodo_actual = nodo_actual.siguiente
        if nodo_actual.siguiente == None:
            nodo_anterior = nodo_actual.anterior
            nodo_anterior.siguiente = None
        else:
            nodo_anterior = nodo_actual.anterior
            nodo_siguiente = nodo_actual.siguiente
            nodo_anterior.siguiente = nodo_siguiente
            nodo_siguiente.anterior = nodo_anterior
        pareja_id = nodo_actual.persona.pareja_id
        nodo_actual = self.cabecera
        while nodo_actual.persona.id != pareja_id:
            nodo_actual = nodo_actual.siguiente
        if nodo_actual.siguiente == None:
            nodo_anterior = nodo_actual.anterior
            nodo_anterior.siguiente = None
        else:
            nodo_anterior = nodo_actual.anterior
            nodo_siguiente = nodo_actual.siguiente
            nodo_anterior.siguiente = nodo_siguiente
            nodo_siguiente.anterior = nodo_anterior

    def imprimir(self):
        nodo_actual = self.cabecera
        while nodo_actual.siguiente != None:
            if nodo_actual == self.cabecera:
                print(f"{nodo_actual.persona.nombre} ->")
            else:
                print(f"<-{nodo_actual.persona.nombre}->")
            nodo_actual = nodo_actual.siguiente
        print(f"<-{nodo_actual.persona.nombre}")