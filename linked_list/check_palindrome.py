from .reverse_list import reverse_list

def is_palindrome(ll):
    rev_ll = reverse_list(ll, True)
    return is_equal(ll.head, rev_ll.head) 

def is_equal(ll, rll):
    if not ll and not rll:
        return True
    if not ll:
        return False
    if not rll:
        return False
    
    return is_equal(ll.next, rll.next) and ll.data == rll.data

