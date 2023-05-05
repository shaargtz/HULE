class Variables:
    def __init__(self, tipo):
        # nombre : (tipo, direccion)
        self.tabla = {
            'var' : {},
            'temp' : {},
        }
        if tipo == 'global':
            self.contadores = {
                'var' : {
                    'ent' : 0000,
                    'flot' : 1000,
                    'car' : 2000,
                    'cadena' : 3000,
                    'bool' : 4000
                },
                'temp' : {
                    'ent' : 5000,
                    'flot' : 6000,
                    'car' : 7000,
                    'cadena' : 8000,
                    'bool' : 9000
                },
            }
        elif tipo == 'local':
            self.contadores = {
                'var' : {
                    'ent' : 10000,
                    'flot' : 11000,
                    'car' : 12000,
                    'cadena' : 13000,
                    'bool' : 14000
                },
                'temp' : {
                    'ent' : 15000,
                    'flot' : 16000,
                    'car' : 17000,
                    'cadena' : 18000,
                    'bool' : 19000
                },
            }

    def insertar(self, var, tipo, alcance):
        if not self.tabla[alcance].get(var):
            self.tabla[alcance][var] = (tipo, self.contadores[alcance][tipo])
            self.contadores[alcance][tipo] = self.contadores[alcance][tipo] + 1
            return self.contadores[alcance][tipo]
        else:
            raise Exception("Variable " + var + " definida multiples veces")