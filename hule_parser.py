from ply import yacc
from hule_lexer import tokens
from directorio_funciones import DirFunciones
from cubo_semantico import CuboSemantico
from memoria_virtual import VonNeumann
from maquina_virtual import MaquinaVirtual
from tabla_variables import Variables
from tabla_constantes import Constantes

dir_funciones = DirFunciones()
cubo_semantico = CuboSemantico()
memoria = VonNeumann()
ctes = Constantes()

func_actual = 'hule'
tipo_actual = None

cuadruplos = []

def p_programa(t):
    '''
    programa : p1 dec HULE p2 '(' ')' '{' bloque '}'
    '''
    # borrar todo en memoria al final

def p_p1(t):
    '''
    p1 : nulo
    '''
    cuadruplos.append(['GOTO', -1, -1, None])

def p_p2(t):
    '''
    p2 : nulo
    '''
    # indicar al primer cuadruplo donde empieza hule()
    cuadruplos[0][3] = len(cuadruplos)
    global func_actual
    func_actual = 'hule'

def p_dec(t):
    '''
    dec : dec_var dec
        | dec_func dec
        | nulo
    '''
    
def p_dec_var(t):
    '''
    dec_var : p3 VAR tipo ID p4 dec_var_prima ';'
    '''

def p_p3(t):
    '''
    p3 : nulo
    '''
    if not dir_funciones.directorio[func_actual][1]:
        if func_actual == 'hule':
            dir_funciones.directorio[func_actual][1] = Variables('global')
        else:
            dir_funciones.directorio[func_actual][1] = Variables('local')

def p_p4(t):
    '''
    p4 : nulo
    '''
    global tipo_actual
    tipo_actual = t[-2]
    dir_funciones.directorio[func_actual][1].insertar(tipo_actual, t[-1])
    
def p_dec_var_prima(t):
    '''
    dec_var_prima : ',' ID p5 dec_var_prima
                  | nulo
    '''

def p_p5(t):
    '''
    p5 : nulo
    '''
    dir_funciones.directorio[func_actual][1].insertar(tipo_actual, t[-1])
    
# por hacer : corregir la declaracion de listas y matrices

def p_dec_lista(t):
    '''
    dec_lista : VAR tipo ID dimension dec_lista_prima ';'
    '''
    
def p_dec_lista_prima(t):
    '''
    dec_lista_prima : ',' ID dimension dec_lista_prima
                    | nulo
    '''
    
def p_dec_matriz(t):
    '''
    dec_matriz : VAR tipo ID dimension dimension dec_matriz_prima ';'
    '''
    
def p_dec_matriz_prima(t):
    '''
    dec_matriz_prima : ',' ID dimension dimension dec_matriz_prima
                     | nulo
    '''
    
def p_dimension(t):
    '''
    dimension : '[' CTE_ENT ']'
    '''

def p_dec_func(t):
    '''
    dec_func : FUNC super_tipo ID p6 '(' param ')' '{' bloque '}' ';'
    '''
    # borrar tabla de variables al terminar de generar sus cuadruplos
    # dir_funciones.directorio[func_actual][1] = None

def p_p6(t):
    '''
    p6 : nulo
    '''
    global func_actual
    func_actual = t[-1]
    dir_funciones.insertar(func_actual, t[-2])
    
def p_super_tipo(t):
    '''
    super_tipo : tipo 
               | VACIO 
    '''
    t[0] = t[1]

def p_tipo(t):
    '''
    tipo : ENT 
         | FLOT 
         | CAR 
         | CADENA
    '''
    t[0] = t[1]

def p_param(t):
    '''
    param : tipo ID p7 param_prima
          | nulo
    '''
    
def p_param_prima(t):
    '''
    param_prima : ',' tipo ID p7 param_prima
                | nulo
    '''

def p_p7(t):
    '''
    p7 : nulo
    '''
    if not dir_funciones.directorio[func_actual][1]:
        dir_funciones.directorio[func_actual][1] = Variables('local')
    dir_funciones.directorio[func_actual][1].insertar(t[-2], t[-1])
    dir_funciones.directorio[func_actual][2].append(t[-2])

def p_bloque(t):
    '''
    bloque : est bloque
           | nulo
    '''

def p_est(t):
    '''
    est : dec_var
        | asig
        | ciclo_m
        | ciclo_p
        | cond
        | llama_func
        | retorno
    '''
    
def p_asig(t):
    '''
    asig : ID '=' hiper_exp ';'
    '''
    # hardcoded
    cuadruplos.append([t[2], t[3], -1, dir_funciones.buscar_variable(func_actual, t[1])])

def p_ciclo_m(t):
    '''
    ciclo_m : MIENTRAS '(' hiper_exp ')' '{' bloque '}' ';'
    '''

def p_ciclo_p(t):
    '''
    ciclo_p : POR '(' ID EN ID ')' '{' bloque '}' ';'
    '''

def p_cond(t):
    '''
    cond : SI '(' hiper_exp ')' '{' bloque '}' sino ';'
    '''

def p_sino(t):
    '''
    sino : SINO '{' bloque '}'
         | nulo
    '''
    
def p_llama_func(t):
    '''
    llama_func : ID '(' llama_param ')' ';'
    '''

def p_llama_param(t):
    '''
    llama_param : ID llama_param_prima
                | cte llama_param_prima
                | nulo
    '''

def p_llama_param_prima(t):
    '''
    llama_param_prima : ',' ID llama_param_prima
                      | nulo
    '''

def p_retorno(t):
    '''
    retorno : REGRESA hiper_exp
    '''

def p_hiper_exp(t):
    '''
    hiper_exp : super_exp hiper_exp_prima
    '''
    t[0] = t[1]

def p_hiper_exp_prima(t):
    '''
    hiper_exp_prima : '&' super_exp
                    | '|' super_exp
                    | nulo
    '''
    
def p_super_exp(t):
    '''
    super_exp : exp super_exp_prima
    '''
    t[0] = t[1]

def p_super_exp_prima(t):
    '''
    super_exp_prima : '>' exp
                    | '<' exp
                    | IGUAL_QUE exp
                    | DIFERENTE_QUE exp
                    | nulo
    '''
    
def p_exp(t):
    '''
    exp : term exp_prima
    '''
    # hardcoded el tipo

    # tengo que regresar el espacio de memoria ya sea
    # del factor o del temporal que tiene el resultado de la operacion
   
    if t[2]:
        temp = dir_funciones.directorio[func_actual][1].insertar('ent')
        cuadruplos.append([t[2][0], t[1], t[2][1], temp])
        t[0] = temp
    else:
        t[0] = t[1]

def p_exp_prima(t):
    '''
    exp_prima : '+' term
              | '-' term
              | nulo
    '''
    if t[1]:
        t[0] = [t[1], t[2]]
    else: 
        t[0] = None
    
def p_term(t):
    '''
    term : factor term_prima
    '''
    t[0] = t[1]

def p_term_prima(t):
    '''
    term_prima : '*' factor
               | '/' factor
               | nulo
    '''

def p_factor(t):
    '''
    factor : llama_func
           | cte
           | var
    '''
    t[0] = t[1]

def p_cte(t):
    '''
    cte : CTE_ENT
        | CTE_FLOT
        | CTE_CAR
        | CTE_CADENA
    '''
    # hardcoded el tipo
    t[0] = ctes.insertar(t[1], 'ent')

def p_var(t):
    '''
    var : ID
        | ID '[' hiper_exp ']'
        | ID '[' hiper_exp ']' '[' hiper_exp ']'
    '''
    # hardcoded
    t[0] = dir_funciones.buscar_variable(func_actual, t[1])

def p_nulo(t):
    '''
    nulo :
    '''
    pass

def p_error(t):
    '''
    '''
    raise Exception("Error en linea " + str(t.lineno))

parser = yacc.yacc()

codigo_1 = '''
func ent f(flot a, flot b) {
    var flot k;
    var flot l;
    l = a - 5;
    k = l * b;
};
hule() 
{
    var ent a, b, c[5];
    a = 2;
    b = 3;
    si (a < b) 
    {
        f('bbb');
    } sino {
        f('aaa');
    };
}
'''

codigo_2 = '''
hule() 
{ 
    var ent a;
    var ent b;
    a = 2;
    b = 3;
    a = a + b;
}
'''

parser.parse(codigo_2)

for i in cuadruplos:
    print(i)
print(dir_funciones.directorio['hule'][1].tabla)
print(ctes.tabla)