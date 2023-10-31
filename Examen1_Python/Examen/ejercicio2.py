# =============================================================================
#EJERCICIO 2
# Escribe un programa que pida al usuario números y los ingrese en una lista hasta 
# que el usuario indique que no quiere introducir más números. Posteriormente, pregunte al 
# usuario por un número y cuente cuantas veces está el número en esta lista.
# Un ejemplo de salida sería: “El numero X aparece Y veces” 
# =============================================================================

lista=[]

while True:
    numero=input("Introduce un numero: ")
    lista.append(numero)
    print(lista)
    confirma=str(input("¿Quieres seguir introduciendo numeros? (si/no): ")) == "si"
    
    if confirma==False:
        break
    
numero2=int(input("Dime un numero: "))

for i in lista:
    var=lista.count(i)
    
print(f"El numero {numero2} aparece", var)