from supermercado import Supermercado
#Pruebas
if __name__ == '__main__':
    supermercado = Supermercado()
    supermercado.insertar("Alejandra",10)
    supermercado.insertar("Diego",11)
    supermercado.insertar("Vanessa",6)
    supermercado.insertar("Daniel",7)
    supermercado.imprimir()
    supermercado.cajero_mas_rapido()
    supermercado.eliminar()
    supermercado.imprimir()