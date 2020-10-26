def up(stair, steps):
    result = 0
    for x in (steps):
        if x == stair:
            result += 1
        if x < stair:
            result += up(stair - x, steps)
    return result
     
