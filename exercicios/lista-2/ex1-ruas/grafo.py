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
        self.__vertices = []

        for i in range(1, qtd_vertices + 1):
            self.__adiciona_vertice(i)

    def __adiciona_vertice(self, vertice):
        if vertice not in self.__vertices:
            self.__mapeamento[vertice] = {}
            self.__mapeamento[vertice][vertice] = 0
            self.__vertices.append(vertice)

    def adiciona_aresta(self, v1, v2, peso):
        if (v1 not in self.__mapeamento):
            raise Exception("Falha ao criar aresta. Os vértices {0} e {1} precisam existir.".format(v1, v2))
        self.__mapeamento[v1][v2] = peso
    
    def remover_aresta(self, v1, v2):
        if (v1 not in self.__mapeamento or v2 not in self.__mapeamento[v1]):
            raise Exception("Falha ao remover aresta. Os vértices {0} e {1} precisam estar relacionados.".format(v1, v2))
        
        del self.__mapeamento[v1][v2]

        if v1 not in self.__mapeamento:
            self.__vertices.remove(v1)
        
        if v2 not in self.__mapeamento:
            self.__vertices.remove(v2)
    
    def qtd_vertices(self):
        return len(self.__mapeamento)

    def map(self):
        return self.__mapeamento
   

if __name__ == "__main__":
    g = GrafoPonderado(4)

    g.adiciona_aresta(1, 3, 3)
    g.adiciona_aresta(1, 4, 0)
    g.adiciona_aresta(2, 1, -2)
    g.adiciona_aresta(2, 4, 4)
    g.adiciona_aresta(3, 4, 5)
    g.adiciona_aresta(4, 2, 1)

    print(g.map())