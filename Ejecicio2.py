import random 

#declarar los 4 NIVELES (range)

nivel_1= range(1,100)
print("nivel 1", range(1,100))

nivel_2=range(1,1000)
print("nivel 2", nivel_2)

nivel_3= range(1,1000000)
print("nivel 3",nivel_3)

nivel_4= range(1,1000000000000)
print("nivel 4",nivel_4)

contador = 0


while True:
      intentos = 10
      print("menu principal")
      nivel = input("Escoja un nivel entre el 1 y el 4: ")
      
      if nivel == "nivel 1":
        
        nivel = nivel_1


      elif nivel == "nivel 2":
        
        nivel = nivel_2

     
      elif nivel == "nivel 3":

        nivel = nivel_3

     
      elif nivel == "nivel 4": 

          nivel= nivel_4

      else:

        print("nivel no existe")
        nivel = input("Error, solo disponibles los niveles del 1 al 4:")

      numero_minimo = min(nivel)

      numero_maximo = max(nivel)

      print("numero minimo del nivel: ", numero_minimo)
      print("numero maximo del nivel: ", numero_maximo)
      
      import random
      numero = random.randint(numero_minimo,numero_maximo)
      

      while True:
        while True:
            print("te quedan",intentos,"intentos")
            intento = input("Introduzca un número entre entre los valores exigidos: ")
            try:
               intento = int(intento)
            except:
                   pass
            else:
              if 0 <= intento <= numero_maximo:
                break
        
        intentos -=1
        
        if intento < numero:
          print("Demasiado pequeño")
        elif intento > numero:
          print("Demasiado grande")
        else:
          print("¡Ha ganado!")
          break

      
        if intentos == 0:
          print("perdiste")
          break

      
      contador +=1
      print("su puntuacion es de",contador)

      if contador == 5:
        print("partida acabada")
        
        break