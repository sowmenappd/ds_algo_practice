print("Array Rotation\n");

def reverse_rotate(array, d):
  l = len(array)

  if d == 0 or l < 2:
    return array
  else:
    d = d % l
    
    array = __reverse(array, 0, d-1);
    array = __reverse(array, d, l-1);
    return  __reverse(array, 0, l-1);


def __reverse(array, start, stop):
    s = start
    e = stop
    
    while s < e:
        t = array[s]
        array[s] = array[e]
        array[e] = t
        s += 1
        e -= 1
    return array


print(reverse_rotate([1, 2, 3, 4, 5, 6, 7], 3))