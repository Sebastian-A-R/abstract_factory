from abc import ABCMeta, abstractmethod

class Triangulo:
    __metaclass__ = ABCMeta

    def __init__(self, ladoA, ladoB, ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC
    
    @abstractmethod
    def getDescripcion(self):
        pass

    @abstractmethod
    def getSuperficie(self):
        pass


    @property
    def ladoA(self):
        return self.ladoA

    @ladoA.setter
    def ladoA(self, valor):
        self._ladoA = valor

    @property
    def ladoB(self):
        return self.ladoB

    @ladoB.setter
    def ladoB(self, valor):
        self._ladoB = valor

    @property
    def ladoC(self):
        return self.ladoC

    @ladoC.setter
    def ladoC(self, valor):
        self._ladoC = valor

  