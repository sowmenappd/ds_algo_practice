def get_intersection_node(list1, list2):
    node_set = set()

    c = list1.head
    while c:
        node_set.add(c)
        c = c.next
    
    c = list2.head
    while c:
        if c in node_set:
            return c
        c = c.next

    return None