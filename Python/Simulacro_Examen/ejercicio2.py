# =============================================================================
#EJERCICIO 2
# Escribir un programa que pida palabras al usuario, los meta en una lista y 
# luego indique que palabra es la más larga 
# =============================================================================

lista=[]
mayor=""

i=True
while i:
    palabra=str(input("Introduce una palabra: "))
    lista.append(palabra)
    i=input("¿Quieres seguir introduciendo palabras? (Si/No)") == "Si"
    print(lista)
    
for a in lista:
    if len(lista[a]>len(mayor)):
        mayor=lista[a]
        
print("La palabra mas grande es: ", mayor)