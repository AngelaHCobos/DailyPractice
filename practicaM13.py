def test(lista, valor):
    bajo = 0
    alto = len(lista)
    central = (bajo + alto) // 2
    while bajo  < alto:
        if chequear(lista[:central])
        else:
            bajo = central + 1
        central = (bajo + alto) // 2
    if valor == lista[central]:
        return central
    else:
        return -1

def chequear(lista):
    if 5 in lista:
        return True
    return False