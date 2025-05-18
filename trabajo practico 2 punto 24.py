
class PersonajeMCU:
    def __init__(self, nombre, cantidad_peliculas):
        self.nombre = nombre
        self.cantidad_peliculas = cantidad_peliculas

    def __str__(self):
        return f"{self.nombre} - {self.cantidad_peliculas} películas"


pila = []


pila.append(PersonajeMCU("Iron Man", 10))
pila.append(PersonajeMCU("Captain America", 9))
pila.append(PersonajeMCU("Thor", 9))
pila.append(PersonajeMCU("Black Widow", 8))
pila.append(PersonajeMCU("Hawkeye", 6))
pila.append(PersonajeMCU("Hulk", 7))
pila.append(PersonajeMCU("Rocket Raccoon", 4))
pila.append(PersonajeMCU("Groot", 5))
pila.append(PersonajeMCU("Doctor Strange", 4))
pila.append(PersonajeMCU("Gamora", 5))
pila.append(PersonajeMCU("Star-Lord", 4))
pila.append(PersonajeMCU("Spider-Man", 3))
pila.append(PersonajeMCU("Captain Marvel", 3))


print("a. Posición desde la cima:")
posicion = 1
for personaje in reversed(pila):  # cima está al final, por eso se recorre al revés
    if personaje.nombre == "Rocket Raccoon":
        print(f"- Rocket Raccoon está en la posición {posicion}")
    if personaje.nombre == "Groot":
        print(f"- Groot está en la posición {posicion}")
    posicion += 1


print("\nb. Personajes que participaron en más de 5 películas:")
for personaje in reversed(pila):
    if personaje.cantidad_peliculas > 5:
        print(f"- {personaje.nombre}: {personaje.cantidad_peliculas} películas")


print("\nc. Cantidad de películas de Black Widow:")
encontrado = False
for personaje in reversed(pila):
    if personaje.nombre == "Black Widow":
        print(f"- Black Widow participó en {personaje.cantidad_peliculas} películas")
        encontrado = True
        break
if not encontrado:
    print("- Black Widow no se encuentra en la pila")


print("\nd. Personajes cuyos nombres empiezan con C, D o G:")
for personaje in reversed(pila):
    if personaje.nombre.startswith(("C", "D", "G")):
        print(f"- {personaje.nombre}")