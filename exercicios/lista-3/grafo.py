from vertice import Vertice
from aresta import Aresta
        
class Grafo:
    def __init__(self):
        self.__ligacoes = {}
        
        self.__computadores = []
        self.__tarefas = []

        self.__sorvedouro = None
        self.__fonte = None
    
    def getSorvedouro(self):
        return self.__sorvedouro
    
    def getFonte(self):
        return self.__fonte

    def adiciona_computador(self, vertice):
        if not isinstance(vertice, Vertice):
            raise ValueError("Além de ser um computador, também precisa ser um vértice.")
        
        if vertice in self.__computadores:
            raise ValueError("O computador já foi adicionado ao mapeamento.")

        self.__adiciona_vertice(vertice)
        self.__computadores.append(vertice)
    
    def adiciona_tarefa(self, vertice):
        if not isinstance(vertice, Vertice):
            raise ValueError("Além de ser uma tarefa, também precisa ser um vértice.")
        
        if vertice in self.__tarefas:
            raise ValueError("A tarefa já foi adicionado ao mapeamento.")

        self.__adiciona_vertice(vertice)
        self.__tarefas.append(vertice)

    def define_sorvedouro(self, vertice):
        self.__adiciona_vertice(vertice)

    def define_fonte(self, vertice):
        self.__adiciona_vertice(vertice)
    
    def __adiciona_vertice(self, vertice):
        if not isinstance(vertice, Vertice):
            raise ValueError("Para adicionar um vértice, ele deve ser provindo da classe Vértice.")
        
        if vertice in self.__ligacoes:
            raise ValueError("Vértice já foi adicionado no grafo.")

        # para cada uma das ligações, haverá uma lista de arestas
        # ao invés de um mapeamento que envolve dicionários sucessivos
        self.__ligacoes[vertice] = []
        
        # Definindo sorvedouros (s) e fontes (s) para evitar percorrimento da lista...
        if vertice.is_sorvedouro():
            if self.__sorvedouro is not None:
                raise ValueError("Sorvedouro (s) já foi definido no grafo.")
            else:
                self.__sorvedouro = vertice

        if vertice.is_fonte():
            if self.__fonte is not None:
                raise ValueError("Fonte (t) já foi definido no grafo.")
            else:
                self.__fonte = vertice
        
        

    def adiciona_aresta(self, inicio, fim, peso):
        if not isinstance(inicio, Vertice) or not isinstance(fim, Vertice):
            raise ValueError("Para adicionar uma aresta, os atributos inicio e " +
                    "fim devem ser provindos da classe Vértice.")
        
        # evita ligação entre dois computadores e duas tarefas
        if inicio in self.__computadores and fim in self.__computadores:
            raise ValueError("Não é possível fazer uma ligação entre dois computadores.")
        
        if inicio in self.__tarefas and fim in self.__tarefas:
            raise ValueError("Não é possível fazer uma ligação entre duas tarefas.")
        
        # evita ligações entre máquinas e tarefas não cadastradas
        # pois neste trecho é garantido que não há ligações entre máquinas/máquinas 
        # e tarefas/tarefas
        if inicio not in self.__computadores and inicio not in self.__tarefas and self.__sorvedouro != inicio:
            raise ValueError("O vértice que representa o início da aresta não foi adicionado.")
            
        if fim not in self.__computadores and fim not in self.__tarefas and self.__fonte != fim:
            raise ValueError("O vértice que representa o fim da aresta não foi adicionado.")

        # Finalmente, posso criar a aresta e fazer atribuições
        ligacao = Aresta(inicio, fim, peso)

        # adiciona aresta presente na ligação e seu devido mapeamento
        self.__ligacoes[inicio].append(ligacao)

    def __adjacentes_ordenados(self, vertice):
        arestas = self.__ligacoes[vertice]

        # ordenação dos elementos a partir do bubble sort
        houve_troca = True
        while houve_troca:
            houve_troca = False
            for indice in range(0, len(arestas) - 1):
                criterio1 = self.__calcula_criterio(arestas[indice])
                criterio2 = self.__calcula_criterio(arestas[indice+1])
                if criterio1 > criterio2:
                    houve_troca = True
                    arestas[indice], arestas[indice+1] = arestas[indice+1], arestas[indice]
        
        return arestas

    def __calcula_criterio(self, aresta):
        # parametro de comparação:
        # - peso da aresta de retorno da aresta atual 
        # - quantidade de adjacentes
        return aresta.peso + len(self.__ligacoes[aresta.destino()])

    def encontrar_caminho(self, inicio, fim, caminho_atual):
        if inicio == fim:
            return caminho_atual
        
        # percorre a adjacencia do vértice inicio
        #
        # Para modificar:
        # a aresta que deve ser buscada é a de menor vizinhança de saída e
        # com peso menor possível
        for aresta in self.__adjacentes_ordenados(inicio):
            # calcula o valor residual da aresta...
            valor_residual = aresta.peso - aresta.fluxo
            # se for possível passar por tal aresta e ela ainda não foi explorada
            if valor_residual > 0 and not (aresta, valor_residual) in caminho_atual:
                # realiza busca recursiva a partir do destino da aresta atual até o 
                # elemento final, para que continue procurando nas arestas
                temp = self.encontrar_caminho(aresta.destino(), fim, caminho_atual + [(aresta, valor_residual)])

                if temp != None:
                    return temp
    
    def executar_fluxo(self):
        if self.__sorvedouro is None or self.__fonte is None:
            raise ValueError("Sorvedouro (s) e/ou Fonte (t) não foram definidos.")
        
        # encontra inicialmente um caminho entre o sorvedouro e a fonte...
        caminho = self.encontrar_caminho(self.__sorvedouro, self.__fonte,  [])

        # enquanto houver caminhos válidos
        while caminho != None:
            # descobre o menor valor residual do fluxo presente no caminho
            # encontrado pela busca...
            fluxo_minimo = min(valor_residual for aresta, valor_residual in caminho)

            # atualiza os fluxos das arestas encontradas no caminho obtido
            # a partir do menor valor residual encontrado no caminho
            for aresta, residual in caminho:
                aresta.fluxo = aresta.fluxo + fluxo_minimo
                # aresta.retorno().fluxo = aresta.retorno().fluxo - fluxo_minimo
            
            # realiza novamente a operação de encontrar um caminho do 
            # sorvedouro (s) até a fonte (t)
            caminho = self.encontrar_caminho(self.__sorvedouro, self.__fonte, [])
        return self.__confere_dados()

    def __confere_dados(self):
        for aresta in self.__ligacoes[self.__sorvedouro]:
            if aresta.fluxo != aresta.peso:
                return "Não há solução para o problema."
                        
        mensagem = "_" * 10
        for atividade in self.__tarefas:
            for aresta in self.__ligacoes[atividade]:
                # faz com que o fluxo seja zero, até pq capacidade-fluxo = 0
                if aresta.fluxo == aresta.peso:
                    # substitui um _ (underscore) de uma determinada
                    # posicao pela tarefa que será executada.
                    # Nota: a posição é o computador
    
                    # indice que representa o computador
                    indice = aresta.destino().nome()
                    # atividade que será executada no computador
                    nome_atividade = atividade.nome()
                    temp=list(mensagem)
                    temp[indice]=nome_atividade
                    mensagem=''.join(temp)
        return mensagem 