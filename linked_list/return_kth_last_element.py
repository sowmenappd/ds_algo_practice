def kth_from_last(ll, k, onFound):
    __helper__(ll.head, k, onFound)


def __helper__(node, k, onFound):
    if not node:
        return -1

    idx = __helper__(node.next, k, onFound) + 1
    if idx == k:
        onFound(node)
    
    return idx