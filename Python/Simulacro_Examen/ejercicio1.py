# =============================================================================
#EJERCICIO 1
 
# Escribir un programa que pida enteros al usuario, los meta en una lista y luego muestre 
# la suma de esos elementos y la multiplicación de los elementos. (tiempo max 10 minutos)
# =============================================================================

# =============================================================================
# numero=int(input("Dime un numero entero: "))
# entero=[numero]

# i=True
# while i:
    # print(entero)
    # numero=int(input("Dime un numero entero: "))
    # entero=[numero]
# =============================================================================

lista=[]

seguir=True
totalsum=0
totalmul=1

while seguir:
    numero=int(input("Introduce un numero: "))
    lista.append(numero)
    seguir = input("¿Quieres seguir introduciendo numeros? (Si/No)") == "Si"
    
for x in lista:
    totalsum += x
    totalmul *= x
    print("Total Suma: ",totalsum, "Total Multiplicacion: ",totalmul)
