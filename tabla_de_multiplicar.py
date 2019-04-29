
numero_tabla = int(input("¡¿De qué # querés la tabla de multiplicar? :"))

for multiplo in range(1,11,1):
    print("{} x {} = {}".format(numero_tabla, multiplo, numero_tabla * multiplo))