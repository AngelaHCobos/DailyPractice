def isPossible(x_start, y_start, x_end, y_end):
    if x_start == x_end and y_start == y_end:
        return "YES"
    if x_start > x_end or y_start > y_end:
        return "NO"
    result = isPossible(x_start + y_start, y_start, x_end, y_end) == "YES" or isPossible(x_start, y_start + x_start, x_end, y_end) == "YES"
    if result:
        return "YES"
    else:
        return "NO"

print(isPossible(1, 1, 2, 5))
print(isPossible(1, 1, 6, 3))