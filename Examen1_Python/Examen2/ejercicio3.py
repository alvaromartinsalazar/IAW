# =============================================================================
#EJERCICIO 3
# Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un 
# alumno. A continuación debe mostrar todas las notas, la nota media, la nota más alta que ha 
# sacado y la menor. 
# =============================================================================

lista=[]

x=0
while x < 5:
    x+=1
    nota=int(input("Dime una nota: "))
    lista.append(nota)
    
for i in lista:
    media=sum(lista) / 5
    i+=1

print("Las notas dadas son: ", lista)
print("La nota media es: ", media)
print("La nota mas alta es:", max(lista))
print("La nota mas baja es: ", min(lista))
