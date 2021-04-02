#!/usr/bin/python3
# Estructura de datos que representa una coleccion de objetos que pueden ser de distintos tipos
# son de tipo inmutable
# las tuplas son un tipo de array de objetos que almacena referencias hacia otros objetos 

tupla = (1, 3.5, "que hizo")            # Declare una tupla con 3 elementos de diferentes tipos

concat = tupla + (2, "jordan")          # las tuplas se pueden concatenar y tambien multiplicar
                                        # gracias a los operadores + y *
for i in concat:                        # iteramos sobre la tupla con el operador in
    print("tupla_concat", i)            # El operador in tambien sirve para comparar
    
# principales metodos de las tuplas

print(concat.index(2))                  # metodo index que recibe como argumento un valor y devuelve
                                        # el numero de indice ubicado en los elementos

print(concat.count(1))                  # cuenta el numero de ocurrencias del parametro pasado

# la funcion len sirve para todos los tipos con elementos

print(len(concat))
