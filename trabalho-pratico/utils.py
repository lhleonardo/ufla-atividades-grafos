import matplotlib.pyplot as a
import matplotlib as mpl
import networkx as nx

import math

def converter_para_grafo_completo(regioes):
    # transforma em grafo completo
    for centro in regioes.keys():
        # pega os clientes do centro
        grafo = regioes[centro]
        clientes_adjacentes = list(grafo.nodes())

        for u in clientes_adjacentes:
            for v in clientes_adjacentes:
                if not grafo.has_edge(u, v) and not grafo.has_edge(v, u) and u is not v:
                    grafo.add_edge(u, v, distancia=distancia(u, v))

def imprime_grafo_simples(grafo, nome_arquivo, limite):
    centros = [x for x in grafo.nodes() if x.centro is True]
    
    mpl.rc("axes", edgecolor="blue")
    a.plot([x.getX() for x in centros], [x.getY() for x in centros], "bo")

    mapeamento_x = []
    mapeamento_y = []

    for vertice in grafo.nodes():
        if vertice not in centros:
            mapeamento_x.append(vertice.getX())
            mapeamento_y.append(vertice.getY())

    a.plot(mapeamento_x, mapeamento_y, "ro")

    for (u, v) in grafo.edges():
        a.plot([u.getX(), v.getX()], [u.getY(), v.getY()], "--k")

    a.axis([0, limite, 0, limite])
    
    a.savefig(nome_arquivo)

def imprime_grafo(regioes, nome_arquivo, limite):
    a.clf()
    centros = list(regioes.keys())

    completo = nx.union(regioes[centros[0]], regioes[centros[1]])
    completo = nx.union(completo, regioes[centros[2]])
    completo = nx.union(completo, regioes[centros[3]])
    completo = nx.union(completo, regioes[centros[4]])

    mapeamento_x = []
    mapeamento_y = []

    for cliente in completo.nodes():
        if cliente not in centros:
            mapeamento_x.append(cliente.getX())
            mapeamento_y.append(cliente.getY())

    mpl.rc("axes", edgecolor="blue")
    a.plot(mapeamento_x, mapeamento_y, "ro")

    mapeamento_x = []
    mapeamento_y = []

    for centro in centros:
        mapeamento_x.append(centro.getX())
        mapeamento_y.append(centro.getY())

    a.plot(mapeamento_x, mapeamento_y, "bo")

    mapeamento_x = []
    mapeamento_y = []

    for centro in centros:
        for u, v in regioes[centro].edges():
            a.plot([u.getX(), v.getX()], [u.getY(), v.getY()], "--k")
    a.axis([0, limite, 0, limite])

    a.savefig(nome_arquivo)

def distancia(c1, c2):
    return math.sqrt(
        ((c2.getX() - c1.getX()) ** 2) +
        ((c2.getY() - c1.getY()) ** 2))