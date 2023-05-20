class EspaciosMemoria:
    def __init__(self):
        self.espacios = {}

    def instanciar(self, contadores):
        if contadores:
            for alcance in contadores.keys():
                self.espacios[alcance] = {}
                for tipo in contadores[alcance].keys():
                    self.espacios[alcance][tipo] = [None] * (contadores[alcance][tipo] % 1000)
