from vecindad1 import Vecindad1
from vecindad2 import Vecindad2
from poblacion import Poblacion

if __name__ == '__main__':
   persona1 = Vecindad1()
   persona1.insertar("Alejandra","100",20,"101") #Si
   persona2 = Vecindad2()
   persona2.insertar("Diego","101",21,"100") #Si
   persona3 = Vecindad1()
   persona3.insertar("Daniel","102",19,"103") #No
   persona4 = Vecindad2()
   persona4.insertar("Vanessa","103",40,"102") #No
   persona5 = Vecindad1()
   persona5.insertar("O","104",19,"105") #No
   persona6 = Vecindad1()
   persona6.insertar("A","105",19,"104") #No
   persona7 = Vecindad1()
   persona7.insertar("x","106",20,"107") #Si
   persona8 = Vecindad2()
   persona8.insertar("y","107",20,"106") #Si
   persona9 = Vecindad1()
   persona9.insertar("z","108",20,"109")
   persona10 = Vecindad2()
   persona10.insertar("c","109",20,"108")
   prueba_parejas =  Poblacion()
   prueba_parejas.insertar(persona1,persona2)
   prueba_parejas.insertar(persona3,persona4)
   prueba_parejas.insertar(persona5,persona6)
   prueba_parejas.insertar(persona7,persona8)
   prueba_parejas.insertar(persona9,persona10)
   prueba_parejas.imprimir()
   prueba_parejas.eliminar("107")
   prueba_parejas.imprimir()