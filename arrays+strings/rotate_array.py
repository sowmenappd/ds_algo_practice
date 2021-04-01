print("Array Rotation\n");

def rotate(array, d): 
  l = len(array)

  if d == 0 or l < 2:
    return array
  else:
    d = d % l
    for _ in range(d):
      save = array[0]
      for i in range(0, l-1): 
        array[i] = array[i+1]
      array[-1] = save
    return array

print(rotate([1, 2, 3, 4, 5, 6, 7], 3));
