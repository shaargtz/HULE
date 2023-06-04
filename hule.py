from src.hule_parser import parser, cuadruplos, dir_funciones
from src.codigos_prueba import *
from src.maquina_virtual import MaquinaVirtual
from src.utilidad import *

nombre_archivo = input('Escribe el nombre del archivo a correr: ')
prueba = input("Es un archivo de prueba? [s]/n : ") or 's'
debug = input("¿Quieres imprimir los datos de debug? s/[n] : ") or 'n'

if prueba == 's':
    nombre_archivo = 'pruebas/' + nombre_archivo

with open("{}.hule".format(nombre_archivo)) as archivo:
    codigo = archivo.read()

parser.parse(codigo)

if debug == 's':
    imprimir_cuadruplos(cuadruplos)
    imprimir_tabla_variables(dir_funciones)

mv = MaquinaVirtual(cuadruplos, dir_funciones)
print('+-------------------EJECUCION-------------------+')
mv.ejecutar()
print('+-----------------------------------------------+')
if debug == 's':
    mv.imprimir_memoria()