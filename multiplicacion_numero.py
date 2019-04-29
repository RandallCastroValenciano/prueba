"""
Dada una lista de números, devolver el resultado de la multiplicacion de todos los números.
"""

lista_numeros = [1,4,5,6,8]
numero_dado = lista_numeros [0]

for numero in lista_numeros:
    if numero * numero_dado:
        numero_dado = numero

print("El resultado de la multiplicacion de todos los números".format(numero * numero_dado ))

