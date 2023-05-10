class DirFunciones:
    def __init__(self):
        self.directorio = {
            # nombre : [tipo, variables, parametros, memoria, cuadruplo, return]
            'hule' : ['void', None, [], {}, None, None]
        }
    
    def insertar(self, func, tipo):
        if not self.directorio.get(func):
            self.directorio[func] = [tipo, None, [], {}, None, None]
        else:
            raise Exception("Funcion " + func + " definida multiples veces")
        
    def buscar_variable(self, func, id):
        var = self.directorio[func][1].tabla['var'].get(id)
        if var:
            return var[1]
        else:
            raise Exception("Variable " + id + " no definida")