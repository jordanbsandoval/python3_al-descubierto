#!/usr/bin/python3
""" Uilizando la sentencia continue: Esto es util, cuando no deseamos ejecutar una sentencia sobre una itera    cion en concreto """
for i in range(1, 10):
    if i % 2 != 0:
        continue
    print(i)
