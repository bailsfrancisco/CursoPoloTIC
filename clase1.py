# 1
def uno():
    mensaje = "Hola mundo!"
    a = 10
    b = 5
    if a > b:
        print(mensaje)

# 2
def dos():
    contador = 0
    try:
        numero = float(input("Ingrese un número decimal: "))
        while contador < 4:
            if not int(numero):
                if type(numero) == float:
                    contador += 1
            else:
                    print("El número debe ser float.")
            numero = float(input("Ingrese un número decimal: "))
    except ValueError:
        print("El número debe ser float (excepción).")

# Main
numero_de_ejercicio = int(input("Seleccione el ejercicio: "))
if numero_de_ejercicio == 1:
    uno()
elif numero_de_ejercicio == 2:
    dos()