from linked_list.core.linked_list import LinkedList

# in this approach two lists are created
# using an additional space of O(n)
# O(n) - time
# O(n) - space
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
# O(1) - space

def partition_linked_list_by_value_optimized_unordered(ll, val):
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