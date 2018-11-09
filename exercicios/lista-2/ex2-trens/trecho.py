class Trecho(object):
    def __init__(self, horaChegada, horaSaida):
        self.__horaChegada = horaChegada
        self.__horaSaida = horaSaida
        self.__tempoGasto = int(self.__horaChegada) - int(self.__horaSaida)

    def tempoGasto(self):
        return self.__tempoGasto

    def __eq__(self, outro):
        return self.__horaChegada == outro.__horaChegada and self.__horaSaida == outro.__horaSaida