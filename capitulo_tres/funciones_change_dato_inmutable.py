#!/usr/bin/python3
a, b = 2, 3
print("Valor actual= a:{} y b:{}".format(a, b))

def change_value(c, d):
    c, d = 5, 6
    return (c, d)

a, b = change_value(a, b)
print("Valor despues= a:{} y b:{}".format(a, b))
