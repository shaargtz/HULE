from prettytable import PrettyTable

def checar_tipo_memoria(direccion):
    tipos = ['ent', 'flot', 'car', 'cadena', 'bool']
    aux = direccion % 5000
    aux = aux // 1000
    return tipos[aux]

def imprimir_cuadruplos(cuadruplos):
    tabla_cuadruplos = PrettyTable(['operador', 'operando1', 'operando2', 'direccion'])
    tabla_cuadruplos.add_rows(cuadruplos)
    print(tabla_cuadruplos)

def imprimir_tabla_variables(dir_funciones):
    tabla_variables = PrettyTable(['funcion', 'especie', 'valor', 'tipo', 'direccion'])
    for f in dir_funciones.directorio:
        for v in dir_funciones.directorio[f][1].tabla['var']:
            tabla_variables.add_row([f, 'var', v, 
                                    dir_funciones.directorio[f][1].tabla['var'][v][0], 
                                    dir_funciones.directorio[f][1].tabla['var'][v][1]])
        for v in dir_funciones.directorio[f][1].tabla['temp']:
            tabla_variables.add_row([f, 'temp', v, 
                                    dir_funciones.directorio[f][1].tabla['temp'][v][0], 
                                    dir_funciones.directorio[f][1].tabla['temp'][v][1]])
    print(tabla_variables)
            
def imprimir_tabla_constantes(constantes):
    tabla_constantes = PrettyTable(['valor', 'tipo', 'direccion'])
    for c in constantes:
        tabla_constantes.add_row([c, constantes[c][0], constantes[c][1]])
    print(tabla_constantes)