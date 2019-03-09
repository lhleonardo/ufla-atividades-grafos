from math import ceil
from math import hypot

class Cliente(object):
    def __init__(self, v, valor, qtdPacotes, coordX, coordY):
        self.volume = v
        self.__valor = valor
        self.pacotes = qtdPacotes
        self.__coordX = coordX
        self.__coordY = coordY
        self.centro = False
        self.soma_distancias = 0

    def getValor(self):
        return self.__valor

    def getX(self):
        return self.__coordX  

    def getY(self):
        return self.__coordY 

    def __repr__(self):
        if self.centro:
            return "({0}, {1}, {2}, {3})".format(ceil(self.__coordX), ceil(self.__coordY), ceil(self.volume), self.pacotes)
        else:    
            return "({0}, {1})".format(ceil(self.__coordX), ceil(self.__coordY))
