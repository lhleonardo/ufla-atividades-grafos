class GrafoPonderado(object):
    def __init__(self):
        self.__mapeamento = {}

    def adiciona_estacao(self, estacao):
        if estacao not in self.__mapeamento:
            # distância de um vértice para ele mesmo é zero.
            self.__mapeamento[estacao] = {}
            self.__mapeamento[estacao][estacao] = []

    def adiciona_trecho(self, v1, v2, trecho):
        if (v1 not in self.__mapeamento):
            raise Exception("Falha ao criar trecho. As estações {0} e {1} precisam existir.".format(v1, v2))
        
        lista_trechos = self.__mapeamento[v1].get(v2, [])
        
        if trecho not in lista_trechos:
            lista_trechos.append(trecho)

        self.__mapeamento[v1][v2] = lista_trechos
    
    def qtd_estacoes(self):
        return len(self.__mapeamento)

    # mapeamento de vértices
    def map(self):
        return self.__mapeamento