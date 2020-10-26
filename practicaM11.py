#n = [1, 2, 3, 3]
#n = [1, 2, 3, 1, 2, 3, 4, 2, 3]
n = [0, 0, 1, 1, 2]

def mostFrequent(n):
    repeat = dict()
    maxi_repe = 0
    maxi_repe_value = 100000
    for x in n:
        if x in repeat.keys():
            repeat[x] += 1
        else:
            repeat[x] = 1
        if repeat[x] == maxi_repe and x < maxi_repe_value:
            maxi_repe_value = x
        if repeat[x] > maxi_repe:
            maxi_repe = repeat[x]
            maxi_repe_value = x
    return maxi_repe_value
    
print(mostFrequent(n))