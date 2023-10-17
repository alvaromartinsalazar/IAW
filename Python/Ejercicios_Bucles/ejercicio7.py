#EJERCICIO 7
#Escribir un programa que almacene la cadena de caracteres contrase√±a en una 
#variable, pregunte al usuario por la contrase√±a hasta que introduzca la contrase√±a 
#correcta.

contra= 1234
contra_pedida=int(input("Ingresa una contraseña PIN: "))
pin_correcto=False;

while (not pin_correcto):
    if contra==contra_pedida:
        pin_correcto=True
        print("Contraseña correcta, bienvenid@")
    else:
        print("Contraseña incorrecta")
        contra_pedida=int(input("Ingresa una contraseña PIN: "))