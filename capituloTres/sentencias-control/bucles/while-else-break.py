#!/usr/bin/python3
""" iterando con while sobre una lista adicionando un else que no se ejecutara por el break """
a, b = 0, 5
while  a < b:
    print(a)
    a += 1
    if a == 4:
        break
else:
    print("fin")
