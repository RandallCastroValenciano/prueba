
tecnicas = []
input_usuario = ""

while input_usuario != "FIN":
    input_usuario = input("¿Qué técnicas deseas dominar? (Escribe FIN para salir): ")
    if input_usuario != "FIN":
        tecnicas.append(input_usuario)

largo_lista = len(tecnicas)

indice_actual = 0

while indice_actual < largo_lista:
    print("Quiero dominar {}".format(tecnicas[indice_actual]))
    indice_actual += 1

print("Estas son las técnicas que quieres dominar bien")