
frase_del_usuario = input("Introduce una frase: ")

mayusculas = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

minusculas = ""

n_mayusculas = 0

n_minusculas = 0

for letra in frase_del_usuario:
    if letra in mayusculas:
        n_mayusculas += 1
    else:
        n_minusculas += 1

print("Las letras mayúsculas son {}".format(n_mayusculas))
print("Las letras minúsculas son {}".format(n_minusculas))
