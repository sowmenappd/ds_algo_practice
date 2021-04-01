# without a temporary buffer
def remove_duplicates(ll):
    n1 = ll.head
    n2 = n1.next
    prev_n2 = n1

    while n1:
        n2 = n1.next
        while n2:
            if n1.data == n2.data:
                prev_n2.next = n2.next
                prev_n2 = n2.next
            else:
                prev_n2 = n2
            n2 = n2.next
        n1 = n1.next
    return ll

# using a buffer
def remove_duplicates_buffered(ll):
    container = set()

    current = ll.head
    prev = None
    while current:
        if current.data not in container:
            container.add(current.data)
            prev = current
            current = current.next
        else:
            prev.next = current.next
            current = current.next

    return ll