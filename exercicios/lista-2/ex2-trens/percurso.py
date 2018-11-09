from grafo import GrafoPonderado
import sys

def extrairProximaCidade(lista):
    menor = lista[0]
    for i in lista :
        if i.distancia < menor.distancia:
            menor = i
    lista.remove(menor)
    return menor

def melhoraHorario (atual,trechos,origem):
    menor = Trecho(2500,2500)
    for i in trechos :
        if i < menor and int(i.horaChegada()) < int(atual.distancia):
            menor = i
            atual.distancia = menor.horaChegada()
            atual.pai = origem
    
def procura_percurso(grafo, origem, destino, horaSaida): 
    cidades = grafo.map().keys()
    mapeamento = grafo.map()
    
    for cidade in cidades:
        cidade.pai = None
        cidade.distancia = sys.maxsize
        
    origem.distancia = 0
    S = []
    Q = cidades
    while len(q) > 0 :
         u = extrairProximaCidade (Q)
         S.append(u)
         for vizinho in mapeamento[u].keys() :
             melhoraHorario (u, mapemanto[u][vizinho], vizinho)
             
    return "{0}-{1}".format(origem.horaSaida(), destino.horaChegada())
            
