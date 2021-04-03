#!/usr/bin/python3
# es mutable
# es una estructura de datos
# internamente es representado como una tabla hash. que reprsenta rapidez de acceso y flexibilidad
diccionario = {'a' : 1, 'b' : 2, 'c' : 3}
print("diccionario con elementos: {}".format(diccionario))

diccionario = dict(a=2, b=3, c=3.5)         # tambien puedo declarar un diccionario con la funcion
                                            # dict
print("declarando diccionario con la funcion dict(): {}".format(diccionario))

diccionario['a'] = 12

print("modificando el valor de un elemento atraves de la palabra clave: {}".format(diccionario))
