# clase para almacenar los datos relevantes sobre las dimensiones
# en variables estructuradas. almacena la cantidad espacios de 
# memoria utilizados asi como valores para la formula de indexacion
class Dimensiones:
    def __init__(self, dims):
        self.total = 1
        if dims:
            self.data = []
            m = 1
            for d in dims:
                self.data.append([d - 1, 0])
                m = m * d # calcular R
            self.total = m
            for x in range(len(dims)):
                m = m / dims[x] # calcular M0, M1, ...
                self.data[x][1] = int(m)

    def retornar_dimensiones(self):
        dims = []
        for d in self.data:
            dims.append(d[0])
        return dims
    
    def retornar_m(self):
        m = []
        for d in self.data:
            m.append(d[1])
        return m