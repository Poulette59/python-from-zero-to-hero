import random

computer_choice = random.choice(["cara", "sello"])
user_option = input("Escoja entre cara y sello")

if computer_choice == user_option:
    print("El computador tiró:", computer_choice)
    print("¡Empate!")

elif computer_choice == "cara" and  user_option == "sello" :
    print("El computador tiró:", computer_choice)
    print("!Ganaste")

else:
    print("El computador tiró:", computer_choice)
    print("Perdiste")