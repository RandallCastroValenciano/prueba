"""
Dada una lista mixta de enteros y strings, devolver dos listas, una con todos los enteros y otra con todas las strings.
"""

list_strings_and_enteros = [3,"sf",56,"sdrt"]
lista_strings = []
lista_enteros = []

for dato in list_strings_and_enteros:
    if dato == str:
        lista_strings.append(dato)
    else:
        lista_enteros.append(dato)

print("Estos son las strings{}".format(lista_strings))
print("Estos son las enteros{}".format(lista_enteros))
