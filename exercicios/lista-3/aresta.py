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
    
    def origem(self):
        return self.__origem
    
    def destino(self):
        return self.__destino
