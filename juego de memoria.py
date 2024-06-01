import random   # para los numero aleatorios
import time     # para el tiempo que dura en pantalla
import os       # Para elegir SO que deseemos aplicar

minimo = 1
maximo = 9

while True:
    numero = str(random.randint(minimo,maximo))
    print(f"Recuerda el numero {numero}...")
    time.sleep(1.5)
    os.system("cls")
    intentoUser = input("Introduce el numero ")
    
    if intentoUser == numero:
        print("Lo has adivinado ")
        minimo *=10
        maximo *=10
        
    else:
        print("Mal, El numero era ", numero)
        break