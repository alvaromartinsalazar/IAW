# =============================================================================
#EJERCICIO 2
# Escribir un programa que pida palabras al usuario, los meta en una lista y 
# luego indique que palabra es la más larga 
# =============================================================================

# Crear una lista para almacenar las palabras ingresadas
palabras = []

# Pedir al usuario que ingrese palabras hasta que ingrese "fin"
while True:
    palabra = input("Ingresa una palabra (o escribe 'fin' para terminar): ")
    
    if palabra.lower() == "fin":
        break
    
    palabras.append(palabra)

# Verificar si la lista de palabras está vacía
if not palabras:
    print("No se ingresaron palabras.")
else:
    # Encontrar la palabra más larga en la lista
    palabra_mas_larga = max(palabras, key=len)

    # Mostrar la palabra más larga
    print(f"La palabra más larga es: {palabra_mas_larga}, con {len(palabra_mas_larga)} caracteres.")
