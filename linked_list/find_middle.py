#works if
def find_middle(list):
    slow, fast = list.head, list.head

    while fast:
        slow = slow.next
        fast = fast.next.next
    
    return slow