# -*- coding: utf-8 -*-

from vertice import Vertice
from grafo import Grafo

from buscas import encontrar_caminho_projetos


def main():
    # nome_arquivo = input("Digite o nome do arquivo:")
    nome_arquivo = "/home/lhleonardo/arquivo.txt"
    # arquivo para leitura
    arquivo = open(nome_arquivo, "r")
    
    quantidade = int(arquivo.readline())

    grafo = Grafo()

    # salva os objetos criados para economizar espaco e utilizá-los
    # na criação das arestas
    vertices_criados = {}
    primeiro_vertice = Vertice(1)
    vertices_criados[1] = primeiro_vertice
    grafo.adiciona_vertice(primeiro_vertice)

    for i in range(2, quantidade + 1):
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

    try:
        resultado = encontrar_caminho_projetos(grafo, primeiro_vertice)
        print("A solução para este problema é: ", resultado)
    except Exception as ex:
        print(ex)
    

    
main()