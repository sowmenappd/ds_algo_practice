def sort(array):
    n = len(array)

    if n == 1:
        return array

    arr1 = array[0: n//2]
    arr2 = array[n//2:]
    
    arr1 = sort(arr1)
    arr2 = sort(arr2)

    return __merge__(arr1, arr2)


def __merge__(arr1, arr2):
    i, j = 0, 0
    temp = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            temp.append(arr1[i])
            i += 1
        else:
            temp.append(arr2[j])
            j += 1

    while i < len(arr1):
        temp.append(arr1[i])
        i+=1
    while j < len(arr2):
        temp.append(arr2[j])
        j+=1
    return temp