#!/usr/bin/python3
conjunto = {2, 4, 6}        # Definicion de un conjunto con sus elementos
conjunto2 = set('678')         # definicion de conjunto via funcion
print(conjunto2)
# metodos integrados para realizar operaciones con conjuntos
# interseccion
interseccion = conjunto & conjunto2
print(interseccion)        # interseccion con el operador (&)

inter2 = conjunto.intersection(conjunto2)
print(inter2)
