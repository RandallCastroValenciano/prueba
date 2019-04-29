

frase_del_usuario = input("Introduce una frase: ")

n_palabras = 0

for palabra in frase_del_usuario:
    if palabra in frase_del_usuario:
        n_palabras += 1

print("Las palabras son {}".format(n_palabras))

