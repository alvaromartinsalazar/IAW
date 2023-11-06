while True:
    try:
        n=int(input("Introduce un numero entero positivo: "))
        if(n<0):
            print("Introduzca un numero entero positivo")
            continue
        for i in range(1, n+1, 2):
            print(i, end=", ")
            break
    except ValueError:
        print("Introduzca un numero entero positivo")
        continue
        