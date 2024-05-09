import os
import time
limpiar_pantalla="cls"
#Variables
total=0
pikachu=4500
otaku=5000
pulpo=5200
anguila=4800
total=0
menu1=0
menu2=0
menu3=0
roll1=0
roll2=0
roll3=0
roll4=0
os.system(limpiar_pantalla)
while menu1==0:
    time.sleep(1)
    print("Bienvenido al Deliveri de sushis")
    print("1. Pikachu Roll $4500\n2. Otaku Roll $5000\n3. Pulpo Venenoso Roll $5200\n4. Anguila Eléctrica Roll $4800 ") 
    respuesta=int(input("Seleccione mediante el numero que indica el Roll que desea llevar: \n"))
    if respuesta==1:
        roll1=int(input("¿Cuantos Pikachu rolls desea llevar?: \n"))
        total=(pikachu*roll1)
        try:
            salida1=int(input("¿Desea agregar otro roll a su pedido? (1=si/2=no)\n"))
            if salida1==1:
                menu1=0
            elif salida1==2:
                menu2=1
        except ValueError:
            print("Ingrese 1 para agrgar rolls o 2 para finalizar pedido ")
    elif respuesta==2:
        roll2=int(input("¿Cuantos Otaku roll desea llevar?: \n"))
        total=(otaku*roll2)
        try:
            salida1=int(input("¿Desea agregar otro roll a su pedido? (1=si/2=no)\n"))
            if salida1==1:
                menu1=0
            elif salida1==2:
                menu2=1
        except ValueError:
            print("Ingrese 1 para agrgar rolls o 2 para finalizar pedido ")
    elif respuesta==3:
        roll3=int(input("¿Cuantos Pulpo Venenoso roll desea llevar?:\n"))
        total=(pulpo*roll3)
        try:
            salida1=int(input("¿Desea agregar otro roll a su pedido? (1=si/2=no)\n"))
            if salida1==1:
                menu1=0
            elif salida1==2:
                menu2=1
        except ValueError:
            print("Ingrese 1 para agrgar rolls o 2 para finalizar pedido ")
    elif respuesta==4:
        roll4=int(input("¿Cuantos Anguila Eléctrica rolls desea llevar?: \n"))
        total=(anguila*roll4)
        try:
            salida1=int(input("¿Desea agregar otro roll a su pedido? (1=si/2=no)\n"))
            if salida1==1:
                menu1=0
            elif salida1==2:
                menu2=1
        except ValueError:
            print("Ingrese 1 para agrgar rolls o 2 para finalizar pedido ")
    else:
        print("Ingrese un valor de 1 a 4")
    
    while menu2==1:
            descuento=input("Ingrese su codigo de descuento: ")
            if descuento=="soyotaku":
                descuento_valor=(total/100)*10
                menu3=1
                break
            else:
                salida2=input("Codigo invalido, ¿desea reingresar el codigo? (x=si/n=no)")
                if salida2=="x":
                    menu2=1  
                elif salida2=="n":
                    menu3=1
                else:
                    print("Ingrese 'x' para reingresar el codigo o 'n' para salir")
    while menu3==1:
                        os.system(limpiar_pantalla)
                        total_productos=(roll1+roll2+roll3+roll4)
                        total_final=(total-descuento_valor)
                        print("------------------------------------")
                        print(F"TOTAL PRODUCTOS: {total_productos}")
                        print("------------------------------------")
                        print(f"Pikachu Roll: {roll1}")
                        print(f"Otaku Roll: {roll2}")
                        print(f"Pulpo Venenoso Roll: {roll3}")
                        print(f"Anguila Eléctrica Roll: {roll4}")
                        print("-------------------------------------")
                        print(f"Subtotal por pagar: ${total}")
                        print(f"Descuento por codigo: ${total-(descuento_valor)}")
                        print(f"TOTAL: ${total_final}")
                        salida3=int(input("¿Desea realizar otro pedido? (1=si/2=no): \n"))
                        if salida3==1:
                            menu1=0
                            menu2=0
                            menu3=0
                            os.system(limpiar_pantalla)
                        elif salida3==2:
                            print("Gracias por su preferencia")
                            menu1=20
                            print(f"{menu1}")
                        else:
                            print("Ingrese una respuesta valida (1-2)")
                            
                           

       



