#Pedir al usuario la temperatura
user_tem = int(input("Ingrese la temperatura: "))

# Si la temperatura es menor que cero imprime me congelo
if user_tem <= 0:
    print("Me congelo")
#Si la temperatura es entre uno y quince imprime tengo frío 
elif user_tem >= 1 and user_tem <= 15:
    print("Tengo frío")
#Si la temperatura esta entre 16 y 25 imprime temperatura ideal
elif user_tem >= 16 and user_tem <= 25:
    print("Temperatura ideal")
#Si la temperatura es mayot a 26  imprime tengo calor  
else:
    print("Tengo calor")

 