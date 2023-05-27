from ply import yacc
from hule_lexer import tokens
from directorio_funciones import DirFunciones
from cubo_semantico import CuboSemantico
from utilidad import *
from maquina_virtual import MaquinaVirtual

dir_funciones = DirFunciones()
cubo_semantico = CuboSemantico()

pila_o = []
pil_oper = []
pila_saltos = []
pila_tipos = []
pila_func = []
pila_llam = []

cuadruplos = []

def p_programa(t):
    '''
    programa : p1 dec HULE p2 '(' ')' '{' bloque '}'
    '''
    # todo: borrar todo en memoria al final
    cuadruplos.append(['ENDPROG', -1, -1, -1])

def p_p1(t):
    '''
    p1 : nulo
    '''
    cuadruplos.append(['GOTO', -1, -1, None])
    dir_funciones.insertar_funcion('global', 'vacia')
    pila_func.append('global')

def p_p2(t):
    '''
    p2 : nulo
    '''
    cuadruplos[0][3] = len(cuadruplos)
    pila_func.append('hule')
    cuadruplos.append(['INSTANCIAR', -1, -1, -1])

def p_dec(t):
    '''
    dec : dec_var dec
        | dec_func dec
        | nulo
    '''

def p_dec_var(t):
    '''
    dec_var : dec_var_simple
            | dec_lista
            | dec_matriz
    '''
    pila_tipos.pop()

def p_dec_var_simple(t):
    '''
    dec_var_simple : p3 VAR tipo ID p4 dec_var_prima ';'
    '''
    pila_tipos.pop()

def p_p3(t):
    '''
    p3 : nulo
    '''
    if not dir_funciones.tiene_tabla_var(pila_func[-1]):
        if (pila_func[-1] == 'global'):
            dir_funciones.insertar_tabla_var('global', 'global')
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
    cuadruplos.append(['ENDFUNC', -1, -1, -1])

def p_p6(t):
    '''
    p6 : nulo
    '''
    pila_func.append(t[-1])
    dir_funciones.insertar_funcion(pila_func[-1], t[-2])
    if t[-2] != 'vacia':
        if not dir_funciones.tiene_tabla_var('global'):
            dir_funciones.insertar_tabla_var('global', 'global')
        ret = dir_funciones.insertar_variable('global', t[-2], '_' + t[-1])
        dir_funciones.insertar_retorno(pila_func[-1], ret)

def p_p16(t):
    '''
    p16 : nulo
    '''
    dir_funciones.directorio[pila_func[-1]][3] = len(cuadruplos)
    
def p_super_tipo(t):
    '''
    super_tipo : tipo 
               | VACIA 
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
    dir_funciones.insertar_parametro(pila_func[-1], t[-2], t[-1])

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
        | imprimir
    '''
    
def p_asig(t):
    '''
    asig : var '=' hiper_exp ';'
    '''
    op_der = pila_o.pop()
    tipo_der = pila_tipos.pop()
    op_izq = pila_o.pop()
    tipo_izq = pila_tipos.pop()
    if (tipo_izq != tipo_der):
        raise Exception("Asignacion incompatible: " + tipo_izq + " = " + tipo_der)
    cuadruplos.append([t[2], op_der, -1, op_izq])

def p_ciclo_m(t):
    '''
    ciclo_m : MIENTRAS p11 '(' hiper_exp ')' p12 '{' bloque '}'
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
    ciclo_p : POR '(' ID EN ID ')' '{' bloque '}'
    '''
    # hasta que haga listas

def p_cond(t):
    '''
    cond : SI '(' hiper_exp ')' p9 '{' bloque '}' sino
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
    llama_func_est : llama_func_exp ';'
    '''

def p_retorno(t):
    '''
    retorno : REGRESA hiper_exp ';'
    '''
    val = pila_o.pop()
    pila_tipos.pop()
    retorno = dir_funciones.buscar_variable(pila_func[-1], '_' + pila_func[-1])
    cuadruplos.append(['REGRESA', val, -1, retorno])

def p_imprimir(t):
    '''
    imprimir : IMPRIME '(' hiper_exp ')' ';'
    '''
    cuadruplos.append(['imprime', -1, -1, pila_o.pop()])
    pila_tipos.pop()

def p_hiper_exp(t):
    '''
    hiper_exp : super_exp super_exp_prima
    '''
    if pil_oper and (pil_oper[-1] in ['&', '|']):
        op_derecho = pila_o.pop()
        tipo_derecho = pila_tipos.pop()
        op_izquierdo = pila_o.pop()
        tipo_izquierdo = pila_tipos.pop()
        operador = pil_oper.pop()
        tipo_resultado = cubo_semantico.emparejar_tipo((operador, tipo_izquierdo, tipo_derecho))
        resultado = dir_funciones.insertar_variable(pila_func[-1], tipo_resultado)
        cuadruplos.append([operador, op_izquierdo, op_derecho, resultado])
        pila_o.append(resultado)
        pila_tipos.append(tipo_resultado)

def p_super_exp_prima(t):
    '''
    super_exp_prima : '&' p14 super_exp
                    | '|' p14 super_exp
                    | nulo
    '''
    
def p_super_exp(t):
    '''
    super_exp : exp exp_prima
    '''
    if pil_oper and (pil_oper[-1] in ['>', '<', '!=', '==']):
        op_derecho = pila_o.pop()
        tipo_derecho = pila_tipos.pop()
        op_izquierdo = pila_o.pop()
        tipo_izquierdo = pila_tipos.pop()
        operador = pil_oper.pop()
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
    if pil_oper and (pil_oper[-1] in ['+', '-']):
        op_derecho = pila_o.pop()
        tipo_derecho = pila_tipos.pop()
        op_izquierdo = pila_o.pop()
        tipo_izquierdo = pila_tipos.pop()
        operador = pil_oper.pop()
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
    if pil_oper and (pil_oper[-1] in ['*', '/']):
        op_derecho = pila_o.pop()
        tipo_derecho = pila_tipos.pop()
        op_izquierdo = pila_o.pop()
        tipo_izquierdo = pila_tipos.pop()
        operador = pil_oper.pop()
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
    pil_oper.append(t[-1])

def p_p17(t):
    '''
    p17 : nulo
    '''
    pil_oper.pop()

def p_factor(t):
    '''
    factor : llama_func_exp
           | cte
           | var
           | sub_exp
    '''

def p_sub_exp(t):
    '''
    sub_exp : '(' p14 hiper_exp ')' p17
    '''

def p_llama_func_exp(t):
    '''
    llama_func_exp : ID p15 '(' p14 arg ')' p17
    '''
    if pila_llam[-1][1][0] < pila_llam[-1][1][1]:
        raise Exception("Funcion " + t[1] + " fue llamada con menos argumentos de los requeridos")
    cuadruplos.append(['GOSUB', -1, -1, dir_funciones.buscar_cuadruplo(t[1])])
    tipo_retorno = dir_funciones.buscar_tipo_funcion(pila_llam[-1][0])
    if tipo_retorno != 'vacia':
        retorno_glob = dir_funciones.buscar_variable(pila_llam[-1][0], '_' + t[1])
        pila_llam.pop()
        retorno_temp = dir_funciones.insertar_variable(pila_llam[-1][0], tipo_retorno)
        cuadruplos.append(['=', retorno_glob, -1, retorno_temp])
        pila_o.append(retorno_temp)
        pila_tipos.append(checar_tipo_memoria(retorno_temp))
    pila_llam.pop()

def p_p15(t):
    '''
    p15 : nulo
    '''
    func = dir_funciones.directorio.get(t[-1])
    pila_llam.append([pila_func[-1], []])
    if func:
        pila_llam.append([t[-1], []])
        cuadruplos.append(['ERA', -1, -1, t[-1]])
        pila_llam[-1][1] = [0, len(func[2])]
    else:
        raise Exception("Funcion " + t[-1] + " no esta definida")

def p_arg(t):
    '''
    arg : hiper_exp p13 arg_prima
        | nulo
    '''

def p_arg_prima(t):
    '''
    arg_prima : ',' hiper_exp p13 arg_prima
              | nulo
    '''

def p_p13(t):
    '''
    p13 : nulo
    '''
    if pila_llam[-1][1][0] == pila_llam[-1][1][1]:
        raise Exception("Funcion " + pila_llam[-1][1] + " fue llamada con mas argumentos de los requeridos")
    arg = pila_o.pop()
    tipo_arg = pila_tipos.pop()
    direccion = dir_funciones.comparar_parametro(pila_llam[-1][0], pila_llam[-1][1][0], tipo_arg)
    cuadruplos.append(['PARAM', arg, -1, direccion])
    pila_llam[-1][1][0] += 1

def p_cte(t):
    '''
    cte : CTE_ENT p8_1
        | CTE_FLOT p8_2
        | CTE_CAR p8_3
        | CTE_CADENA p8_4
    '''
    mem = dir_funciones.insertar_constante(pila_tipos[-1], t[1])
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
    direccion = dir_funciones.buscar_variable(pila_func[-1], t[1])
    pila_o.append(direccion)
    pila_tipos.append(checar_tipo_memoria(direccion))

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
func ent fact(ent a) {
    si (a == 1 | a == 0) {
        regresa 1;
    } sino {
        regresa a * fact(a - 1);
    }
};
hule() 
{
    imprime(fact(10));
    imprime(3 - (4 * (5 - 2)));
}
'''

codigo_2 = '''
var ent a, b;
func vacia imprime_x_veces(cadena w, ent veces) {
    var ent cont;
    cont = 0;
    mientras (cont < veces) {
        imprime(w);
        cont = cont + 1;
    }
};
func ent exponente(ent base, ent exp) {
    var ent res;
    res = 1;
    mientras (exp > 0) {
        res = res * base;
        exp = exp - 1;
    }
    regresa res;
};
hule() 
{
    var ent c;
    a = 3;
    b = 4;
    c = a + b;
    mientras (c > b){
        b = b + 1;
        a = a * 2;
    }
    si (a / 3 > 10) {
        imprime('aaa');
    } sino {
        imprime('bbb');
    }
    imprime(c);
    imprime(a);
    imprime_x_veces('hola', 5);
    imprime(exponente(3, exponente(2, 3)));
}
'''

parser.parse(codigo_2)

imprimir_cuadruplos(cuadruplos)
imprimir_tabla_variables(dir_funciones)

mv = MaquinaVirtual(cuadruplos, dir_funciones)
mv.ejecutar()
mv.imprimir_memoria()