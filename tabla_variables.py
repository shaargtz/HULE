class Variables:
    def __init__(self, alcance):
        # nombre : (tipo, direccion, dimensiones)
        if alcance == 'global':
            self.tabla = {
                'glob' : {}
            }
            self.contadores = {
                'glob' : {
                    'ent' : 0000,
                    'flot' : 1000,
                    'car' : 2000,
                    'cadena' : 3000,
                    'bool' : 4000
                }
            }
        elif alcance == 'local':
            self.tabla = {
                'local' : {},
                'temp' : {},
            }
            self.contadores = {
                'local' : {
                    'ent' : 5000,
                    'flot' : 6000,
                    'car' : 7000,
                    'cadena' : 8000,
                    'bool' : 9000
                },
                'temp' : {
                    'ent' : 10000,
                    'flot' : 11000,
                    'car' : 12000,
                    'cadena' : 13000,
                    'bool' : 14000
                },
            }
        elif alcance == 'ctes':
            self.tabla = {
                'ctes' : {}
            }
            self.contadores = {
                'ctes' : {
                    'ent' : 15000,
                    'flot' : 16000,
                    'car' : 17000,
                    'cadena' : 18000,
                    'bool' : 19000
                }
            }

    def insertar_variable(self, tipo, var=None):
        if var:
            alcance = list(self.tabla.keys())[0]
            if not self.tabla[alcance].get(var):
                self.tabla[alcance][var] = (tipo, self.contadores[alcance][tipo], 0)
                self.contadores[alcance][tipo] += 1
                return self.contadores[alcance][tipo] - 1
            else:
                raise Exception("Variable " + var + " definida multiples veces")
        else:
            if 'temp' not in self.tabla.keys():
                raise Exception("No se pueden instertar temporales a una tabla global")
            nueva_temp = tipo + str(self.contadores['temp'][tipo] % 1000)
            self.tabla['temp'][nueva_temp] = (tipo, self.contadores['temp'][tipo], 0)
            self.contadores['temp'][tipo] += 1
            return self.contadores['temp'][tipo] - 1
        
    def insertar_constante(self, tipo, cte):
        dir = self.tabla['ctes'].get(cte)
        if dir:
            return dir[1]
        else:
            self.tabla['ctes'][cte] = (tipo, self.contadores['ctes'][tipo])
            self.contadores['ctes'][tipo] = self.contadores['ctes'][tipo] + 1
            return self.contadores['ctes'][tipo] - 1