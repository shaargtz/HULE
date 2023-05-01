import math
import random

class MaquinaVirtual:
    def __init__(self, cuadruplos, memoria, variables, funciones):
        self.cuadruplos = cuadruplos
        self.memoria = memoria
        self.variables = variables
        self.funciones = funciones
    
    def ejecutar(self):
        contador = 0
        while (contador < len(self.cuadruplos)):
            operador = self.cuadruplos[contador][0]
            operando_1 = self.cuadruplos[contador][1]
            operando_2 = self.cuadruplos[contador][2]
            destino = self.cuadruplos[contador][3]
            mem = self.memoria
            if operador == '+':
                print("{mem[operando_1]} + {mem[operando_2]} = " + str(mem[operando_1] + mem[operando_2]))
                mem[destino] = mem[operando_1] + mem[operando_2]
            elif operador == '-':
                print("{mem[operando_1]} - {mem[operando_2]} = " + str(mem[operando_1] - mem[operando_2]))
                mem[destino] = mem[operando_1] - mem[operando_2]
            elif operador == '*':
                print("{mem[operando_1]} * {mem[operando_2]} = " + str(mem[operando_1] * mem[operando_2]))
                mem[destino] = mem[operando_1] * mem[operando_2]
            elif operador == '/':
                print("{mem[operando_1]} / {mem[operando_2]} = " + str(mem[operando_1] / mem[operando_2]))
                mem[destino] = mem[operando_1] / mem[operando_2]
            elif operador == '&':
                print("{mem[operando_1]} & {mem[operando_2]} = " + str(mem[operando_1] and mem[operando_2]))
                mem[destino] = mem[operando_1] and mem[operando_2]
            elif operador == '|':
                print("{mem[operando_1]} | {mem[operando_2]} = " + str(mem[operando_1] or mem[operando_2]))
                mem[destino] = mem[operando_1] or mem[operando_2]
            elif operador == '>':
                print("{mem[operando_1]} > {mem[operando_2]} = " + str(mem[operando_1] > mem[operando_2]))
                mem[destino] = mem[operando_1] > mem[operando_2]
            elif operador == '<':
                print("{mem[operando_1]} < {mem[operando_2]} = " + str(mem[operando_1] < mem[operando_2]))
                mem[destino] = mem[operando_1] < mem[operando_2]
            elif operador == '==':
                print("{mem[operando_1]} == {mem[operando_2]} = " + str(mem[operando_1] == mem[operando_2]))
                mem[destino] = mem[operando_1] == mem[operando_2]
            elif operador == '!=':
                print("{mem[operando_1]} != {mem[operando_2]} = " + str(mem[operando_1] != mem[operando_2]))
                mem[destino] = mem[operando_1] != mem[operando_2]
            elif operador == '=':
                print("{destino} = {mem[operando_1]}")
                mem[destino] = mem[operando_1]
            elif operador == 'imprime':
                print("imprime({mem[operando_1]})")
                print(mem[operando_1])
            elif operador == 'sen':
                print("sen({mem[operando_1]}) = " + str(math.sen(mem[operando_1])))
                mem[destino] = math.sen(mem[operando_1])
            elif operador == 'cos':
                print("cos({mem[operando_1]}) = " + str(math.cos(mem[operando_1])))
                mem[destino] = math.cos(mem[operando_1])
            elif operador == 'tan':
                print("tan({mem[operando_1]}) = " + str(math.tan(mem[operando_1])))
                mem[destino] = math.tan(mem[operando_1])
            elif operador == 'senh':
                print("senh({mem[operando_1]}) = " + str(math.senh(mem[operando_1])))
                mem[destino] = math.senh(mem[operando_1])
            elif operador == 'cosh':
                print("cosh({mem[operando_1]}) = " + str(math.cosh(mem[operando_1])))
                mem[destino] = math.cosh(mem[operando_1])
            elif operador == 'tanh':
                print("tanh({mem[operando_1]}) = " + str(math.tanh(mem[operando_1])))
                mem[destino] = math.tanh(mem[operando_1])
            elif operador == 'min':
                print("min({mem[operando_1]}, {mem[operando_2]}) = " + str(min(mem[operando_1], mem[operando_2])))
                mem[destino] = min(mem[operando_1], mem[operando_2])
            elif operador == 'max':
                print("max({mem[operando_1]}, {mem[operando_2]}) = " + str(max(mem[operando_1], mem[operando_2])))
                mem[destino] = max(mem[operando_1], mem[operando_2])
            elif operador == 'largo':
                # por hacer listas
                print("largo de la lista {operando_1} = ")
            elif operador == 'media':
                # por hacer listas
                print("media de la lista {operando_1} = ")
            elif operador == 'moda':
                # por hacer listas
                print("moda de la lista {operando_1} = ")
            elif operador == 'mediana':
                # por hacer listas
                print("mediana de la lista {operando_1} = ")
            elif operador == 'piso':
                print("piso({mem[operando_1]}) = " + str(math.floor(mem[operando_1])))
                mem[destino] = math.floor(mem[operando_1])
            elif operador == 'techo':
                print("techo({mem[operando_1]}) = " + str(math.ceil(mem[operando_1])))
                mem[destino] = math.ceil(mem[operando_1])
            elif operador == 'aleatorio':
                rand = random.randint()
                print("aleatorio() = {rand}")
                mem[destino] = rand
            elif operador == 'poder':
                print("{mem[operando_1]} ^ {mem[operando_2]} = " + str(pow(mem[operando_1], mem[operando_2])))
                mem[destino] = pow(mem[operando_1], mem[operando_2])
            elif operador == 'log':
                print("{mem[operando_1]} log {mem[operando_2]} = " + str(math.log(mem[operando_1], mem[operando_2])))
                mem[destino] = math.log(mem[operando_1], mem[operando_2])
            elif operador == 'abs':
                print("abs({mem[operando_1]}) = " + str(abs(mem[operando_1])))
                mem[destino] = abs(mem[operando_1])
            elif operador == 'sec':
                # por hacer listas
                print("sec({mem[operando_1]}, mem[operando_1]}) = ")
            elif operador == 'GOTOF':
                if (not mem[operando_1]):
                    contador = destino - 1
            elif operador == 'GOTOV':
                if (mem[operando_1]):
                    contador = destino - 1
            elif operador == 'GOTO':
                contador = destino - 1
            else:
                print("Operador no reconocido: {operador}")
            
            contador = contador + 1