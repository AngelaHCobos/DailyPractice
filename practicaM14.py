def find(number):
    porciento = 0
    goles = 0
    tiros = 0
    while porciento != number:
        if porciento < number:
            goles += 1
        tiros += 1
        porciento = goles / tiros
    return tiros