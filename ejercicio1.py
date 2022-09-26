import csv

productos = [
    {"Producto": "cocacola", "Cantidad": 3, "PrecioUnitario": 33.4},
    {"Producto": "fanta", "Cantidad": 2, "PrecioUnitario": 22.2},
    {"Producto": "sprite", "Cantidad": 1, "PrecioUnitario": 11.1},
]


def usd_a_peso(valor: float):
    return valor * 880


def transformar(producto: dict):
    producto['PrecioUnitario'] = usd_a_peso(producto['PrecioUnitario'])  # modificando columna
    producto['Subtotal']=producto['PrecioUnitario']*producto['Cantidad'] # agregando columna
    return producto


resultado = list(map(transformar, productos))
print(resultado)

with open('productos.csv','w',newline='') as csv_file:  # abro el archivo
    archivocsv=csv.writer(csv_file,delimiter=';')  # aqui le indico que mi csv va a ser productos.csv
    datos=["Producto","Cantidad","PrecioUnitario","Subtotal"]
    archivocsv.writerow(datos) # guardo el encabezado
    for fila in resultado:
        print(fila)
        datos=[fila['Producto'],fila['Cantidad'],fila['PrecioUnitario'],fila['Subtotal']]
        print(datos)
        archivocsv.writerow(datos)

