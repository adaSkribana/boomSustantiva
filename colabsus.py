from time import sleep

for num in reversed(range(11)):
    print(num)

    if num == 2:
        user_option=(input("Ingresa una opcion de entre estos colores para detener la bomba:\n \
                    'SOLO TIENES UNA OPORTUNIDAD\n rojo \n verde\n \
                      ¿cual escoges? r: "))
        if user_option == "rojo":
            print("Te salvaste")
            break
        else:
            print("cagaste")
    elif num == 0:
        print("Kaboom")    
    sleep(1)  

        
