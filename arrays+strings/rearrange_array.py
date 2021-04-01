print("Array rearrange such that arr[i] = i\n");

def rearrange(array):
    for i in range(len(array)):
        elem = array[i]

        if elem == -1:
            continue
        else:
            if elem == i:
                continue
            else:
                diffElem = array[elem] # 
                array[elem] = elem
                array[i] = -1
                while diffElem != -1 and array[diffElem] != i:
                    if array[diffElem] == -1:
                        array[diffElem] = diffElem
                        break
                    diffElem = array[diffElem]

    return array

srt = [3, -1, -1, 0, 4]
srt = [4, 3, 2, 1, 0]
# srt = [-1, -1, 6, 1, 9, 3, 2, -1, 4,-1]
print(rearrange(srt))