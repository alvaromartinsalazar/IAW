#EJERCICIO 4
#Solicitar al usuario que ingrese tres numeros y mostrar cual es el mayor de los tres.

a=input("Introduce el primer número: ")
b=input("Introduce el segundo: ")
c=input("Introduce el tercer número: ")

if(a>b and a>c):
    print("El primer número dado(",a,"),es el número más grande")
elif(b>a and b>c):
    print("El segundo número dado(",b,"),es el número más grande")
elif(a==b or a==c or b==c):
    print("Hay más de un número del mismo valor")    
else:
    print("El último número dado(",c,"),es el número más grande")