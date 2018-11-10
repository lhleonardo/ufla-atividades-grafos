from percurso import procura_percurso
from grafo import GrafoPonderado
from trecho import Trecho
from estacao import Estacao

def main():
    grafo = GrafoPonderado()
    """
        Dicionario para guardar as estações mapeadas pelo seu nome
    """
    estacoes = {}
    
    qtdCidades = int(input("Quantidade cidades: "))
    
    for i in range(qtdCidades):
        nome = input("Estação {}: ".format(i))
        estacao = Estacao(nome)

        estacoes[nome] = estacao

        grafo.adiciona_estacao(estacao)
    
    qtdTrens = int(input("Quantidade de trens: "))
    
    for i in range(qtdTrens):        
        hora1 = input("Hora de saida")
        nomeEstacao1 = input("Estação de saida: ")
        estacao1 = estacoes[nomeEstacao1]

        hora2 = input("Hora de chegada")
        nomeEstacao2 = input("Estação de chegada: ")
        estacao2 = estacoes[nomeEstacao2]


        grafo.adiciona_trecho(estacao1, estacao2, Trecho(hora2, hora1))
    
    
    horaPassageiro = input("Horario que o passageiro sai: ")
    origem = input("Estação de origem: ")
    destino = input("Estação de destino: ")
    
    print(procura_percurso(grafo, origem, destino, horaPassageiro))

if __name__ == "__main__":
    main()
