#Ejercicio Laberinto

def laberinto(muro, dim):
   
 
   lab = []
 
   for i in range(dim):

     f = []
     
     for k in range(dim):


        if tuple([i, k]) in muro: 
        
          f.append("X")

          
        else:

          f.append(" ")

     lab.append(f)
   return lab

       
muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3)) 
dim = 5

lab = laberinto(muro, dim)

for i in lab:
    print(''.join(i))





def recorrer_lab(lab,numero):

  fila = column = 0 
 
 

  mov = ['Abajo']

  while(fila < numero-1 and column < numero -1 ):

    if mov[-1] != "Arriba" and fila+1 < numero and lab[fila+1][column] != "X":

      fila += 1 
      mov.append("Abajo")

    elif mov[-1] !="Abajo" and fila-1 > 0 and lab[fila-1][column] != "X":

      fila -= 1
      mov.append("Arriba")

    elif mov[-1] != 'Izquierda' and column +1 < numero and lab[fila][column +1] != 'X':

      column += 1
      mov.append("Derecha")

    elif mov[-1] !="Derecha" and column-1 > 0 and lab[fila][column-1] !="X":

      column -= 1
      mov.append("Izquierda")
    
    else:

      mov.append("por aqui no es la salida")
    

  return mov


print("Para encontrar la salida: ",recorrer_lab(lab,5))
