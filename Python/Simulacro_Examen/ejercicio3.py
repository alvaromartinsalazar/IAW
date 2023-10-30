# =============================================================================
# Escribir un programa que pida palabras al usuario, los meta en una lista y además le pida un entero 
# y muestre todas las palabras que su longitud es mayor a ese entero.
# =============================================================================

# =============================================================================
# lista=[]
# while True:
    # palabra=input("Introduce una palabra (escribe fin si quieres finalizar): ")
    
    # if palabra.lower()=="fin":
        # break
    
    # lista.append(palabra)
    # print(lista)

# numero=int(input("Ahora dime un numero entero: "))
# if not lista:
    # print("No se han añadido palabras")
# else:
    # palabras_filtradas = [palabra for palabra in lista if len(palabra) >= numero]
    # print(f"Las palabras {palabra} son mas grandes que {numero}")
# =============================================================================




# Crear una lista para almacenar las palabras ingresadas
palabras = []

# Pedir al usuario que ingrese palabras hasta que ingrese "fin"
while True:
    palabra = input("Ingresa una palabra (o escribe 'fin' para terminar): ")
    
    if palabra.lower() == "fin":
        break
    
    palabras.append(palabra)

# Pedir al usuario un número entero
try:
    longitud_minima = int(input("Ingresa un número entero para la longitud mínima de las palabras a mostrar: "))
except ValueError:
    print("Ingresa un número entero válido.")
else:
    # Filtrar y mostrar las palabras con longitud mayor o igual a la longitud mínima
    palabras_filtradas = [palabra for palabra in palabras if len(palabra) >= longitud_minima]
    
    if palabras_filtradas:
        print("Palabras con longitud mayor o igual a", longitud_minima, ":")
        for palabra in palabras_filtradas:
            print(palabra)
    else:
        print("No hay palabras con longitud mayor o igual a", longitud_minima)
