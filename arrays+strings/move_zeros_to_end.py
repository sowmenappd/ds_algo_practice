print("Program to move zeros to end of array");

def move_zeros(array):
    zero_count = sum([ x == 0 for x in array ])
    
    l = len(array)
    wall = 0

    for i in range(0, l):
        if array[i] != 0:
            array[i-wall] = array[i]
        else:
            wall += 1
    
    for i in range(-zero_count, 0):
        array[i] = 0

    return array


def move_zeros2(array):
    l = len(array)
    count = 0

    for i in range(l):
        if array[i] != 0:
            array[count] = array[i]
            count += 1

    for i in range(count, l):
        array[i] = 0
    
    return array

print(move_zeros2([1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0]))