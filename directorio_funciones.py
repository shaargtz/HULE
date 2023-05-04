class DirFunciones:
    def __init__(self):
        self.directorio = {
            # nombre : [tipo, tabla de variables, parametros]
            'hule' : ['void', None, []]
        }
    
    def insertar(self, func, tipo):
        if not self.directorio.get(func):
            self.directorio[func] = [tipo, None, []]
        else:
            raise Exception("Funcion " + func + " definida multiples veces")