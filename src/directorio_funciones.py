from src.tabla_variables import Variables
 
class DirFunciones:
    def __init__(self):
        self.directorio = {
            # nombre : [tipo, variables, parametros, cuadruplo, return]
            'hule' : ['vacia', Variables('local'), None, None, None]
        }
    
    def insertar_funcion(self, func, tipo):
        if not self.directorio.get(func):
            self.directorio[func] = [tipo, None, [], None, None]
        else:
            raise Exception("Funcion " + func + " definida multiples veces")
        
    def insertar_tabla_var(self, func, alcance):
        self.directorio[func][1] = Variables(alcance)
        
    def insertar_variable(self, func, tipo, var=None, dims=None):
        # caso en que inserte temporales sin tener variables locales
        if not var and not self.directorio[func][1]:
            self.insertar_tabla_var(func, 'local')
        return self.directorio[func][1].insertar_variable(tipo, var, dims)
    
    def insertar_constante(self, tipo, cte):
        if 'ctes' not in self.directorio.keys():
            self.directorio['ctes'] = ['vacia', Variables('ctes'), None, None, None, None]
        return self.directorio['ctes'][1].insertar_constante(tipo, cte)

    def insertar_parametro(self, func, tipo, var):
        self.directorio[func][2].append((var, tipo))
        self.insertar_variable(func, tipo, var)

    def buscar_variable(self, func, id):
        if self.directorio[func][1]:
            var = self.directorio[func][1].tabla['local'].get(id)
            if var:
                return var[1]
        if self.directorio['global'][1]:
            var = self.directorio['global'][1].tabla['glob'].get(id)
            if var:
                return var[1]
        raise Exception("Variable " + id + " no definida")
        
    def tiene_tabla_var(self, func):
        return self.directorio[func][1] != None
    
    def comparar_parametro(self, func, pos, arg):
        param = self.directorio[func][2][pos]
        if arg != param[1]:
            raise Exception("Argumento " + str(pos) + " es de tipo " + str(arg) + " y deberia ser " + param[1])
        else:
            return self.buscar_variable(func, param[0])
    
    def insertar_retorno(self, func, dir):
        self.directorio[func][4] = dir

    def buscar_contadores_var(self, func):
        if self.directorio[func][1]:
            return self.directorio[func][1].contadores
        else:
            return None
        
    def buscar_ctes(self):
        if 'ctes' in self.directorio.keys():
            return self.directorio['ctes'][1].tabla['ctes']
    
    def buscar_cuadruplo(self, func):
        return self.directorio[func][3]
    
    def buscar_tipo_funcion(self, func):
        return self.directorio[func][0]
    
    def buscar_dimensiones(self, func, id):
        if self.directorio[func][1]:
            var = self.directorio[func][1].tabla['local'].get(id)
            if var:
                return var[2].retornar_dimensiones()
        if self.directorio['global'][1]:
            var = self.directorio['global'][1].tabla['glob'].get(id)
            if var:
                return var[2].retornar_dimensiones()
        raise Exception("Variable " + id + " no definida")
    
    def buscar_m(self, func, id):
        if self.directorio[func][1]:
            var = self.directorio[func][1].tabla['local'].get(id)
            if var:
                return var[2].retornar_m()
        if self.directorio['global'][1]:
            var = self.directorio['global'][1].tabla['glob'].get(id)
            if var:
                return var[2].retornar_m()
        raise Exception("Variable " + id + " no definida")