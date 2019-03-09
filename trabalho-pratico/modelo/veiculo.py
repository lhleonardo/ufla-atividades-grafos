import random
class Veiculo(object):
    #V : volume máximo (em m 3 ) que o veículo pode transportar;
    #P : valor máximo (em reais) que o veículo pode transportar;
    #Nv : quantidade de veículos disponíveis;
    #(vf) : velocidade a qual o veículo se move entre o centro de distribuição e a primeira
    #entrega, assim como entre a última entrega e o centro de distribuição;
    #(vd) : velocidade com a qual o veículo se move entre duas entregas;
    #(tc) : tempo médio para se carregar um pacote no veículo;
    #(td) : tempo médio necessário para descarregar um pacote do veículo e entregá-lo ao
    #cliente;
    #(ph) : custo médio por hora do veículo;
    #(pkm) : custo médio por quilômetro percorrido pelo veículo;
    #(pf) : custo fixo diário do veículo;

    def __init__(self, V, P, Nv, vf, vd, tc, td, ph, pkm, pf):
        self.V = V
        self.P = P
        self.Nv = Nv
        self.vf = random.randint(vf - 5, vf + 5)
        self.vd = random.randint(vd - 5, vd + 5)
        self.tc = random.uniform(tc, 3*tc)
        self.td = td
        self.ph = ph
        self.pkm = pkm
        self.pf = pf
        
        
    def imprime(self):
        print(self.V, self.P, self.Nv, self.vf, self.vd, self.tc, self.td, self.ph, self.pkm, self.pf)
    def calculaCustoBeneficio(self):
        return ((self.ph+self.pkm+self.pf) / (self.V))
        
    def __repr__(self):
        return "({0}, {1})".format(self.V, self.Nv)

    
