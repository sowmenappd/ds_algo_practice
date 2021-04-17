class SetOfStacks:
    def __init__(this, set_count=3):
        this.stacks = [[] for i in range(set_count)]
        this.threshold = 5
        this.stack_idx = -1

    def push(this, item):
        if this.empty() or len(this.stacks[this.stack_idx]) == this.threshold:
            this.stack_idx += 1
        if this.stack_idx < len(this.stacks):
            this.stacks[this.stack_idx].append(item)
        else:
            raise IndexError("Stack index out of range")

    def pop(this):
        if not this.empty():
            this.stacks[this.stack_idx].pop()
            
            if len(this.stacks[this.stack_idx]) == 0:
                this.stack_idx -= 1
        else:
            raise Exception("Stack is empty")
    
    def peek(this):
        return this.stacks[this.stacks][-1]

    def empty(this):
        return this.stack_idx < 0

    def pop_at(self, idx):
        pass

    def print(this):
        s = []
        for stack in this.stacks:
            for x in stack:
                s.append(x)

        print(s)