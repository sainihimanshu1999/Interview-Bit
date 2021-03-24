class MinStack:
    def __init__(self):
        self.stack = []
        self.mini = []
    
    # @param x, an integer
    def push(self, x):
        if len(self.mini)==0 or self.mini[-1]>=x:
            self.mini.append(x)
        self.stack.append(x)


    # @return nothing
    def pop(self):
        if len(self.stack)>0:
            temp = self.stack[-1]
            self.stack.pop()
            if len(self.mini)>0 and self.mini[-1]==temp:
                self.mini.pop()


    # @return an integer
    def top(self):
        if len(self.stack)>0:
            return self.stack[-1]
        return -1


    # @return an integer
    def getMin(self):
        if len(self.mini)>0:
            return self.mini[-1]
        return -1

