import math
import random
from memoria_virtual import VonNeumann

class MaquinaVirtual:
    def __init__(self, cuadruplos, memoria):
        self.cuadruplos = cuadruplos
        self.memoria = memoria
    
    def ejecutar(self):
        apuntador = 0
        while (apuntador < len(self.cuadruplos)):
            operador = self.cuadruplos[apuntador][0]
            operando_1 = self.cuadruplos[apuntador][1]
            operando_2 = self.cuadruplos[apuntador][2]
            destino = self.cuadruplos[apuntador][3]
            mem = self.memoria.memoria
            if operador == '+':
                print("{} + {} = ".format(operando_1, operando_2) + str(mem[operando_1] + mem[operando_2]))
                mem[destino] = mem[operando_1] + mem[operando_2]
            elif operador == '-':
                print("{} - {} = ".format(operando_1, operando_2) + str(mem[operando_1] - mem[operando_2]))
                mem[destino] = mem[operando_1] - mem[operando_2]
            elif operador == '*':
                print("{} * {} = ".format(operando_1, operando_2) + str(mem[operando_1] * mem[operando_2]))
                mem[destino] = mem[operando_1] * mem[operando_2]
            elif operador == '/':
                print("{} / {} = ".format(operando_1, operando_2) + str(mem[operando_1] / mem[operando_2]))
                mem[destino] = mem[operando_1] / mem[operando_2]
            elif operador == '&':
                print("{} & {} = ".format(operando_1, operando_2) + str(mem[operando_1] and mem[operando_2]))
                mem[destino] = mem[operando_1] and mem[operando_2]
            elif operador == '|':
                print("{} | {} = ".format(operando_1, operando_2) + str(mem[operando_1] or mem[operando_2]))
                mem[destino] = mem[operando_1] or mem[operando_2]
            elif operador == '>':
                print("{} > {} = ".format(operando_1, operando_2) + str(mem[operando_1] > mem[operando_2]))
                mem[destino] = mem[operando_1] > mem[operando_2]
            elif operador == '<':
                print("{} < {} = ".format(operando_1, operando_2) + str(mem[operando_1] < mem[operando_2]))
                mem[destino] = mem[operando_1] < mem[operando_2]
            elif operador == '==':
                print("{} == {} = ".format(operando_1, operando_2) + str(mem[operando_1] == mem[operando_2]))
                mem[destino] = mem[operando_1] == mem[operando_2]
            elif operador == '!=':
                print("{} != {} = ".format(operando_1, operando_2) + str(mem[operando_1] != mem[operando_2]))
                mem[destino] = mem[operando_1] != mem[operando_2]
            elif operador == '=':
                print("{} = {}".format(destino, operando_1))
                mem[destino] = mem[operando_1]
            elif operador == 'imprime':
                print("imprime({})".format(operando_1))               
                print(mem[operando_1])
            elif operador == 'sen':
                print("sen({}) = ".format(operando_1) + str(math.sen(mem[operando_1])))
                mem[destino] = math.sen(mem[operando_1])
            elif operador == 'cos':
                print("cos({}) = ".format(operando_1) + str(math.cos(mem[operando_1])))
                mem[destino] = math.cos(mem[operando_1])
            elif operador == 'tan':
                print("tan({}) = ".format(operando_1) + str(math.tan(mem[operando_1])))
                mem[destino] = math.tan(mem[operando_1])
            elif operador == 'senh':
                print("senh({}) = ".format(operando_1) + str(math.senh(mem[operando_1])))
                mem[destino] = math.senh(mem[operando_1])
            elif operador == 'cosh':
                print("cosh({}) = ".format(operando_1) + str(math.cosh(mem[operando_1])))
                mem[destino] = math.cosh(mem[operando_1])
            elif operador == 'tanh':
                print("tanh({}) = ".format(operando_1) + str(math.tanh(mem[operando_1])))
                mem[destino] = math.tanh(mem[operando_1])
            elif operador == 'min':
                print("min({}, {}) = ".format(operando_1, operando_2) + str(min(mem[operando_1], mem[operando_2])))
                mem[destino] = min(mem[operando_1], mem[operando_2])
            elif operador == 'max':
                print("max({}, {}) = ".format(operando_1, operando_2) + str(max(mem[operando_1], mem[operando_2])))
                mem[destino] = max(mem[operando_1], mem[operando_2])
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
                print("piso({}) = ".format(operando_1) + str(math.floor(mem[operando_1])))
                mem[destino] = math.floor(mem[operando_1])
            elif operador == 'techo':
                print("techo({}) = ".format(operando_1) + str(math.ceil(mem[operando_1])))
                mem[destino] = math.ceil(mem[operando_1])
            elif operador == 'aleatorio':
                rand = random.randint()
                print("aleatorio() = {}".format(rand))
                mem[destino] = rand
            elif operador == 'poder':
                print("{} ^ {} = ".format(operando_1, operando_2) + str(pow(mem[operando_1], mem[operando_2])))
                mem[destino] = pow(mem[operando_1], mem[operando_2])
            elif operador == 'log':
                print("{} log {} = ".format(operando_1, operando_2) + str(math.log(mem[operando_1], mem[operando_2])))
                mem[destino] = math.log(mem[operando_1], mem[operando_2])
            elif operador == 'abs':
                print("abs({}) = ".format(operando_1) + str(abs(mem[operando_1])))
                mem[destino] = abs(mem[operando_1])
            elif operador == 'sec':
                # por hacer listas
                print("sec({}) = ".format(operando_1))
            elif operador == 'GOTOF':
                print("GOTOF {} {}".format(operando_1, destino))
                if (not mem[operando_1]):
                    apuntador = destino - 1
            elif operador == 'GOTOV':
                print("GOTOV {} {}".format(operando_1, destino))
                if (mem[operando_1]):
                    apuntador = destino - 1
            elif operador == 'GOTO':
                print("GOTO {}".format(destino))
                apuntador = destino - 1
            else:
                print("Operador no reconocido: {}".format(operador))
            
            apuntador = apuntador + 1