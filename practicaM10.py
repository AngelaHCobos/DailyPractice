n = 2

def nonPalindromicMultiples(n):
    counter = 0
    for x in range(1000, 10000):
        unit = x % 10
        ten = (x % 100) // 10 
        hundred = (x % 1000) // 100
        thousand = x // 1000
        if (unit != thousand or ten != hundred) and (x % n == 0):
            counter += 1
    return counter

print(nonPalindromicMultiples(n))