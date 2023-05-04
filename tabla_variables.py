class Variables:
    def __init__(self, tipo):
        # nombre : (tipo, direccion)
        self.tabla = {}
        if tipo == 'global':
            self.contadores = {
                'ent' : 0,
                'flot' : 1000,
                'car' : 2000,
                'cadena' : 3000,
                'bool' : 4000
            }
        elif tipo == 'local':
            self.contadores = {
                'ent' : 5000,
                'flot' : 6000,
                'car' : 7000,
                'cadena' : 8000,
                'bool' : 9000
            }
        elif tipo == 'temp':
            self.contadores = {
                'ent' : 10000,
                'flot' : 11000,
                'car' : 12000,
                'cadena' : 13000,
                'bool' : 14000
            }
        elif tipo == 'ctes':
            self.contadores = {
                'ent' : 15000,
                'flot' : 16000,
                'car' : 17000,
                'cadena' : 18000,
                'bool' : 19000
            }

    def insertar_variable(self, var, tipo):
        if not self.tabla.get(var):
            self.tabla[var] = (tipo, self.contadores[tipo])
            self.contadores[tipo] = self.contadores[tipo] + 1
            return self.contadores[tipo]
        return -1