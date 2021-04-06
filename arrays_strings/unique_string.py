print("Program to find if string has all unique characters\n")

# O(n^2)
def all_unique_chars(string):
    l = len(string)
    for i in range(l):
        for j in range(l):
            if i != j and string[i] == string[j]:
                return False
    return True

# Time O(n log(n))
# Time O(n log(n))
def all_unique_chars2(string):
    s = sorted(string)
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return False
    return True

# Time O(n)
# Memory O(1)
def all_unique_chars3(string):
    l = len(string)
    charset = [ False for i in range(127) ]

    for i in range(l):
        idx = ord(string[i]) - ord('a')
        if charset[idx] == True:
            return False
        charset[idx] = True
    
    return True


print(all_unique_chars("abccd"))
print(all_unique_chars2("abccd"))
print(all_unique_chars3("abccd"))