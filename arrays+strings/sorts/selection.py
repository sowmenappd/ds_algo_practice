print("Selection sort\n");

# ascending
def sort(array):
    l = len(array)
    for i in range(l-1):
        minIdx = i

        j = i + 1
        while j < l:
            if array[minIdx] > array[j]:
                minIdx = j
            j += 1
        
        if minIdx != i:
            array[minIdx], array[i] = array[i], array[minIdx]
    
    return array

print(sort([4, 3, 2, 1, 5, 4, 7, 69, 12, 34, 65, 76]))