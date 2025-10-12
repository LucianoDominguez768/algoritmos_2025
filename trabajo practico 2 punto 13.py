"""13. Dada una pila con los trajes de Iron Man utilizados en las películas de Marvel Cinematic Uni-
verse (MCU) de los cuales se conoce el nombre del modelo, nombre de la película en la que se

usó y el estado en que quedó al final de la película (Dañado, Impecable, Destruido), resolver
las siguientes actividades:
a. determinar si el modelo Mark XLIV (Hulkbuster) fue utilizado en alguna de las películas,
además mostrar el nombre de dichas películas;
b. mostrar los modelos que quedaron dañados, sin perder información de la pila.
c. eliminar los modelos de los trajes destruidos mostrando su nombre;
d. un modelo de traje puede usarse en más de una película y en una película se pueden usar
más de un modelo de traje, estos deben cargarse por separado;
e. agregar el modelo Mark LXXXV a la pila, tener en cuenta que no se pueden cargar modelos
repetidos en una misma película;
f. mostrar los nombre de los trajes utilizados en las películas “Spider-Man: Homecoming” y
“Capitan America: Civil War”."""

from stack import Stack

#definimos traje
def crear_traje(modelo, pelicula, estado):
    return {
        "modelo": modelo,
        "pelicula": pelicula,
        "estado": estado
    }

# cargamos la pila
pila_trajes = Stack()
pila_trajes.push(crear_traje("Mark III", "Iron Man", "Dañado"))
pila_trajes.push(crear_traje("Mark XLIV", "Avengers: Age of Ultron", "Impecable")) 
pila_trajes.push(crear_traje("Mark XLVII", "Spider-Man: Homecoming", "Dañado"))
pila_trajes.push(crear_traje("Mark XLVI", "Capitan America: Civil War", "Destruido"))
pila_trajes.push(crear_traje("Mark L", "Avengers: Infinity War", "Impecable"))

# a) Verificar si el modelo Hulkbuster aparece y mostrar sus películas
def buscar_hulkbuster(pila):
    aux = Stack()
    encontrado = False
    while pila.size() > 0:
        traje = pila.pop()
        if traje["modelo"] == "Mark XLIV":
            print(f"El modelo Hulkbuster fue usado en: {traje['pelicula']}")
            encontrado = True
        aux.push(traje)
    
   # Aca se restaura la pila
    while aux.size() > 0:
        pila.push(aux.pop())
    if not encontrado:
        print("El modelo Hulkbuster no fue encontrado.")

# b) Mostrar los modelos dañados
def mostrar_dañados(pila):
    aux = Stack()
    print("Modelos dañados:")
    while pila.size() > 0:
        traje = pila.pop()
        if traje["estado"] == "Dañado":
            print(traje["modelo"], "-", traje["pelicula"])
        aux.push(traje)
    while aux.size() > 0:
        pila.push(aux.pop())

# c) Eliminar los destruidos
def eliminar_destruidos(pila):
    aux = Stack()
    print("Eliminando modelos destruidos:")
    while pila.size() > 0:
        traje = pila.pop()
        if traje["estado"] == "Destruido":
            print("Eliminado:", traje["modelo"], "-", traje["pelicula"])
        else:
            aux.push(traje)
    while aux.size() > 0:
        pila.push(aux.pop())

# e) que no se repitan
def agregar_mark_lxxxv(pila, modelo, pelicula, estado):
    aux = Stack()
    repetido = False
    while pila.size() > 0:
        traje = pila.pop()
        if traje["modelo"] == modelo and traje["pelicula"] == pelicula:
            print('Este traje ya se encuantra con esas especificaciones')
            repetido = True
            aux.push(traje)
          
        
    while aux.size() > 0:
        pila.push(aux.pop())
    if not repetido:
       
        pila.push(crear_traje(modelo, pelicula, estado))
        print("El traje se agrego a la pila")

# f) Mostrar trajes de dos películas específicas
def mostrar_trajes_peliculas(pila, peliculas):
    aux = Stack()
    print(f"Trajes usados en {peliculas}:")
    while pila.size() > 0:
        traje = pila.pop()
        if traje["pelicula"] in peliculas:
            print(traje["modelo"], "-", traje["pelicula"])
        aux.push(traje)
    while aux.size() > 0:
        pila.push(aux.pop())



# Ejecución
buscar_hulkbuster(pila_trajes)
print()
mostrar_dañados(pila_trajes)
print()
eliminar_destruidos(pila_trajes)
print()
agregar_mark_lxxxv(pila_trajes, "Avengers: Endgame")
print()
mostrar_trajes_peliculas(pila_trajes, ["Spider-Man: Homecoming", "Capitan America: Civil War"])





