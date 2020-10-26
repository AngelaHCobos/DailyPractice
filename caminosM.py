def proba(paths):
    total = 0
    minimo = min(paths)
    for x in paths:
        if x == minimo:
            total += (x * 2) + 12
        else:
            total += (x * 2) - 3      
    return total / len(paths)

PATHS = [1, 5, 2, 1]
print(proba(PATHS))