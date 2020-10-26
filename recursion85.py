def multiplicity(a, b):
    if a == 1:
        return b  
    return multiplicity(a -1, b) + a 