# -*- coding: utf-8 -*-
import networkx as nx
import math 
import random
import copy

from utils import imprime_grafo, imprime_grafo_simples, distancia, converter_para_grafo_completo
from balanceamento import balanceamento_por_demanda, balanceamento_por_volume

from modelo.clientes import Cliente
from modelo.veiculo import Veiculo

from rotas import MontaCaminhos
        
def ler_cliente(x, y, volume, valor, pacotes,flag):
    return Cliente(volume, valor, pacotes, x, y)

def ler_veiculo(V, P, Nv, vf, vd, tc, td, ph, pkm, pf):
    return Veiculo(V, P, Nv, vf, vd, tc, td, ph, pkm, pf)

nome_arquivo = input("Informe o arquivo de entrada: ")

arquivo = open("docs/{0}".format(nome_arquivo), "r")

qtd_casas = int(arquivo.readline())
qtd_centros = int(arquivo.readline())
qtd_veiculos = int(arquivo.readline())
qtd_horas = int(arquivo.readline())

# para cada centro de distribuição, existe um grafo
regioes = {}

clientes = []
veiculos = []

for i in range(qtd_centros):
    leitura = arquivo.readline().split()
    cliente = ler_cliente(float(leitura[0]), float(leitura[1]), float(leitura[2]), float(leitura[3]), float(leitura[4]), True)
    cliente.centro = True
    cliente.maior_distancia = 0 - float("inf")

    regioes[cliente] = nx.Graph()
    regioes[cliente].add_node(cliente, pos = (cliente.getX(), cliente.getY()))

for i in range(qtd_casas - qtd_centros):
    leitura = arquivo.readline().split()
    clientes.append(ler_cliente(float(leitura[0]), float(leitura[1]), float(leitura[2]), float(leitura[3]), float(leitura[4]), False))

for i in range(qtd_veiculos):
    leitura = arquivo.readline().split()    
    veiculos.append(ler_veiculo(float(leitura[0]), float(leitura[1]), float(leitura[2]), float(leitura[3]),
    float(leitura[4]), float(leitura[5]), float(leitura[6]), float(leitura[7]), float(leitura[8]), float(leitura[9])))

volume_total = 0
distancia_total = 0

# definição a partir de proximidade
for cliente in clientes: 
    menor_centro = list(regioes.keys())[0]
    menor_distancia = distancia(cliente, menor_centro)
    
    for centro in regioes.keys():
        if (distancia(cliente, centro) < distancia(cliente, menor_centro)):
            menor_centro = centro
            menor_distancia = distancia(cliente, centro)

    regioes[menor_centro].add_node(cliente)
    regioes[menor_centro].add_edge(cliente, menor_centro, distancia=menor_distancia)
    menor_centro.volume += cliente.volume
    menor_centro.pacotes += cliente.pacotes
    
    menor_centro.soma_distancias += distancia(cliente, menor_centro)

    # encontra a maior distancia de cliente e centro
    if menor_centro.maior_distancia < menor_distancia:
        menor_centro.maior_distancia = menor_distancia

    volume_total += cliente.volume

imprime_grafo(regioes, "exibicao/{0}sem-melhoria.png".format(nome_arquivo), qtd_casas)

# etapas de balanceamento: por volume e logo após por demanda
balanceamento_por_volume(regioes, volume_total, qtd_centros)

balanceamento_por_demanda(regioes, qtd_casas, qtd_centros)

imprime_grafo(regioes, "exibicao/{0}com-melhoria.png".format(nome_arquivo), qtd_casas)

# transforma cada grafo dos centros de distribuição em grafos completos
converter_para_grafo_completo(regioes)

# grafos completos estão dentro de regioes {}
# lista de veículos estão dentro de veículos[]
veiculos_melhorados = {}

for centro in regioes.keys():
    volume_temp = centro.volume / volume_total

    veiculos_temp = [copy.copy(x) for x in veiculos]

    for veiculo in veiculos_temp:
        veiculo.Nv = math.floor(veiculo.Nv * volume_temp)

    veiculos_melhorados[centro] = veiculos_temp

grafo = nx.Graph()

total = 0
for regiao in regioes.keys():
    grafo.add_nodes_from(list(regioes[regiao].nodes()))

    resultado = MontaCaminhos(regioes[regiao],veiculos_melhorados[regiao])

    for caminho in resultado:

        soma_qtd_pacotes = 0
        km_percorrido = 0
        tempo_percorrido = 0
        veiculo_utilizado = None
        distancia_ctcasa = 0
        distancia_casact = 0
        tempo_carregamento = 0
        tempo_descarregamento = 0
        tempo_total = 0
        tempoInicial = 0
        tempoRota = 0

        for rota_temp in caminho.keys():
            rota, veiculo = caminho[rota_temp]
            veiculo_utilizado = veiculo
            
            for i in range(len(rota)-1):
                soma_qtd_pacotes += rota[i].pacotes
                
                valor = len(rota)-1

                if i == 0:
                    distancia_ctcasa = distancia(rota[0],rota[1])
                elif i == valor:
                    distancia_casact += distancia(rota[valor],rota[0])

                km_percorrido += distancia(rota[i], rota[i+1])
                grafo.add_edge(rota[i], rota[i+1], distancia=distancia(rota[i], rota[i+1]))


        soma_qtd_pacotes += rota[len(rota)-1].pacotes
        # print("Soma quantidade de pacotes",soma_qtd_pacotes)        
        tempo_carregamento += (soma_qtd_pacotes*veiculo_utilizado.tc)
        # print("Tempo td:", veiculo_utilizado.tc)
        tempo_descarregamento += (soma_qtd_pacotes*veiculo_utilizado.td)
        tempoInicial = (distancia_casact + distancia_ctcasa)/veiculo_utilizado.vf 
        tempoRota = km_percorrido/veiculo_utilizado.vd
        tempo_total = tempo_carregamento + tempo_descarregamento + tempoInicial + tempoRota
        # print("Tempo inicial: ", tempoInicial)
        # print("Tempo carregamento: ", tempo_carregamento)
        # print("Tempo descarregamento: ", tempo_descarregamento)
        # print("Tempo da rota: ", tempoRota)

        grafo.add_edge(rota[0], rota[len(rota)-1])

        custo_por_km = (km_percorrido+distancia_casact + distancia_ctcasa) * veiculo_utilizado.pkm
        custo_por_hr = tempo_total * veiculo_utilizado.ph
        custo_fixo = veiculo_utilizado.pf

        total_veiculo = custo_fixo + custo_por_hr + custo_por_km   
        # print("Tempo gasto: ", tempo_total)
        # print("Rota com veículo ", veiculo_utilizado, " gastou: ", total_veiculo)

        total += total_veiculo
# print("Total de gastos: ", total)

imprime_grafo_simples(grafo, "exibicao/rotas", qtd_casas)