#EJERCICIO 7
#Escribir un programa que almacene la cadena de caracteres contraseña en una 
#variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña 
#correcta.

contra= 1234
contra_pedida=int(input("Ingresa una contrase�a PIN: "))
pin_correcto=False;

while (not pin_correcto):
    if contra==contra_pedida:
        pin_correcto=True
        print("Contrase�a correcta, bienvenid@")
    else:
        print("Contrase�a incorrecta")
        contra_pedida=int(input("Ingresa una contrase�a PIN: "))