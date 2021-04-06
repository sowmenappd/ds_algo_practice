print("Program to find whether a string is a permutation of a palindrome\n");

def is_palindrome_permutation(string):
    lookup = {}

    for x in string.lower():
        if x != ' ':
            if x in lookup:
                lookup[x] += 1
            else:
                lookup[x] = 1

    count1s = 0

    for x in lookup:
        if lookup[x] % 2 != 0:
            count1s += 1

    return count1s < 2

print(is_palindrome_permutation("20 203"))