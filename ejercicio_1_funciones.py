import csv
from functools import reduce


def usd_a_peso(valor: float):
    return valor * 880


def fn_filtrar(producto: dict):
    if producto['Categoria'] == 'cat1':
        return True
    else:
        return False


def transformar_fila(producto: dict):
    producto['PrecioUnitario'] = usd_a_peso(producto['PrecioUnitario'])  # modificando columna
    producto['Subtotal'] = producto['PrecioUnitario'] * producto['Cantidad']  # agregando columna
    return producto


def generar_csv(nombre: str, productos: list):
    with open(nombre, 'w', newline='') as csv_file:  # abro el archivo
        archivocsv = csv.writer(csv_file, delimiter=';')  # aqui le indico que mi csv va a ser productos.csv
        datos = ["Producto", "Cantidad", "PrecioUnitario", "Subtotal","Categoria"]
        archivocsv.writerow(datos)  # guardo el encabezado
        for fila in productos:
            datos = [fila['Producto'], fila['Cantidad'], fila['PrecioUnitario'], fila['Subtotal'], fila["Categoria"]]
            archivocsv.writerow(datos)


def transformar_listado_diccionario(fila: list):
    return {"Producto": fila[0], "Cantidad": int(fila[1]), "PrecioUnitario": float(fila[2]), "Categoria": fila[3]}


def leer_csv(nombre: str):
    with open(nombre, 'r', newline='') as csv_file:
        lector = csv.reader(csv_file, delimiter=';')
        valores = list(lector)  # list de listado
        valores.pop(0)  # eliminar el encabezado (el primer elemento de la lista)
        valores2 = list(map(transformar_listado_diccionario, valores))  # list de diccionario
        return valores2

def fn_reducir(producto: dict):
    return dict['Subtotal']

def filtrar(productos:list):
    return list(filter(fn_filtrar,productos))

def transformar(productos:list):
    return list(map(transformar_fila, productos))

# def total(productos:list):
#    return reduce(fn_reducir,productos)