mensaje = input("Introduce el mensaje: ")
desplazamiento = ""
while desplazamiento.isdigit() == False:
    desplazamiento = input("Introduce el desplazamiento: ")

desplazamiento = int(desplazamiento)
output = ""

for i in range(len(mensaje)):
    output += chr((ord(mensaje[i]) + desplazamiento) % 256)

print("El mensaje es: " + output)
