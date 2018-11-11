from grafo import GrafoPonderado
from trecho import Trecho
import sys

def extrairProximaCidade(lista):
    menor = lista[0]
    for i in lista :
        if int(i.distancia) < int(menor.distancia):
            menor = i
    lista.remove(menor)
    return menor

def melhoraHorario (atual,trechos,origem):
    menor = Trecho(2500,2500)
    for i in trechos :
        if i < menor and int(i.horaChegada()) < int(origem.distancia) and int(atual.distancia) <= int(i.horaSaida()):
            menor = i
            origem.distancia = menor.horaChegada()
            origem.pai = atual
    
def procura_percurso(grafo, origem, destino, horaSaida): 
    cidades = grafo.map().keys()
    cidades = list(cidades)
    mapeamento = grafo.map()
    
    for cidade in cidades:
        cidade.pai = None
        cidade.distancia = sys.maxsize
        
    origem.distancia = 0
    origem.pai = None
    S = []
    Q = cidades
    while len(Q) > 0 :
         u = extrairProximaCidade (Q)
         S.append(u)
         for vizinho in mapeamento[u].keys() :
             melhoraHorario (u, mapeamento[u][vizinho], vizinho)
             
    return "{0}-{1}".format(origem.distancia, destino.distancia)
            