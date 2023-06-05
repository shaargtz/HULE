# clase para comparar los tipos de expresiones escritas por el usuario en el codigo
# self.cubo tiene todas las combinaciones validas de operador con operandos y su
# tipo de retorno correspondiente
class CuboSemantico:
    def __init__(self):
        self.cubo = {
            ('+', 'ent', 'ent')         : 'ent',
            ('+', 'ent', 'flot')        : 'flot',
            ('+', 'flot', 'ent')        : 'flot',
            ('+', 'flot', 'flot')       : 'flot',
            ('+', 'cadena', 'cadena')   : 'cadena',
            ('+', 'car', 'car')         : 'cadena',
            ('+', 'car', 'cadena')      : 'cadena',
            ('+', 'cadena', 'car')      : 'cadena',
            ('-', 'ent', 'ent')         : 'ent',
            ('-', 'ent', 'flot')        : 'flot',
            ('-', 'flot', 'ent')        : 'flot',
            ('-', 'flot', 'flot')       : 'flot',
            ('*', 'ent', 'ent')         : 'ent',
            ('*', 'ent', 'flot')        : 'flot',
            ('*', 'flot', 'ent')        : 'flot',
            ('*', 'flot', 'flot')       : 'flot',
            ('/', 'ent', 'ent')         : 'ent',
            ('/', 'ent', 'flot')        : 'flot',
            ('/', 'flot', 'ent')        : 'flot',
            ('/', 'flot', 'flot')       : 'flot',
            ('&', 'bool', 'bool')       : 'bool',
            ('|', 'bool', 'bool')       : 'bool',
            ('>', 'ent', 'ent')         : 'bool',
            ('>', 'ent', 'flot')        : 'bool',
            ('>', 'flot', 'ent')        : 'bool',
            ('>', 'flot', 'flot')       : 'bool',
            ('<', 'ent', 'ent')         : 'bool',
            ('<', 'ent', 'flot')        : 'bool',
            ('<', 'flot', 'ent')        : 'bool',
            ('<', 'flot', 'flot')       : 'bool',
            ('==', 'ent', 'ent')        : 'bool',
            ('==', 'ent', 'flot')       : 'bool',
            ('==', 'flot', 'ent')       : 'bool',
            ('==', 'flot', 'flot')      : 'bool',
            ('==', 'car', 'car')        : 'bool',
            ('==', 'cadena', 'cadena')  : 'bool',
            ('==', 'bool', 'bool')      : 'bool',
            ('!=', 'ent', 'ent')        : 'bool',
            ('!=', 'ent', 'flot')       : 'bool',
            ('!=', 'flot', 'ent')       : 'bool',
            ('!=', 'flot', 'flot')      : 'bool',
            ('!=', 'car', 'car')        : 'bool',
            ('!=', 'cadena', 'cadena')  : 'bool',
            ('!=', 'bool', 'bool')      : 'bool',
        }

    # funcion para retornar el tipo correspondiente para la expresion
    def emparejar_tipo(self, tupla):
        tipo = self.cubo.get(tupla)
        if tipo:
            return tipo
        else:
            raise Exception("Tipos incompatibles: " + tupla[1] + " " + tupla[0] + " " + tupla[2])