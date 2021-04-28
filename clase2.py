from math import pi
# 1
def calcularArea(r):
    return (pi*r**2)

def uno():
    try:
        radio = float(input("Ingrese el radio del circulo: "))
        print(calcularArea(radio))
    except ValueError:
        print("El radio debe ser un número.")

#2
def dos():
    try:
        numero = int(input("Ingrese un numero: "))
        print(numero + (numero*numero) + (numero*numero*numero))
    except ValueError:
        print("El número debe ser entero.")

#3
def tres():
    cont = 0
    cadena = input("Ingrese una cadena: ")
    if cadena != "":
        print("El tamaño de la cadena es: ", len(cadena))
    else:
        print("El tamaño de la cadena es 0.")
    for c in cadena:
        if c == "a":
            cont += 1
        elif c == "A":
            cont += 1
    print("La cantidad de letras A o a es: ", cont)

from datetime import datetime
#4
def cuatro():
    horaActual = "La hora actual es: " + str(datetime.now().hour) + ":" + str(datetime.now().minute) + ":" + str(datetime.now().second)
    print( horaActual.strip())
    horaActualMasDos = "La hora actual es: " + str(datetime.now().hour + 2) + ":" + str(datetime.now().minute) + ":" + str(datetime.now().second)
    print(horaActualMasDos.strip())

# Main
numero_de_ejercicio = int(input("Seleccione el ejercicio: "))
if numero_de_ejercicio == 1:
    uno()
elif numero_de_ejercicio == 2:
    dos()
elif numero_de_ejercicio == 3:
    tres()
elif numero_de_ejercicio == 4:
    cuatro()