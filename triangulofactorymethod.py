from abc import ABCMeta, abstractmethod

class TrianguloFactoryMethod:

    __metaclass__ = ABCMeta
    
    @abstractmethod
    def createTriangulo(self,ladoA,ladoB,ladoC):
        pass