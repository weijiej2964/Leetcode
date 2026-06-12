class MinStack:

    def __init__(self):
        self.stack = deque()
        self.minrecord = deque()

    def push(self, value: int) -> None:
        self.stack.append(value)
        if len(self.minrecord) == 0 or value < self.minrecord[-1]:
            self.minrecord.append(value)
        else:
            self.minrecord.append(self.minrecord[-1])
        

    def pop(self) -> None:
        self.stack.pop()
        self.minrecord.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minrecord[-1]
    
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()