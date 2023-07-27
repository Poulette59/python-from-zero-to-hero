#El for es una estructura que sirve para ejecutar un conjunto de sentencias por cad elemento de una colección. Además el for no da una variable para accder en cada vuelta al elemento que corresponde.

example_string = "Esto es un ejemplo"

#Esta es la forma manual carretera ordinaria, picante, vulgar
print(example_string[0])
print(example_string[1])
print(example_string[2])
print(example_string[3])
print(example_string[4])
print(example_string[5])
print(example_string[6])

print("----------------------")
#Esta es la forma pirula, elegante o correcta de recorrer el texto usando un while
position = 0

while position < len(example_string):
    print(example_string[position])
    position += 1

print("-----------------------")

#Esta es la forma ma´s sencilla, elegante pytoneza de recorrer un string
for letter in example_string:
    print(letter)

#forma correcta de recorrer un while
