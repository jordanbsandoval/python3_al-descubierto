#!/usr/bin/python3
x = 5
y = 8

for i in range(1, 5): 
    print(i)

lista = ["uno", "dos", "tres"]  # lista con sus elementos
string = ""

for i in lista:        # apunto a los objetos que contiene la funcion range
    string += i
    
print(string)

# for admite la sentencia else. Si esta aparece todas las sentencias posteriores se ejecutan

tupla = (1, "hola", 2.8)
for i in tupla:
    print("imprime la tupla: {}".format(i))
else:
    print("ejecutando el else que posteriormente seran ejecutas todas las sentencias")

# Tambien existe otro bucle como while

while x < y:
    print(x)
    x += 1
    if x == 7:
        break                   # Esta sentencia se utiliza para salir del ciclo
    else:
        print("x es igual que 8")
