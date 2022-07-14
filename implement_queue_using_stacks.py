class MyQueue:
    
    
    def __init__(self):
        self.in_stack = deque()
        self.out_stack = deque()
        

    def push(self, x: int) -> None:
        while len(self.out_stack):
            self.in_stack.append(self.out_stack.pop())
        self.in_stack.append(x)

    def pop(self) -> int:
        while len(self.in_stack):
            self.out_stack.append(self.in_stack.pop())
        if len(self.out_stack):
            return self.out_stack.pop()

    def peek(self) -> int:
        if len(self.out_stack):
            # no in-built peek operation but this accomplishes same thing
            return self.out_stack[-1]
        while len(self.in_stack):
            self.out_stack.append(self.in_stack.pop())
        if len(self.out_stack):
            return self.out_stack[-1]
        

    def empty(self) -> bool:
        return not (len(self.in_stack) or len(self.out_stack))
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
