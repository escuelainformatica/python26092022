import csv
from ejercicio_1_funciones import transformar, generar_csv, leer_csv

productos = leer_csv('prod1.csv')
print("inicial:----")
print(productos)

resultado = list(map(transformar, productos))
print("final:----")
print(resultado)
generar_csv("prod2.csv",resultado)

