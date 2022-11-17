# Pedir al ordenador que escoja un numero entre el 0 y el 100

import random 
numero = random.randint(0, 100) 

# Pedir al usuario que escriba un numero
while True:
    
    while True:
    
    =input("Escribe un numero entre 0 y 100")

    try:
      intento = int(intento)

    except:
        pass
    else:
            #Hacer comparación
        if 0 <= intento <= 100:
            break

    if intento < numero:
        print("Muy grande")
    elif intento > numero:
        print("Demasiado grande")
    else:
        print("¡Ha ganado!")
    # Hemos terminado, salimos del BUCLE 1
    break

