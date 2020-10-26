class Solution():
    def fibonacci(self, n):
        a = 0
        b = 1
        for _ in range(n - 1):
            aux = a
            a = b
            b = b + aux
        return b 

n = 9
print(Solution().fibonacci(n))
# 34