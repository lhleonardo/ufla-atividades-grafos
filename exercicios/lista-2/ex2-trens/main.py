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
    nome_arquivo = input("Digite o caminho para o arquivo de dados: ")

    arquivo = open(nome_arquivo, "r")

    qtdCidades = int(arquivo.readline())
    
    contador = 0
    while contador < qtdCidades:
        nome = arquivo.readline().splitlines()[0]
        estacao = Estacao(nome)

        estacoes[nome] = estacao

        grafo.adiciona_estacao(estacao)

        contador = contador + 1
    
    qtdTrens = int(arquivo.readline())
    
    i = 0
    while i < qtdTrens:
        qtd_partidas = int(arquivo.readline())

        # lista de tuplas
        partidas = []
        j = 0
        while j < qtd_partidas:
            # formato da linha: 
            # HoraPartida1 Cidade1
            leitura = arquivo.readline().splitlines()[0].split()
            hora = leitura[0]
            estacao = leitura[1]
            # cria uma nova tupla no formato (hora, estacao)
            partidas.append((hora, estacao))
            
            j = j + 1
        
        j = 0

        # nunca possuirá menos que duas partidas, já que possui
        # origem de uma aresta e destino a outra...
        while j < (len(partidas) - 1):
            partida1 = partidas[j]
            partida2 = partidas[j+1]
            grafo.adiciona_trecho(estacoes[partida1[1]], estacoes[partida2[1]], Trecho(partida2[0], partida1[0]))
            j = j + 1
        
        i = i + 1
    
    horaPassageiro = arquivo.readline().splitlines()[0]
    origem = arquivo.readline().splitlines()[0]
    destino = arquivo.readline().splitlines()[0]
    
    print(procura_percurso(grafo, estacoes[origem], estacoes[destino], horaPassageiro))

if __name__ == "__main__":
    main()
