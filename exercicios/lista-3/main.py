from grafo import Grafo
from vertice import Vertice

def main():
    caminho = input("Digite o caminho do arquivo: ")

    arquivo = open(caminho, "r")
    computadores = {}
    tarefas = {}
    
    # cria o grafo
    grafo = Grafo()

    # adiciona os 10 computadores, de 0 a 9
    for i in range(10):
        vertice = Vertice(i)
        grafo.adiciona_computador(vertice)
        # mapeamento de computador para cada IDentificador
        computadores[i] = vertice

    for linha in arquivo:
        leitura = linha.split()

        bloco1, computadores_usados = leitura[0], leitura[1]
        
        tarefa, qtd = bloco1[0], bloco1[1]

        vertice = Vertice(tarefa)
        grafo.adiciona_tarefa(vertice)
        tarefas[tarefa] = (vertice, int(qtd))

        # cria aresta entre a tarefa e todos os computadores que ela pode utilizar
        for computador in computadores_usados:
            grafo.adiciona_aresta(vertice, computadores[int(computador)], 1)

    sorvedouro = Vertice("s", is_sorvedouro = True)
    fonte = Vertice("t", is_fonte = True)
    
    grafo.define_sorvedouro(sorvedouro)
    grafo.define_fonte(fonte)

    # cria arestas do sorvedouro as atividades com os capacidades relativas 
    # a quantidade de instâncias que deverão ser executadas pela 
    # determinada tarefa
    for chave in tarefas:
        (vertice, qtd) = tarefas[chave]
        grafo.adiciona_aresta(sorvedouro, vertice, qtd)

    # cria arestas dos computadores para a fonte, todas com capacidade 1
    for chave in computadores:
        grafo.adiciona_aresta(computadores[int(chave)], fonte, 1)
    
    print(grafo.executar_fluxo())

main()