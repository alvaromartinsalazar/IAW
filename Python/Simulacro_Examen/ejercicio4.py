# =============================================================================
# Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona 
# (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. 
# Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.  
# =============================================================================



# =============================================================================
# diccionario={"nombre":"","edad":"", }
# while True:
    # diccionario["nombre"]=input("Dime el nombre de la persona: ")
    # print("El nombre ingresado es:", diccionario["nombre"])
    # diccionario["edad"]=int(input("Dime la edad de la persona: "))
    # print("La edad ingresada es:", diccionario["edad"])
# =============================================================================


persona = {}

continuar = True
while continuar:
    clave = input('¿Qué dato quieres introducir? ')
    valor = input(clave + ': ')
    persona[clave] = valor
    print(persona)
    continuar = input('¿Quieres añadir más información (Si/No)? ') == "Si"
    
    if not continuar==True:
        print(persona)