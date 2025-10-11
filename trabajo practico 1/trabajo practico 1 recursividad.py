#5. Desarrollar una función que permita convertir un número romano en un número decimal.

def romano_a_decimal_rec(romano):
    valores = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    romano = romano.upper()

   
    if not romano:
        return 0

  
    if len(romano) == 1:
        return valores[romano]

    actual = valores[romano[0]]
    siguiente = valores[romano[1]]

    if actual < siguiente:
        
        return siguiente - actual + romano_a_decimal_rec(romano[2:])
    else:
       
        return actual + romano_a_decimal_rec(romano[1:])

print(romano_a_decimal_rec("MCMXCIV"))

"""El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u
otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos
objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con
ayuda de la fuerza” realizar las siguientes actividades:
a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no
queden más objetos en la mochila;

b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sa-
car para encontrarlo;

c. Utilizar un vector para representar la mochila."""

def usar_la_fuerza(mochila, objetos_sacados=0):
   
    if len(mochila) == 0:
        print("No se encontró el sable de luz.")
        return False, objetos_sacados

    
    objeto = mochila.pop(0)
    objetos_sacados += 1

    
    if objeto == "sable de luz":
        print(f"Sable de luz encontrado después de sacar {objetos_sacados} objetos.")
        return True, objetos_sacados
    else:
       
        return usar_la_fuerza(mochila, objetos_sacados)

