#!/usr/bin/python3
""" Declarando una lista por una construccion sintatica. Nos permite declarar una lista atraves de otra """
lista = [ele for ele in (1, 3, 2, 7)]
print(lista)

otraLista = []
for i in ("hola", 1 , 6.8):
    otraLista.append(i)
print(otraLista)
