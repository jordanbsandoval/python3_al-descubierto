#!/usr/bin/python3
c, d = 2, 3

# declaracion y llamado a una funcion
def funcion():              # palabra clave para definir una funcion que sera un objeto
                            # y el nombre utilizado seguido de la palabra clave def sera quien
                            # apunte al objeto funcion, posteriormente no tiene parametros
    print("invocando la funcion")
funcion()                   # llamando a la funcion

print("variables para probar ejemplos. var c = {}, d = {}".format(c, d))
# Paso de parametros a funciones
# el paso de parametros implica la asignacion de un nombre de variable a un objeto
# el paso de parametros ocurre por valor o referencia en funcion de si los tipos son mutables o inmtb

def cambiar_valor(a, b):                    # Es posible modificar el favor una variable de tipo 
                                            # inmutable utilizando una tecnica que consiste en 
                                            # devolver una tupla y asignandola a las variables
    a = 6
    b = 8
    return(a, b)                            # de esta manera devuelva una tupla con dos valores

c, d = cambiar_valor(c, d)                  # asigno el resultado de la funcion a las variables

print("Cambiando el valor de variables inmutables atraves de una funcion. retornando una tupla")
print("var c = {}, d = {}".format(c, d))

# Es posible no modificar un elemento de un objeto mutable definiendolo asi en la funcion
# pasa el argumento abriendo el indice con el operador :

lista = [2, 4, 6]

def not_modificar_inmutable(lista):
    lista[0]= 1

print(lista)

# valores por defecto

# Es posible declarar valores por defecto en los parametros de la funcion

def funcion(a, b, c = 4):                       # declaro una funcion con 3 parametros
                                                # en el ultimo parametro declaro una variable
                                                # con un valor por defecto. Sino se pasa ningun valor
                                                # al parametro este. sera el valor por defecto
    print("valor de funcion predeterminada")
    print("a={}, b={}, c={}".format(a, b, c))

funcion(c, d)

# Es posible pasar argumentos a funciones utilizando nombres y obviando la posicion que ocupan

def nombre_parametro(a, b, c):
    print("Pasando valor por nombres de referencia")
    print("c = {}, b = {}, a = {}".format(c, b, a))

nombre_parametro(c = 5, b = 3, a = 1)


