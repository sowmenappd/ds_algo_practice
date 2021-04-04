from linked_list.core.linked_list import LinkedList

def weave_list(ll):
    slow, fast = ll.head, ll.head
    while fast:
        slow = slow.next
        fast = fast.next.next
    
    middle = slow
    first = ll.head


    new_ll = LinkedList()
    while first and middle:
        new_ll.add(first.data)
        new_ll.add(middle.data)

        first = first.next
        middle = middle.next

    return new_ll