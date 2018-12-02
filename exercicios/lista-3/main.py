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

    # percorre as linhas do arquivo
    for linha in arquivo:
        # remove o ; do final da linha, já que não é essencial para 
        # diferenciar as entradas, pois o \n já faz esse trabalho...
        linha = linha.replace(";", "")
        
        # divide a leitura em 
        # Atividade:Qtd Pc1Pc2...PcN
        leitura = linha.split()
        
        # bloco 1 com a parte Atividade:Qtd
        # computadores_usados com Pc1Pc2...PcN
        bloco1, computadores_usados = leitura[0], leitura[1]
        
        # descobre a tarefa [A-Z] e a quantidade de máquinas 
        # que deverão executá-la
        tarefa, qtd = bloco1[0], bloco1[1]
        
        # vértice que referencia a tarefa
        vertice = Vertice(tarefa)
        grafo.adiciona_tarefa(vertice)
        
        # a quantidade de execuções para a tarefa deve ser salva, pois será necessário
        # criar uma ligação entre o sorvedouro (s) e esta mesma tarefa, sendo o peso
        # da aresta definido pela quantidade de execuções
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
