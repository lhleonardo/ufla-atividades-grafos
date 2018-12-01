class Vertice:
    def __init__(self, nome, is_sorvedouro = False, is_fonte = False):
        self.__nome = nome
        self.__is_sorvedouro = is_sorvedouro
        self.__is_fonte = is_fonte

    def nome(self):
        return self.__nome

    def is_fonte(self):
        return self.__is_fonte
    
    def is_sorvedouro(self):
        return self.__is_sorvedouro
    
    def __repr__(self):
        return "{}".format(self.__nome)