from vertice import Vertice

class Aresta:
    def __init__(self, origem, destino, peso = 0):
        if not isinstance(origem, Vertice) or not isinstance(destino, Vertice):
            raise ValueError("A origem e destino da aresta devem ser vértices.")
        
        self.__origem = origem
        self.__destino = destino

        self.peso = peso

        # para controlar o fluxo que "volta" da aresta
        # utilizado no caminho aumentante
        self.fluxo = 0

        # aresta de retorno para definir qual é a aresta subsequente 
        # ao grafo, ou seja, a que representa aresta do fluxo
        self.__retorno = None
    
    def origem(self):
        return self.__origem
    
    def destino(self):
        return self.__destino

    def retorno(self):
        return self.__retorno

    def set_retorno(self, aresta):
        if not isinstance(aresta, Aresta):
            raise ValueError("A aresta de retorno precisa ser uma instância da classe Aresta.")

        self.__retorno = aresta
    
    def __repr__(self):
        return "[{0}-{1}||{2}-{3}]".format(self.__origem, self.__destino, self.peso, self.fluxo)