import csv
from ejercicio_1_funciones import transformar, generar_csv, leer_csv, fn_filtrar, filtrar

productos = leer_csv('prod1.csv')
print("inicial:----")
print(productos)

productosfiltrados=filtrar(productos)
print("filtrado:----")
print(productosfiltrados)

resultado = transformar(productosfiltrados)
print("final:----")



print(resultado)
generar_csv("prod2.csv",resultado)

# print("reduce:------")
#print(red)
