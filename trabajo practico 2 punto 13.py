
from stack import Stack


def crear_traje(modelo, pelicula, estado):
    return {
        "modelo": modelo,
        "pelicula": pelicula,
        "estado": estado
    }


pila_trajes = Stack()
pila_trajes.push(crear_traje("Mark III", "Iron Man", "Dañado"))
pila_trajes.push(crear_traje("Mark XLIV", "Avengers: Age of Ultron", "Impecable"))  # Hulkbuster
pila_trajes.push(crear_traje("Mark XLVII", "Spider-Man: Homecoming", "Dañado"))
pila_trajes.push(crear_traje("Mark XLVI", "Capitan America: Civil War", "Destruido"))
pila_trajes.push(crear_traje("Mark L", "Avengers: Infinity War", "Impecable"))


def buscar_hulkbuster(pila):
    aux = Stack()
    encontrado = False
    while pila.size() > 0:
        traje = pila.pop()
        if traje["modelo"] == "Mark XLIV":
            print(f"El modelo Hulkbuster fue usado en: {traje['pelicula']}")
            encontrado = True
        aux.push(traje)
    
  
    while aux.size() > 0:
        pila.push(aux.pop())
    if not encontrado:
        print("El modelo Hulkbuster no fue encontrado.")


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


def agregar_mark_lxxxv(pila, pelicula):
    aux = Stack()
    repetido = False
    while pila.size() > 0:
        traje = pila.pop()
        if traje["modelo"] == "Mark LXXXV" and traje["pelicula"] == pelicula:
            repetido = True
        aux.push(traje)
    while aux.size() > 0:
        pila.push(aux.pop())
    if not repetido:
        pila.push(crear_traje("Mark LXXXV", pelicula, "Impecable"))
        print("Mark LXXXV agregado en", pelicula)
    else:
        print("Mark LXXXV ya estaba en esa película.")


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




buscar_hulkbuster(pila_trajes)
print()
mostrar_dañados(pila_trajes)
print()
eliminar_destruidos(pila_trajes)
print()
agregar_mark_lxxxv(pila_trajes, "Avengers: Endgame")
print()
mostrar_trajes_peliculas(pila_trajes, ["Spider-Man: Homecoming", "Capitan America: Civil War"])
