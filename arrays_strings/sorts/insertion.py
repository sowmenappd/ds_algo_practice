# ascending
def sort(array):
    l = len(array)

    for i in range(l-1):
        j = i + 1

        while j > 0 and array[j-1] > array[j]:
            array[j], array[j-1] = array[j-1], array[j]
            j -= 1

    return array