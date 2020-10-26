def getAnimals(weights, capacity):
    set_weights = set()
    maxi = -1
    for x in weights:
        if capacity - x in set_weights:
            pair = max(x, capacity - x)
            if pair > maxi:
                maxi = pair
        set_weights.add(x)
    if maxi == -1:
        return []
    else:
        return [maxi, capacity - maxi]
            
print(getAnimals([1, 5, 2, 7, 9, 3], 10))
print(getAnimals([1, 5, 2, 7, 9, 3], 2))