print("Program to rearrange positive and negative elements of an array with constant space allowed");

def rearrange(array):
    for i in range(len(array)):
        j = i
        while j < len(array) and array[j] > 0:
            j += 1
        
        if j >= len(array):
            continue

        neg_num = array[j]
        
        k = j
        while k > i:
            array[k] = array[k-1]
            k -= 1
        array[k] = neg_num
    return array

print(rearrange([ -12, 11, -13, -5,
        6, -7, 5, -3, -6 ]))