class Variables:
    def __init__(self, alcance):
        # nombre : (tipo, direccion, dimensiones)
        self.tabla = {
            'var' : {},
            'temp' : {},
        }
        if alcance == 'global':
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
        elif alcance == 'local':
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

    def insertar(self, tipo, var=None):
        if var:
            if not self.tabla['var'].get(var):
                self.tabla['var'][var] = (tipo, self.contadores['var'][tipo], 0)
                self.contadores['var'][tipo] += 1
                return self.contadores['var'][tipo] - 1
            else:
                raise Exception("Variable " + var + " definida multiples veces")
        else:
            nueva_temp = tipo + str(self.contadores['temp'][tipo] % 1000)
            self.tabla['temp'][nueva_temp] = (tipo, self.contadores['temp'][tipo], 0)
            self.contadores['temp'][tipo] += 1
            return self.contadores['temp'][tipo] - 1