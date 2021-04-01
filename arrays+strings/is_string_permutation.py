print("Program to identify whether one string is permutation of another one\n");

def is_permutation(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    if l1 != l2:
        return False
    
    c1, c2 = 0, 0
    
    for i in range(l1):
        c1 += get_ascii(s1[i])
        c2 += get_ascii(s2[i])

    return c1 == c2

def get_ascii(char):
    return ord(char) - ord('a')


print(is_permutation("dog", "ogg"));