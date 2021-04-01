#!/usr/bin/python3
lista1 = [9, 8, 7]

print("al objeto que apunta lista1= ",lista1)

lista2 = lista1

print("al objeto que apunta lista2= ", lista2)

lista2[2] = 5
print("valor de lista2 al modificar un elemento de la lista",lista2)

print("modifique el valor de lista2 para ver si afecta directamente a lista 1. valor lista 1: ", lista1)
