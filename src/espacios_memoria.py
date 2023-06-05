from src.utilidad import *

# clase para guardar los segmentos de memoria y sus valores que se modifican en ejecucion.
# se instancia a partir de los contadores que tienen las tablas de variables en el directorio
# de funciones.
class EspaciosMemoria:
    def __init__(self):
        self.espacios = {}

    def instanciar(self, contadores):
        if contadores:
            for alcance in contadores.keys():
                self.espacios[alcance] = {}
                for tipo in contadores[alcance].keys():
                    # el overflow del segmento hace que agarre memoria de otro tipo
                    if tipo != checar_tipo_memoria(contadores[alcance][tipo]):
                        raise Exception("Limite de memoria de tipo {} {} excedido".format(alcance, tipo))
                    self.espacios[alcance][tipo] = [None] * (contadores[alcance][tipo] % 1000)
