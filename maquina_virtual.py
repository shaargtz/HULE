import math
import random
from memoria_virtual import VonNeumann

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
                # print("{} / {} = ".format(operando_1, operando_2) + str(self.memoria.buscar_casilla(operando_1) / self.memoria.buscar_casilla(operando_2)))
                self.memoria.asignar_casilla(destino, self.memoria.buscar_casilla(operando_1) / self.memoria.buscar_casilla(operando_2))
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
                # print("{} = {}".format(destino, operando_1))
                self.memoria.asignar_casilla(destino, self.memoria.buscar_casilla(operando_1))
            elif operador == 'imprime':
                # print("imprime({})".format(destino))               
                print(self.memoria.buscar_casilla(destino))
            elif operador == 'sen':
                # print("sen({}) = ".format(operando_1) + str(math.sen(self.memoria.buscar_casilla(operando_1))))
                self.memoria.asignar_casilla(destino, math.sen(self.memoria.buscar_casilla(operando_1)))
            elif operador == 'cos':
                # print("cos({}) = ".format(operando_1) + str(math.cos(self.memoria.buscar_casilla(operando_1))))
                self.memoria.asignar_casilla(destino, math.cos(self.memoria.buscar_casilla(operando_1)))
            elif operador == 'tan':
                # print("tan({}) = ".format(operando_1) + str(math.tan(self.memoria.buscar_casilla(operando_1))))
                self.memoria.asignar_casilla(destino, math.tan(self.memoria.buscar_casilla(operando_1)))
            elif operador == 'senh':
                # print("senh({}) = ".format(operando_1) + str(math.senh(self.memoria.buscar_casilla(operando_1))))
                self.memoria.asignar_casilla(destino, math.senh(self.memoria.buscar_casilla(operando_1)))
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
                # por hacer listas
                print("largo de la lista {} = ".format(operando_1))
            elif operador == 'media':
                # por hacer listas
                print("media de la lista {} = ".format(operando_1))
            elif operador == 'moda':
                # por hacer listas
                print("moda de la lista {} = ".format(operando_1))
            elif operador == 'mediana':
                # por hacer listas
                print("mediana de la lista {} = ".format(operando_1))
            elif operador == 'piso':
                # print("piso({}) = ".format(operando_1) + str(math.floor(self.memoria.buscar_casilla(operando_1))))
                self.memoria.asignar_casilla(destino, math.floor(self.memoria.buscar_casilla(operando_1)))
            elif operador == 'techo':
                # print("techo({}) = ".format(operando_1) + str(math.ceil(self.memoria.buscar_casilla(operando_1))))
                self.memoria.asignar_casilla(destino, math.ceil(self.memoria.buscar_casilla(operando_1)))
            elif operador == 'aleatorio':
                rand = random.randint()
                # print("aleatorio() = {}".format(rand))
                self.memoria.asignar_casilla(destino, rand)
            elif operador == 'poder':
                # print("{} ^ {} = ".format(operando_1, operando_2) + str(pow(self.memoria.buscar_casilla(operando_1), self.memoria.buscar_casilla(operando_2))))
                self.memoria.asignar_casilla(destino, pow(self.memoria.buscar_casilla(operando_1), self.memoria.buscar_casilla(operando_2)))
            elif operador == 'log':
                # print("{} log {} = ".format(operando_1, operando_2) + str(math.log(self.memoria.buscar_casilla(operando_1), self.memoria.buscar_casilla(operando_2))))
                self.memoria.asignar_casilla(destino, math.log(self.memoria.buscar_casilla(operando_1), self.memoria.buscar_casilla(operando_2)))
            elif operador == 'abs':
                # print("abs({}) = ".format(operando_1) + str(abs(self.memoria.buscar_casilla(operando_1))))
                self.memoria.asignar_casilla(destino, abs(self.memoria.buscar_casilla(operando_1)))
            elif operador == 'sec':
                # por hacer listas
                print("sec({}) = ".format(operando_1))
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
                self.pila_apuntador.append(self.dir_func.buscar_cuadruplo(destino) - 1)
                self.memoria.apilar_memoria()
            elif operador == 'REGRESA':
                # print("REGRESA {} {}".format(operando_1, destino))
                self.memoria.asignar_casilla(destino, self.memoria.buscar_casilla(operando_1))
            elif operador == 'INSTANCIAR':
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
                self.memoria.dormir_memoria
                self.pila_apuntador.pop()
            elif operador == 'ENDPROG':
                # print("ENDFUNC")
                pass
            else:
                print("Operador no reconocido: {}".format(operador))
            
            self.pila_apuntador[-1] += 1