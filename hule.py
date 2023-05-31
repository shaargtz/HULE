from hule_parser import parser, cuadruplos, dir_funciones
from codigos_prueba import *
from maquina_virtual import MaquinaVirtual
from utilidad import *

parser.parse(codigo_10)

imprimir_cuadruplos(cuadruplos)
imprimir_tabla_variables(dir_funciones)

mv = MaquinaVirtual(cuadruplos, dir_funciones)
print('+-------------------EJECUCION-------------------+')
mv.ejecutar()
print('+-----------------------------------------------+')
mv.imprimir_memoria()