#!/usr/bin/python3
# Contamos con sentencias para escoger que imprimir en determinada ocasion y que no. O en caso tal
x = 5
y = 8

if  x < y:
    print("if: Si el valor es verdadero. Se ejecuta la sentencia")
else: print("else: Se ejecuta si la condicion del if es false")

# tambien existe la sentencia elif en caso tal de que su antecesor de False

if x == 9:
    print("igual que 5")
elif y == 8:
    print("y igual q 8")
else:
    print("ninguna afirmacion es verdad")
