from prettytable import PrettyTable

def checar_tipo_memoria(direccion):
    tipos = ['ent', 'flot', 'car', 'cadena', 'bool']
    aux = direccion % 5000
    aux = aux // 1000
    return tipos[aux]

def checar_alcance_memoria(direccion):
    alcances = ['glob', 'local', 'temp', 'ctes']
    aux = direccion // 5000
    return alcances[aux]

def imprimir_cuadruplos(cuadruplos):
    tabla_cuadruplos = PrettyTable(['operador', 'operando1', 'operando2', 'direccion'])
    tabla_cuadruplos.add_rows(cuadruplos)
    print(tabla_cuadruplos)

def imprimir_tabla_variables(dir_funciones):
    tabla_variables = PrettyTable(['funcion', 'especie', 'valor', 'tipo', 'direccion'])
    for f in dir_funciones.directorio:
        if dir_funciones.directorio[f][1]:
            for a in dir_funciones.directorio[f][1].tabla.keys():
                for v in dir_funciones.directorio[f][1].tabla[a]:
                    tabla_variables.add_row([f, a, v, 
                                            dir_funciones.directorio[f][1].tabla[a][v][0], 
                                            dir_funciones.directorio[f][1].tabla[a][v][1]])
    print(tabla_variables)