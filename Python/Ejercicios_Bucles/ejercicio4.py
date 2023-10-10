#EJERCICIO 4
#Escribir un programa que pida al usuario un n�mero entero positivo y muestre por 
#pantalla la cuenta atr�s desde ese n�mero hasta cero separados por comas.

numero = int(input("Ingrese un n�mero entero positivo: "))

if numero <= 0:
    print("El n�mero ingresado no es positivo.")
else:
    cuenta = []
    
    for i in range(numero, -1, -1):
        cuenta.append(str(i))
    
    cuenta_str = ', '.join(cuenta)
    
    print("Cuenta atr�s hasta 0:", cuenta_str)