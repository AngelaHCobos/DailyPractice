lista = [2, 1, 4, 3, 15, 20, 27, 31]
valor = 3

def binario(lista, valor):
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
        return -1

def binario_modificado(lista, valor):
    bajo = 0
    alto = len(lista)
    central = (bajo + alto) // 2
    while bajo < alto and lista[central] != valor and lista[central + 1] != valor and lista[central - 1] != valor:
        if valor < lista[central]:
            alto = central - 1
        else:
            bajo = central + 1
        central = (bajo + alto) // 2
    if valor == lista[central]:
        return central
    if valor == lista[central + 1]:
        return central + 1
    if valor == lista[central -1]:
        return central - 1 
    else:
        return -1

print(binario_modificado(lista, valor))