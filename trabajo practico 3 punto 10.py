

"""10. Dada una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone,
de las cual se cuenta con la hora de la notificación, la aplicación que la emitió y el mensaje,
resolver las siguientes actividades:
a. escribir una función que elimine de la cola todas las notificaciones de Facebook;
b. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya
la palabra "Python", si perder datos en la cola;
c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las
11:43 y las 15:57, y determinar cuántas son."""

from queue_ import Queue
from stack import Stack

queue = Queue()

queue.arrive({"hour": "10:30", "app": "Facebook", "message": "Nuevo comentario"})
queue.arrive({"hour": "11:00", "app": "Twitter", "message": "Aprendiendo Java!"})
queue.arrive({"hour": "12:00", "app": "Facebook", "message": "Nuevo like"})
queue.arrive({"hour": "13:00", "app": "Twitter", "message": "Python es increíble"})
queue.arrive({"hour": "14:00", "app": "Instagram", "message": "Nueva foto publicada"})
queue.arrive({"hour": "15:00", "app": "Facebook", "message": "Nuevo mensaje privado"})

#A)
def del_facebook(queue: Queue):
    
    for i in range(queue.size()):
        
        noti = queue.attention()
        if noti["app"] != "Facebook":
           queue.arrive(noti)
           
    return queue

#B)
def twitter(queue):
    aux_queue = Queue()
    word = 'Python'
    
    while queue.size() > 0:
        noti = queue.attention()
        
        if noti["app"] == 'Twitter' and word in noti["message"]:
           print(noti)
        
        aux_queue.arrive(noti)
        
    while aux_queue.size() > 0:
        queue.arrive(aux_queue.attention())

#C)
def hour_messages(queue: Queue):
    stack = Stack()
    cont = 0
    
    while queue.size() > 0:
        noti = queue.attention()
        
        if noti["hour"] >= "11:43" and noti["hour"] <= "15:57":
            stack.push(noti)
            cont += 1
    
    while stack.size() > 0:
        queue.arrive(stack.pop())
    
    return cont

print("a) ")
del_facebook(queue).show()

print("b) ")
twitter(queue)

print(f"c) Notificaciones producidas entre las 11:43 y las 15:57: {hour_messages(queue)}")

