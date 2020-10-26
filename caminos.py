def estimatedValue(paths):
    path_short = min(paths)
    path_long = max(paths)
    aux_sum = 0
    for x in paths:
        if x == path_short:
            aux_sum += 5
        elif x == path_long:
            aux_sum -= 3
        aux_sum += 2 * x
    return aux_sum/len(paths)

PATH = [1, 5, 3]

print(estimatedValue(PATH))