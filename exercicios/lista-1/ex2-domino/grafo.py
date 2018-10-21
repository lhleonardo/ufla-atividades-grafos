# -*- coding: utf-8 -*-

"""
    Representação simples de um grafo, utilizando dicionário
    para mapeamento de suas arestas
"""
class Grafo:
    def __init__(self):
        self.vertices = []
        self.arestas = {}

    def __iter__(self):
        return iter(self.vertices)

    def adjacentes(self, vertice):
        return self.arestas[vertice]

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
        