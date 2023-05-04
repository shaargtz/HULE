class VonNeumann:
    def __init__(self):
        # Contador de los 20 bloques de memoria
        # 4 segmentos con 5 tipos cada uno
        self.cont = [0] * 20

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
        ##############
        # CONSTANTES #
        ##############
        # 15 [ 15000 -> 15999 : ent ]
        # 16 [ 16000 -> 16999 : flot ]
        # 17 [ 17000 -> 17999 : car ]
        # 18 [ 18000 -> 18999 : cadena ]
        # 19 [ 19000 -> 19999 : bool ]
        self.data = []

    def obtener(self, direccion):
        indice = direccion // 1000
        espacio = direccion % 1000
        while indice:
            espacio += self.cont[indice - 1]
            indice -= 1
        return self.data[espacio]

    def asignar(self, direccion, valor):
        indice = direccion // 1000
        espacio = direccion % 1000
        while indice:
            espacio += self.cont[indice - 1]
            indice -= 1
        print(espacio)
        self.data[espacio] = valor
            
    def siguiente_espacio(self, tipo):
        codigo = {
            'global_ent' : 0,
            'global_flot' : 1,
            'global_car' : 2,
            'global_cadena' : 3,
            'global_bool' : 4,
            'local_ent' : 5,
            'local_flot' : 6,
            'local_car' : 7,
            'local_cadena' : 8,
            'local_bool' : 9,
            'temp_ent' : 10,
            'temp_flot' : 11,
            'temp_car' : 12,
            'temp_cadena' : 13,
            'temp_bool' : 14,
            'cte_ent' : 15,
            'cte_flot' : 16,
            'cte_car' : 17,
            'cte_cadena' : 18,
            'cte_bool' : 19,
        }
        indice = codigo['tipo']
        espacio = self.cont[indice] + indice * 1000
        return espacio

        