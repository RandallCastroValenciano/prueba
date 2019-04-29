"""

Obtener los tipos de datos que hay en una lista.
"""

lista_datos = [1,"sd",4.5,False,[]]
lista_tipos = []

for dato in lista_datos:
    lista_tipos.append(type(dato))

print(lista_tipos)