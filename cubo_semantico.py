class CuboSemantico:
    def __init__(self):
        self.cubo = {
            ('+', 'ent', 'ent')         : 'ent',
            ('+', 'ent', 'flot')        : 'flot',
            ('+', 'flot', 'ent')        : 'flot',
            ('+', 'flot', 'flot')       : 'flot',
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

    def emparejar_tipo(self, tupla):
        tipo = self.cubo.get(tupla)
        if tipo:
            return tipo
        else:
            raise Exception("Tipos incompatibles: " + tupla[1] + " " + tupla[0] + " " + tupla[2])