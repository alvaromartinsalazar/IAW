#EJERCICIO 1
# =============================================================================
# Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 
# 'Yen':'Y'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de 
# aviso si la divisa no está en el diccionario
# =============================================================================

monedas={'Euro':'€', 'Dollar':'$', 'Yen':'Y'}

divisa=input("¿Que moneda quieres ver?: ") 
moneda=monedas.get(divisa)

if moneda is not None:
    print(f"El simbolo del {divisa} es: {moneda}")    
else:
    print("La divisa buscada no está en el diccionario")    