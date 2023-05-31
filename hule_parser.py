from ply import yacc
from hule_lexer import tokens
from directorio_funciones import DirFunciones
from cubo_semantico import CuboSemantico
from utilidad import *

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
    dec_var : p3 VAR tipo ID dimensiones p4 dec_var_prima ';'
    '''
    pila_tipos.pop()
    pila_o.pop()

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
    pila_tipos.append(t[-3])
    dir_funciones.insertar_variable(pila_func[-1], pila_tipos[-1], t[-2], t[-1])
    pila_o.append(t[-2])

def p_dec_var_prima(t):
    '''
    dec_var_prima : ',' ID dimensiones p5 dec_var_prima p5_1
                  | nulo
    '''

def p_p5(t):
    '''
    p5 : nulo
    '''
    dir_funciones.insertar_variable(pila_func[-1], pila_tipos[-1], t[-2], t[-1])
    pila_o.append(t[-2])

def p_p5_1(t):
    '''
    p5_1 : nulo
    '''
    pila_o.pop()

def p_dimensiones(t):
    '''
    dimensiones : dimension dimension dimension
                | dimension dimension
                | dimension
                | nulo
    '''
    if t[1]:
        t[0] = []
        for i in range(1, len(t)):
            t[0].append(int(t[i]))

def p_dimension(t):
    '''
    dimension : '[' CTE_ENT ']'
    '''
    t[0] = t[2]

def p_dec_func(t):
    '''
    dec_func : FUNC super_tipo ID p6 '(' param ')' p16 '{' bloque '}' ';'
    '''
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
        | graf
    '''

def p_graf(t):
    '''
    graf : GRAFICAR '(' ID ',' ID ')' ';' p27
    '''

def p_p27(t):
    '''
    p27 : nulo
    '''
    dir_val = dir_funciones.buscar_variable(pila_func[-1], t[-5])
    dims_val = dir_funciones.buscar_dimensiones(pila_func[-1], t[-5])
    dir_etiq = dir_funciones.buscar_variable(pila_func[-1], t[-3])
    dims_etiq = dir_funciones.buscar_dimensiones(pila_func[-1], t[-3])
    if checar_tipo_memoria(dir_etiq) not in ['car', 'cadena']:
        raise Exception("Funcion graficar() que el segundo arreglo sea de tipo caracter o cadena")
    if len(dims_val) < 1 or len(dims_etiq) < 1:
        raise Exception("Funcion graficar() espera dos argumento tipo arreglo y encontro una variable")
    elif len(dims_val) > 1 or len(dims_etiq) > 1:
        raise Exception("Funcion graficar() espera dos arreglos de una dimension y encontro uno de {}".format(max(len(dims_val), len(dims_etiq))))
    elif dims_val[0] != dims_etiq[0]:
        raise Exception("Funcion graficar() espera dos arreglos del mismo tamaño")
    cuadruplos.append(['graficar', dir_val, dir_etiq, dims_val[0] + 1])

def p_asig(t):
    '''
    asig : var '=' hiper_exp ';'
    '''
    op_der = pila_o.pop()
    tipo_der = pila_tipos.pop()
    op_izq = pila_o.pop()
    tipo_izq = pila_tipos.pop()
    if tipo_izq != tipo_der:
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
    ciclo_p : POR '(' ID EN hiper_exp ')' p25 '{' bloque '}'
    '''
    fin_ciclo = pila_saltos.pop()
    retorno = pila_saltos.pop()
    contador = pila_o.pop()
    uno = dir_funciones.insertar_constante('ent', 1)
    cuadruplos.append(['+', contador, uno, contador])
    cuadruplos.append(['GOTO', -1, -1, retorno])
    cuadruplos[fin_ciclo][3] = len(cuadruplos)
    
def p_p25(t):
    '''
    p25 : nulo
    '''
    limite = pila_o.pop()
    limite_t = pila_tipos.pop()
    if limite_t != 'ent':
        raise Exception("Solo se pueden usar limites enteros para el ciclo POR")
    contador = dir_funciones.insertar_variable(pila_func[-1], 'ent', t[-4])
    cero = dir_funciones.insertar_constante('ent', 0)
    cuadruplos.append(['=', cero, -1, contador])
    pila_saltos.append(len(cuadruplos))
    chequeo = dir_funciones.insertar_variable(pila_func[-1], 'bool')
    cuadruplos.append(['<', contador, limite, chequeo])
    cuadruplos.append(['GOTOF', chequeo, -1, None])
    pila_saltos.append(len(cuadruplos) - 1)
    pila_o.append(contador)

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
    super_exp_prima : '&' p14 hiper_exp
                    | '|' p14 hiper_exp
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
    exp_prima : '>' p14 super_exp
              | '<' p14 super_exp
              | IGUAL_QUE p14 super_exp
              | DIFERENTE_QUE p14 super_exp
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
    term_prima : '+' p14 exp
               | '-' p14 exp
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
    factor_prima : '*' p14 term
                 | '/' p14 term
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
    factor : func_esp
           | llama_func_exp
           | cte
           | var
           | sub_exp
           | lee
           | conversion
    '''

def p_conversion(t):
    '''
    conversion : tipo '(' p14 hiper_exp ')' p17
    '''
    valor = pila_o.pop()
    print(valor, t[1], pila_tipos.pop())
    temp = dir_funciones.insertar_variable(pila_func[-1], t[1])
    cuadruplos.append([t[1], valor, -1, temp])
    pila_o.append(temp)
    pila_tipos.append(t[1])

def p_lee(t):
    '''
    lee : LEE '(' ')'
    '''
    temp = dir_funciones.insertar_variable(pila_func[-1], 'cadena')
    cuadruplos.append(['LEE', -1, -1, temp])
    pila_o.append(temp)
    pila_tipos.append('cadena')

def p_func_esp(t):
    '''
    func_esp : func_esp_1
             | func_esp_2
    '''

def p_func_esp_1(t):
    '''
    func_esp_1 : SEN '(' p14 hiper_exp ')' p17 p18
               | COS '(' p14 hiper_exp ')' p17 p18
               | TAN '(' p14 hiper_exp ')' p17 p18
               | SENH '(' p14 hiper_exp ')' p17 p18
               | COSH '(' p14 hiper_exp ')' p17 p18
               | TANH '(' p14 hiper_exp ')' p17 p18
               | LOG '(' p14 hiper_exp ')' p17 p18
               | ABS '(' p14 hiper_exp ')' p17 p18
               | PISO '(' p14 hiper_exp ')' p17 p18
               | TECHO '(' p14 hiper_exp ')' p17 p18
               | MEDIA '(' ID ')' p26
               | MODA '(' ID ')' p26
               | MEDIANA '(' ID ')' p26
               | LARGO '(' ID ')' p26
    '''

def p_p18(t):
    '''
    p18 : nulo
    '''
    val = pila_o.pop()
    val_t = pila_tipos.pop()
    if val_t not in ['ent', 'flot']:
        raise Exception("Funcion {}() espera un argumento entero o flotante".format(t[-6]))
    if t[-4] == 'abs':
        temp_t = val_t
    elif t[-4] in ['piso', 'techo']:
        temp_t = 'ent'
    else:
        temp_t = 'flot'
    temp = dir_funciones.insertar_variable(pila_func[-1], temp_t)
    cuadruplos.append([t[-6], val, -1, temp])
    pila_o.append(temp)
    pila_tipos.append(temp_t)

def p_p26(t):
    '''
    p26 : nulo
    '''
    dir = dir_funciones.buscar_variable(pila_func[-1], t[-2])
    dims = dir_funciones.buscar_dimensiones(pila_func[-1], t[-2])
    dir_t = checar_tipo_memoria(dir)
    if len(dims) < 1:
        raise Exception("Funcion {}() espera un argumento tipo arreglo y encontro una variable".format(t[-4]))
    elif len(dims) > 1:
        raise Exception("Funcion {}() espera un arreglo de una dimension y encontro uno de {}".format(t[-4], len(dims)))
    if t[-4] == 'largo':
        temp_t = 'ent'
    else:
        temp_t = 'flot'
        if dir_t not in ['ent', 'flot']:
            raise Exception("Funcion {}() espera un argumento tipo lista ent/flot y encontro una lista {}".format(t[-4], dir_t ))
    temp = dir_funciones.insertar_variable(pila_func[-1], temp_t)
    cuadruplos.append([t[-4], dir, dims[0] + 1, temp])
    pila_o.append(temp)
    pila_tipos.append(temp_t)

def p_func_esp_2(t):
    '''
    func_esp_2 : ALEATORIO '(' p14 hiper_exp p17 ',' p14 hiper_exp ')' p17 p19
               | PODER '(' p14 hiper_exp p17 ',' p14 hiper_exp ')' p17 p19
               | MIN '(' p14 hiper_exp p17 ',' p14 hiper_exp ')' p17 p20
               | MAX '(' p14 hiper_exp p17 ',' p14 hiper_exp ')' p17 p20
    '''

def p_p19(t):
    '''
    p19 : nulo
    '''
    op1 = pila_o.pop()
    op2 = pila_o.pop()
    op1_t = pila_tipos.pop()
    op2_t = pila_tipos.pop()
    if op1_t != 'ent' or op2_t != 'ent':
        raise Exception("Funcion {}() espera dos argumentos de tipo entero".format(t[-10]))
    temp = dir_funciones.insertar_variable(pila_func[-1], op1_t)
    cuadruplos.append([t[-10], op2, op1, temp])
    pila_o.append(temp)
    pila_tipos.append(op1_t)

def p_p20(t):
    '''
    p20 : nulo
    '''
    op1 = pila_o.pop()
    op2 = pila_o.pop()
    op1_t = pila_tipos.pop()
    op2_t = pila_tipos.pop()
    if op2_t != op1_t:
        raise Exception("Funcion {}() espera dos argumentos de tipo entero o dos de tipo flotante".format(t[-8]))
    temp = dir_funciones.insertar_variable(pila_func[-1], op1_t)
    cuadruplos.append([t[-8], op2, op1, temp])
    pila_o.append(temp)
    pila_tipos.append(op1_t)

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
    var : ID '[' p14 hiper_exp ']' p17 '[' p14 hiper_exp ']' p17 '[' p14 hiper_exp ']' p17 p21
        | ID '[' p14 hiper_exp ']' p17 '[' p14 hiper_exp ']' p17 p22
        | ID '[' p14 hiper_exp ']' p17 p23
        | ID p24
    '''

def p_p21(t):
    '''
    p21 : nulo
    '''
    s3 = pila_o.pop()
    s3tipo = pila_tipos.pop()
    s2 = pila_o.pop()
    s2tipo = pila_tipos.pop()
    s1 = pila_o.pop()
    s1tipo = pila_tipos.pop()
    dirBase = dir_funciones.buscar_variable(pila_func[-1], t[-16])
    dimensiones = dir_funciones.buscar_dimensiones(pila_func[-1], t[-16])
    m = dir_funciones.buscar_m(pila_func[-1], t[-16])

    if not all(tipo == 'ent' for tipo in [s1tipo, s2tipo, s3tipo]):
        raise Exception("Los tipos de indexacion no son enteros")

    cuadruplos.append(['VERIFICAR', 0, dimensiones[0], s1]) 
    cuadruplos.append(['VERIFICAR', 0, dimensiones[1], s2])
    cuadruplos.append(['VERIFICAR', 0, dimensiones[2], s3])
    temp1 = dir_funciones.insertar_variable(pila_func[-1], 'ent')
    cuadruplos.append(['*dir', s1, m[0], temp1])
    temp2 = dir_funciones.insertar_variable(pila_func[-1], 'ent')
    cuadruplos.append(['*dir', s2, m[1], temp2])
    temp3 = dir_funciones.insertar_variable(pila_func[-1], 'ent')
    cuadruplos.append(['+', temp1, temp2, temp3])
    temp4 = dir_funciones.insertar_variable(pila_func[-1], 'ent')
    cuadruplos.append(['+', temp3, s3, temp4])
    apt = dir_funciones.insertar_variable(pila_func[-1], 'apuntador')
    cuadruplos.append(['+dir', temp4, dirBase, apt])
    pila_o.append(apt)
    pila_tipos.append(checar_tipo_memoria(dirBase))

def p_p22(t):
    '''
    p22 : nulo
    '''
    s2 = pila_o.pop()
    s2tipo = pila_tipos.pop()
    s1 = pila_o.pop()
    s1tipo = pila_tipos.pop()
    dirBase = dir_funciones.buscar_variable(pila_func[-1], t[-11])
    dimensiones = dir_funciones.buscar_dimensiones(pila_func[-1], t[-11])
    m = dir_funciones.buscar_m(pila_func[-1], t[-11])

    if not all(tipo == 'ent' for tipo in [s1tipo, s2tipo]):
        raise Exception("Los tipos de indexacion no son enteros")

    cuadruplos.append(['VERIFICAR', 0, dimensiones[0], s1]) 
    cuadruplos.append(['VERIFICAR', 0, dimensiones[1], s2])
    temp1 = dir_funciones.insertar_variable(pila_func[-1], 'ent')
    cuadruplos.append(['*dir', s1, m[0], temp1])
    temp2 = dir_funciones.insertar_variable(pila_func[-1], 'ent')
    cuadruplos.append(['+', temp1, s2, temp2])
    apt = dir_funciones.insertar_variable(pila_func[-1], 'apuntador')
    cuadruplos.append(['+dir', temp2, dirBase, apt])
    pila_o.append(apt)
    pila_tipos.append(checar_tipo_memoria(dirBase))
    
def p_p23(t):
    '''
    p23 : nulo
    '''
    s1 = pila_o.pop()
    s1tipo = pila_tipos.pop()
    dirBase = dir_funciones.buscar_variable(pila_func[-1], t[-6])
    dimensiones = dir_funciones.buscar_dimensiones(pila_func[-1], t[-6])

    if s1tipo != 'ent':
        raise Exception("El tipo de indexacion no es entero")

    cuadruplos.append(['VERIFICAR', 0, dimensiones[0], s1])
    apt = dir_funciones.insertar_variable(pila_func[-1], 'apuntador')
    cuadruplos.append(['+dir', s1, dirBase, apt])
    pila_o.append(apt)
    pila_tipos.append(checar_tipo_memoria(dirBase))

def p_p24(t):
    '''
    p24 : nulo
    '''
    direccion = dir_funciones.buscar_variable(pila_func[-1], t[-1])
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