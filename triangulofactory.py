from triangulofactorymethod import TrianguloFactoryMethod
from equilatero import Equilatero
from isosceles import Isosceles
from escaleno import Escaleno

class TrianguloFactory(TrianguloFactoryMethod):

    
    def createTriangulo(self,ladoA, ladoB, ladoC):
        if ((ladoA == ladoB) and (ladoA == ladoC)):
            return Equilatero(ladoA,ladoB,ladoC)
        elif ((ladoA != ladoB)and(ladoA != ladoC)and(ladoB != ladoC)):
            return Escaleno(ladoA,ladoB,ladoC)
        else:
            return Isosceles(ladoA,ladoB,ladoC)
    