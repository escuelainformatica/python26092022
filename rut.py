def modificar_fila_cliente(cliente: dict):
    cliente['nombre'] = primer_letra_mayuscula(cliente['nombre'])
    cliente['rut']=limpiar_rut(cliente['rut'])
    return cliente


def primer_letra_mayuscula(argumento: str):
    listado = argumento.split(' ')
    transformado = list(map(str.capitalize, listado))
    resultado = ' '.join(transformado)
    return resultado


def limpiar_rut(rut: str):
    limpiar = rut.replace('.', '') # limpiar= 222222222-k
    limpiar2 = limpiar.upper()  # limpiar=2222222-K
    return limpiar2


clientes = [
    {"rut": "11.223.444-k", "nombre": "John Doe"},
    {"rut": "13223444-K", "nombre": "anna smith"},
]  # listado de diccionario

print(list(map(modificar_fila_cliente, clientes)))
