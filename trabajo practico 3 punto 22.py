
from collections import namedtuple, deque


Personaje = namedtuple('Personaje', ['nombre_real', 'superheroe', 'genero'])



def personaje_de_capitana_marvel(cola):
    aux = deque()
    resultado = None
    while cola:
        p = cola.popleft()
        if p.superheroe.lower() == 'capitana marvel':
            resultado = p.nombre_real
        aux.append(p)
    while aux:
        cola.append(aux.popleft())
    if resultado:
        print(f"El nombre del personaje de Capitana Marvel es: {resultado}")
    else:
        print("Capitana Marvel no se encuentra en la cola.")

def superheroes_femeninos(cola):
    aux = deque()
    print("Superhéroes femeninos:")
    while cola:
        p = cola.popleft()
        if p.genero.upper() == 'F':
            print(f"- {p.superheroe}")
        aux.append(p)
    while aux:
        cola.append(aux.popleft())

def personajes_masculinos(cola):
    aux = deque()
    print("Personajes masculinos:")
    while cola:
        p = cola.popleft()
        if p.genero.upper() == 'M':
            print(f"- {p.nombre_real}")
        aux.append(p)
    while aux:
        cola.append(aux.popleft())

def superheroe_de_scott_lang(cola):
    aux = deque()
    resultado = None
    while cola:
        p = cola.popleft()
        if p.nombre_real.lower() == 'scott lang':
            resultado = p.superheroe
        aux.append(p)
    while aux:
        cola.append(aux.popleft())
    if resultado:
        print(f"El superhéroe de Scott Lang es: {resultado}")
    else:
        print("Scott Lang no se encuentra en la cola.")

def nombres_con_s(cola):
    aux = deque()
    print("Personajes o superhéroes que comienzan con 'S':")
    while cola:
        p = cola.popleft()
        if p.nombre_real.lower().startswith('s') or p.superheroe.lower().startswith('s'):
            print(f"- {p}")
        aux.append(p)
    while aux:
        cola.append(aux.popleft())

def buscar_carol_danvers(cola):
    aux = deque()
    encontrado = False
    heroe = None
    while cola:
        p = cola.popleft()
        if p.nombre_real.lower() == 'carol danvers':
            encontrado = True
            heroe = p.superheroe
        aux.append(p)
    while aux:
        cola.append(aux.popleft())
    if encontrado:
        print(f"Carol Danvers está en la cola. Su superhéroe es: {heroe}")
    else:
        print("Carol Danvers no se encuentra en la cola.")


cola = deque([
    Personaje("Tony Stark", "Iron Man", "M"),
    Personaje("Steve Rogers", "Capitán América", "M"),
    Personaje("Natasha Romanoff", "Black Widow", "F"),
    Personaje("Carol Danvers", "Capitana Marvel", "F"),
    Personaje("Scott Lang", "Ant-Man", "M"),
    Personaje("Stephen Strange", "Doctor Strange", "M"),
])


def menu():
    while True:
        
        print("1. Mostrar personaje de Capitana Marvel")
        print("2. Mostrar superhéroes femeninos")
        print("3. Mostrar personajes masculinos")
        print("4. Mostrar superhéroe de Scott Lang")
        print("5. Mostrar datos de nombres que comienzan con 'S'")
        print("6. Buscar Carol Danvers y mostrar su superhéroe")
        print("7. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            personaje_de_capitana_marvel(cola)
        elif opcion == '2':
            superheroes_femeninos(cola)
        elif opcion == '3':
            personajes_masculinos(cola)
        elif opcion == '4':
            superheroe_de_scott_lang(cola)
        elif opcion == '5':
            nombres_con_s(cola)
        elif opcion == '6':
            buscar_carol_danvers(cola)
        elif opcion == '7':
            print("Adios")
            break
        else:
            print("Funcion incorrecta, intente otra vez")


menu()