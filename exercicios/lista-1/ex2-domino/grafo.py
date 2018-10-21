# -*- coding: utf-8 -*-

from random import shuffle

"""
    Representação simples de um grafo, utilizando dicionário
    para mapeamento de suas arestas
"""
class Grafo:
    def __init__(self):
        self.vertices = []
        self.arestas = {}

    # sobrecarga de operadores para comodidade
    def __getitem__(self, indice):
        return self.vertices[indice]

    def adjacentes(self, vertice):
        valores = self.arestas[vertice]
        # se houver uma aresta (vertice-vertice) em loop, ela deve
        # ser priorizada na descoberta, ou seja, adicionada no inicio
        # da lista de adjacentes retornada
        if len(valores) > 0:
            if vertice in valores:
                valores.remove(vertice)
                valores.insert(0, vertice)            
        
        return valores

    def adiciona_vertice(self, vertice):
        # não permite vértices duplicados
        if vertice not in self.vertices:
            self.vertices.append(vertice)
            # mapeamento vazio para um vértice que
            # acaba de ser adicionado
            self.arestas[vertice] = []

    """
        Faz a relação de uma aresta com outra, e vice-versa
    """
    def adiciona_aresta(self, v1, v2):
        # adiciona v2 em v1 no final da lista ou cria com
        # apenas este elemento (caso não exista)
        
        # e vice-versa
        self.arestas[v1] = self.arestas.get(v1, []) + [v2]
        self.arestas[v2] = self.arestas.get(v2, []) + [v1]

    def qtd_vertices(self):
        return len(self.vertices)

    def qtd_arestas(self):
        return sum(len(lista) for chave, lista in self.arestas.items()) // 2
    

    def is_euleriano(self):
        for vertice in self:
            if len(self.adjacentes(vertice)) % 2 == 1:
                return False
        
        return True
