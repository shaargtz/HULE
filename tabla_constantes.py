class Constantes:
    def __init__(self):
        self.tabla = {}
        self.contadores = {
            'ent' : 20000,
            'flot' : 21000,
            'car' : 22000,
            'cadena' : 23000,
            'bool' : 24000
        }
    
    def insertar(self, var, tipo):
        if not self.tabla.get(var):
            self.tabla[var] = (tipo, self.contadores[tipo])
            self.contadores[tipo] = self.contadores[tipo] + 1
            return self.contadores[tipo]
        return -1