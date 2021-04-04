#!/usr/bin/python3
# la sentencia with se utiliza con objetos que soportan el protocolo de manejador de contexto
# y garantiza que una o varias sentencias seran ejecutadas automaticamente.
# ejemplo un fichero de texto. Al terminar esta operacion siempre es recomendable cerrar el fichero
# con with esto ocurrira automaticamente, sin necesidad de llamar al metodo close()
with open(r'./README.md') as myFile:
    for line in myFile:
        print(line)
