#Podemos encontrar  situaciones en que se requiere de más de una evalución condicional para determinar el flujo de ejecucíon del programa. Esto lo hacemos con la estructura eluf que también evalúa una sentencia booleana.

first_num = int(input("Ingresa el primer número: "))
second_num = int(input("Ingresa el segundo número: "))

if first_num > second_num:
    print("El primer número es mayor")
elif first_num < second_num:
    print("El segundo número es mayor")
else:
    print("Son iguales")
    