import os
import time
limpiar_pantalla="cls"
os.system(limpiar_pantalla)
pikachuRoll=4500
otakuRoll=5000
pulpoRoll=5200
anguilaRoll=4800
total=0
porPagar=0

x=True

print("Binevenido a nuestro delivery de sushis")
cantidad=int(input("Ingrese la cantidad de rolls que desea llevar:\n"))
respuesta=input("Lista de precios, ingrese sus opciones: \n1. Pikachu Roll $4500\n2. Otaku Roll $5000\n3. Pulpo Venenoso Roll $5200\n4. Anguila Electrica Roll $4800\n")

while x==True:
    for i in range(1,cantidad+1):
        if respuesta=="1":
            print(f"Pikachu Roll ${pikachuRoll}")
            total+=pikachuRoll
        elif respuesta=="2":
            print(f"Otaku Roll ${otakuRoll}")
            total+=otakuRoll
        elif respuesta=="3":
            print(f"Pulpo Venenoso Roll ${pulpoRoll}")
            total+=pulpoRoll
        elif respuesta=="4":
            print(f"Anguila Electrica Roll ${anguilaRoll}")
            total+=anguilaRoll
        else:
            print("ingrese opcion valida (1-4)")
            x==False
            
    
    
        
        
        