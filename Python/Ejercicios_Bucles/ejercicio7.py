#EJERCICIO 7
#Escribir un programa que almacene la cadena de caracteres contraseña en una 
#variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña 
#correcta.

contra= "1234"
contra_pedida=int(input("Ingresa una contrase�a PIN: "))
pin_correcto=True;

while (not pin_correcto):
    if contra_pedida==contra:
        print("Contrase�a correcta, bienvenid@")
        pin_correcto=True
    else:
        print("Contrase�a incorrecta")
        contra_pedida=int(input("Ingresa una contrase�a PIN: "))