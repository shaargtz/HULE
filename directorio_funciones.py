from tabla_variables import Variables

memoria_vacia = {
                    'total' : 0,
                    'ent' : 0,
                    'flot' : 0,
                    'car' : 0,
                    'cadena' : 0,
                    'bool' : 0,
                }, 

class DirFunciones:
    def __init__(self):
        self.directorio = {
            # nombre : [tipo, variables, parametros, memoria, cuadruplo, return]
            'hule' : ['void', None, [], memoria_vacia, None, None]
        }
    
    def insertar_funcion(self, func, tipo):
        if not self.directorio.get(func):
            self.directorio[func] = [tipo, None, [], memoria_vacia, None, None]
        else:
            raise Exception("Funcion " + func + " definida multiples veces")
        
    def insertar_tabla_var(self, func, alcance):
        self.directorio[func][1] = Variables(alcance)
        
    def insertar_variable(self, func, tipo, var=None):
        self.directorio[func][3][0][tipo] += 1
        self.directorio[func][3][0]['total'] += 1
        return self.directorio[func][1].insertar(tipo, var)

    def insertar_parametro(self, func, tipo, var):
        self.directorio[func][2].append((var, tipo))
        self.insertar_variable(func, tipo, var)

    def buscar_variable(self, func, id, glob=False):
        var = self.directorio[func][1].tabla['var'].get(id)
        if var:
            return var[1]
        if glob:
            var = self.directorio['hule'][1].tabla['var'].get(id)
            if var:
                return var[1]
        raise Exception("Variable " + id + " no definida")
        
    def tiene_tabla_var(self, func):
        return self.directorio[func][1] != None
    
    def comparar_parametro(self, func, pos, arg):
        param = self.directorio[func][2][pos]
        if arg != param[1]:
            raise Exception("Argumento " + str(pos) + " es de tipo " + arg + " y deberia ser " + param[1])
        else:
            return self.buscar_variable(func, param[0])