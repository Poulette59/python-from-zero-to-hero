#Podemos terminar un loop utilizando la palabra clave break
#En general se utilizará con una estructura de control como if/elif

spaces = " "
for letter in "murciélago" :
    print(spaces,letter)
    
    if letter == "a":
        break
    
    spaces += " "