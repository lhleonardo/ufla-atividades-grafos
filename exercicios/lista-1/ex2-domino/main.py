# -*- coding: utf-8 -*-
from grafo import Grafo

from busca import verifica_sequencia

if __name__ == "__main__":
    grafo = Grafo()
    
    # nome_arquivo = input("Digite o caminho para o arquivo: ")
    nome_arquivo = "/home/lhleonardo/Área de Trabalho/atividades-grafos/exercicios/lista-1/ex2-domino/arquivo.txt"
    arquivo = open(nome_arquivo, "r")    
    
    quantidade = int(arquivo.readline())
    
    for i in range(1, 7):
        grafo.adiciona_vertice(i)


    for linha in arquivo:
        linha = linha.split()
        
        u = int(linha[0])
        v = int(linha[1])
        
        grafo.adiciona_aresta(u, v)
    
    try:
        resultado = verifica_sequencia(grafo)
        
        indice = 0
        print("Sequência de peças: ", end="")
        while indice < len(resultado) - 1:
            print("(", end="")
            print(resultado[indice], "-", resultado[indice + 1], end="")
            print(")", end="")
            if indice is not (len(resultado) - 2):
                print(" -> ", end="")
            indice = indice + 1
        print()
    except Exception as ex:
        print(ex)
