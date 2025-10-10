""" 
    Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se conoce el nombre del personaje, el nombre del superhéroe y su género 
    (Masculino M y FemeninoF), por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Romanoff, Black Widow, F}, etc., 
    desarrollar un algoritmo que resuelva las siguientes actividades:
    a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
    b. mostrar los nombre de los superhéroes femeninos;
    c. mostrar los nombres de los personajes masculinos;
    d. determinar el nombre del superhéroe del personaje Scott Lang;
    e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan con la letra S;
    f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroes.
"""

from queue_ import Queue

queue = Queue()

queue.arrive({"name": "Tony Stark", "superhero": "Iron Man", "gender": "M"})
queue.arrive({"name": "Steve Rogers", "superhero": "Capitán América", "gender": "M"})
queue.arrive({"name": "Natasha Romanoff", "superhero": "Black Widow", "gender": "F"})
queue.arrive({"name": "Carol Danvers", "superhero": "Capitana Marvel", "gender": "F"})
queue.arrive({"name": "Scott Lang", "superhero": "Ant-Man", "gender": "M"})
queue.arrive({"name": "Bruce Banner", "superhero": "Hulk", "gender": "M"})
queue.arrive({"name": "Clint Barton", "superhero": "Hawkeye", "gender": "M"})
queue.arrive({"name": "Wanda Maximoff", "superhero": "Scarlet Witch", "gender": "F"})

#A
def identify_caharacter(queue: Queue, name):
    
    for i in range(queue.size()):
        charater = queue.attention()
        
        if charater["superhero"] == name:
            char = charater["name"]
    
        queue.arrive(charater)
    return char

print('A)Nombre de capitana Marvel:')
print(identify_caharacter(queue, "Capitana Marvel"))

#B
def identify_names_F(queue: Queue):
    for i in range(queue.size()):
        char = queue.attention()
        if char["gender"] == "F":
            print(f'{char["name"]} - {char["superhero"]} ')
               
        queue.arrive(char)
        
print("B)Nombres femeninos: ")
identify_names_F(queue)
            
#C
def identify_names_M(queue: Queue):
    
    for i in range(queue.size()):
        char = queue.attention()
        if char["gender"] == "M":
            print(f'{char["name"]} - {char["superhero"]} ')
               
        queue.arrive(char)

print("C) Nombres Masculinos: ")
identify_names_M(queue)

#D
def serch_scott_lang(queue: Queue):
    for i in range(queue.size()):
        char = queue.attention()
        if char["name"] == "Scott Lang":
            print(f'{char["name"]} es: {char["superhero"]}')
            
        queue.arrive(char)
        
print('D) Buscar a Scott Lang en la cola')
serch_scott_lang(queue)

#E
def superhero_with_s(queue: Queue):
    new_queue = Queue()
    
    for i in range(queue.size()):
        char = queue.attention()
        
        if char["name"][0] == 'S' or char["superhero"][0] == "S":
            new_queue.arrive(char)
            
        queue.arrive(char)
        
    return new_queue

print('E) Nombre o superheroes que comienzan con "S" ')
superhero_with_s(queue).show()

#F
def serch_character(queue: Queue,name):
    for i in range (queue.size()):
        char = queue.attention()
        
        if char["name"] == name:
            print(f'{name} esta en la cola y es {char["superhero"]}')
            
        queue.arrive(char)
        
print('F) Identificar si Carol Danvers esta en la cola')
serch_character(queue,'Carol Danvers')

