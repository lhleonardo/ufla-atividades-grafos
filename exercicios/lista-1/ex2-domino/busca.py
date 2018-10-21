# -*- coding: utf-8 -*-
from itertools import chain

"""
    Verifica a sequência de peças do dominó com o algoritmo de Hierholzer.

    Para que aconteça o "match" das peças (a última peça se conecte com a primeira), 
    é necessário que o grafo seja exclusivamente euleriano (os graus de todos os vértices
    são pares). 

    Como o conjunto de peças é um ciclo euleriano, usa-se o algoritmo de Hierholzer 
    para encontrar o caminho deste ciclo, resultando no conjunto de peças em sua sequencia
"""
def verifica_sequencia(grafo):
    # se não for um ciclo euleriano, já cancela a instrução
    for vertice in grafo:
        if len(grafo.adjacentes(vertice)) % 2 == 1:
            raise RuntimeError("A solução não pode ser encontrada.")

    inicial = next(grafo.__iter__())
    resultado = [inicial]

    arestas = {}
    # variável para saber qual a posição do elemento que está 
    # na verificação dos ciclos, para realização da concatenação
    posicao = 0
    
    # repete enquanto houver vértices que não foram colocados no circuito
    # critério de parada: enquanto não for adicionada todas as arestas e também 
    # o indice de substituição da lista é válido (principalmente utilizado quando
    # o grafo é um Cn)
    while len(arestas) // 2 < grafo.qtd_arestas() and posicao < len(resultado):
        ciclo_interno = []
        # faz a descoberta de um ciclo de forma recursiva, utilizando
        # a ideia da visita em uma busca em profundidade, passando 
        # o nó inicial e atual, que de início serão os mesmos
        __verifica_sequencia_recursiva(grafo, resultado[posicao], resultado[posicao], ciclo_interno, arestas)
        
        # se foi encontrado um ciclo na chamada recursiva, adiciona ao resultado
        if len(ciclo_interno) != 0: 
            # concatenação de listas, colocando na frente da posição cont o subcaminho 
            # encontrado no ciclo  
            # resumo da operação:
            # resultado[:posicao+1] cria uma sublista com todos os elementos, incluindo o atual
            # onde esses são concatenados com ciclo_interno. Logo após, tudo que tinha depois da
            # posição do elemento atual é concatenado ao conteúdo gerado anteriormente
            resultado = list(chain(resultado[:posicao+1], ciclo_interno, resultado[posicao+1:]))
        
        posicao = posicao + 1

    return resultado

"""
    Consulta baseada na descoberta do DFS, com intenção de obter ciclo entre 
    os vértices. 

    Parâmetros: 
        1) grafo: 
                    Grafo euleriano de origem
        2) atual: 
                    Atual em descoberta recursiva
        3) inicio: 
                    Elemento inicial do ciclo ("cabeça" da lista circular). 
                    Utilizado como critério de parada
        4) ciclo_interno:
                    Representação dos elementos encontrados no ciclo descoberto pela 
                    busca em profundidade, a partir do "inicio"
        5) arestas:
                    Arestas mapeadas no ciclo
"""
def __verifica_sequencia_recursiva(grafo, atual, inicio, ciclo_interno, arestas):
    # percorre os adjacentes do vértice com intuito de encontrar ciclo
    for adj in grafo.adjacentes(atual):
        # se não existir uma aresta (inicial-adj) nos adjacentes, agora é adicionada
        # e inserida no ciclo
        if verifica_mapeamento(atual, adj, arestas):
            arestas[(atual, adj)] = True
            arestas[(adj, atual)] = True
            
            ciclo_interno.append(adj)
            
            # se não chegou ao vertice "inicio" do ciclo, deve continuar a procurar
            # elementos
            if adj != inicio:
                __verifica_sequencia_recursiva(grafo, adj, inicio, ciclo_interno, arestas)

"""
   Função auxiliar que verifica se um par de vértice (uma aresta entre esses dois)
   estão inseridas dentro do ciclo.
   
   Utilizada para visitar apenas a aresta que ainda não foi adicionada ao ciclo
"""
def verifica_mapeamento(atual, pai, adjacencia):
    return (atual,pai) not in adjacencia or (pai, atual) not in adjacencia
