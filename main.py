nombre = "john doe"  # str (texto)


def mifuncion(argumento: str):
    listado = argumento.split(' ')
    transformado = list(map(str.capitalize, listado))
    resultado = ' '.join(transformado)
    return resultado


print(mifuncion(nombre))
print(mifuncion("maria tenia un corderito"))
