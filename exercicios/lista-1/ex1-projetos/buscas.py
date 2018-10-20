# -*- coding: utf-8 -*-

from grafo import Grafo
from vertice import Vertice
import heapq

def encontrar_caminho_projetos(grafo, primeiro_projeto):
    # todos os vértices no grafo
    vertices = grafo.vertices()

    # marca todo mundo como falso... 
    # Complexidade: O(n), sendo n o número de vértices
    for vertice in vertices:
        vertice.marcado = False

    # marco o primeiro elemento como visitado, já que ele será o vértice
    # de início
    primeiro_projeto.marcado = True

    # cria a fila auxiliar já com o primeiro vértice
    fila = [primeiro_projeto]
    
    # lista final que conterá a ordem que os elementos foram visitados
    resultado = []
    
    # enquanto não for uma lista vazia...
    # Complexidade: O(n), sendo n o número de vértices do grafo
    while len(fila) != 0:
        # retiro o primeiro da fila
        vertice = fila.pop(0)
        # adiciono esse elemento como primeira descoberta
        resultado.append(vertice)
        # removo ele de todos os vértices, já que ele foi descoberto
        vertices.remove(vertice)
        # obtem a lista de sucessores do vértice atual
        sucessores = vertice.sucessores()
        
        # Remove a dependencia que existem entre os sucessores deste vértices,
        # ou seja, ele "não é mais um antecessor" necessário para que o sucessor
        # possa ser descoberto (já que o próprio acaba de ser visitado)
        # -------
        # Lembrando que a lista de antecessores de um determinado vértice são aqueles 
        # que precisam ser explorados antes que esse determinado vértice seja
        # também explorado
        # --------
        # Complexidade: O(m), sendo m o número de sucessores
        for sucessor in sucessores:
            sucessor.remove_antecessor(vertice)

        # aplica o heapify nos sucessores, para que sempre fique no topo do heap 
        # o vértice que contém o menor número de sucessores (geralmente zero)
        heapq.heapify(sucessores)

        # percorre todos os sucessores, do que possui menos dependentes até o maior
        while len(sucessores) != 0:
            # recebe o primeiro sucessor 
            atual = sucessores.pop(0)
            if not atual.marcado:
                # marca o vértice atual e adiciona ele na fila de descobertas
                atual.marcado = True
                fila.append(atual)

                

    
    # se a lista de vértices estiver vazia, quer dizer que todos foram alcançáveis. 
    # Esse caso engloba também o fato de que o grafo pode ser desconexo.
    if len(vertices) == 0:
        return resultado
    else:
        raise Exception("Não há soluções para este problema.")
        
