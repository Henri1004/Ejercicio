# Pedir al ordenador que escoja un numero entre el 0 y el 100

import random 

numero = random.randint(0, 100) 

print(numero)


while True:

    intento = input("Escribe un numero entre 0 y 100: ")
    
    try:

      intento = int(intento)

    except:
        pass
    else:
            #Hacer comparación
        if 0 <= intento < 100:
            break


if intento < numero:
        print("Demasiado pequeño")
elif intento > numero:
        print("Demasiado grande")
else:
        print("¡Ha ganado!")
    # Hemos terminado, salimos del BUCLE 1
      

#PARTE 2 

print("Intente encontrar el número a adivinar")

while True:  # BUCLE 1
    # Entramos en un bucle infinito
    # que permite jugar varios turnos

    while True:  # BUCLE 2
        # Entramos en un bucle infinito
        # que permite corregir un error de escritura

        # Pedimos introducir un número
        intento = input("Introduzca un número entre 0 y 99 incluídos: ")

        try:
            intento = int(intento)
        except:
            pass
        else:
            # Hacer la comparación
            if 0 <= intento <= 99:
                # Tenemos lo que queremos, salimos del BUCLE 2
                break

    # Se prueba si el intento es correcto o no
    if intento < numero:
        print("Demasiado pequeño")
    elif intento > numero:
        print("Demasiado grande")
    else:
        print("Victoria!")
        # Terminamos la partida, salimos del BUCLE 1
        break
