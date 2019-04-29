
frase_del_usuario = input("Introduce una frase: ")

espacio = [" "]
punto = ["."]
coma = [","]

n_espacios = 0
n_puntos = 0
n_comas = 0

for signo_ortografico in frase_del_usuario:
    if signo_ortografico in espacio:
        n_espacios += 1
    elif signo_ortografico in punto:
        n_puntos += 1
    elif signo_ortografico in coma:
        n_comas += 1

print("Los espacios son {}".format(n_espacios))
print("Los puntos son {}".format(n_puntos))
print("Las comas son {}".format(n_comas))







