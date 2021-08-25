""" Iterando sobre un diccionario atraves de sus elementos, segun el metodo """
dicc = {'edad': 28, 'nombre':"jordan", 'peso':"67.2"}
for i ,x in dicc.items():
    print("clave={}, valor={}".format(i, x))

for i in dicc.values():
    print("valor={}".format(i))

for i in dicc.keys():
    print("clave={}".format(i))
