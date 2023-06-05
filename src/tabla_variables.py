from src.dimensiones import Dimensiones

# clase que almacena la tabla de variables, modelada en base al alcance que tiene.
# se asigna el siguiente espacio de memoria de cada segmento por medio de un contador
# que tambien nos puede dar la cantidad de variables en un segmento utilizando
# la operacion modulo.
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
                    'bool' : 14000,
                    'apuntador' : 15000
                },
            }
        elif alcance == 'ctes':
            self.tabla = {
                'ctes' : {}
            }
            self.contadores = {
                'ctes' : {
                    'ent' : 16000,
                    'flot' : 17000,
                    'car' : 18000,
                    'cadena' : 19000
                }
            }

    # principal metodo para modificar el directorio. si no tiene nombre de variable es una temporal.
    # si no tiene dimensiones es una variable simple.
    def insertar_variable(self, tipo, var=None, dims=None):
        if var:
            alcance = list(self.tabla.keys())[0]
            if not self.tabla[alcance].get(var):
                self.tabla[alcance][var] = (tipo, self.contadores[alcance][tipo], Dimensiones(dims))
                antes = self.contadores[alcance][tipo]
                self.contadores[alcance][tipo] += self.tabla[alcance][var][2].total
                # solo hay 1000 espacios para cada segmento
                if antes // 1000 != self.contadores[alcance][tipo] // 1000:
                    raise Exception("Limite de memoria de tipo {} {} excedido".format(alcance, tipo))
                return self.contadores[alcance][tipo] - 1
            else:
                raise Exception("Variable " + var + " definida multiples veces")
        else:
            if 'temp' not in self.tabla.keys():
                raise Exception("No se pueden instertar temporales a una tabla global")
            # nombres genericos para las temporales
            nueva_temp = tipo + str(self.contadores['temp'][tipo] % 1000)
            self.tabla['temp'][nueva_temp] = (tipo, self.contadores['temp'][tipo], Dimensiones(dims))
            self.contadores['temp'][tipo] += 1
            return self.contadores['temp'][tipo] - 1
        
    # metodo para interactuar con la tabla de constantes
    def insertar_constante(self, tipo, cte):
        dir = self.tabla['ctes'].get(cte)
        if dir:
            return dir[1]
        else:
            self.tabla['ctes'][cte] = (tipo, self.contadores['ctes'][tipo])
            self.contadores['ctes'][tipo] = self.contadores['ctes'][tipo] + 1
            return self.contadores['ctes'][tipo] - 1
        
    # metodo para manejo de variables dimensionadas en compilacion
    def insertar_dimensiones(self, var, dims):
        alcance = list(self.tabla.keys())[0]
        if self.tabla[alcance].get(var):
            self.tabla[alcance][var][2].insertar_dimensiones(dims)
        else:
            raise Exception("Variable " + var + " multidimensional no definida")