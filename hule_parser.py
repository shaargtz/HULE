from ply import yacc
from hule_lexer import tokens
from directorio_funciones import DirFunciones
from cubo_semantico import CuboSemantico
from maquina_virtual import MaquinaVirtual
from tabla_variables import Variables
from tabla_constantes import Constantes
from utilidad import *
import json
import pprint

dir_funciones = DirFunciones()
cubo_semantico = CuboSemantico()
ctes = Constantes()

pila_o = []
p_oper = []
pila_saltos = []
pila_tipos = []
pila_func = []

cuadruplos = []

def p_programa(t):
    '''
    programa : p1 dec HULE p2 '(' ')' '{' bloque '}'
    '''
    # borrar todo en memoria al final
    cuadruplos.append(['ENDPROG', -1, -1, -1])

def p_p1(t):
    '''
    p1 : nulo
    '''
    pila_func.append('hule')
    cuadruplos.append(['GOTO', -1, -1, None])

def p_p2(t):
    '''
    p2 : nulo
    '''
    # indicar al primer cuadruplo donde empieza hule()
    cuadruplos[0][3] = len(cuadruplos)

def p_dec(t):
    '''
    dec : dec_var dec
        | dec_func dec
        | nulo
    '''

# puedo usar variables globales en una funcion?

def p_dec_var(t):
    '''
    dec_var : p3 VAR tipo ID p4 dec_var_prima ';'
    '''
    pila_tipos.pop()

def p_p3(t):
    '''
    p3 : nulo
    '''
    if not dir_funciones.tiene_tabla_var(pila_func[-1]):
        if pila_func[-1] == 'hule':
            dir_funciones.insertar_tabla_var(pila_func[-1], 'global')
        else:
            dir_funciones.insertar_tabla_var(pila_func[-1], 'local')

def p_p4(t):
    '''
    p4 : nulo
    '''
    pila_tipos.append(t[-2])
    dir_funciones.insertar_variable(pila_func[-1], pila_tipos[-1], t[-1])
    
def p_dec_var_prima(t):
    '''
    dec_var_prima : ',' ID p5 dec_var_prima
                  | nulo
    '''

def p_p5(t):
    '''
    p5 : nulo
    '''
    dir_funciones.insertar_variable(pila_func[-1], pila_tipos[-1], t[-1])
    
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
    dec_func : FUNC super_tipo ID p6 '(' param ')' p16 '{' bloque '}' ';'
    '''
    # todo: borrar tabla de variables al terminar de generar sus cuadruplos
    # todo: parametros endfunc
    pila_func.pop()
    cuadruplos.append(['ENDFUNC', None, None, None])

def p_p6(t):
    '''
    p6 : nulo
    '''
    pila_func.append(t[-1])
    dir_funciones.insertar_funcion(pila_func[-1], t[-2])

def p_p16(t):
    '''
    p16 : nulo
    '''
    dir_funciones.directorio[pila_func[-1]][4] = len(cuadruplos)
    
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
         | BOOL
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
    if not dir_funciones.tiene_tabla_var(pila_func[-1]):
        dir_funciones.insertar_tabla_var(pila_func[-1], 'local')
    dir_funciones.insertar_variable(pila_func[-1], t[-2], t[-1])
    dir_funciones.insertar_parametro(pila_func[-1], t[-2])

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
        | llama_func_est
        | retorno
    '''
    
def p_asig(t):
    '''
    asig : ID '=' hiper_exp ';'
    '''
    op_izq = dir_funciones.buscar_variable(pila_func[-1], t[1])
    tipo_izq = checar_tipo_memoria(op_izq)
    op_der = pila_o.pop()
    tipo_der = pila_tipos.pop()
    if (tipo_izq != tipo_der):
        raise Exception("Asignacion incompatible: " + tipo_izq + " = " + tipo_der)
    cuadruplos.append([t[2], op_der, -1, op_izq])

def p_ciclo_m(t):
    '''
    ciclo_m : MIENTRAS p11 '(' hiper_exp ')' p12 '{' bloque '}' ';'
    '''
    fin_ciclo = pila_saltos.pop()
    retorno = pila_saltos.pop()
    cuadruplos.append(['GOTO', -1, -1, retorno])
    cuadruplos[fin_ciclo][3] = len(cuadruplos)

def p_p11(t):
    '''
    p11 : nulo
    '''
    pila_saltos.append(len(cuadruplos))

def p_p12(t):
    '''
    p12 : nulo
    '''
    tipo_exp = pila_tipos.pop()
    if tipo_exp != 'bool':
        raise Exception("Ciclo MIENTRAS esperaba una expresion bool y encontro " + tipo_exp)
    else:
        cuadruplos.append(['GOTOF', pila_o.pop(), -1, None])
        pila_saltos.append(len(cuadruplos) - 1)

def p_ciclo_p(t):
    '''
    ciclo_p : POR '(' ID EN ID ')' '{' bloque '}' ';'
    '''

def p_cond(t):
    '''
    cond : SI '(' hiper_exp ')' p9 '{' bloque '}' sino ';'
    '''
    fin_cond = pila_saltos.pop()
    cuadruplos[fin_cond][3] = len(cuadruplos)

def p_p9(t):
    '''
    p9 : nulo
    '''
    tipo_exp = pila_tipos.pop()
    if tipo_exp != 'bool':
        raise Exception("Condicion SI esperaba una expresion bool y encontro " + tipo_exp)
    else:
        cuadruplos.append(['GOTOF', pila_o.pop(), -1, None])
        pila_saltos.append(len(cuadruplos) - 1)

def p_sino(t):
    '''
    sino : SINO p10 '{' bloque '}'
         | nulo
    '''
    
def p_p10(t):
    '''
    p10 : nulo
    '''
    cuadruplos.append(['GOTO', -1, -1, None])
    falso = pila_saltos.pop()
    pila_saltos.append(len(cuadruplos) - 1)
    cuadruplos[falso][3] = len(cuadruplos)

def p_llama_func_est(t):
    '''
    llama_func_est : ID p15 '(' llama_param ')' ';'
    '''
    # todo: parametros gosub
    cuadruplos.append(['GOSUB', None, None, None])
    pila_func.pop()

def p_p15(t):
    '''
    p15 : nulo
    '''
    func = dir_funciones.directorio.get(t[-1])
    if func:
        pila_func.append(t[-1])
        mem = func[3]['total']
        cuadruplos.append(['ERA', mem, -1, -1])
    else:
        raise Exception("Funcion " + t[-1] + " no esta definida")

def p_llama_param(t):
    '''
    llama_param : ID llama_param_prima
                | cte llama_param_prima
                | p17 nulo
    '''

def p_llama_param_prima(t):
    '''
    llama_param_prima : ',' ID llama_param_prima
                      | nulo
    '''

def p_p17(t):
    '''
    p17 : nulo
    '''
    if pila_tipos[-1] != 'vacio':
        raise Exception("Funcion " + pila_func[-1] + " requiere parametros y no se llamaron")

def p_retorno(t):
    '''
    retorno : REGRESA hiper_exp
    '''

def p_hiper_exp(t):
    '''
    hiper_exp : super_exp super_exp_prima
    '''
    if p_oper and (p_oper[-1] in ['&', '|']):
        op_derecho = pila_o.pop()
        tipo_derecho = pila_tipos.pop()
        op_izquierdo = pila_o.pop()
        tipo_izquierdo = pila_tipos.pop()
        operador = p_oper.pop()
        tipo_resultado = cubo_semantico.emparejar_tipo((operador, tipo_izquierdo, tipo_derecho))
        resultado = dir_funciones.insertar_variable(pila_func[-1], tipo_resultado)
        cuadruplos.append([operador, op_izquierdo, op_derecho, resultado])
        pila_o.append(resultado)
        pila_tipos.append(tipo_resultado)

def p_super_exp_prima(t):
    '''
    super_exp_prima : '&' super_exp
                    | '|' super_exp
                    | nulo
    '''
    
def p_super_exp(t):
    '''
    super_exp : exp exp_prima
    '''
    if p_oper and (p_oper[-1] in ['>', '<', '!=', '==']):
        op_derecho = pila_o.pop()
        tipo_derecho = pila_tipos.pop()
        op_izquierdo = pila_o.pop()
        tipo_izquierdo = pila_tipos.pop()
        operador = p_oper.pop()
        tipo_resultado = cubo_semantico.emparejar_tipo((operador, tipo_izquierdo, tipo_derecho))
        resultado = dir_funciones.insertar_variable(pila_func[-1], tipo_resultado)
        cuadruplos.append([operador, op_izquierdo, op_derecho, resultado])
        pila_o.append(resultado)
        pila_tipos.append(tipo_resultado)

def p_exp_prima(t):
    '''
    exp_prima : '>' p14 exp
              | '<' p14 exp
              | IGUAL_QUE p14 exp
              | DIFERENTE_QUE p14 exp
              | nulo
    '''
    
def p_exp(t):
    '''
    exp : term term_prima
    '''
    if p_oper and (p_oper[-1] in ['+', '-']):
        op_derecho = pila_o.pop()
        tipo_derecho = pila_tipos.pop()
        op_izquierdo = pila_o.pop()
        tipo_izquierdo = pila_tipos.pop()
        operador = p_oper.pop()
        tipo_resultado = cubo_semantico.emparejar_tipo((operador, tipo_izquierdo, tipo_derecho))
        resultado = dir_funciones.insertar_variable(pila_func[-1], tipo_resultado)
        cuadruplos.append([operador, op_izquierdo, op_derecho, resultado])
        pila_o.append(resultado)
        pila_tipos.append(tipo_resultado)

def p_term_prima(t):
    '''
    term_prima : '+' p14 term
               | '-' p14 term
               | nulo
    '''
    
def p_term(t):
    '''
    term : factor factor_prima
    '''
    if p_oper and (p_oper[-1] in ['*', '/']):
        op_derecho = pila_o.pop()
        tipo_derecho = pila_tipos.pop()
        op_izquierdo = pila_o.pop()
        tipo_izquierdo = pila_tipos.pop()
        operador = p_oper.pop()
        tipo_resultado = cubo_semantico.emparejar_tipo((operador, tipo_izquierdo, tipo_derecho))
        resultado = dir_funciones.insertar_variable(pila_func[-1], tipo_resultado)
        cuadruplos.append([operador, op_izquierdo, op_derecho, resultado])
        pila_o.append(resultado)
        pila_tipos.append(tipo_resultado)

def p_factor_prima(t):
    '''
    factor_prima : '*' p14 factor
                 | '/' p14 factor
                 | nulo
    '''

def p_p14(t):
    '''
    p14 : nulo
    '''
    p_oper.append(t[-1])

def p_factor(t):
    '''
    factor : llama_func_exp
           | cte
           | var
    '''
    # no funciona la llamada de funcion

def p_llama_func_exp(t):
    '''
    llama_func_exp : ID '(' llama_param ')'
    '''
    # todo: parametros gosub
    cuadruplos.append(['GOSUB', None, None, None])
    pila_func.pop()

def p_cte(t):
    '''
    cte : CTE_ENT p8_1
        | CTE_FLOT p8_2
        | CTE_CAR p8_3
        | CTE_CADENA p8_4
    '''
    mem = ctes.insertar(t[1], pila_tipos[-1])
    pila_o.append(mem)

# checar si usare constantes booleanas

def p_p8_1(t):
    '''
    p8_1 : nulo
    '''
    pila_tipos.append('ent')

def p_p8_2(t):
    '''
    p8_2 : nulo
    '''
    pila_tipos.append('flot')

def p_p8_3(t):
    '''
    p8_3 : nulo
    '''
    pila_tipos.append('car')

def p_p8_4(t):
    '''
    p8_4 : nulo
    '''
    pila_tipos.append('cadena')

def p_var(t):
    '''
    var : ID
        | ID '[' hiper_exp ']'
        | ID '[' hiper_exp ']' '[' hiper_exp ']'
    '''
    # hardcoded para unicamente la primer regla
    mem = dir_funciones.buscar_variable(pila_func[-1], t[1])
    pila_o.append(mem)
    pila_tipos.append(checar_tipo_memoria(mem))

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
    var ent a, b;
    var flot c;
    var bool d;
    a = 2;
    b = 3;
    a = a + b;
    c = b * 1.5;
    d = a > c;
    si (d) {
        a = b - 5;
    } sino {
        c = a * 0.6;
    };
    mientras (b < c) {
        b = b + 2;
    };
}
'''

parser.parse(codigo_2)

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(cuadruplos)
pp.pprint(dir_funciones.directorio['hule'][1].tabla)
pp.pprint(ctes.tabla)