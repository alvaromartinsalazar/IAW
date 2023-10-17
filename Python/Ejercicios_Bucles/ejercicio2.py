#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los 
#años que ha cumplido (desde 1 hasta su edad).

i=0
v_edad=int(input("Tu edad: "))

while i<v_edad:
    i=i+1
    print("Has cumplido: ",i," anos")