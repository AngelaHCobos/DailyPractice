def continousSequence(array):
    i = 0
    result = 0
    result2 = 0
    while i < len(array):
        result += array[i] 
        if result > result2:
            result2 = result            
        elif result < 0:
            result = 0
        i += 1
    return result

LISTNUMBER = [5, -9, 6, -2, 3]

print(continousSequence(LISTNUMBER))