from prettytable import PrettyTable

def checar_tipo_memoria(direccion):
    if direccion < 1000 or (direccion >= 5000 and direccion < 6000) or (direccion >= 10000 and direccion < 11000) or (direccion >= 16000 and direccion < 17000):
        return 'ent'
    elif direccion < 2000 or (direccion >= 6000 and direccion < 7000) or (direccion >= 11000 and direccion < 12000) or (direccion >= 17000 and direccion < 18000):
        return 'flot'
    elif direccion < 3000 or (direccion >= 7000 and direccion < 8000) or (direccion >= 12000 and direccion < 13000) or (direccion >= 18000 and direccion < 19000):
        return 'car'
    elif direccion < 4000 or (direccion >= 8000 and direccion < 9000) or (direccion >= 13000 and direccion < 14000) or (direccion >= 19000 and direccion < 20000):
        return 'cadena'
    elif direccion >= 15000 and direccion < 16000:
        return 'apuntador'
    else:
        return 'bool'

def checar_alcance_memoria(direccion):
    if direccion < 5000:
        return 'glob'
    elif direccion < 10000:
        return 'local'
    elif direccion < 16000:
        return 'temp'
    else:
        return 'ctes'

def imprimir_cuadruplos(cuadruplos):
    tabla_cuadruplos = PrettyTable(['#', 'operador', 'operando1', 'operando2', 'direccion'])
    for c in range(len(cuadruplos)):
        tabla_cuadruplos.add_row([c] + cuadruplos[c])
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