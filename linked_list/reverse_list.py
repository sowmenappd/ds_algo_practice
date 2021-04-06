def reverse_list(ll):
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
