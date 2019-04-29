"""
Dada una lista de strings, devolver una lista con el largo de cada string:
"""

lista_strings = ["sfas","sd","sfg","yth","lkl"]
lista_largo_de_cada_string = []

for string in lista_strings:
    lista_largo_de_cada_string.append(len(string))

print(lista_largo_de_cada_string)