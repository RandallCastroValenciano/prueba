"""
Preguntar al usuario un serie de 10 # y determinar cual de estos es el más alto.
"""

numeros_usuario = []
numero_del_usuario = ""

while len(numeros_usuario) < 10:
    while not numero_del_usuario.isdigit():
        numero_del_usuario = input("Dime un número: ")
    numeros_usuario.append(int(numero_del_usuario))
    numero_del_usuario = ""
    print("¡Número añadido!")

numero_pequenno = numeros_usuario[0]

for numero in numeros_usuario:
    if numero < numero_pequenno:
        numero_pequenno = numero

print("El número más bajo es {}".format(numero_pequenno))