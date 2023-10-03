#EJERCICIO 2
#Solicitar al usuario que ingrese dos números y mostrar cuál de los dos es menor. No 
#considerar el caso en que ambos números son iguales.

a= input("Introduce un número cualquiera: ")
b= input("Introduce un segundo número: ")

if(a>b):
    print("El número ",a ,"es mayor que ",b)
else:
    print("El número ",b ,"es mayor que ",a)