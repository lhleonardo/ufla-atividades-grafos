# -*- coding: utf-8 -*-

import heapq

"""
    Classe responsável por representar um determinado vértice presente
    no grafo. Cada vértice possuirá seu valor, seu conjunto de antecessores
    e sucessores. 

    Os antecessores de um determinado vértice são aqueles que estão diretamente
    relacionados com o atual. 

    Por exemplo: 
        Seja o grafo G=([1, 2, 3, 4], [{1-2}, {3-2}, {2-4}]), os sucessores e 
        antecessores dos vértices são, respectivamente: 
                    Vértice | ANTECESSORES | SUCESSORES
                        1   |      []      |      [2]
                        2   |    [1, 3]    |      [4]
                        3   |      []      |      [2]
                        4   |      [2]     |      [ ]

"""
class Vertice:
    """
        Construtor padrão que recebe a chave e os antecessores/sucessores
    """
    def __init__(self, chave, antecessores = None, sucessores = None):
        if (antecessores == None):
            antecessores = []

        if (sucessores == None):
            sucessores = []

        self.__chave = chave
        self.__antecessores = antecessores
        self.__sucessores = sucessores
    
    """
        Adiciona um antecessor à lista de antecessores de um vértice
    """
    def adiciona_antecessor(self, vertice):
        if isinstance(vertice, Vertice):
            self.__antecessores.append(vertice)

    """
        Adiciona um sucessor à lista de sucessores de um vértice
    """
    def adiciona_sucessor(self, vertice): 
        if isinstance(vertice, Vertice):
            self.__sucessores.append(vertice)

    """
        Remove um antecessor da lista de antecessores de um vértice
    """
    def remove_antecessor(self, antecessor):
        if antecessor in self.__antecessores:
            self.__antecessores.remove(antecessor)

    def remove_dependencia_dos_sucessores(self):
        for sucessor in self.__sucessores:
            sucessor.remove_antecessor(self)

    """
        Retorna todos os antecessores de um vértice
    """
    def antecessores(self):
        return self.__antecessores

    """
        Retorna todos os sucessores de um vértice
    """
    def sucessores(self):
        sucessores = self.__sucessores

        i = 0
        while(i < len(sucessores) - 1):
            if len(sucessores[i].antecessores()) > len(sucessores[i].antecessores()):
                sucessores[i], sucessores[i+1] = sucessores[i+1], sucessores[i]
            i = i + 1
        return sucessores

    """
        Modificada a representação de um vértice (mostrando apenas seu valor)
    """
    def __repr__(self):
        return "{0}".format(self.__chave, self.__antecessores, self.__sucessores)


    """
        Comparador especial entre vértices. 
        
        Principal motivo de implementação define-se para utilização
        de critério das comparações realizadas no procedimento heapify.

        Faz com que os elementos que possuem menos dependentes são priorizados
    """
    def __lt__(self, outro):
        if outro in self.__antecessores:
            return False
        elif self in outro.__antecessores:
            return True
        else:
            return len(self.__antecessores) < len(outro.__antecessores)