#punto 1
def buscar_capitan(lista, index=0):
    if index >= len(lista):
        return False
    if lista[index] == "Capitan America":
        return True
    return buscar_capitan(lista, index + 1)


def listar_superheroes(lista, index=0):
    if index >= len(lista):
        return
    print(lista[index])
    listar_superheroes(lista, index + 1)


if __name__ == "__main__":
    superheroes = [
        "iron man", "thor", "hulk", "viuda negra", "wolverine",
        "hombre haraña", "doctor strange", "pantera negra", "Ant-Man", "avispa",
        "bruja escarlata", "vision", "falcon", "soldado del invierno", "Capitan America"
    ]

    
    encontrado = buscar_capitan(superheroes)
    print(f"\n¿Capitan America está en la lista?: {'Sí' if encontrado else 'No'}")

   
    print("\nLista de superhéroes:")
    listar_superheroes(superheroes)



