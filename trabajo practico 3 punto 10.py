

from queue_ import Queue
from stack import Stack


def eliminar_facebook(c: Queue) -> None:
    aux = Queue()
    while c.size() > 0:
        notif = c.attention()
        if notif["app"] != "Facebook":
            aux.arrive(notif)
  
    while aux.size() > 0:
        c.arrive(aux.attention())


def mostrar_twitter_python(c: Queue) -> None:
    for _ in range(c.size()):
        notif = c.move_to_end()
        if notif["app"] == "Twitter" and "Python" in notif["mensaje"]:
            print(notif)


def contar_intervalo(c: Queue, inicio="11:43", fin="15:57") -> int:
    pila = Stack()
    contador = 0
    for _ in range(c.size()):
        notif = c.move_to_end()
        if inicio <= notif["hora"] <= fin:
            pila.push(notif)
            contador += 1
    return contador


if __name__ == "__main__":
    cola = Queue()
    cola.arrive({"hora": "10:15", "app": "Facebook", "mensaje": "Hola"})
    cola.arrive({"hora": "12:00", "app": "Twitter", "mensaje": "Aprendiendo Python"})
    cola.arrive({"hora": "14:30", "app": "Instagram", "mensaje": "Nueva foto"})
    cola.arrive({"hora": "16:00", "app": "Twitter", "mensaje": "Otro tweet"})
    cola.arrive({"hora": "13:20", "app": "Twitter", "mensaje": "Python es genial!"})

    print("Cola inicial:")
    cola.show()

    print("Eliminar Facebook:")
    eliminar_facebook(cola)
    cola.show()

    print("Notificaciones de Twitter con 'Python':")
    mostrar_twitter_python(cola)

    print("Cantidad de notificaciones entre 11:43 y 15:57:")
    print(contar_intervalo(cola))
