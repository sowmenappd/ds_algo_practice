# O(n) time and space
def has_loop(ll):
    visited = set()

    curr = ll.head
    while curr:
        if curr in visited:
            return True
        visited.add(curr)
        curr = curr.next
    return False


# O(n) time, O(1) space
def has_loop_optimized(ll):
    slow, fast = ll.head, ll.head

    while True:
        slow = slow.next
        fast = fast.next.next

        if not fast or not fast.next:
            return None

        if slow and slow == fast:
            slow = ll.head
            break
    
    if not fast or not fast.next:
        return None


    while True:
        slow = slow.next
        fast = fast.next

        if slow == fast:
            return slow
    