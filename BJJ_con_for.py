
tecnicas = []
input_usuario = ""

while input_usuario != "FIN":
    input_usuario = input("¿Qué técnicas deseas dominar? (Escribe FIN para salir): ")
    if input_usuario != "FIN":
        tecnicas.append(input_usuario)

for item in tecnicas:
    print("Quiero dominar {}".format(item))

print("Estas son las técnicas que quieres dominar bien")