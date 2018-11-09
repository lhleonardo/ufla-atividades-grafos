class Trecho(object):
    def __init__(self, horaChegada, horaSaida):
        self.__horaChegada = horaChegada
        self.__horaSaida = horaSaida
        self.__tempoGasto = int(self.__horaChegada) - int(self.__horaSaida)

    def tempoGasto(self):
        return self.__tempoGasto
    
    def horaChegada (self):
        return self.__horaChegada
        
    def horaSaida (self):
        return self.__horaSaida
    
    def __eq__(self, outro):
        return int(self.__horaChegada) == int(outro.__horaChegada) and int(self.__horaSaida) == int(outro.__horaSaida)
        
    def __lt__ (self, outro):
        return int(self.__horaChegada) < int(outro.__horaChegada) 
