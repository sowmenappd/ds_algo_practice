print("Array reversal");

def reverse(array):
    s = 0
    e = len(array) - 1

    while(s < e):
        t = array[s]
        array[s] = array[e]
        array[e] = t

        s += 1
        e -= 1
    return array


print(reverse([1, 2, 3, 4, 5, 6, 7]))