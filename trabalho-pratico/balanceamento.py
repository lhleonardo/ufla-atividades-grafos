from utils import distancia
import math

def balanceamento_por_demanda(regioes, qtd_casas, qtd_centros):
    # distribuição por demanda
    centros = list(regioes.keys())
    demanda_ideal = (qtd_casas - qtd_centros) / qtd_centros

    for centro in regioes.keys():
        grafo = regioes[centro]
        
        if (len(list(grafo.neighbors(centro))) <= demanda_ideal):
            continue
        
        for cliente in list(grafo.neighbors(centro)):
            centros.sort(reverse=True, key=lambda centro : distancia(centro, cliente))
            
            if (len(list(regioes[centros[1]].neighbors(centros[1]))) < demanda_ideal):
                if (centros[1].maior_distancia * 1.2) >= distancia(cliente, centros[1]):
                    grafo.remove_node(cliente)
                    regioes[centros[1]].add_node(cliente)
                    regioes[centros[1]].add_edge(cliente, centros[1], distancia=distancia(centros[1], cliente))
            elif (len(list(regioes[centros[2]].neighbors(centros[2]))) <= demanda_ideal):
                if (centros[2].maior_distancia * 1.2) >= distancia(cliente, centros[2]):
                    grafo.remove_node(cliente)
                    regioes[centros[2]].add_node(cliente)
                    regioes[centros[2]].add_edge(cliente, centros[2], distancia=distancia(centros[2], cliente))
            
            if (len(list(grafo.neighbors(centro))) <= demanda_ideal):
                break

def balanceamento_por_volume(regioes, volume_total, qtd_centros):
    volume_ideal = volume_total / qtd_centros

    for centro in regioes.keys():
        if (centro.volume <= volume_ideal):
            continue
        
        # ordena a partir dos clientes mais distantes
        clientes = list(regioes[centro].neighbors(centro))
        clientes.sort(reverse=True, key=lambda cliente : distancia(centro, cliente))

        # quantidade de clientes que serão deslocados, garantidos pela taxa de 87%
        # de melhoria das distribuições de serviços
        qtd_melhoria = math.floor(len(clientes) * 0.90)
        while qtd_melhoria > 0 and centro.volume > volume_ideal:
            # pega o cliente
            cliente = clientes.pop(0)

            # remove esse cliente para entrega deste centro de distribuição
            regioes[centro].remove_node(cliente)
            
            # atualiza o volume
            centro.volume -= cliente.volume

            possiveis_centros = list(regioes.keys())
            possiveis_centros.remove(centro)
            possiveis_centros.sort(reverse=True, key=lambda c: distancia(c, cliente))
            
            definiu = False
            contador = 0
            while not definiu and len(possiveis_centros) > 0 and contador < 2:
                contador += 1
                possivel_centro = possiveis_centros.pop(0)

                if (possivel_centro.volume + cliente.volume) <= volume_ideal:
                    if (possivel_centro.maior_distancia * 1.2) >= distancia(cliente, possivel_centro):
                        definiu = True
                        regioes[possivel_centro].add_node(cliente)
                        regioes[possivel_centro].add_edge(cliente, possivel_centro, distancia=distancia(possivel_centro, cliente))
                        possivel_centro.volume += cliente.volume

            # caso não seja encontrado um outro centro de distribuição que 
            # consiga atender este cliente, ele deverá ainda ser atendido pelo
            # centro em que já se encontrava
            if not definiu:
                regioes[centro].add_node(cliente)
                regioes[centro].add_edge(cliente, centro, distancia=distancia(centro, cliente))
                centro.volume += cliente.volume

            # atualiza a quantidade de clientes que podem ser melhorados
            qtd_melhoria -= 1
        