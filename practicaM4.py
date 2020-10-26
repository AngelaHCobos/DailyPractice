def fibonacci(number1, number2, position):
    """for x in range(position - 1):
        aux = number1
        number1 = number2
        number2 = aux + number2"""
    if position == 0:
        return number1
    if position == 1:
        return number2
    result = fibonacci(number1, number2, position - 1) + fibonacci(number1, number2, position - 2)
    return(result)

def jaimeRoos(number1, number2, number3, position):
    if position == 0:
        return number1
    if position == 1:
        return number2
    if position == 2:
        return number3
    result = jaimeRoos(number1, number2, number3, position - 1) + jaimeRoos(number1, number2, number3, position - 2) + jaimeRoos(number1, number2, number3, position - 3)
    return result

print(fibonacci(0, 1, 5))
print(jaimeRoos(1, 1, 1, 6))

