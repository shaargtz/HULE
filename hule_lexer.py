from ply import lex

tokens = [
    'IGUAL_QUE',
    'DIFERENTE_QUE',
    'CTE_ENT',
    'CTE_FLOT',
    'CTE_CAR',
    'CTE_CADENA',
    'ID'
]

reserved = {
    'hule' : 'HULE',
    'func' : 'FUNC',
    'var' : 'VAR',
    'si' : 'SI',
    'sino' : 'SINO',
    'vacia' : 'VACIA',
    'bool' : 'BOOL',
    'ent' : 'ENT',
    'flot' : 'FLOT',
    'car' : 'CAR',
    'cadena' : 'CADENA',
    'por' : 'POR',
    'en' : 'EN',
    'mientras' : 'MIENTRAS',
    'regresa' : 'REGRESA',
    'imprime' : 'IMPRIME',
    'sen' : 'SEN',
    'cos' : 'COS',
    'tan' : 'TAN',
    'senh' : 'SENH',
    'cosh' : 'COSH',
    'tanh' : 'TANH',
    'min' : 'MIN',
    'max' : 'MAX',
    'largo' : 'LARGO',
    'media' : 'MEDIA',
    'moda' : 'MODA',
    'mediana' : 'MEDIANA',
    'piso' : 'PISO',
    'techo' : 'TECHO',
    'aleatorio' : 'ALEATORIO',
    'poder' : 'PODER',
    'log' : 'LOG',
    'abs' : 'ABS',
    'graficar' : 'GRAFICAR',
}

literals = ',;][}{)(=+-*/><=&|'

tokens = tokens + list(reserved.values())

t_IGUAL_QUE = r'=='
t_DIFERENTE_QUE = r'!='

t_CTE_ENT = r'[0-9]+'
t_CTE_FLOT = r'[0-9]+\.[0-9]+'
t_CTE_CAR = r'\'.\''
t_CTE_CADENA = r'\'.{2,}\''

t_ignore = ' \t'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Caracter invalido '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()