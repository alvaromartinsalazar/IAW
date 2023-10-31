# =============================================================================
# EJERCICIO 4
# Escriba un programa que, a partir de dos listas, devuelva si hay un elemento 
# común o no.
# No hace falta pedir valores al usuario, puedes utilizar por ejemplo estas dos listas
# lista1 = [1, 5, 8, 4, 3]
# lista2 = [4, 5, 2, 1]
# Para este caso la salida sería: “Sí existen elementos repetidos en ambas listas” 
# =============================================================================


lista1=[1,5,8,4,3]
lista2=[4,5,2,1]

for i in lista1:
    for j in lista2:
        if i==j:
            break
            
print("Sí existen elementos repetidos en ambas listas")