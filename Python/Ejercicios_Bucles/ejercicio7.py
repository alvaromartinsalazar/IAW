#EJERCICIO 7
#Escribir un programa que almacene la cadena de caracteres contrase√±a en una 
#variable, pregunte al usuario por la contrase√±a hasta que introduzca la contrase√±a 
#correcta.

contra= "1234"
contra_pedida=int(input("Ingresa una contraseña PIN: "))
pin_correcto=True;

while (not pin_correcto):
    if contra_pedida==contra:
        print("Contraseña correcta, bienvenid@")
        pin_correcto=True
    else:
        print("Contraseña incorrecta")
        contra_pedida=int(input("Ingresa una contraseña PIN: "))