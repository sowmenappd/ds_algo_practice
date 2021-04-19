

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

    def depth(this):
        return this.__height__(this.root)

    def tree(this):
        return this.__traverse2__(this.root, 0, {})

    def __traverse__(this, target):
        if not target:
            return

        this.__traverse__(target.left)
        print(target.value)
        this.__traverse__(target.right)

    def __traverse2__(this, target, level, levels):
        if level not in levels:
            levels[level] = []
        if target:
            levels[level].append(target.value)
            this.__traverse2__(target.left, level + 1, levels)
            this.__traverse2__(target.right, level + 1, levels)
        else:
            levels[level].append(None)

        return levels
    
    def __height__(this, node):
        if not node:
            return -1

        lHeight = this.__height__(node.left) + 1
        rHeight = this.__height__(node.right) + 1
        return max(lHeight, rHeight)


class Node:
    def __init__(this, value):
        this.value = value
        this.left = None
        this.right = None
        this.parent = None
            