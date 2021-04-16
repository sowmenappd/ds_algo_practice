from linked_list.core.linked_list import LinkedList

# in this approach two lists are created
# using an additional memory of O(n)
# O(n) - time
# O(n) - memory
def partition_linked_list_by_value(ll, val):
    before = LinkedList()
    after = LinkedList()

    current = ll.head
    while current:
        next = current.next
        if current.data < val:
            before.add(current.data)
        else:
            after.add(current.data)
        current = next

    c = before.head
    while c.next:
        c = c.next

    c.next = after.head

    return before

 

# in this approach the order of 
# nodes are not maintained
# we add nodes to the front if less 
# and at the end if equal or more
# O(n) - time
# O(1) - memory

def partition_linked_list_by_value_optimized_unstable(ll, val):
    head = ll.head
    tail = ll.head

    current = ll.head

    while current:
        next = current.next 
        if current.data < val:
            current.next = head
            head = current
        else:
            tail.next = current
            tail = current

        current = next
    tail.next = None
    
    ll.head = head

    return ll


# in this approach we use 4 variables 
# to keep track of the nodes added 
# before or after, the list is stably 
# organised
# O(n) - time
# O(1) - memory

def partition_linked_list_by_value_optimized_stable(ll, val):
    beforeHead = None
    beforeTail = beforeHead
    
    afterHead = None
    afterTail = afterHead

    current = ll.head

    while current:
        next = current.next

        if current.data < val:
            if not beforeHead:
                beforeHead, beforeTail = current, current
            else:
                beforeTail.next = current
                beforeTail = current
        else:
            if not afterHead:
                afterHead, afterTail = current, current
            else:
                afterTail.next = current
                afterTail = current
        current = next

    afterTail.next = None
    
    beforeTail.next = afterHead

    ll.head = beforeHead
    return ll