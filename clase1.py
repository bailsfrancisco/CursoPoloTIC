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

# 3
def tres():
    contador = 0
    lista = []
    while contador <= 4:
        numero_entero = int(input("Coloque un número entero: "))
        lista.append(numero_entero)
        contador += 1
    
    for y in lista:
        print(y)

#4
def cuatro():
    lista1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
    for y in lista1:
        if y > 150:
            break
        else:
            if y % 5 == 0:
                print(y)

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