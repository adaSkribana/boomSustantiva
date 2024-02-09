from time import sleep
print("******************************************************")
print("**********Bienvenidos a nuestra bomba virtual*********")
print("******************************************************")
for num in reversed(range(11)):
    print(num)

    if num == 2:
        user_option=(input("Ingresa una opcion de entre estos colores para detener la bomba\n \
                    'SOLO TIENES UNA OPORTUNIDAD'\n \
                           rojo \n \
                           verde\n \
                      ¿cual escoges? r: "))
        if user_option == "rojo":
            print("salvao - bomba desactivada")
            break
        else:
            print("cagaste")
    elif num == 0:
        print("**bo0m**")    
    sleep(1)  

        
