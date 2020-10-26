def maxMoney(n, k):
    total = 0
    pointer = 1
    for t in range(n + 1):
        if total + t != k:
            total = (total + t) % (10 ** 9 + 7)
        else:
            total = ((total + t) - pointer) % (10 ** 9 + 7)
            pointer += 1
    return total

print(maxMoney(3, 3))
        

