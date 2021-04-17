import math

class Stack:
    def __init__(self):
        self.index = -1
        self.stack = []
        self.minItems = []
    
    def push(self, val):
        self.index += 1
        self.stack.append(val)
        if len(self.minItems) > 0:
            if val < self.minItems[-1]:
                self.minItems.append(val)
        else:
            self.minItems.append(val)
    def pop(self):
        if self.empty():
            raise IndexError()

        if len(self.minItems) > 0:
            if self.minItems[-1] == self.stack[-1]:
                self.minItems.pop()
        
        self.stack.pop()
        self.index -= 1
    
    def empty(self):
        return self.index < 0

    def peek(self):
        if self.index > -1:
            return self.stack[self.index]
        else:
            return None

    def min(self):
        if len(self.minItems) > 0:
            return self.minItems[-1]
        else:
            return None

    def print(self):
        print(self.stack)