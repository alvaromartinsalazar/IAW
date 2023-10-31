# =============================================================================
#EJERCICIO 2
# Crea un programa que pida al usuario un número de mes (por ejemplo, el 4) y diga 
# cuántos días tiene (por ejemplo, 30) y el nombre del mes. Debes usar listas 
# =============================================================================

diccionario={"Enero":"1","Febrero":"2","Marzo":"3",""}

while True:
    mes=int(input("Introduce el número de mes: "))
    if mes%2:
        diccionario[""]=mes
        print(f"El mes {mes} iene 31 dias", diccionario)
    elif mes==2:
        print(f"El mes {mes} tiene menos de 30 dias")
    elif mes==8:
        print(f"El mes {mes} tiene 31 dias")
    else:
        print(f"El mes {mes} tiene 30 dias")
        