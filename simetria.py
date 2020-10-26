def simetria(array):
    result = []
    i = 0
    while i < len(array)-1:
        resta = array[i + 1] -array[i]
        result.append(resta)
        i +=2
    return sum(result)

def memo(array):
    distancia_maxima = 0
    elemento = 0
    for i, x in enumerate(array):
        if i == 0:
            distancia_anterior = 10000
            distancia_siguiente = array[i+1] - x
        elif i == len(array)-1:
            distancia_siguiente = 10000
            distancia_anterior = x - array[i-1] 
        else: 
            distancia_siguiente = array[i+1] - x
            distancia_anterior = x - array[i-1] 
        distancia_menor = min(distancia_anterior, distancia_siguiente)
        if distancia_menor > distancia_maxima:
            distancia_maxima = distancia_menor
            elemento = i
    array.pop(elemento)
    return array

def solve(array):
    if len(array) % 2 == 1:
        array = memo(array)
    return simetria(array)

LISTA = [1, 2, 9, 15, 16]

print(solve(LISTA))



        


