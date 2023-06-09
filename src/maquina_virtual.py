import math
import random
import pprint
import plotext as plt
from src.memoria_virtual import VonNeumann
from src.utilidad import *

class MaquinaVirtual:
    def __init__(self, cuadruplos, dir_func):
        self.cuadruplos = cuadruplos
        self.memoria = VonNeumann()
        self.pila_apuntador = [0]
        self.dir_func = dir_func
    
    def ejecutar(self):
        while (self.pila_apuntador[-1] < len(self.cuadruplos)):
            operador = self.cuadruplos[self.pila_apuntador[-1]][0]
            operando_1 = self.cuadruplos[self.pila_apuntador[-1]][1]
            operando_2 = self.cuadruplos[self.pila_apuntador[-1]][2]
            destino = self.cuadruplos[self.pila_apuntador[-1]][3]
            # estos tres operadores trabajan con apuntadores y se quiere el valor dentro del apuntador
            if operador not in ['+dir', '*dir', 'ERA']:
                if operando_1 >= 15000 and operando_1 < 16000:
                    operando_1 = self.memoria.buscar_casilla(operando_1)
                if operando_2 >= 15000 and operando_2 < 16000:
                    operando_2 = self.memoria.buscar_casilla(operando_2)
                if destino >= 15000 and destino < 16000:
                    destino = self.memoria.buscar_casilla(destino)
            if operador == '+':
                # print("{} + {} = ".format(operando_1, operando_2) + str(self.memoria.buscar_casilla(operando_1) + self.memoria.buscar_casilla(operando_2)))
                self.memoria.asignar_casilla(destino, self.memoria.buscar_casilla(operando_1) + self.memoria.buscar_casilla(operando_2))
            elif operador == '-':
                # print("{} - {} = ".format(operando_1, operando_2) + str(self.memoria.buscar_casilla(operando_1) - self.memoria.buscar_casilla(operando_2)))
                self.memoria.asignar_casilla(destino, self.memoria.buscar_casilla(operando_1) - self.memoria.buscar_casilla(operando_2))
            elif operador == '*':
                # print("{} * {} = ".format(operando_1, operando_2) + str(self.memoria.buscar_casilla(operando_1) * self.memoria.buscar_casilla(operando_2)))
                self.memoria.asignar_casilla(destino, self.memoria.buscar_casilla(operando_1) * self.memoria.buscar_casilla(operando_2))
            elif operador == '/':
                if checar_tipo_memoria(destino) == 'flot':
                    # print("{} / {} = ".format(operando_1, operando_2) + str(self.memoria.buscar_casilla(operando_1) / self.memoria.buscar_casilla(operando_2)))
                    self.memoria.asignar_casilla(destino, self.memoria.buscar_casilla(operando_1) / self.memoria.buscar_casilla(operando_2))
                else:
                    # division entera
                    # print("{} // {} = ".format(operando_1, operando_2) + str(self.memoria.buscar_casilla(operando_1) // self.memoria.buscar_casilla(operando_2)))
                    self.memoria.asignar_casilla(destino, self.memoria.buscar_casilla(operando_1) // self.memoria.buscar_casilla(operando_2))
            elif operador == '&':
                # print("{} & {} = ".format(operando_1, operando_2) + str(self.memoria.buscar_casilla(operando_1) and self.memoria.buscar_casilla(operando_2)))
                self.memoria.asignar_casilla(destino, self.memoria.buscar_casilla(operando_1) and self.memoria.buscar_casilla(operando_2))
            elif operador == '|':
                # print("{} | {} = ".format(operando_1, operando_2) + str(self.memoria.buscar_casilla(operando_1) or self.memoria.buscar_casilla(operando_2)))
                self.memoria.asignar_casilla(destino, self.memoria.buscar_casilla(operando_1) or self.memoria.buscar_casilla(operando_2))
            elif operador == '>':
                # print("{} > {} = ".format(operando_1, operando_2) + str(self.memoria.buscar_casilla(operando_1) > self.memoria.buscar_casilla(operando_2)))
                self.memoria.asignar_casilla(destino, self.memoria.buscar_casilla(operando_1) > self.memoria.buscar_casilla(operando_2))
            elif operador == '<':
                # print("{} < {} = ".format(operando_1, operando_2) + str(self.memoria.buscar_casilla(operando_1) < self.memoria.buscar_casilla(operando_2)))
                self.memoria.asignar_casilla(destino, self.memoria.buscar_casilla(operando_1) < self.memoria.buscar_casilla(operando_2))
            elif operador == '==':
                # print("{} == {} = ".format(operando_1, operando_2) + str(self.memoria.buscar_casilla(operando_1) == self.memoria.buscar_casilla(operando_2)))
                self.memoria.asignar_casilla(destino, self.memoria.buscar_casilla(operando_1) == self.memoria.buscar_casilla(operando_2))
            elif operador == '!=':
                # print("{} != {} = ".format(operando_1, operando_2) + str(self.memoria.buscar_casilla(operando_1) != self.memoria.buscar_casilla(operando_2)))
                self.memoria.asignar_casilla(destino, self.memoria.buscar_casilla(operando_1) != self.memoria.buscar_casilla(operando_2))
            elif operador == '=':
                # print("{} = {}".format(destino, self.memoria.buscar_casilla(operando_1)))
                self.memoria.asignar_casilla(destino, self.memoria.buscar_casilla(operando_1))
            elif operador == 'imprime':
                # print("imprime({})".format(destino))      
                print(self.memoria.buscar_casilla(destino))
            elif operador == 'sen':
                # print("sen({}) = ".format(operando_1) + str(math.sen(self.memoria.buscar_casilla(operando_1))))
                self.memoria.asignar_casilla(destino, math.sin(self.memoria.buscar_casilla(operando_1)))
            elif operador == 'cos':
                # print("cos({}) = ".format(operando_1) + str(math.cos(self.memoria.buscar_casilla(operando_1))))
                self.memoria.asignar_casilla(destino, math.cos(self.memoria.buscar_casilla(operando_1)))
            elif operador == 'tan':
                # print("tan({}) = ".format(operando_1) + str(math.tan(self.memoria.buscar_casilla(operando_1))))
                self.memoria.asignar_casilla(destino, math.tan(self.memoria.buscar_casilla(operando_1)))
            elif operador == 'senh':
                # print("senh({}) = ".format(operando_1) + str(math.senh(self.memoria.buscar_casilla(operando_1))))
                self.memoria.asignar_casilla(destino, math.sinh(self.memoria.buscar_casilla(operando_1)))
            elif operador == 'cosh':
                # print("cosh({}) = ".format(operando_1) + str(math.cosh(self.memoria.buscar_casilla(operando_1))))
                self.memoria.asignar_casilla(destino, math.cosh(self.memoria.buscar_casilla(operando_1)))
            elif operador == 'tanh':
                # print("tanh({}) = ".format(operando_1) + str(math.tanh(self.memoria.buscar_casilla(operando_1))))
                self.memoria.asignar_casilla(destino, math.tanh(self.memoria.buscar_casilla(operando_1)))
            elif operador == 'min':
                # print("min({}, {}) = ".format(operando_1, operando_2) + str(min(self.memoria.buscar_casilla(operando_1), self.memoria.buscar_casilla(operando_2))))
                self.memoria.asignar_casilla(destino, min(self.memoria.buscar_casilla(operando_1), self.memoria.buscar_casilla(operando_2)))
            elif operador == 'max':
                # print("max({}, {}) = ".format(operando_1, operando_2) + str(max(self.memoria.buscar_casilla(operando_1), self.memoria.buscar_casilla(operando_2))))
                self.memoria.asignar_casilla(destino, max(self.memoria.buscar_casilla(operando_1), self.memoria.buscar_casilla(operando_2)))
            elif operador == 'largo':
                # print("largo({}) = ".format(operando_1))
                self.memoria.asignar_casilla(destino, operando_2)
            elif operador == 'media':
                # calculo de la media
                acum = 0
                for i in range(operando_2):
                    acum += self.memoria.buscar_casilla(operando_1 + i)
                media = acum / operando_2
                # print("media de la lista {} = {}".format(operando_1, media))
                self.memoria.asignar_casilla(destino, media)
            elif operador == 'moda':
                # calculo de la moda
                valores = {}
                for i in range(operando_2):
                    val = self.memoria.buscar_casilla(operando_1 + i)
                    if val in valores.keys():
                        valores[val] += 1
                    else:
                        valores[val] = 1
                max_key = max(valores, key=valores.get)
                # print("moda de la lista {} = {}".format(operando_1, max_key))
                self.memoria.asignar_casilla(destino, max_key)
            elif operador == 'mediana':
                # calculo de la mediana
                valores = []
                for i in range(operando_2):
                    valores.append(self.memoria.buscar_casilla(operando_1 + i))
                orden = sorted(valores)
                if operando_2 % 2:
                    mediana = orden[operando_2 // 2]
                else:
                    mediana = (orden[operando_2 // 2] + orden[(operando_2 // 2) + 1]) / 2
                # print("mediana de la lista {} = {}".format(operando_1, mediana))
                self.memoria.asignar_casilla(destino, mediana)
            elif operador == 'graficar':
                # print("graficar({}, {})".format(operando_1, operando_2))
                valores = []
                etiquetas = []
                for i in range(destino):
                    valores.append(self.memoria.buscar_casilla(operando_1 + i))
                    etiquetas.append(self.memoria.buscar_casilla(operando_2 + i))
                plt.bar(etiquetas, valores)
                plt.theme('clear')
                plt.show()
            elif operador == 'piso':
                # print("piso({}) = ".format(operando_1) + str(math.floor(self.memoria.buscar_casilla(operando_1))))
                self.memoria.asignar_casilla(destino, math.floor(self.memoria.buscar_casilla(operando_1)))
            elif operador == 'techo':
                # print("techo({}) = ".format(operando_1) + str(math.ceil(self.memoria.buscar_casilla(operando_1))))
                self.memoria.asignar_casilla(destino, math.ceil(self.memoria.buscar_casilla(operando_1)))
            elif operador == 'aleatorio':
                # print(operando_1, operando_2)
                rand = random.randint(self.memoria.buscar_casilla(operando_1), self.memoria.buscar_casilla(operando_2))
                # print("aleatorio({}, {}) = {}".format(operando_1, operando_2, rand))
                self.memoria.asignar_casilla(destino, rand)
            elif operador == 'poder':
                # print("{} ^ {} = ".format(operando_1, operando_2) + str(pow(self.memoria.buscar_casilla(operando_1), self.memoria.buscar_casilla(operando_2))))
                self.memoria.asignar_casilla(destino, pow(self.memoria.buscar_casilla(operando_1), self.memoria.buscar_casilla(operando_2)))
            elif operador == 'log':
                # print("log {} = ".format(operando_1) + str(math.log(self.memoria.buscar_casilla(operando_1))))
                self.memoria.asignar_casilla(destino, math.log(self.memoria.buscar_casilla(operando_1)))
            elif operador == 'abs':
                # print("abs({}) = ".format(operando_1) + str(abs(self.memoria.buscar_casilla(operando_1))))
                self.memoria.asignar_casilla(destino, abs(self.memoria.buscar_casilla(operando_1)))
            elif operador == 'VERIFICAR':
                # print("VERIFICAR {} <= {} <= {}".format(operando_1, destino, operando_2))
                aux = self.memoria.buscar_casilla(destino)
                if aux < operando_1 or aux > operando_2:
                    raise Exception("Rango de indexacion invalido {} <= {} <= {}".format(operando_1, aux, operando_2))
            elif operador == '+dir':
                if operando_1 >= 15000 and operando_1 < 16000:
                    # es un apuntador
                    operando_1 = self.memoria.buscar_casilla(operando_1)
                # print("{} +dir {} = ".format(self.memoria.buscar_casilla(operando_1), operando_2) + str(self.memoria.buscar_casilla(operando_1) + operando_2))
                self.memoria.asignar_casilla(destino, self.memoria.buscar_casilla(operando_1) + operando_2)
            elif operador == '*dir':
                # es un apuntador
                if operando_1 >= 15000 and operando_1 < 16000:
                    operando_1 = self.memoria.buscar_casilla(operando_1)
                # print("{} *dir {} = ".format(self.memoria.buscar_casilla(operando_1), operando_2) + str(self.memoria.buscar_casilla(operando_1) + operando_2))
                self.memoria.asignar_casilla(destino, self.memoria.buscar_casilla(operando_1) * operando_2)
            elif operador == 'GOTOF':
                # print("GOTOF {} {}".format(operando_1, destino))
                if (not self.memoria.buscar_casilla(operando_1)):
                    self.pila_apuntador[-1] = destino - 1
            elif operador == 'GOTOV':
                # print("GOTOV {} {}".format(operando_1, destino))
                if (self.memoria.buscar_casilla(operando_1)):
                    self.pila_apuntador[-1] = destino - 1
            elif operador == 'GOTO':
                # print("GOTO {}".format(destino))
                self.pila_apuntador[-1] = destino - 1
            elif operador == 'GOSUB':
                # print("GOSUB {}".format(destino))
                self.pila_apuntador.append(destino -1)
                self.memoria.apilar_memoria()
            elif operador == 'REGRESA':
                # print("REGRESA {} {}".format(operando_1, destino))
                self.memoria.asignar_casilla(destino, self.memoria.buscar_casilla(operando_1))
            elif operador == 'INSTANCIAR':
                # se pasa la memoria de compilacion a la memoria de ejecucion
                # print("INSTANCIAR")
                self.memoria.instanciar('hule', self.dir_func.buscar_contadores_var('hule'))
                self.memoria.instanciar('global', self.dir_func.buscar_contadores_var('global'))
                self.memoria.instanciar('ctes', self.dir_func.buscar_contadores_var('ctes'))
                self.memoria.inicializar_ctes(self.dir_func.buscar_ctes())
            elif operador == 'ERA':
                # print("ERA {}".format(destino))
                self.memoria.era(self.dir_func.buscar_contadores_var(destino))
            elif operador == 'PARAM':
                # print("PARAM {} {}".format(operando_1, destino))
                self.memoria.param(operando_1, destino)
            elif operador == 'ENDFUNC':
                # print("ENDFUNC")
                self.memoria.dormir_memoria()
                self.pila_apuntador.pop()
            elif operador == 'LEE':
                # print("LEE")
                aux = input()
                self.memoria.asignar_casilla(destino, aux)
            elif operador == 'ent':
                # conversion de datos
                # print("ent({})".format(operando_1))
                valor = self.memoria.buscar_casilla(operando_1)
                conversion = int(valor)
                self.memoria.asignar_casilla(destino, conversion)
            elif operador == 'flot':
                # conversion de datos
                # print("flot({})".format(operando_1))
                valor = self.memoria.buscar_casilla(operando_1)
                conversion = float(valor)
                self.memoria.asignar_casilla(destino, conversion)
            elif operador == 'car':
                # conversion de datos
                # print("car({})".format(operando_1))
                valor = self.memoria.buscar_casilla(operando_1)
                conversion = chr(valor)
                self.memoria.asignar_casilla(destino, conversion)
            elif operador == 'cadena':
                # conversion de datos
                # print("cadena({})".format(operando_1))
                valor = self.memoria.buscar_casilla(operando_1)
                conversion = str(valor)
                self.memoria.asignar_casilla(destino, conversion)
            elif operador == 'bool':
                # conversion de datos
                # print("bool({})".format(operando_1))
                valor = self.memoria.buscar_casilla(operando_1)
                conversion = bool(valor)
                self.memoria.asignar_casilla(destino, conversion)
            elif operador == 'ENDPROG':
                # print("ENDPROG")
                pass
            else:
                raise Exception("Operador no reconocido: {}".format(operador))
            
            self.pila_apuntador[-1] += 1

    def imprimir_memoria(self):
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(self.memoria.memoria_global.espacios)
        pp.pprint(self.memoria.memoria_ctes.espacios)
        print(str(len(self.memoria.pila_funciones)) + " stack de memoria")
        for m in self.memoria.pila_funciones:
            pp.pprint(m.espacios)