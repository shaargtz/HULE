from src.espacios_memoria import EspaciosMemoria
from src.utilidad import *

class VonNeumann:
    def __init__(self):
        ############
        # GLOBALES #
        ############
        # 0 [ 0000 -> 0999 : ent ]
        # 1 [ 1000 -> 1999 : flot ]
        # 2 [ 2000 -> 2999 : car ]
        # 3 [ 3000 -> 3999 : cadena ]
        # 4 [ 4000 -> 4999 : bool ]
        ###########
        # LOCALES #
        ###########
        # 5 [ 5000 -> 5999 : ent ]
        # 6 [ 6000 -> 6999 : flot ]
        # 7 [ 7000 -> 7999 : car ]
        # 8 [ 8000 -> 8999 : cadena ]
        # 9 [ 9000 -> 9999 : bool ]
        ############
        # TEMPORAL #
        ############
        # 10 [ 10000 -> 10999 : ent ]
        # 11 [ 11000 -> 11999 : flot ]
        # 12 [ 12000 -> 12999 : car ]
        # 13 [ 13000 -> 13999 : cadena ]
        # 14 [ 14000 -> 14999 : bool ]
        # 15 [ 15000 -> 15999 : apuntador ]
        ##############
        # CONSTANTES #
        ##############
        # 16 [ 16000 -> 16999 : ent ]
        # 17 [ 17000 -> 17999 : flot ]
        # 18 [ 18000 -> 18999 : car ]
        # 19 [ 19000 -> 19999 : cadena ]

        # pila de ejecucion de funciones
        self.pila_funciones = []
        # memoria que esta siendo instanciada
        self.nueva_memoria = []
        self.memoria_global = EspaciosMemoria()
        self.memoria_ctes = EspaciosMemoria()
        # espacios totales que no deben pasar el limite estipulado
        self.total_apilado = 0

    def instanciar(self, alcance, contadores):
        if alcance == 'hule':
            self.era(contadores)
            self.apilar_memoria()
        elif alcance == 'global':
            self.memoria_global.instanciar(contadores)
        elif alcance == 'ctes':
            self.memoria_ctes.instanciar(contadores)

    # creamos una nueva memoria
    def era(self, contadores):
        self.nueva_memoria.append(EspaciosMemoria())
        self.nueva_memoria[-1].instanciar(contadores)
    
    # le damos un parametro a la memoria que se esta creando
    def param(self, dir1, dir2):
        val = self.buscar_casilla(dir1)
        self.asignar_param(dir2, val)
 
    def apilar_memoria(self):
        self.pila_funciones.append(self.nueva_memoria.pop())
        self.total_apilado += len(self.pila_funciones[-1].espacios)
        if self.total_apilado > 11000:
            raise Exception("Limite de memoria en la pila excedido")

    # despues de una funcion liberamos la memoria
    def dormir_memoria(self):
        self.total_apilado -= len(self.pila_funciones[-1].espacios)
        self.pila_funciones.pop()

    # principal metodo para accesar a la memoria en ejecucion
    def buscar_casilla(self, dir):
        alcance = checar_alcance_memoria(dir)
        tipo = checar_tipo_memoria(dir)
        indice = dir % 1000
        if alcance in ['local', 'temp']:
            ret = self.pila_funciones[-1].espacios[alcance][tipo][indice]
            if ret == None:
                raise Exception("Casilla de memoria {} no encontrada".format(dir))
            return ret
        elif alcance == 'glob':
            ret = self.memoria_global.espacios[alcance][tipo][indice]
            if ret == None: 
                raise Exception("Casilla de memoria {} no encontrada".format(dir))
            return ret
        elif alcance == 'ctes':
            ret = self.memoria_ctes.espacios[alcance][tipo][indice]
            if ret == None:
                raise Exception("Casilla de memoria {} no encontrada".format(dir))
            return ret

    # principal metodo usado para el manejo de memoria en ejecucion
    def asignar_casilla(self, dir, val):
        alcance = checar_alcance_memoria(dir)
        tipo = checar_tipo_memoria(dir)
        indice = dir % 1000
        if alcance in ['local', 'temp']:
            self.pila_funciones[-1].espacios[alcance][tipo][indice] = val
        elif alcance == 'glob':
            self.memoria_global.espacios[alcance][tipo][indice] = val
        elif alcance == 'ctes':
            self.memoria_ctes.espacios[alcance][tipo][indice] = val

    # pasamos el valor del parametro entre memoria y memoria
    def asignar_param(self, dir, val):
        alcance = checar_alcance_memoria(dir)
        tipo = checar_tipo_memoria(dir)
        indice = dir % 1000
        self.nueva_memoria[-1].espacios[alcance][tipo][indice] = val

    def inicializar_ctes(self, tabla):
        for cte in tabla:
            # nombre : (tipo, direccion, dimensiones)
            if tabla[cte][0] == 'ent':
                self.asignar_casilla(tabla[cte][1], int(cte))
            if tabla[cte][0] == 'flot':
                self.asignar_casilla(tabla[cte][1], float(cte))
            if tabla[cte][0] in ['car', 'cadena']:
                self.asignar_casilla(tabla[cte][1], cte)