#EJERCICIO 3
#Escribir un programa que pida al usuario un nœmero entero positivo y muestre por 
#pantalla todos los numeros impares desde 1 hasta ese numero separados por comas.

numero = int(input("Ingrese un numero entero positivo: "))

if numero <= 0:
    print("El numero ingresado no es positivo.")
else:
    impares = []

    for i in range(1, numero + 1, 2):
        impares.append(str(i))

    impares_str = ', '.join(impares)

    print("Numeros impares desde 1 hasta", numero, ":", impares_str)
