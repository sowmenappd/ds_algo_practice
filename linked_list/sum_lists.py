from linked_list.core.linked_list import LinkedList, Node

def sum_lists(list1, list2):
    sum = (__helper__(list1.head, 0) + __helper__(list2.head, 0))
    print("sum", sum)
    nll = LinkedList()
    nll.head = Node(0)
    __store__(sum, nll.head)
    return nll


def __helper__(ll, k):
    if not ll:
        return 0
    return ll.data * 10 ** k + __helper__(ll.next, k+1)

def __store__(value, node):
    if value == 0:
        return

    node.data = value % 10
    if value // 10 > 0:
        node.next = Node(-1)
        __store__(value // 10, node.next)