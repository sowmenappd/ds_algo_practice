print("Program to rearrange positive and negative numbers in an array\n");


# This algorithm doesn't maintain the relative order
def rearrange(array):
    l = len(array)

    idx = 0
    for i in range(l):
        if array[i] < 0:
            array[idx], array[i] = array[i], array[idx]
            idx += 1

    p = idx
    n = 0

    while p > 0 and n < l:
        array[p], array[n] = array[n], array[p]
        p += 1
        n += 2

    return array

print(rearrange([-1, 2, -3, 4, 5, 6, -7, 8, 9, -1]))