# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "SPEEDMIND"
__date__ = "$05/06/2023 14:19:50$"

if __name__ == "__main__":
    import math
    class Tfigura:
        def __init__(self,base,altura):
            self.__base=base
            self.__altura=altura
        def setbase(self,base):
            self.__base=base
        def setaltura(self,altura):
            self.__altura=altura
        def getbase(self):
            return self.__base
        def getaltura(self):
            return self.__altura
        def hipotenusa(self):
            return 0
        def area(self):
            return 0
        def perimetro(self):
            return 0
    class Ttriangulo(Tfigura):
        def __init__(self,base,altura):
            super().__init__(base,altura)
        def hipotenusa(self):
            return math.sqrt((self.getbase()**2)+(self.getaltura()**2))
        def area(self):
            return (self.getbase()*self.getaltura())/2
        def perimetro(self):
            return self.getbase()+self.getaltura()+self.hipotenusa()
    class TRectangulo(Tfigura):
        def __init__(self,base,altura):
            super().__init__(base,altura)
        def area(self):
            return self.getbase()*self.getaltura()
        def perimetro(self):
            return 2*self.getbase()+2*self.getaltura()
    _base=int(input("Ingrese el valor de la base: "))
    _altura=int(input("Ingrese el valor de la altura: "))
    f=Tfigura(_base,_altura)
    t=Ttriangulo(_base,_altura)
    r=TRectangulo(_base,_altura)
    print("el area del triangulo es: ",t.area())
    print("el perimetro del triangulo es:",t.perimetro())
    print("la hipotenusa es: ",t.hipotenusa())
    print("el area del Rectangulo es: ",r.area())
    print("el perimetro del Rectangulo es:",r.perimetro())
    