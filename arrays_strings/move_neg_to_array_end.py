print("Program to move all negative elements of an array to the end of the array");

def move_neg(array):
    t_arr = [ x for x in array if x >= 0 ]

    for x in array:
        if x < 0:
            t_arr.append(x)
    
    for i in range(len(t_arr)):
        array[i] = t_arr[i]
    
    return array

print(move_neg([-5, 7, -3, -4, 9, 10, -1, 11]))