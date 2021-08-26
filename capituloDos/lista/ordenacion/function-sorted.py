#!/usr/bin/python3
""" function sorted(): Ordena los elementos de una lista de mayor a menor por defecto
    podemos utilizar la opcion reverse para ordenar de menor a mayor su valor debe ser True 
    El valor del objeto no es modificado permanentemente """
lista = [2, 8, 6, 3, 9]
print(lista)
print("valor por defecto: {}".format(sorted(lista)))
print("valor reverse=True: {}".format(sorted(lista, reverse=True)))
print(lista)
