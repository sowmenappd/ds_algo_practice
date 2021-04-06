from linked_list.core.linked_list import LinkedList, Node

def __reverse_inplace__(ll):
    prev = None
    current = ll.head
    next = None

    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next

    ll.head = prev # current is null at this point
    return ll

def __clone_and_reverse__(ll):
    ll2 = LinkedList()
    
    current = ll.head
    while current:
        n = Node(current.data)
        ll2.addNode(n)
        current = current.next

    return __reverse_inplace__(ll2)

def reverse_list(ll, clone=False):
    if not clone:
        return __reverse_inplace__(ll)
    else:
        return __clone_and_reverse__(ll)
