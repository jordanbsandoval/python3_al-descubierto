#!/usr/bin/python3
# es mutable
# es una estructura de datos
# internamente es representado como una tabla hash. que reprsenta rapidez de acceso y flexibilidad
diccionario = {'a' : 1, 'b' : 2, 'c' : 3}
print("diccionario con elementos: {}".format(diccionario))

diccionario = dict(a=2, b=3, c=3.5)         # tambien puedo declarar un diccionario con la funcion
                                            # dict
print("declarando diccionario con la funcion dict(): {}".format(diccionario))
print("accediendo al valor de un diccionario: {}".format(diccionario['a']))

diccionario['a'] = 12                       # modificando el valor de un elemento atraves de su 
                                            # palabra clave que se asemeja al indice de cualquier
                                            # objeto iterable
print("modificando el valor de un elemento atraves de la palabra clave: {}".format(diccionario))

diccionario['d'] = "hola"                   # si la palabra clave no existe creara un nuevo
                                            # elemento
print("si una palabra clave no esta en el diccionario la creara al final de esta:{}",format(diccionario))

del(diccionario['a'])
print("la funcion del() sirve para eliminar un elemento del diccionario atraves de su palabra clave: {}".format(diccionario))

# metodos y funciones para iterar sobre un diccionario

for k in diccionario.keys():
    print("lista de palabras clave del diccionario: {}".format(k))

for x in diccionario.values():
    print("lista de los valores de los elementos del diccionario: {}".format(x))

for k, x in diccionario.items():
    print("clave:{}, value:{}".format(k, x))

# Crear diccionarios por comprension

dicc_comp = {k: k+1 for k in (1, 2, 3)}
print("cree un diccionario por comprension atraves de un for y una tupla:{}".format(dicc_comp))

new_dicc = {k: 1 for k in ['a', 'b', 'c']}
print("cree un diccionario por compresion declarando un mismo valor para todos:{}".format(new_dicc))
