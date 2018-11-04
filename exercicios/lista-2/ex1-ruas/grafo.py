# Esquema de mapeamento das arestas
# {
#     v1: {
#         v2 : 3, 
#         v3: 1,
#         v4: 5
#     }
# }

class GrafoPonderado(object):
    def __init__(self, qtd_vertices = 0):
        self.__mapeamento = {}

        for i in range(1, qtd_vertices + 1):
            self.__adiciona_vertice(i)

    def __adiciona_vertice(self, vertice):
        if vertice not in self.__mapeamento:
            # distância de um vértice para ele mesmo é zero.
            self.__mapeamento[vertice] = {}
            self.__mapeamento[vertice][vertice] = 0

    def adiciona_aresta(self, v1, v2, peso):
        if (v1 not in self.__mapeamento):
            raise Exception("Falha ao criar aresta. Os vértices {0} e {1} precisam existir.".format(v1, v2))
        self.__mapeamento[v1][v2] = peso
    
    def qtd_vertices(self):
        return len(self.__mapeamento)

    # mapeamento de vértices
    def map(self):
        return self.__mapeamento