#EJERCICIO 5
#Requerir al usuario que ingrese un día de la semana en minusculas e imprimir un 
#mensaje si es lunes, otro mensaje diferente si es viernes, otro mensaje diferente si es 
#sábado o domingo. Si el día ingresado no es ninguno de esos, imprimir otro mensaje.


a=input("Introduce un día de la semana en minúsculas: ")

if(a=="lunes"):
    print("Hoy empieza la semana pero tranquil@ se pasará volando")
elif(a=="viernes"):
    print("Prepárate que hoy empieza la fiesta, bueno y el finde tambien")
elif(a=="sábado" or a=="sabado"):
    print("Disfruta del día que mañana ya es el último de la semana")
elif(a=="domingo"):
    print("Aprovecha y haz lo que te quede de deberes del insti que mñana empiezan las clases")
else:
    print("Hoy es un día sin más... O has escrito mal el día")