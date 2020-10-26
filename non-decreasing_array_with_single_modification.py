"""
You are given an array of integers in an arbitrary order. 
Return whether or not it is possible to make the array non-decreasing by modifying at most 1 element to any value.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example:

[13, 4, 7] should return true, since we can modify 13 to any value 4 or less, to make it non-decreasing.

[13, 4, 1] however, should return false, since there is no way to modify just one element to make the array non-decreasing.
"""

def check(lst):
    counter = 0
    for i,x in enumerate(lst):
        if i < len(lst) - 1:
            if x > lst[i+1]:
                counter += 1
                if counter > 1:
                    return False
                if i == 0:
                    lst[i] = lst[i+1]
                else:
                    lst[i] = lst[i-1]
    return True
            


print(check([1,2,3,14,13,6]))
# True
print(check([5,1,3,2,5]))
# False