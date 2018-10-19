# -*- coding: utf-8 -*-

from vertice import Vertice
from grafo import Grafo

from buscarProjeto import encontrar_caminho_projetos


def main():
    nome_arquivo = input("Digite o nome do arquivo:")
    # arquivo para leitura
    arquivo = open(nome_arquivo, "r")
    
    quantidade = int(arquivo.readline())

    grafo = Grafo()

    # salva os objetos criados para economizar espaco e utilizá-los
    # na criação das arestas
    vertices_criados = {}

    for i in range(1, quantidade + 1):
        vertices_criados[i] = Vertice(i)
        grafo.adiciona_vertice(vertices_criados[i])

    for leitura in arquivo:
        if not leitura:
            break
        
        # separa dois valores pelo espaco
        valores_vertices = leitura.split()
        v1 = vertices_criados[int(valores_vertices[0])]
        v2 = vertices_criados[int(valores_vertices[1])]

        grafo.adiciona_aresta(v1, v2)

    grafo.imprime_vertices()
main()