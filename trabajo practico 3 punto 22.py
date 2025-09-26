

def personaje_capitana_marvel(c: Queue) -> str:
    for _ in range(c.size()):
        dato = c.move_to_end()
        if dato["superheroe"] == "Capitana Marvel":
            return dato["personaje"]
    return "No encontrado"


def superheroes_femeninos(c: Queue) -> None:
    for _ in range(c.size()):
        dato = c.move_to_end()
        if dato["genero"] == "F":
            print(dato["superheroe"])


def personajes_masculinos(c: Queue) -> None:
    for _ in range(c.size()):
        dato = c.move_to_end()
        if dato["genero"] == "M":
            print(dato["personaje"])


def superheroe_scott_lang(c: Queue) -> str:
    for _ in range(c.size()):
        dato = c.move_to_end()
        if dato["personaje"] == "Scott Lang":
            return dato["superheroe"]
    return "No encontrado"


def comienzan_con_s(c: Queue) -> None:
    for _ in range(c.size()):
        dato = c.move_to_end()
        if dato["personaje"].startswith("S") or dato["superheroe"].startswith("S"):
            print(dato)


def carol_danvers(c: Queue) -> str:
    for _ in range(c.size()):
        dato = c.move_to_end()
        if dato["personaje"] == "Carol Danvers":
            return f"Está en la cola, su superhéroe es {dato['superheroe']}"
    return "Carol Danvers no se encuentra en la cola"



if __name__ == "__main__":
    cola = Queue()
    cola.arrive({"personaje": "Tony Stark", "superheroe": "Iron Man", "genero": "M"})
    cola.arrive({"personaje": "Steve Rogers", "superheroe": "Capitán América", "genero": "M"})
    cola.arrive({"personaje": "Natasha Romanoff", "superheroe": "Black Widow", "genero": "F"})
    cola.arrive({"personaje": "Carol Danvers", "superheroe": "Capitana Marvel", "genero": "F"})
    cola.arrive({"personaje": "Scott Lang", "superheroe": "Ant-Man", "genero": "M"})
    cola.arrive({"personaje": "Sam Wilson", "superheroe": "Falcon", "genero": "M"})

    print("a)", personaje_capitana_marvel(cola))
    print("b) Superhéroes femeninos:")
    superheroes_femeninos(cola)

    print("c) Personajes masculinos:")
    personajes_masculinos(cola)

    print("d)", superheroe_scott_lang(cola))

    print("e) Comienzan con S:")
    comienzan_con_s(cola)

    print("f)", carol_danvers(cola))
