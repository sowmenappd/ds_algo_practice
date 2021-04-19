

class BinarySearchTree:
    
    def __init__(this):
        this.root = None

    

    def insert(this, value):
        node = Node(value)
        if not this.root:
            this.root = node
            return
        
        current = this.root
        while current:
            if node.value < current.value:
                if current.left:
                    current = current.left
                else:
                    current.left = node
                    node.parent = current
                    return
            else:
                if current.right:
                    current = current.right
                else:
                    current.right = node
                    node.parent = current
                    return

    # performs an inorder traversal
    def print(this): 
        current = this.root
        this.__traverse__(current)


    def __traverse__(this, target):
        if not target:
            return

        this.__traverse__(target.left)
        print(target.value)
        this.__traverse__(target.right)



class Node:
    def __init__(this, value):
        this.value = value
        this.left = None
        this.right = None
        this.parent = None
            