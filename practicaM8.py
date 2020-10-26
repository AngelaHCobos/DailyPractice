L = [3, 7, 2, 8]
K = 10

def pair(L, K):
    result = 0 
    for i, x in enumerate(L[:-2]):
        for y in L[i + 1:]:
            if x + y < K:
               result += 1
    return result

print(pair(L, K)) 
