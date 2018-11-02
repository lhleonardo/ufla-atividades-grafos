# Esquema de mapeamento das arestas
# {
#     v1: {
#         v2 : 3, 
#         v3: 1,
#         v4: 5
#     }
# }

class GrafoPonderado(object):
    def __init__(self):
        self.__mapeamento = {}

    def adiciona_aresta(self, v1, v2, peso):
        if (v1 not in self.__mapeamento):
            raise Exception("Falha ao criar aresta. Os vértices {0} e {1} precisam existir.".format(v1, v2))
        
        self.__mapeamento[v1][v2] = peso
    
    def remover_aresta(self, v1, v2):
        if (v1 not in self.__mapeamento or v2 not in self.__mapeamento[v1]):
            raise Exception("Falha ao remover aresta. Os vértices {0} e {1} precisam estar relacionados.".format(v1, v2))
        
        del self.__mapeamento[v1][v2]