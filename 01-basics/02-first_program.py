#Practicamente la totalidad de las aplicaciones y programas computacionales realizan las mismas operaciones:
# -Tomar datos desde el exterior como el teclado, el mause, las redes (internet) u algún otro dispositivo como sensores o cámaras.

#Python  trae también una función básica para ingresar datos desde el teclado. La función input()

#2- SALIDA datos al exterior como la terminal como un archivo, enviarlo por la red (internet) o un parlante , etc. 

#Python trae para esto la función print() que veremos mas en detalle más adelante.

#3- Otra operacón que hace la mayoria de los programas es la EJECUCIÓN CONDICIONAL, que dependiendo de los valores ingresados, ejecutan programas de cieta forma.
#Python trae para esto las ESTRUCTURA DE CONTROL que también conoceremos más adelante 

#4- También los programas realizan operaciones con los valores, ya sea combinando, sumando, acumulando, calculando, etc.

#5- Repeticiones : Muchas veces para obtener un resultado es neesario repetir pasos sucesivos (receta de cocina).

username = input("Hola. ¿Cúal es tu nombre?")

print("Hola "+username)

if username == "Harvys":
    print("¡Somos tocayos!")

for letra in username:
    print(letra)
