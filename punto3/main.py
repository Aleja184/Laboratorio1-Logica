from cajas import Cajas_Disponibles
from pedidos import Pedidos

if __name__ == '__main__':
    cajas = Cajas_Disponibles()
    cajas.insertar("1515")
    cajas.insertar("1010")
    cajas.insertar("2121")
    cajas.insertar("5656")
    cajas.insertar("7878")
    pedidos = Pedidos(cajas)
    pedidos.insertar()
    pedidos.insertar()
    pedidos.insertar()
    pedidos.imprimir()