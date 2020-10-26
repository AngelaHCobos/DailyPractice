"""def binario(lista, valor):
    bajo = 0
    alto = len(lista)
    central = (bajo + alto) // 2
    while bajo  < alto and lista[central] != valor:
        if valor < lista[central]:
            alto = central - 1
        else:
            bajo = central + 1
        central = (bajo + alto) // 2
    if valor == lista[central]:
        return central
    else:
        return -1"""

lista = [5, 8, 10, 1, 3]
#lista = [1, 2, 3, 4]
valor = 10

def modificado(lista, valor):
    alto = 0
    bajo = len(lista)
    central = (bajo + alto) // 2
    while alto > bajo and lista[central] > lista[central-1]:
        if lista[central] < lista[-1]:
            alto = central - 1
        else:
            bajo = central + 1
        central = (bajo + alto) // 2
    lista = lista[central+1:] + lista[:central+1]
    offset = central +1
    print(lista)
    """-----------------------------------------------------"""    
    bajo = 0
    alto = len(lista)
    central = (bajo + alto) // 2
    while bajo  < alto and lista[central] != valor:
        if valor < lista[central]:
            alto = central - 1
        else:
            bajo = central + 1
        central = (bajo + alto) // 2
    if valor == lista[central]:
        return offset - central 
    else:
        return -1

print(modificado(lista, valor))