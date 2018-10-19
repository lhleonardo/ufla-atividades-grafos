# -*- coding: utf-8 -*-

import heapq

class Vertice:
    def __init__(self, chave, antecessores = None, sucessores = None):
        if (antecessores == None):
            antecessores = []

        if (sucessores == None):
            sucessores = []

        self.__chave = chave
        self.__antecessores = antecessores
        self.__sucessores = sucessores
    
    def adiciona_antecessor(self, vertice):
        if isinstance(vertice, Vertice):
            self.__antecessores.append(vertice)

    def adiciona_sucessor(self, vertice): 
        if isinstance(vertice, Vertice):
            self.__sucessores.append(vertice)

    def antecessores(self):
        return self.__antecessores

    def sucessores(self):
        return self.__sucessores

    def __repr__(self):
        return "{0}".format(self.__chave)

    def __lt__(self, outro):
        return len(self.__antecessores) < len(outro.__antecessores)