"""You are given a positive integer N which represents the number of steps in a staircase.
 You can either climb 1 or 2 steps at a time. Write a function that returns the number of unique ways to climb the stairs."""

visited = {}

def staircase(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n in visited:
        return visited[n]
    ways = staircase(n-1) + staircase(n-2)
    visited[n] = ways
    return ways

  
print(staircase(4))
# 5
print(staircase(1000))
# 8