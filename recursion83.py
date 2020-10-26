A = [-4, -3, 1, 2, 3]

def magic(A, k = 0):
    if k >= len(A):
        return "No hay elementos"
    if (A[k]) == k:
        return k   
    return magic(A, k+1)

print(magic(A))