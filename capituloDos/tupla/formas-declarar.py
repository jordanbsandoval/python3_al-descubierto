#!/usr/bin/python3
""" Maneras de declarar una tupla """
maneraUno = ('c', 10, 3.5)
print(maneraUno)
maneraDos = ('b', 12, 4.6, )
print(maneraDos)
# una tupla dentro de otra tupla, es posible declarar, ya que tambien es un objeto
maneratres = (maneraUno, 'z', 27)
print(maneratres)
