print("Bubble sort\n");

def sort(array, asc = True):
    l = len(array)
    for i in range(l):
        for j in range(i+1, l):
            if asc:
                if array[i] > array[j]:
                    array[i], array[j] = array[j], array[i] #swap
            else:
                if array[i] < array[j]:
                    array[i], array[j] = array[j], array[i] #swap
    return array
    