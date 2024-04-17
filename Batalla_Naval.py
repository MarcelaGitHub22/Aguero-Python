# ### Batalla naval
#Crear un programa que permita jugar la batalla naval entre dos jugadores. 
# #Cada uno debe ubicar un barco que contiene 3 secciones. 
# Luego cada jugador tira una bomba por turno indicando la posición en x y la posición en y. 
# Si acierta, esa sección del barco queda destruida y se muestra un mensaje por pantalla. Gana el jugador que logre destruir el barco completo del rival.

batalla_naval=[[" 0","0 ","0 ","0","0"],["0 "," 1"," 1","1","0"],["0 "," 0"," 0","0"],[" 0","0"," 0","0"]]
contados=0
for i in range(1,6):
    fila=int(input("Ingresa fila: "))
    columna=int(input("Ingresa columna: "))
    if batalla_naval[fila][columna]==0:
     print("Agua")
    else: 
        contados+=1  
        if contados==3:
            print(contados)
            print("Hundido")
            contados=0
            break
        else:
            if contados==1 or contados==2:
                print("averiado")
                
               