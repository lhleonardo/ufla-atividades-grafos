# -*- coding: utf-8 -*-
from grafo import Grafo

from busca import verifica_sequencia

if __name__ == "__main__":
    grafo = Grafo()

    grafo.adiciona_vertice(1)
    grafo.adiciona_vertice(2)
    grafo.adiciona_vertice(3)
    grafo.adiciona_vertice(4)
    grafo.adiciona_vertice(5)

    grafo.adiciona_aresta(2, 1)
    grafo.adiciona_aresta(2, 2)
    grafo.adiciona_aresta(3, 1)
    grafo.adiciona_aresta(3, 4)
    grafo.adiciona_aresta(2, 4)
    
    try:
        print(verifica_sequencia(grafo))
    except Exception as ex:
        print(ex)
