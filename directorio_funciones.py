from tabla_variables import Variables

class Funciones:
    def __init__(self):
        self.directorio = {
            # nombre : [tipo, tabla de variables]
            'global' : ['void', Variables(True)]
        }
    
    def insertar_funcion(self, func, tipo):
        if (not self.directorio.get(func)):
            self.directorio[func] = [tipo, Variables(False)]