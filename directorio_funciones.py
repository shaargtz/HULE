from tabla_variables import Variables

class DirFunciones:
    def __init__(self):
        self.directorio = {
            # nombre : [tipo, tabla de variables]
            'hule' : ['void', Variables('global')]
        }
    
    def insertar_funcion(self, func, tipo):
        if not self.directorio.get(func):
            self.directorio[func] = [tipo, Variables('local')]