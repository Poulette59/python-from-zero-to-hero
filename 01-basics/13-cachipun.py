import random 
#Programar con estructuras de control y expresiones booleanas un juego del cachiún
#El programa debe solicitar al usuario que escriba piedra, papel o tijeras

computer_choice = random.choice(["piedra", "papel", "tijeras"])
print("Bienvenidoos al juego del cachipún")

user_option = input("Escoje entre piedra, papel y tijeras: ")

if user_option ==  computer_choice:
    print ("La opción del computador es :" ,
    computer_choice)
    print("¡Empate!")

elif (user_option == "tijeras" and computer_choice == "papel") or (user_option == "piedra" and computer_choice == "tijeras") or (user_option == "papel" and computer_choice == "piedra"):
    print ("La opción del computador es :" ,
    computer_choice)
    print("¡Ganaste!")

else:
    print ("La opción del computador es :",
    computer_choice)
    print("¡Perdiste!")




 