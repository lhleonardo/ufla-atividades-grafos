# -*- coding: utf-8 -*-

from vertice import Vertice
from grafo import Grafo

def main():
    quantidade = int(input("Digite o número de arestas: "))

    grafo = Grafo()

    for i in range(quantidade):
        v1 = Vertice(int(input("")))
        v2 = Vertice(int(input("")))

        if not grafo.existe_vertice(v1):
            grafo.adiciona_vertice(v1)
        
        if not grafo.existe_vertice(v2):
            grafo.adiciona_vertice(v2)

        grafo.adiciona_aresta(v1, v2)

    print(grafo)
main()