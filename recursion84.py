set1 = [1, 2, 3]

def subset(set1):
    if len(set1) == 0:
        return  "No hay elementos"
    return subset(set1.pop())

print(subset(set1))
    