from grafo import GrafoPonderado

def extrair_peso(matriz, v1, v2):
    temp = matriz.get(v1, None)

    if temp is None:
        return None
    
    temp = temp.get(v2, None)

    return temp

def somar_distancias(d_v1, d_v2):
    if d_v1 is None or d_v2 is None:
        return None
    
    return d_v1 + d_v2

def melhorar_distancia(d_v1, d_v2):
    if d_v1 is None and d_v2 is not None:
        return True
    
    if d_v2 is None:
        return False
    
    return d_v1 > d_v2

def FloydWarshall(grafo):
    pesos = grafo.map()

    qtd_vertices = grafo.qtd_vertices()

    for k in pesos:
        for j in pesos:
            for i in pesos:
                d_ik = extrair_peso(pesos, i, k)
                d_kj = extrair_peso(pesos, k, j)
                d_ij = extrair_peso(pesos, i, j)
                temp = somar_distancias(d_ik, d_kj)

                if melhorar_distancia(d_ij, temp):
                    pesos[i][j] = temp                    

    return pesos