""" La compresion de diccionarios puede ser muy util para inicializar 
    un diccionario a un determinado valor, tomando como claves los elementos de una lista """
lista = ["nombre", "apellido", "ciudad"]
dicc = {value: 1 for value in lista}
print(dicc)
