"""
Implement a class for a stack that supports all the regular functions (push, pop) and an additional function of max() 
which returns the maximum element in the stack (return None if the stack is empty). Each method should run in constant time.
"""


class MaxStack:
    
    def __init__(self):
        self.maximo = -1  
        self.stack = []
        self.history = []

    def push(self, val):
        self.stack.append(val)
        if val > self.maximo:
            self.history.append(self.maximo)
            self.maximo = val

    def pop(self):
        pop = self.stack.pop()
        if pop == self.maximo:
            self.maximo = self.history.pop()

    def max(self):
        return self.maximo
       
s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print(s.max())
# 3
s.pop()
s.pop()
print(s.max())
# 2