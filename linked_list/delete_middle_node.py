def delete_middle_node(node):
    if not node or not node.next:
        return False

    next = node.next

    node.data = next.data
    node.next = next.next
    return True