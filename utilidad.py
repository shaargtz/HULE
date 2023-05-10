def checar_tipo_memoria(direccion):
    tipos = ['ent', 'flot', 'car', 'cadena', 'bool']
    aux = direccion % 5000
    aux = aux // 1000
    return tipos[aux]
