class MinStack:
    # since stack LIFO, we can maintain a prefix min stack to record the min at each stage
    def __init__(self):
        self.stack = []
        self.prefix_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not len(self.prefix_stack):
            self.prefix_stack.append(val)
        else:
            self.prefix_stack.append(min(self.prefix_stack[-1], val))

    def pop(self) -> None:
        self.stack.pop()
        self.prefix_stack.pop()


    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.prefix_stack[-1]
        
