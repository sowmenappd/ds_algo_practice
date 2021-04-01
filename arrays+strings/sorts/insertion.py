print("Insertion sort\n");

# ascending
def sort(array):
    l = len(array)

    for i in range(l-1):
        j = i + 1

        while j > 0 and array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
            j -= 1

    return array

print(sort([4, 3, 2, 1, 5, 4, 7, 69, 12, 34, 65, 76]))