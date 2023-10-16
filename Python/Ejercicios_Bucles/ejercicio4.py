#EJERCICIO 4
#Escribir un programa que pida al usuario un nœmero entero positivo y muestre por 
#pantalla la cuenta atr‡s desde ese nœmero hasta cero separados por comas.

numero = int(input("Ingrese un numero entero positivo: "))

if numero <= 0:
    print("El numero ingresado no es positivo.")
else:
    cuenta = []
    
    for i in range(numero, -1, -1):
        cuenta.append(str(i))
    
    cuenta_str = ', '.join(cuenta)
    
    print("Cuenta atras hasta 0:", cuenta_str)