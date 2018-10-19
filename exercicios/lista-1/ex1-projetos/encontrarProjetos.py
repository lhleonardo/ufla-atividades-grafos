from grafo import Grafo
from vertice import Vertice

def encontrar_caminho_projetos(grafo, primeiro_projeto):
    vertices = grafo.vertices()

    for vertice in vertices:
        vertice.marcado = False
    
    

