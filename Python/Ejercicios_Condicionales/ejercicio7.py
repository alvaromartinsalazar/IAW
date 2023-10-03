#EJERCICIO 7
#Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos 
#ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte 
#al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene 
#que tributar o no.

edad=int(input("Introduzca su edad: "))
ing=input("Introduzca ahora sus ingresos mensuales: ")

if (edad>16):
    if(ing>=1000):
        print("Usted tiene que tributar")
    else:
        print("Usted NO tiene que tributar")
else:
    print("Usted no tiene la edad mínima para poder tributar")