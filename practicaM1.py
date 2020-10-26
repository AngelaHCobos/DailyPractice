def kinderSquare(numbers):
    result = []
    for x in numbers:
        calculation = x ** 2 + 10
        if not ((calculation % 10) == 5 or (calculation % 10) == 6):
            result.append(calculation)
    return result

a = [3, 1, 4,]
print(kinderSquare(a))