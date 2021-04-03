#!/usr/bin/python3
# Ordenamiento de listas por metodo sort o la funcion sorted, 
lista = [1, 3, 2, 8, 5]                         # Creo una lista con elementos enteros
print(lista)

print("funcion= ",sorted(lista, reverse=True))  # utilizo la funcion sorted con el parametro reverse
                                                # ordenando asi de mayor a menor por defecto el valor
                                                # es False. No guarda los cambios
print(lista)
lista.sort()
print("metodo sort {}".format(lista))           # utilizo el metodo sort que ordena los elementos 
                                                # automaticamente de menor a mayor. Si guarda los
                                                # cambios
print(lista)
lista.reverse()
print("metodo reverse", lista)                  # este metodo ordena la lista de mayou a menor y 
                                                # guarda los cambios

print(lista)
