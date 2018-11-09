from percurso import procura_percurso
from grafo import GrafoPonderado
from trecho import Trecho

def main():
    grafo = GrafoPonderado()
    
    qtdCidades = int(input("Quantidade cidades: "))
    
    for i in range(qtdCidades):
        estacao = input("Estação {}: ".format(i))
        grafo.adiciona_estacao(estacao)
    
    qtdTrens = int(input("Quantidade de trens: "))
    
    for i in range(qtdTrens):        
        hora1 = input("Hora de saida")
        cidade1 = input("Cidade de saida: ")
        
        hora2 = input("Hora de chegada")
        cidade2 = input("Cidade de chegada: ")
        
        grafo.adiciona_trecho(cidade1, cidade2, Trecho(hora2, hora1))
    
    
    horaPassageiro = input("Horario que o passageiro sai: ")
    origem = input("Cidade de origem: ")
    destino = input("Cidade de destino: ")
    
    print(procura_percurso(grafo, origem, destino, horaPassageiro))

if __name__ == "__main__":
    main()
