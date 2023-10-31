# =============================================================================
#EJERCCIO 5
# Adivine el número de 1 a 100. Escribe un programa que guarde un valor constante 
# en una variable llamada adivinaNumero. Posteriormente pregunte al usuario que intente 
# acertar el número. Para cada intento se ha de indicar si el número guardado es mayor o menor 
# que el ingresado por el usuario. Al final del programa, cuando acierte el número, se ha de 
# indicar los intentos utilizados.
# Un ejemplo de salida sería: “Has acertado el número, te ha llevado X intentos 
# =============================================================================


lista=[]

adivinaNumero=3

a=True
while a:
    numero=input("Introduce un numero: ")
    lista.append(numero)
    
    if numero < adivinaNumero:
        print("numero dado mas pequeño")
    elif numero > adivinaNumero:
        print("numero dado mayor")
    else:
        print("has acertado")
        a==False
        
print(len(lista[numero]))