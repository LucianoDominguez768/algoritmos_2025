

def crear_personaje(nombre, cant_peliculas):
    return {
        "nombre": nombre,
        "peliculas": cant_peliculas
    }


pila_personajes = Stack()
pila_personajes.push(crear_personaje("Iron Man", 10))
pila_personajes.push(crear_personaje("Captain America", 9))
pila_personajes.push(crear_personaje("Thor", 9))
pila_personajes.push(crear_personaje("Black Widow", 8))
pila_personajes.push(crear_personaje("Hawkeye", 5))
pila_personajes.push(crear_personaje("Rocket Raccoon", 4))
pila_personajes.push(crear_personaje("Groot", 4))
pila_personajes.push(crear_personaje("Doctor Strange", 5))
pila_personajes.push(crear_personaje("Captain Marvel", 2))
pila_personajes.push(crear_personaje("Gamora", 4))


def buscar_posiciones(pila, nombres):
    aux = Stack()
    posiciones = {}
    pos = 1
    while pila.size() > 0:
        personaje = pila.pop()
        if personaje["nombre"] in nombres:
            posiciones[personaje["nombre"]] = pos
        aux.push(personaje)
        pos += 1
   
    while aux.size() > 0:
        pila.push(aux.pop())
    return posiciones


def mas_de_cinco(pila):
    aux = Stack()
    print("Personajes con más de 5 películas:")
    while pila.size() > 0:
        personaje = pila.pop()
        if personaje["peliculas"] > 5:
            print(f"{personaje['nombre']} - {personaje['peliculas']} películas")
        aux.push(personaje)
    while aux.size() > 0:
        pila.push(aux.pop())


def peliculas_black_widow(pila):
    aux = Stack()
    cantidad = None
    while pila.size() > 0:
        personaje = pila.pop()
        if personaje["nombre"] == "Black Widow":
            cantidad = personaje["peliculas"]
        aux.push(personaje)
    while aux.size() > 0:
        pila.push(aux.pop())
    if cantidad is not None:
        print("Black Widow participó en", cantidad, "películas")
    else:
        print("Black Widow no está en la pila.")


def personajes_iniciales(pila, letras):
    aux = Stack()
    print(f"Personajes cuyos nombres empiezan con {', '.join(letras)}:")
    while pila.size() > 0:
        personaje = pila.pop()
        if personaje["nombre"][0] in letras:
            print(personaje["nombre"])
        aux.push(personaje)
    while aux.size() > 0:
        pila.push(aux.pop())



posiciones = buscar_posiciones(pila_personajes, ["Rocket Raccoon", "Groot"])
print("Posiciones de Rocket y Groot:", posiciones)
print()

mas_de_cinco(pila_personajes)
print()

peliculas_black_widow(pila_personajes)
print()

personajes_iniciales(pila_personajes, ["C", "D", "G"])
