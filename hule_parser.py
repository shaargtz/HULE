from ply import yacc
from hule_lexer import tokens

def p_programa(t):
    '''
    programa : dec HULE '(' ')' '{' bloque '}'
    '''

def p_dec(t):
    '''
    dec : dec_var dec
        | dec_func dec
        | nulo
    '''
    
def p_dec_var(t):
    '''
    dec_var : VAR tipo ID dec_var_prima ';'
            | dec_lista
    '''
    
def p_dec_var_prima(t):
    '''
    dec_var_prima : ',' ID dec_var_prima
                  | ',' ID dimension dec_lista_prima
                  | nulo
    '''
    
def p_dec_lista(t):
    '''
    dec_lista : VAR tipo ID dimension dec_lista_prima ';'
              | dec_matriz
    '''
    
def p_dec_lista_prima(t):
    '''
    dec_lista_prima : ',' ID dimension dec_lista_prima
                    | ',' ID dimension dimension dec_matriz_prima
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

def p_tipo(t):
    '''
    tipo : ENT 
         | FLOT 
         | CAR 
         | CADENA
    '''
    
def p_dec_func(t):
    '''
    dec_func : dec_func_t
             | dec_func_v
    '''

def p_dec_func_t(t):
    '''
    dec_func_t : FUNC ID '(' param ')' TIPO tipo '{' bloque REGRESA hiper_exp '}' ';'
    '''

def p_dec_func_v(t):
    '''
    dec_func_v : FUNC ID '(' param ')' TIPO VACIO '{' bloque '}' ';'
    '''

def p_param(t):
    '''
    param : tipo ID param_prima
          | nulo
    '''
    
def p_param_prima(t):
    '''
    param_prima : ',' tipo ID param_prima
                | nulo
    '''

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
    '''
    
def p_asig(t):
    '''
    asig : ID '=' hiper_exp ';'
    '''

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

def p_hiper_exp(t):
    '''
    hiper_exp : super_exp hiper_exp_prima
    '''

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

def p_exp_prima(t):
    '''
    exp_prima : '+' term
              | '-' term
              | nulo
    '''
    
def p_term(t):
    '''
    term : factor term_prima
    '''

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

def p_cte(t):
    '''
    cte : CTE_ENT
        | CTE_FLOT
        | CTE_CAR
        | CTE_CADENA
    '''

def p_var(t):
    '''
    var : ID
        | ID '[' hiper_exp ']'
        | ID '[' hiper_exp ']' '[' hiper_exp ']'
    '''

def p_nulo(t):
    '''
    nulo :  
    '''

def p_error(t):
    '''
    '''
    print("error en token: " + str(t))

parser = yacc.yacc()

codigo = '''
hule() 
{ 
    var ent a, b, c[5];
    a = 2;
    b = 3;
    si (a < b) 
    {
        imprime('bbb');
    } sino {
        imprime('aaa');
    };
}
'''

parser.parse(codigo)