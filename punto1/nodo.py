"""Nodo creado para cada persona.
#Los parametros que se deben enviar al nodo son el nombre de la persona, un id para identificarlo, su indice de masa corporal y 
#un id para identificar a su pareja(esto último con el objetivo de al momento de eliminar la pareja en la nueva población se tenga
certeza cuál es su pareja asociada)"""
class Nodo:
    def __init__(self,nombre,id,imc,pareja_id):
        self.nombre = nombre
        self.id = id
        self.imc = imc
        self.pareja_id = pareja_id
        self.siguiente = None