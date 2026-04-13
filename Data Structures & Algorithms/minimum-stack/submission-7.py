import math
class MinStack:


    def __init__(self):
        self.stack = []
        self.minimum = math.inf
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.minimum:
            self.minimum = val
            self.min_stack.append(val)
        else:
            if self.min_stack:
                self.min_stack.append(self.min_stack[-1]) # Old top of min stack is still smallest after the latest addition to stack
            else:
                self.min_stack.append(val)
            
    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        if self.min_stack:  
            self.minimum = self.min_stack[-1]
        else:
            self.minimum = math.inf

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.min_stack[-1]
        
