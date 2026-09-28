class MinStack:

    def __init__(self):
        self.prefix = []
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.prefix:
            self.prefix.append(val)
        else:
            new_min = min(val,self.prefix[-1])
            self.prefix.append(new_min)
        

    def pop(self) -> None:
        self.stack.pop()
        self.prefix.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.prefix[-1]
        
