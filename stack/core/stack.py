class Stack:
    def __init__(self):
        self.index = -1
        self.stack = []
    
    def push(self, val):
        self.index += 1
        self.stack.append(val)

    def pop(self):
        if index < 0:
            raise IndexError()
        self.stack.pop()
        self.index -= 1
    
    def peek(self):
        if self.index > -1:
            return self.stack[self.index]
        else:
            return None