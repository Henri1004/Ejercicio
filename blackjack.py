
# blackjack
from random import choice, sample

cartas = {
    chr(0x1f0a1): 11,
    chr(0x1f0a2): 2,
    chr(0x1f0a3): 3,
    chr(0x1f0a4): 4,
    chr(0x1f0a5): 5,
    chr(0x1f0a6): 6,
    chr(0x1f0a7): 7,
    chr(0x1f0a8): 8,
    chr(0x1f0a9): 9,
    chr(0x1f0aa): 10,
    chr(0x1f0ab): 10,
    chr(0x1f0ad): 10,
    chr(0x1f0ae): 10,
}

print("Cartas: {}".format(" ".join(cartas.keys())))
print("Puntos: {}".format(list(cartas.values())))

print("1\ Iteración estándar sobre un diccionario")
for carta, valor in cartas.items():
    print("la carta {} vale {}".format(carta, valor))

print("2\ Iteración ordenada sobre un diccionario")
for carta in sorted(cartas.keys()):
    print("la carta {} vale {}".format(carta, cartas[carta]))

print("3\ Black Jack")
lista_cartas = list(cartas)

print("Ha seleccionado:", end=" ")
carta = choice(lista_cartas) #carta1
score = cartas[carta]
print(carta, end=" ")
carta = choice(lista_cartas) #carta2
score += cartas[carta]
print(carta, end=" ")
print(" >>> su puntuación es de", score)

main_banca = sample(lista_cartas, 2)
score_banca = sum(cartas[carta] for carta in main_banca)
print("La banca tiene: {} {}  >> su puntuación es de {}".format(main_banca[0],
                                                          main_banca[1],
                                                          score_banca))

while True:
  if score_banca < 17:
     carta_nueva_banca = choice(lista_cartas)
     score_banca += cartas[carta_nueva_banca]
     print(carta_nueva_banca, end=" ")
     print("  La puntuacion de la banca es de", score_banca)
     if score_banca > 21:
       print ("ganaste")
     break
  elif score_banca > 21:
    print("ganaste")
  elif score_banca==21:
    print("perdiste")
    break
while True:
  if score <= 21 :
    variable = input("si quieres otra carta escriba X, en caso contrario escriba Y:")
    if variable == "X":
      print("Ha seleccionado:", end=" ")
      carta_nueva = choice(lista_cartas)
      score += cartas[carta_nueva]
      print(carta_nueva, end=" ")  
      print(" >>>su puntuación es de", score)
    elif variable =="Y":
      if 21 > score > score_banca:
       print("La puntuación del jugador es mayor que el de la banca ganaste")
      elif 21 < score:
        print("te pasaste")
      elif score == 21:
        if score > score_banca:
          print("Black Jack del jugador,ganaste")
      elif score == score_banca:
       print("Empate")
      elif score_banca > 21:
        print("ganaste")
      break

  elif score > 21:
      print("perdiste")
