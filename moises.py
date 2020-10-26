def moises(ways):
    even_list = []
    odd_list = []
    for x in ways:
        if x % 2 == 0:
            even_list.append(x)
        else:
            odd_list.append(x)
    return bubble(even_list) + bubble(odd_list)

def bubble(number_list):
    aux = 0
    i = 0
    j = 0
    leng = len(number_list)
    while i < leng:
        j = 0
        while j < leng-1:
            if number_list[j] > number_list[j+1]:
                aux = number_list[j]
                number_list[j] = number_list[j+1]
                number_list[j+1] = aux
            else:
                j += 1
        i += 1
    return number_list

WAYS = [1, 9, 7, 5, 4, 6, 10, 11]

print(moises(WAYS))
