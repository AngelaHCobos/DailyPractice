class SetOfStack:
    def __init__(self, n):
        self.max = n
        self.stacks = [[]]
        
    def push(self, e):
        if len(self.stacks[-1]) < self.max:
            self.stacks[-1].append(e)
        else:
            self.stacks.append([e])
    
    def pop(self):
        number = self.stacks[-1].pop()
        if len(self.stacks[-1]) == 0 and len(self.stacks) > 1:
            self.stacks.pop()
        return number
    
    def getList(self, i):
        if len(self.stacks) > i:
            return self.stacks[i]
        return []

    def pushMany(self, l):
        for x in l:
            self.push(x)

    def emptyLast(self):
        self.stacks.pop()
        if not len(self.stacks) > 0:         
            self.stacks.append([])

MYSTACK = SetOfStack(3)

MYSTACK.push(4)
MYSTACK.emptyLast()
# [[]]
print(MYSTACK.getList(0)) # []
