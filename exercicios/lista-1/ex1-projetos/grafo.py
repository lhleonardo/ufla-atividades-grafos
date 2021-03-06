# -*- coding: utf-8 -*-

from vertice import Vertice

class Grafo:
    def __init__(self):
        # mapeamento de todos os vértices e suas arestas
        self.__elementos = {}

    def adiciona_vertice(self, vertice):
        if not isinstance(vertice, Vertice):
            return

        if vertice not in self.__elementos:
            self.__elementos[vertice] = []

    def existe_vertice(self, vertice):
        return vertice in self.__elementos

    def adiciona_aresta(self, v1, v2):
        if not v1 in self.__elementos or not v2 in self.__elementos:
            raise Exception("Os vértices v1 e v2 precisam existir para que uma aresta seja criada.")
        
        self.__elementos[v1].append(v2)

        # faz a ligação para acesso em tempo constante
        v1.adiciona_sucessor(v2)
        v2.adiciona_antecessor(v1)
    
    def vertices(self):
        return list(self.__elementos.keys())
    
    def vizinhos_vertice(self, vertice):
        return self.__elementos[vertice]

    def __str__(self):
        return str(self.__elementos)

    def imprime(self):
        for chave in self.__elementos.keys():
            
            print("{0}, ant={1}, suc={2}".format(chave, chave.antecessores(), chave.sucessores()))
