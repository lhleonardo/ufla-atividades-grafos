from grafo import GrafoPonderado
from floyd_warshall import FloydWarshall

def verifica_distancias(d1, d2, x, y):
    if d1 is None or d2 is None:
        if d1 is None and x == 0:
            d1 = 0
        else:
            return False
    
    temp = d1 * x + y

    return temp >= d2

def montar_grafo(qtd_vertices, arquivo):
    g = GrafoPonderado(qtd_vertices)

    for i in range(qtd_vertices):
        leitura = arquivo.readline().split()
        atual = int(leitura[0])

        del leitura[0]

        for j in leitura:
            temp = int(j)
            # o peso de ir de uma rua para outra é 1, 
            # mas qualquer valor fixo aqui funcionará.
            g.adiciona_aresta(atual, temp, 1)

    return g

def verifica_ruas_equivalentes(antigo, novo, multiplicador, independente):
    for i in antigo:
        for j in antigo:
            d_original = antigo[i][j]
            d_atualizada = novo[i][j]
            if not verifica_distancias(d_original, d_atualizada, multiplicador, independente):
                return False
    
    return True

if __name__ == "__main__":
    nome_arq = input("Digite o arquivo com dados:")
    arquivo = open(nome_arq, "r")

    qtd_vertices = int(arquivo.readline())

    grafo_original = montar_grafo(qtd_vertices, arquivo)
    grafo_atualizado = montar_grafo(qtd_vertices, arquivo)

    distancias_base = FloydWarshall(grafo_original)
    distancias_nova = FloydWarshall(grafo_atualizado)

    leitura = arquivo.readline().split()
    x = int(leitura[0])
    y = int(leitura[1])

    arquivo.close()

    if verifica_ruas_equivalentes(distancias_base, distancias_nova, x, y):
        print ("Sim")
    else:
        print ("Não")
