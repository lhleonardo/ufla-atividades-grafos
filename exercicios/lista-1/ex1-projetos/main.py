# -*- coding: utf-8 -*-

from vertice import Vertice
from grafo import Grafo

def main():
    quantidade = int(input("Digite o número de vértices: "))

    grafo = Grafo()

    # salva os objetos criados para economizar espaco e utilizá-los
    # na criação das arestas
    vertices_criados = {}

    for i in range(1, quantidade + 1):
        vertices_criados[i] = Vertice(i)
        grafo.adiciona_vertice(vertices_criados[i])

    print (vertices_criados)

    while True:
        leitura = input("")
        
        if not leitura:
            break
        
        # separa dois valores pelo espaco
        valores_vertices = leitura.split()
        v1 = vertices_criados[int(valores_vertices[0])]
        v2 = vertices_criados[int(valores_vertices[1])]

        grafo.adiciona_aresta(v1, v2)

    grafo.imprime_vertices()
main()