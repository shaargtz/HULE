class VonNeumann:
    def __init__(self):
        self.memoria = [None] * 20000
        self.glob = 0
        # 0000 -> 0999 : ent
        # 1000 -> 1999 : flot
        # 2000 -> 2999 : car
        # 3000 -> 3999 : cadena
        # 4000 -> 4999 : bool
        self.local = 5000
        # 5000 -> 5999 : ent
        # 6000 -> 6999 : flot
        # 7000 -> 7999 : car
        # 8000 -> 8999 : cadena
        # 9000 -> 9999 : bool
        self.temp = 10000
        # 10000 -> 10999 : ent
        # 11000 -> 11999 : flot
        # 12000 -> 12999 : car
        # 13000 -> 13999 : cadena
        # 14000 -> 14999 : bool
        self.ctes = 15000
        # 15000 -> 15999 : ent
        # 16000 -> 16999 : flot
        # 17000 -> 17999 : car
        # 18000 -> 18999 : cadena
        # 19000 -> 19999 : bool

    def cambiar_valor(self, destino, valor):
        self.memoria[destino] = valor