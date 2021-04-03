#!/usr/bin/python3
# es mutable
# Basicamente una lista es una coleccion ordenada de objetos similar a un 
# array dinamico: No tiene un tamano fijo, permiten que se quiten o anadan elementos

# definiciendo una lista

lista = []          # defino una lista vacia

lista = [2, 4.5, "hola parce"]      # defino una lista entre corchete 
lista[1] = 3.5                      # de esta manera modifico atraves de un indice el valor asignado

valor_true = "2" in lista           # podemos comprobar si un determinado valor existe en los 
                                    # elementos de la lista atraves del operador in
print(valor_true)

# insertar y eliminar elementos de una lista
# insertando
lista.append(7)                     # este metodo toma el argumento pasado y lo inserta 
                                    # a la lista ubicandolo al final de la lista automaticamente
print(lista)

lista.insert(9, "hola")             # Este metodo toma 2 argumentos el primero indica el indice
                                    # donde desea agregar el elemento y el siguiente parametro
                                    # se utiliza para indicar el valor a asignar 
                                    # si este excede al numero de elementos en la lista se insertara
                                    # al final de la lista
print(lista)

# eliminando
# para eliminar elementos de una lista contamos con funciones y metodos

del(lista[1])                   # para eliminar usamos la funcion del y como argumento 
                                # recibira una lista seguido del indice que desea eliminar
print(lista)

lista.remove(7)                 # El memtodo remove recibe por agumento el valor a eliminar
                                # de la lista

print(lista)

lista.pop(0)                    # a diferencia del metodo remove. El metodo pop devuelve el
                                # elemento borrado y recibe como para el indice a eliminar
                                # sino se pasa valor sera el ultimo elemento el eleminado
print(lista)
