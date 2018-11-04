from grafo import GrafoPonderado

"""
    Função auxiliar que obtem o peso na matriz de pesos.
    No Floyd-Warshall, quando um vértice e outro não são
    acessíveis, é representado pelo simbolo de Infinito. 
    Neste caso, infinito é None
"""
def extrair_peso(matriz, v1, v2):
    # pega o primeiro dicionario, do vertice de saida
    temp = matriz.get(v1, None)

    # verifica se esse vertice nao foi mapeado
    if temp is None:
        return None
    
    # caso tenha mapeamento, acesse o segundo valor dentro
    # do dicionario presente no primeiro acesso
    temp = temp.get(v2, None)

    return temp

"""
    Somar duas distâncias, fazendo o tratamento
    de somar alguma coisa com infinito (None). 
    Caso isso aconteça, infinito deverá ser o 
    resultado, que consequentemente é None
"""
def somar_distancias(d_v1, d_v2):
    if d_v1 is None or d_v2 is None:
        return None
    
    return d_v1 + d_v2

"""
    Verifica se a distância de v1 pode ser melhorada
    utilizando v2. Quando a distancia de v1 é infinito, 
    considera que v1 é maior que v2 (caso não seja infinito)
"""
def pode_melhorar_distancia(d_v1, d_v2):
    if d_v1 is None and d_v2 is not None:
        return True
    
    if d_v2 is None:
        return False
    
    return d_v1 > d_v2

"""
    Implementação padrão do algoritmo de Floyd-Warshall, que encontra
    o melhor caminho de todos os vértices com destino a todos, incluindo
    seus respectivos sub-caminhos, de forma dinâmica.
"""
def FloydWarshall(grafo):
    pesos = grafo.map()

    qtd_vertices = grafo.qtd_vertices()

    for k in pesos:
        for j in pesos:
            for i in pesos:
                # Distancia de v[i] + v[k]
                d_ik = extrair_peso(pesos, i, k)
                # Distancia de v[k] + v[j]
                d_kj = extrair_peso(pesos, k, j)
                # Distancia de v[i] + v[i]
                d_ij = extrair_peso(pesos, i, j)
                # soma das possíveis distancias existentes, tratando
                # ocorrencias de distâncias infinitas
                temp = somar_distancias(d_ik, d_kj)

                # se a distância D[i][j] for maior que a presente com
                # o vértice intermediário, deverá ser melhorada.
                if pode_melhorar_distancia(d_ij, temp):
                    pesos[i][j] = temp                    

    return pesos