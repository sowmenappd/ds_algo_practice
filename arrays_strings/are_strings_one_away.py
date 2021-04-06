print("Program to determing whether strings are only different by 1 character\n");

def is_one_edit_away(f, s):
    needEdit = False
    
    for i in range(len(s)):
        if f[i] != s[i]:
            if needEdit == True:
                return False
            needEdit = True
    
    return needEdit

def is_one_insert_away(f, s):
    i1, i2 = 0, 0
    l1, l2 = len(f), len(s)

    while i1 < l1 and i2 < l2:
        if f[i1] != s[i2]:
            if i1 != i2:
                return False
            i2 += 1
        else:
            i1 += 1
            i2 += 1
    return True

def is_one_away(s1, s2):
    if len(s1) == len(s2):
        return is_one_edit_away(s1, s2)
    elif len(s1) - len(s2) == 1:
        return is_one_insert_away(s2, s1)
    elif len(s2) - len(s1) == 1:
        return is_one_insert_away(s1, s2)
    
    return False

print(is_one_away("palse", "pale"));