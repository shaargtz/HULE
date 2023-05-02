class Variables:
    def __init__(self, es_global):
        # nombre : (tipo, direccion)
        self.tabla = {}
        if (es_global):
            self.contadores = {
                'ent' : 0,
                'flot' : 1000,
                'car' : 2000,
                'cadena' : 3000,
                'bool' : 4000
            }
        else:
            self.contadores = {
                'ent' : 5000,
                'flot' : 6000,
                'car' : 7000,
                'cadena' : 8000,
                'bool' : 9000
            }

    def insertar_variable(self, var, tipo):
        if (not self.tabla.get(var)):
            self.tabla[var] = (tipo, self.contadores[tipo])
            self.contadores[tipo] = self.contadores[tipo] + 1
            return self.contadores[tipo]
        return -1