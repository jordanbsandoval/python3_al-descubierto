#!/usr/bin/python3
""" iterando con for, utilizando la sentencia continue: sirve para hacer caso omiso a cierto caso concreto"""
for i in range(0, 11):
    if i % 2 != 0:
        continue
    print(i)
