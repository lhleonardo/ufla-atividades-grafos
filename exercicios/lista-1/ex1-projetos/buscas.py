# -*- coding: utf-8 -*-

from grafo import Grafo
from vertice import Vertice
import heapq

"""
    Busca em largura utilizada para encontrar o percurso entre etapas de um projeto.
    
    Esse percurso tem que passar por todas as etapas possíveis, em 
    correta ordem de descoberta.

    Parâmetros:
        1) grafo: grafo qualquer contendo o mapeamento das 
                etapas do projeto
        2) primeiro_projeto: primeiro projeto informado, 
                utilizado como início do percurso
    
    Retorno: Lista contendo as etapas, em sua correta ordem de 
        descoberta.
    
    Erros:
        1) RuntimeError: caso não seja encontrado um percurso 
            que passe por todas as etapas presentes
"""
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
    
    # Remove a dependencia que existem entre os sucessores deste vértices,
    # ou seja, ele "não é mais um antecessor" necessário para que o sucessor
    # possa ser descoberto (já que o próprio acaba de ser visitado)
    # -------
    # Lembrando que a lista de antecessores de um determinado vértice são aqueles 
    # que precisam ser explorados antes que esse determinado vértice seja
    # também explorado
    # --------
    # Complexidade: O(m), sendo m o número de sucessores
    primeiro_projeto.remove_dependencia_dos_sucessores()

    # cria a fila auxiliar já com o primeiro vértice
    fila = [primeiro_projeto]
    
    # lista final que conterá a ordem que os elementos foram visitados
    resultado = []
    
    # enquanto não for uma lista vazia...
    # Complexidade: O(n), sendo n o número de vértices do grafo
    while len(fila) != 0:
        # retiro o primeiro da fila
        vertice = fila.pop(0)
        vertice.marcado = True
        
        # adiciona esse elemento na fila de descobertas
        resultado.append(vertice)
        
        # removo ele da lista de vértices não descobertos
        vertices.remove(vertice)
        
        # obtem a lista de sucessores do vértice atual
        # ordenada a partir de quem devo fazer a descoberta primeiramente
        sucessores = vertice.sucessores()

        # percorre todos os sucessores, do que possui menos dependentes até o maior
        while len(sucessores) != 0:
            # recebe o primeiro sucessor 
            atual = sucessores.pop(0)

            if not atual.marcado and len(atual.antecessores()) == 0:
                # marca o vértice atual e adiciona ele na fila de descobertas
                atual.marcado = True
                atual.remove_dependencia_dos_sucessores()
                fila.append(atual)
                
    # se a lista de vértices estiver vazia, quer dizer que todos foram alcançáveis. 
    # Esse caso engloba também o fato de que o grafo pode ser desconexo.
    if len(vertices) == 0:
        return resultado
    else:
        raise Exception("Não há soluções para este problema.")
