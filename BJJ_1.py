
tecnicas = []
input_usuario = ""

input_usuario = input("¿Qué técnicas deseas dominar? (Escribe FIN para salir): ")

while input_usuario != "FIN":
        tecnicas.append(input_usuario)
        input_usuario = input("¿Qué técnicas deseas dominar? (Escribe FIN para salir): ")

largo_lista = len(tecnicas)

indice_actual = 0

while indice_actual < largo_lista:
    print("Quiero dominar {}".format(tecnicas[indice_actual]))
    indice_actual += 1

print("Estas son las técnicas que quieres dominar bien")