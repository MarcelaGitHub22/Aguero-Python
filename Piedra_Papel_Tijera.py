# Piedra Papel o Tijera
import random

print ("Ingrese Piedra Papel O Tijera")
elige=int(input("1. Piedra 2. Papel 3. Tijera: "))
numero_aleatorio = random.randint(1, 3)
if (elige==numero_aleatorio):
    print ("Empataron")
else:
    if (elige==1 and numero_aleatorio==3) or (elige==2 and numero_aleatorio==1) or (elige==3 and numero_aleatorio==2):
        print(f"La Computadora eligió: {numero_aleatorio}")
        print("Ganastes")
    else:
        if (elige==1 and numero_aleatorio==2) or (elige==2 and numero_aleatorio==3) or (elige==3 and numero_aleatorio==1):
            print(f"La Computadora eligió: {numero_aleatorio}")
            print("Perdistes")
