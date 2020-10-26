from collections import defaultdict

def distancia(array):
    resultados = defaultdict(int)
    for i, x in enumerate(array):
        resultados[array[i+1] - x] += 1 
        if resultados[array[i+1] - x] > 2:
            return array[i+1] - x

def binario(lista):
    dist = distancia(lista)
    bajo = 0
    alto = len(lista)
    central = (bajo + alto) // 2
    while bajo  < alto:
        if lista[0] + central * dist < lista[central]:
            alto = central - 1
        else:
            bajo = central + 1
        if dist + lista[central - 1] != lista[central]:
            return lista[central] - dist
        if lista[central + 1] != lista[central] + dist:
            return lista[central] + dist
        central = (bajo + alto) // 2

LISTA = [4, 6, 10, 12, 14, 16, 18]

print(binario(LISTA))