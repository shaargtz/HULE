from utilidad import *

class EspaciosMemoria:
    def __init__(self):
        self.espacios = {}

    def instanciar(self, contadores):
        if contadores:
            for alcance in contadores.keys():
                self.espacios[alcance] = {}
                for tipo in contadores[alcance].keys():
                    if tipo != checar_tipo_memoria(contadores[alcance][tipo]):
                        raise Exception("Limite de memoria de tipo {} {} excedido".format(alcance, tipo))
                    self.espacios[alcance][tipo] = [None] * (contadores[alcance][tipo] % 1000)
