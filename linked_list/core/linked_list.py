from .node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def from_list(lst):
        ll = LinkedList()

        for x in lst:
            ll.add(x)
        return ll

    def add(self, data):
        currentHead = self.head

        if not currentHead:
            self.head = Node(data)
            return self.head

        while currentHead.next != None:
            currentHead = currentHead.next
        currentHead.next = Node(data)

        return currentHead.next

    def delete(self, data):
        if not self.head:
            return None

        if self.head.data == data:
            d = self.head
            self.head = self.head.next
            return d

        current = self.head
        while current.next and current.next.data != data:
            current = current.next

        if not current:
            return None

        delNode = current.next
        current.next = current.next.next
        
        return delNode

    def at_pos(self, pos):
        i = 0

        if not self.head:
            return None

        current = self.head
        while i < pos:
            if current.next:
                current = current.next
            else:
                break
            i += 1
        return current

    def size(self):
        if not self.head:
            return 0

        i = 1

        c = self.head
        while c:
            c = c.next
            i += 1

        return i-1

    def print(self):
        s = ""
        c = self.head

        while c:
            s += str(c.data)
            if c.next:
                s += " -> "
            c = c.next

        print(s)
