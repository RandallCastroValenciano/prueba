
quiere_clases_input = input("¿Quieres tomar clases de español (SI/NO):").upper()

if quiere_clases_input == "SI":
    quiere_clases = True
elif quiere_clases_input == "NO":
    quiere_clases = False
else:
    print("Si tu respuesta es otra a SI o NO la intepretamos como no")
    quiere_clases = False

conocimiento_previo_espanol_input = input("¿Estudiaste español antes? (SI/NO):").upper()
clase_semanal_input = input("¿Quieres una clase todas las semanas? (SI/NO):").upper()
paquete_clases_input = input("¿Quieres un paquete de 20 clases? (SI/NO):").upper()

quiere_clases = quiere_clases_input == "SI"
conocimiento_previo_espanol = conocimiento_previo_espanol_input == "SI"
clase_semanal = clase_semanal_input == "SI"
paquete_clases = paquete_clases_input == "SI"
quiere_otra_opcion = clase_semanal or paquete_clases

if quiere_clases and quiere_otra_opcion and conocimiento_previo_espanol:
    print("Bienvenido")
else:
    print("Le deseamos lo mejor")

