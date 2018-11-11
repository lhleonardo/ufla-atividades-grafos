class Estacao(object):

    def __init__(self, nome):
        self.__nome = nome

    def __eq__(self, outra):
        return self.__nome == outra.__nome

    def __hash__(self):
        return hash(self.__nome)