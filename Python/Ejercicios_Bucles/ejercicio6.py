#EJERCICIO 6
#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.


lista=[]
n=1

for i in range (1,11):
    print("La tabla de multiplicar del: ", i)
    for j in range (1,11):
        print(i,"x",j,"=",i*j)
        j=j+1
    i=i+1
