class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def attachNodeToTail(self, data):
        self.next = Node(data)