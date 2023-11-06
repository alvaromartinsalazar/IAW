while True:
    try:
        age=int(input("¿Cuantos años tienes? "))
        for i in range(age):
            print("Has cumplido "+str(i+1)+" años")
        break
    except ValueError:
        print("Tienes que introducir un numero")
        continue