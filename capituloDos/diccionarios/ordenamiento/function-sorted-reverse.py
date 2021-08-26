""" Function sorted(): para obtener una lista ordenada por las claves contenidas """
# Para cambiar el valor por defecto de la funcion de ordenamiento sorted, podemos utilizar el parametro
# reverse=True. Pdta: su valor por defecto es False
dicc = {'nombre':"jordan", 'edad': 27, 'peso':"67.2"}
print(dicc)
print(sorted(dicc, reverse=True))
